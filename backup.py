"""Module"""

import os
import logging
import tarfile
from datetime import datetime
import paramiko
from scp import SCPClient
from paramiko import AuthenticationException

SOURCE_DIR = '/backup'
REMOTE_HOST = 'remote_host'
REMOTE_PORT = 22 # optional
REMOTE_USER = 'remote_user'
REMOTE_PASSWORD = 'remote_password'
REMOTE_DIR = '/backed_up_files/'
LOG_FILE = 'backup.log'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_tarball(source_dir, tarball_path):
    """Method to create a tarball"""
    try:
        with tarfile.open(tarball_path, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        logging.info(f"Tarball created at {tarball_path}")
    except Exception as e:
        logging.error(f"Failed to create tarball: {e}")

def upload_to_remote(local_path, remote_path):
    """Method to upload files"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(REMOTE_HOST, port=REMOTE_PORT, username=REMOTE_USER, password=REMOTE_PASSWORD)
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_path, remote_path)

        upload_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Uploaded {local_path} to {REMOTE_HOST}:{remote_path} at {upload_time}")
    except AuthenticationException:
        logging.error("Authentication failed, please verify your credentials")
    except Exception as e:
        logging.error(f"Failed to upload file: {e}")
    finally:
        ssh.close()

def main():
    """Main method"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    tarball_path = f"{SOURCE_DIR}_{timestamp}.tar.gz"

    try:
        create_tarball(SOURCE_DIR, tarball_path)

        remote_path = os.path.join(REMOTE_DIR, os.path.basename(tarball_path))
        upload_to_remote(tarball_path, remote_path)

        logging.info("Backup successful.")
        print("Backup successful. Check the log file for details.")
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        print("Backup failed. Check the log file for details.")
    finally:
        if os.path.exists(tarball_path):
            os.remove(tarball_path)

if __name__ == "__main__":
    main()
