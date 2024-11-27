#!/usr/bin/env python3
from time import sleep
import paramiko

def send_file_via_ssh(local_path, remote_path, remote_host, remote_user, rsa_key_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    
    # Load SSH host keys
    ssh.load_system_host_keys()
    
    # Add the remote server's SSH key automatically
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the remote server using RSA key authentication
    ssh.connect(remote_host, username=remote_user, key_filename=rsa_key_path)
    
    # Use SFTP to transfer the file
    sftp = ssh.open_sftp()
    sftp.put(local_path, remote_path)
    
    # Close the SFTP session and SSH connection
    sftp.close()
    ssh.close()

# Define the file paths and connection details
local_file_path = '/var/log/command_log.csv'
remote_file_path = '/home/user/command_log.csv'
remote_host = '192.168.100.5'
remote_user = 'user'
rsa_key_path = '/home/vboxuser/.ssh/id_rsa'

while True:
    send_file_via_ssh(local_file_path, remote_file_path, remote_host, remote_user, rsa_key_path)
    sleep(10)
    print("FIle sent")
