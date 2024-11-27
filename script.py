from time import sleep
import paramiko

def setup_ssh_connection(remote_host, remote_user, rsa_key_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    
    # Load SSH host keys
    ssh.load_system_host_keys()
    
    # Add the remote server's SSH key automatically
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the remote server using RSA key authentication
    ssh.connect(remote_host, username=remote_user, key_filename=rsa_key_path)
    
    return ssh

def send_file_via_sftp(sftp, local_path, remote_path):
    # Use SFTP to transfer the file
    sftp.put(local_path, remote_path)

# Define the file paths and connection details
local_file_path = '/var/log/command_log.csv'
remote_file_path = '/home/user/command_log.csv'
remote_host = '192.168.100.5'
remote_user = 'user'
rsa_key_path = '/home/vboxuser/.ssh/id_rsa'

# Setup SSH connection and SFTP session
ssh = setup_ssh_connection(remote_host, remote_user, rsa_key_path)
sftp = ssh.open_sftp()

try:
    while True:
        send_file_via_sftp(sftp, local_file_path, remote_file_path)
        sleep(10)
        print("File sent")
finally:
    # Close the SFTP session and SSH connection
    sftp.close()
    ssh.close()
    print("Connection ended")
