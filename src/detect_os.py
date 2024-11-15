# OS detection python script!!
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        print("It's " + os_name + "system!")
    if os_name == "Darwin":
        print("It's " + os_name + "system!")
    if os_name == "Windows":
        print("It's " + os_name + "system!")
    else:
        print("It's " + os_name + "system!")
detect_os()