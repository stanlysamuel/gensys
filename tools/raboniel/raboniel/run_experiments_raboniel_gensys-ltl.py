import os
import subprocess
import time
import re

# Define the folder path containing the benchmark files
# raboniel_folder_path = '/home/stanly/Project/gensys/tools/raboniel/raboniel/examples/gensys-ltl'
raboniel_folder_path = '/gensys/tools/raboniel/raboniel/examples/gensys-ltl'

# Define the output CSV file path
output_csv = './results.csv'

# Define the timeout duration in seconds (15 minutes)
timeout_duration = 900

# Custom sorting key function that sorts baseq on the number in the file name
def get_file_number(filename):
    # Extract the number from the file name
    parts = filename.split("_", 1)
    return int(parts[0])

consynth_results = ['-', 'T/O', '765.3', '2.5', '19.52', '10.01', '18', '436', '4.7', '-', '53.3', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '3.7', '0.4', '1.9', '1.5', 'T/O', '0.4', 'T/O']

# Raboniel results

raboniel_results = []

# Define the regular expression pattern for intermediate files of the form _R[0-9]+.tsl. Eg: "_R0.tsl". We do not want to synthesize for these files.
pattern = r"_R\d+\.tsl"

files = sorted(os.listdir(raboniel_folder_path), key=get_file_number)

for file in files:
    # Check if the file is a TSL file
    if file.endswith('.tsl') and not re.search(pattern, file):
        # Get the full path to the benchmark file
        benchmark_path = os.path.join(raboniel_folder_path, file)
        
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

            if exit_code == 5:
                    # exit code 5 corresponds to total time -1 viz. N/A 
                    total_time = -1
            if exit_code == 6:
                    # exit code 6 corresponds to total time -2 viz. (manual) T/O
                    total_time = -2
            if exit_code != 0 and exit_code != 5 and exit_code != 6:
                print(f"Error running {file}:")
                print(stderr)
                print('-' * 30)
                break

        except subprocess.TimeoutExpired:
            total_time = -2
        raboniel_results.append(round(total_time,2))

print("Cleanup all intermediate files")
# List all files in the current directory
files_ = os.listdir(raboniel_folder_path)

# Iterate over the files
for file_ in files_:
    # Check if the file matches the pattern
    if re.search(pattern, file_) or file_.endswith('.tlsf') or file_.endswith('.kiss'):
    # if re.match(pattern, file_):
        # Construct the file path
        file_path = os.path.join(raboniel_folder_path, file_)
        
        # Delete the file
        os.remove(file_path)
        
        # Print a message indicating the deletion
        print(f"Deleted file: {file_path}")

    # G = round(min,2)
    # C = consynth_results[get_file_number(file)]
    # R = raboniel_results[get_file_number(file)]
    # speedup_C = '-'
    # speedup_R = '-'

    # if G != 'T/O' and G != '-':
    #     G = float(G)
    #     if C != 'T/O' and C != '-':
    #         C = float(C)
    #         speedup_C = round(C/G,2)
    #         consynth_speedup.append(speedup_C)
    #     if R != 'T/O' and R != '-':
    #         R = float(R)
    #         speedup_R = round(R/G,2)
    #         raboniel_speedup.append(speedup_R)

    # row.append(C)
    # row.append(R)
    # row.append(G)
    # row.append(fastest_approach)
    # row.append(speedup_C)
    # row.append(speedup_R)

    # # Write row replacing -1 with N/A and -2 with T/O
    # for i in range(len(row)):
    #     if row[i] == -1:
    #         row[i] = "N/A"
    #     if row[i] == -2:
    #         row[i] = "T/O"
    #     if row[i] == 100000000:
    #         row[i] = "T/O"
    #     if row[i] == "None":
    #         row[i] = "T/O"
    #     if row[i] == "simple":
    #         row[i] = "G-S"
    #     if row[i] == "product-buchi":
    #         row[i] = "GF-P"
    #     if row[i] == "product-co-buchi":
    #         row[i] = "FG-P"
    #     if row[i] == "otf":
    #         row[i] = "OTF"
    # # Write the results to the CSV file
    # csvwriter.writerow(row)


# raboniel_results = ['-', 'T/O', 'T/O', '3.1', '-', '-', 'T/O', 'T/O', 'T/O', 'T/O', '-', '1.8', '2.2', '5.1', '27.4', '108.0', '19.4', '51.0', '51.0', '650.1', 'T/O', '1.2', '0.3', '6.4', '3.4', '94.0', '0.3', 'T/O']

print(raboniel_results)
