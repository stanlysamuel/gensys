import os
import subprocess
import csv
import time

# Define the folder path containing the benchmark files
folder_path = './benchmarks'

# Define the output CSV file path
output_csv = './results.csv'

# Define the timeout duration in seconds (15 minutes)
timeout_duration = 900

# Custom sorting key function that sorts baseq on the number in the file name
def get_file_number(filename):
    # Extract the number from the file name
    parts = filename.split("_", 1)
    return int(parts[0])

# Create or overwrite the CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Benchmark', 'G-S', 'GF-P', 'FG-P', 'OTF', 'G'])

    # Flush the buffer to ensure the line is written immediately
    csvfile.flush()

    # Move the file pointer to the end of the file
    csvfile.seek(0, 2)
    
    # Get a list of all files in the folder
    # sort based on number in file name

    files = sorted(os.listdir(folder_path), key=get_file_number)

    # Loop through each file in the folder
    print("Running ASE 2023 Benchmark Suite. View results.csv for results.")
    for file in files:
        # Check if the file is a Python script
        if file.endswith('.py'):
            # Get the full path to the benchmark file
            benchmark_path = os.path.join(folder_path, file)
            
            row = []
            row.append(file)
            # Run the gensys command using subprocess
            specs = ['simple', 'product-buchi', 'product-co-buchi', 'otf']
            min = 100000000
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
                row.append(round(total_time,2))
                # Display stdout
                # print(f"Output for {file}:")
                # print(stdout)
                # print('-' * 30)
            
            row.append(round(min,2))
            # Write row replacing -1 with N/A and -2 with T/O
            for i in range(len(row)):
                if row[i] == -1:
                    row[i] = "N/A"
                if row[i] == -2:
                    row[i] = "T/O"
                if row[i] == 100000000:
                    row[i] = "T/O"
            # Write the results to the CSV file
            csvwriter.writerow(row)

            # Flush the buffer to ensure the line is written immediately
            csvfile.flush()

            # Move the file pointer to the end of the file
            csvfile.seek(0, 2)

print(f"Benchmark results stored in {output_csv}")