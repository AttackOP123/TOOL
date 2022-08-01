import os

os.system("echo $(cat terminals.txt) >> /root/.zshrc")
os.system("cp -rf Versatile.py /usr/share")
os.system("echo $(cat IP_addr.txt) >> /root/.zshrc")
