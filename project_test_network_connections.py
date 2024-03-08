import subprocess
command = 'ping -n 1 8.8.8.3'
# command= 'ping -c 1 8.8.8.3' # Linux or Mac

output = subprocess.check_output(command.split())
print(output.decode())

