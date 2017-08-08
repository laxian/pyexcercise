#!/usr/bin/python

import datetime

if __name__ == '__main__':


    print(datetime.date.today().strftime('%d/%m/%Y'))

    d1 = datetime.date(1942, 1,2)
    print(d1.strftime('%d/%m/%Y'))

    d2=d1+datetime.timedelta(days=6)

    print(d2)

    print(d2.replace(year=2010))