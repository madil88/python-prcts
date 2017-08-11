from common import IP_LIST, do_ping

import time

z= []

for ip in IP_LIST:
 p = do_ping(ip)
 z.append((p, ip))

for p, ip in z:
 print time.asctime(), ip, "Returned", p.returncode
