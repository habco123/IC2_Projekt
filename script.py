import os
import csv
import time
import getpass
import paramiko

# Define the log file and remote server details
log_file = "/home/logs/command_log.csv"
remote_server = "192.168.10.5"
remote_user = "user"  # Replace with the actual username on the remote server
remote_path = "/home/user/logs/command_log.csv"  # Updated path on the remote server

# Function to log commands
def log_command(command):
    with open(log_file, 'a', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), getpass.getuser(), command])

# Function to send log file to remote server
def send_log():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_server, username=remote_user, key_filename='/home/kali/.ssh/id_rsa')
    sftp = ssh.open_sftp()
    sftp.put(log_file, remote_path)
    sftp.close()
    ssh.close()

# Main loop to capture commands
try:
    while True:
        command = input("$ ")
        log_command(command)
        os.system(command)
        send_log()
except KeyboardInterrupt:
    print("\nLogging stopped.")
