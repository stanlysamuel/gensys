import os
import subprocess
import time
import re

# Define the folder path containing the benchmark files
raboniel_benchmarks_folder_path = '/gensys/tools/raboniel/raboniel/examples/gensys-ltl'

# Define the timeout duration in seconds (15 minutes)
timeout_duration = 900

# Custom sorting key function that sorts baseq on the number in the file name
def get_file_number(filename):
    # Extract the number from the file name
    parts = filename.split("_", 1)
    return int(parts[0])

# Run Raboniel and get the results.

def get_raboniel_results():
    print("Running Raboniel on Gensys-LTL benchmarks")
    raboniel_results = ['-']

    # Define the regular expression pattern for intermediate files of the form _R[0-9]+.tsl. Eg: "_R0.tsl". We do not want to synthesize for these files.
    pattern = r"_R\d+\.tsl"

    files = sorted(os.listdir(raboniel_benchmarks_folder_path), key=get_file_number)

    for file in files:
        # Check if the file is a TSL file and not an intermediate tsl file.
        if file.endswith('.tsl') and not re.search(pattern, file):
            # Get the full path to the benchmark file
            benchmark_path = os.path.join(raboniel_benchmarks_folder_path, file)
            
            command = ['./raboniel', '--spec', benchmark_path]
            # Record start time
            start_time = time.time()
            # Run the command with a timeout
            try:
                print(file)
                process = subprocess.run(command,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        text=True,
                                        timeout=timeout_duration)

                # Get the output and exit code
                stdout = process.stdout
                stderr = process.stderr
                exit_code = process.returncode

                # Calculate total time taken
                total_time = time.time() - start_time

                if exit_code != 0:
                    total_time = -1

            except subprocess.TimeoutExpired or subprocess.CalledProcessError or subprocess.SubprocessError:
                total_time = -1

            if total_time  == -1:
                raboniel_results.append("T/O")
            else:
                raboniel_results.append(round(total_time,2))

    # Cleanup all intermediate files (.kiss, .tlsf, _R*.tsl)
    files_ = os.listdir(raboniel_benchmarks_folder_path)

    for file_ in files_:
        # Check if the file matches the patterns
        if re.search(pattern, file_) or file_.endswith('.tlsf') or file_.endswith('.kiss'):
            # Construct the file path
            file_path = os.path.join(raboniel_benchmarks_folder_path, file_)
            
            # Delete the file
            os.remove(file_path)

    return raboniel_results