# Write a script to read from a file named "input.txt", delete alternate lines, and write result to a file named "output.txt"

# Open input file
input_file = open("repaircritical", "r")

# Open output file
output_file = open("repaircritical_", "w")

# Read lines from input file
lines = input_file.readlines()

# Close input file
input_file.close()

# Write lines to output file
for i in range(1, len(lines), 3):
    output_file.write(lines[i])

# Close output file
output_file.close()
