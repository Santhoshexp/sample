"""Module"""

import time
import logging
import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
SLEEP_INTERVAL = 120

logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage():
    """Method to check cpu usage"""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert_message = f"High CPU Usage: {cpu_usage}%"
        logging.warning(alert_message)

def check_memory_usage():
    """Method to check memory usage"""
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert_message = f"High Memory Usage: {memory_usage}%"
        logging.warning(alert_message)

def check_disk_usage():
    """Method to check disk usage"""
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        alert_message = f"High Disk Usage: {disk_usage}%"
        logging.warning(alert_message)

def check_running_processes():
    """Method to check process count"""
    process_count = len(psutil.pids())
    alert_message = f"Number of Running Processes: {process_count}"
    logging.info(alert_message)

def main():
    """Main method"""
    print("System Health Check Started")
    logging.info("System Health Check Started")
    try:
        while True:
            check_cpu_usage()
            check_memory_usage()
            check_disk_usage()
            check_running_processes()

            print(f"Waiting for {SLEEP_INTERVAL} seconds before the next check...")
            logging.info(f"Waiting for {SLEEP_INTERVAL} seconds before the next check...")

            time.sleep(SLEEP_INTERVAL)
    except KeyboardInterrupt:
        print("System Health Check Stopped")
        logging.info("System Health Check Stopped")

if __name__ == "__main__":
    main()
