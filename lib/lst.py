import datetime
from datetime import datetime

def time():
    f = open('lib/date.txt', 'r')
    date1 = datetime.strptime(f.read(), "%Y-%m-%d %H:%M:%S.%f")
    f.close()
    date2 = datetime.now()
    delta = date2 - date1
    res = delta.total_seconds() // 60
    f = open('lib/date.txt', 'w')
    f.write(str(datetime.now()))
    f.close()
    return res