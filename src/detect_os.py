import platform

def detect_os():
    os_name = platform.system()
    print(f"Detected OS: {os_name}")

detect_os()