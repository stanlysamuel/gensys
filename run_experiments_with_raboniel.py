import os
import subprocess
import csv
import time
from tools.raboniel.raboniel import run_experiments_raboniel_gensys_ltl as raboniel

# Define the folder path containing the benchmark files
benchmarks_folder_path = './benchmarks'

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

# Run Raboniel and get the results.
# Change the current working directory to the desired folder
os.chdir('tools/raboniel/raboniel/')
# print("Current working directory:", os.getcwd())
raboniel_results = raboniel.get_raboniel_results()
print("Raboniel results:")
print(raboniel_results)

# Change the current working directory back to the original folder
os.chdir('../../../')
cwd = os.getcwd()

consynth_speedup = []
raboniel_speedup = []

# Run GenSys-LTL and get the results.
# Create or overwrite the CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Benchmark', 'G-S (Simple)', 'GF-P (Product-Buchi)', 'FG-P (Product-Co-Buchi)', 'OTF (On-The-Fly)','ConSynth Results', 'Raboniel Results', 'G (Fastest Time - Gensys)', 'Fastest Approach - GenSys', 'Speedup (over ConSynth)', 'Speedup (over Raboniel)'])

    # Flush the buffer to ensure the line is written immediately
    csvfile.flush()

    # Move the file pointer to the end of the file
    csvfile.seek(0, 2)
    
    # Get a list of all files in the folder
    # sort based on number in file name

    files = sorted(os.listdir(benchmarks_folder_path), key=get_file_number)

    # Loop through each file in the folder
    print("Running ASE 2023 Benchmark Suite. View results.csv for results.")
    for file in files:
        # Check if the file is a Python script
        if file.endswith('.py'):
            # Get the full path to the benchmark file
            benchmark_path = os.path.join(benchmarks_folder_path, file)
            
            row = []
            row.append(file)
            # Run the gensys command using subprocess
            specs = ['simple', 'product-buchi', 'product-co-buchi', 'otf']
            min = 100000000
            fastest_approach = "None"
            for spec in specs:
                command = ['python3', benchmark_path, spec]
                # Record start time
                start_time = time.time()
                # Run the command with a timeout
                try:
                    print(file, spec)
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
                    #  total time -2 is T/O
                    total_time = -2

                if total_time < min and total_time >=0:
                    min = total_time
                    fastest_approach = spec
                row.append(round(total_time,2))
                # Display stdout
                # print(f"Output for {file}:")
                # print(stdout)
                # print('-' * 30)
            
            G = round(min,2)
            C = consynth_results[get_file_number(file)]
            R = raboniel_results[get_file_number(file)]
            speedup_C = '-'
            speedup_R = '-'

            if G != 'T/O' and G != '-':
                G = float(G)
                if C != 'T/O' and C != '-':
                    C = float(C)
                    speedup_C = round(C/G,2)
                    consynth_speedup.append(speedup_C)
                if R != 'T/O' and R != '-':
                    R = float(R)
                    speedup_R = round(R/G,2)
                    raboniel_speedup.append(speedup_R)

            row.append(C)
            row.append(R)
            row.append(G)
            row.append(fastest_approach)
            row.append(speedup_C)
            row.append(speedup_R)

            # Write row replacing -1 with N/A and -2 with T/O
            for i in range(len(row)):
                if row[i] == -1:
                    row[i] = "N/A"
                if row[i] == -2:
                    row[i] = "T/O"
                if row[i] == 100000000:
                    row[i] = "T/O"
                if row[i] == "None":
                    row[i] = "T/O"
                if row[i] == "simple":
                    row[i] = "G-S"
                if row[i] == "product-buchi":
                    row[i] = "GF-P"
                if row[i] == "product-co-buchi":
                    row[i] = "FG-P"
                if row[i] == "otf":
                    row[i] = "OTF"
            # Write the results to the CSV file
            csvwriter.writerow(row)

            # Flush the buffer to ensure the line is written immediately
            csvfile.flush()

            # Move the file pointer to the end of the file
            csvfile.seek(0, 2)

print(f"Benchmark results stored in {output_csv}")
print(f"Average (arithmetic mean) speedup over ConSynth: {round(sum(consynth_speedup)/len(consynth_speedup),2)}")
print(f"Average (arithmetic mean) speedup over Raboniel: {round(sum(raboniel_speedup)/len(raboniel_speedup),2)}")