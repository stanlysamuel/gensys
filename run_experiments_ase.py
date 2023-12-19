import os
import subprocess
import csv
import time

commandList = []

command = ['python3', os.path.join('./benchmarks_ase/', 'repairLock.py'), 'simple']
process = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
                
# Wait for the process to finish
stdout, stderr = process.communicate()
exit_code = process.returncode

print(stdout)