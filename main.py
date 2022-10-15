import paramiko
import time
import os
from io import StringIO

key = """\
-----BEGIN RSA PRIVATE KEY-----
{}
-----END RSA PRIVATE KEY-----""".format(os.getenv("KEY_VALUE"))
commands = {
    "cd": "cd proyecto",
    "compile": "java -jar target/ortopedicWork-0.0.1-SNAPSHOT.jar"
}

def connect(ip):
    global ssh
    pkey = paramiko.RSAKey.from_private_key(StringIO(key))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username='opc', pkey=pkey)
    shell = ssh.invoke_shell()
    position = ''
    while True:
        if position != "compile":
            for command in commands:
                shell.send(commands[command]+'\n')
                time.sleep(1)
                if(command == "compile"): 
                    position = command
                    break

ip = os.getenv("IP")
connect(ip)