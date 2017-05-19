import sys
import os
import platform
import subprocess
from line import LineClient, LineGroup, LineContact

user = 'saranpong.kom@gmail.com'
passw = ''
No = 1

plat = platform.system()
scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
lines = hostsFile.readlines()
if plat == "Windows":
    for line in lines:
        line = line.strip()
        ping = subprocess.Popen(

            ["ping", "-n", "1", "-l", "1", "-w", "100", line],

            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE

        )
        out, error = ping.communicate()
        client = LineClient(user , passw)

        kitti = client.groups[No] 
        kitti.sendMessage(out)

if plat == "Linux":
    for line in lines:
        line = line.strip( )
        line = line.strip( )
    
        ping = subprocess.Popen(
            ["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", line],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
         
        )
        out, error = ping.communicate()
        client = LineClient(user , passw)
        kitti = client.groups[1] 
        kitti.sendMessage(out)


hostsFile.close()