# import datetime
#
# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.now() .time())

from datetime import datetime
from datetime import date

print(datetime.today())
print(datetime.now().time())
print(datetime.today().month)
print(datetime.now().year)

now = datetime.now()
print(now.strftime("%d/%m/%Y %H:%M"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))
print(date.today().strftime("%d-%b-%Y"))