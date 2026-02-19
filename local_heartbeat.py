
import platform
import os
import datetime

def check_system():
    print(f"--- Heartbeat Report: {datetime.datetime.now()} ---")
    print(f"Node Name: {platform.node()}")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Current User: {os.getlogin() if hasattr(os, 'getlogin') else 'github-runner'}")
    print(f"Architecture: {platform.machine()}")
    print("------------------------------------------")

if __name__ == "__main__":
    check_system()
