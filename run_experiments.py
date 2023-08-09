import os
import subprocess
import csv
import time

# Define the folder path containing the benchmark files
folder_path = './benchmarks_ase'

# Define the output CSV file path
output_csv = './results.csv'

# Create or overwrite the CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Benchmark', 'G-S', 'GF-P', 'FG-P', 'G'])

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Loop through each file in the folder
    for file in files:
        # Check if the file is a Python script
        if file.endswith('.py'):
            # Get the full path to the benchmark file
            benchmark_path = os.path.join(folder_path, file)
            
            # Record start time
            start_time = time.time()
            
            row = []
            row.append(file)
            # Run the gensys command using subprocess
            specs = ['simple', 'buchi', 'cobuchi']
            min = 100000000
            for spec in specs:
                command = ['python3', benchmark_path, spec]
                process = subprocess.Popen(command,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        text=True)
                
                # Wait for the process to finish
                stdout, stderr = process.communicate()
                exit_code = process.returncode
                
                if exit_code != 0:
                    print(f"Error running {file}:")
                    print(stderr)
                    print('-' * 30)
                    break
                # Calculate total time taken
                total_time = time.time() - start_time
                if total_time < min:
                    min = total_time
                row.append(round(total_time,2))
                # Display stdout
                print(f"Output for {file}:")
                print(stdout)
                print('-' * 30)
            
            row.append(round(min,2))
            # Write the results to the CSV file
            csvwriter.writerow(row)

print(f"Benchmark results stored in {output_csv}")