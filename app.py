import os
import json
import base64
import subprocess
import _thread as thread
import time


UUID = ""
PATH = "/dypfucksao"


def cmd_run(args):
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)



if __name__ == '__main__':
    data = {}
    inbounds = {}
    settings = {}
    clients = {}
    clients["id"] = UUID
    clients["level"] = 0
    settings["clients"] = [clients]
    settings["decryption"] = "none"
    streamSettings = {}
    streamSettings["network"] = "ws"
    path = {}
    path["path"] = PATH
    streamSettings["wsSettings"] = path
    inbounds["port"] = 8080
    inbounds["protocol"] = "vless"
    inbounds["settings"] = settings
    inbounds["streamSettings"] = streamSettings
    protocol = {}
    protocol["protocol"] = "freedom"
    data["inbounds"] = [inbounds]
    data["outbounds"] = [protocol]
    with open("config.json", "w") as f:
        json.dump(data, f)
        f.close

    cmd_run(args=("chmod", "+x", "config.json"))
    cmd_run(args=("./v", "-c", "config.json"))
    cmd_run(args=("rm", "app", "a.json", "a.py", "-rf"))
