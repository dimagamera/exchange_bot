from datetime import datetime
from datetime import timedelta
import datetime
import requests
import matplotlib.pyplot as plt

def graffi(message):
    i = 1
    inf= []
    date = []
    history = message
    try:
        while i < 7:
            data = datetime.date.today() - timedelta(days=i)
            date.append(data)
            r  = requests.get(f'https://openexchangerates.org/api/historical/{data}.json?app_id=dd0cdb5c177f4d1e8537175f1b6852a6').json()
            rating = r['rates'][str(history)]
            rating = '%.2f' % rating
            inf.append(rating)
            i+=1

        plt.plot(date, inf)
        plt.savefig('lib/history.png')
    except:
        return 'error'