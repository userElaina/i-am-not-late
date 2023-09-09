import time
from iamnotlate import notLate

t = time.mktime(time.strptime("080800 23", "%H%M%S %y"))
tmie = notLate(t, 'H')
print(time.ctime(t))
print(tmie.ctime(t))
# Sun Jan  1 08:08:00 2023
# Sun Jan  1 07:68:00 2023

t = time.mktime(time.strptime("04 Jun 23", "%d %b %y"))
tmie = notLate(t, 'b')
print(time.ctime())
print(tmie.ctime())
# Mon May 22 07:09:56 2023
# Mon May 22 07:09:56 2023
print(time.ctime(t))
print(tmie.ctime(t))
# Sun Jun  4 00:00:00 2023
# Sun May 35 00:00:00 2023
