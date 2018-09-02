import subprocess
from wifi import Cell, Scheme
from commands import getstatusoutput as call


def checkIfInternetIsWorking(interface):
    cmd = "ping -c 1 -I {} 8.8.8.8 | grep -o [0-9]*%".format(interface)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    output = int(output[:-2])
    if output == 100:
        return False
    else:
        return True


def main():
    print(checkIfInternetIsWorking("wlan0"))
        


main()
