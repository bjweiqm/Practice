

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# from core import main
from day03_网络_demo.FTPServerDemo.MadFtpServer.core import main

if __name__ == "__main__":
    print(sys.path)
    main.ArvgHandler()
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
