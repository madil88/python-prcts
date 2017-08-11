import subprocess
import time


IP_LIST = ['google.com', 'yahoo.com', 'amazon.com', 'yelp.com', 'gmail.com']

cmd_std = 'ping -c 5 %s'

def do_ping(addr):
 print time.asctime()  , "Doing ping for", addr
 cmd = cmd_std % (addr,)
 return subprocess.Popen (cmd, shell=True, stdout=subprocess.PIPE)

