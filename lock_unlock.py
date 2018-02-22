import os
import subprocess as sp
import time

def ipcheck(pop):
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
    if status == 0:
        print("System " + str(pop) + " is UP !")
    else:
        print("System " + str(pop) + " is DOWN !")
    return status

subnet = "192.168.151."

hostname = subnet + str(253)
while(1):
	time.sleep(1)
	p = ipcheck(hostname)
	if (p!=0):
		os.system("gnome-screensaver-command -l")
		#print("hello")
	else:
		sp.Popen(['gnome-screensaver-command', '--deactivate'], shell=False, stdout=sp.PIPE)
	

    