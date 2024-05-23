import os
import shlex
import rich

from rich import inspect
from rich.console import Console
from rich.traceback import install

install()
c = Console()

def get_gtc_status():
    try:
        # for line in os.popen("systemctl --type=service --state=running"):
        status_list = []
        for line in os.popen("systemctl status gtclash.service"):
            service = line.split()
            if "gtclash.service" in service:
                status_list.append(service)
        if len(status_list) > 1:
            current_status_line = status_list[-1]
            if "Started" in current_status_line:
                print("GTClash is running, it needs to be stopped")
            elif "Stopped" in current_status_line:
                print("GTClash is already stopped")
        else:
            current_status = "Stopped"
            print("GTClash is already stopped")
    except OSError as ose:
        print("Error while running the command", ose)
    pass

def stop_gtc_process():
    try:
        os.popen("sudo systemctl stop gtclash.service")
    except OSError as ose:
        print("Error stopping GTClash")

get_gtc_status()
# stop_gtc_process()

