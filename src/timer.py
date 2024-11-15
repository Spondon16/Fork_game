import os
import platform
import time
from tqdm import tqdm

def detect_os():
    for _ in tqdm(range(100), desc="Initializing", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
        time.sleep(0.9)  # Simulate loading time

    print("It works!!")

if __name__ == "__main__":