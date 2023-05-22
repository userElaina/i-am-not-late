import time
from iamnotlate import notLate

t = time.mktime(time.strptime("080000 23", "%H%M%S %y"))
a = notLate(t, 'H')
print(a.ctime(t+480))
# Sun Jan  1 07:68:00 2023

t = time.mktime(time.strptime("04 Jun 23", "%d %b %y"))
a = notLate(t, 'b')
print(a.ctime())
# Mon May 22 06:56:32 2023
print(a.ctime(t))
# Sun May 35 00:00:00 2023
