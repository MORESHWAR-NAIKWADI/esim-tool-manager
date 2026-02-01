import os
import json
import platform
import subprocess
import argparse
from datetime import datetime

LOG_FILE = "tool_manager.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def load_tools():
    with open("tools.json") as f:
        return json.load(f)

def get_os():
    os_name = platform.system().lower()
    if "linux" in os_name:
        return "linux"
    elif "windows" in os_name:
        return "windows"
    else:
        return None

def run_cmd(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return out.decode()
    except:
        return None





def install_tool(name):
    tools = load_tools()
    os_type = get_os()

    if name not in tools:
        print("Tool not found")
        return

    print(f"Installing {name}...")
    os.system(tools[name][os_type])
    log(f"Installed {name}")

def update_tool(name):
    tools = load_tools()
    os_type = get_os()

    if name not in tools:
        print("Tool not found")
        return

    print(f"Updating {name}...")

    if os_type == "linux":
        os.system(f"sudo apt update && sudo apt install --only-upgrade -y {name}")
    elif os_type == "windows":
        os.system(f"choco upgrade {name} -y")

    log(f"Updated {name}")

def check_version(name):
    tools = load_tools()
    cmd = tools[name]["version_cmd"]

    out = run_cmd(cmd)
    if out:
        print(out)
        log(f"Checked version for {name}")
    else:
        print(f"{name} not installed")

def list_tools():
    tools = load_tools()
    for t in tools:
        print("-", t)

def check_dependencies():
    print("Checking dependencies...\n")

    deps = {
        "python": "python --version",
        "git": "git --version",
        "pip": "pip --version"
    }

    for name, cmd in deps.items():
        out = run_cmd(cmd)
        if out:
            print(f"{name}: OK")
        else:
            print(f"{name}: Missing or not in PATH")

    log("Checked dependencies")


def configure_paths():
    print("Configuring environment...\n")

    path = os.environ.get("PATH", "")
    if path:
        print("PATH variable detected.")
    else:
        print("PATH not set properly.")

    print("Environment check completed.")
    log("Configured environment variables")







def main():
    parser = argparse.ArgumentParser(description="eSim Tool Manager")

    parser.add_argument("--install", help="Install tool")
    parser.add_argument("--update", help="Update tool")
    parser.add_argument("--version", help="Check version")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--check-deps", action="store_true")
    parser.add_argument("--config", action="store_true")

    args = parser.parse_args()

    if args.install:
        install_tool(args.install)
    elif args.update:
        update_tool(args.update)
    elif args.version:
        check_version(args.version)
    elif args.list:
        list_tools()
    elif args.check_deps:
        check_dependencies()
    elif args.config:
        configure_paths()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
