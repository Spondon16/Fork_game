import platform

def detect_os():
    os_info = platform.uname()
    print(f"Detected OS: {os_info.system}")
    print(f"OS Version: {os_info.version}")
    print(f"System Architecture: {os_info.machine}")

    if os_info.system == "Linux":
        print("Running Linux-specific commands...")
    elif os_info.system == "Darwin":
        print("Running macOS-specific commands...")
    elif os_info.system == "Windows":
        print("Running Windows-specific commands...")
    else:
        print("Unsupported OS detected.")

detect_os()