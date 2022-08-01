import requests
import json
import datetime as dtm


def get_dates(days: int):
    dt = dtm.datetime.now()
    sec_now = int(dt.timestamp())
    sec_yesterday = sec_now - sec_now % 86400 - 86400 * (days - 1)
    return sec_yesterday, sec_now


def out_questions(url: str, days: int):
    par = {'fromdate': get_dates(days)[0], 'todate': get_dates(days)[1], 'order': 'desc', 'sort': 'votes',
           'tagged': 'Python',
           'site': 'stackoverflow'}
    res = requests.get(url, params=par)
    for item in res.json()['items']:
        print(item['title'])


if __name__ == '__main__':
    URL = 'https://api.stackexchange.com/2.3/questions'
    DAYS = 2
    out_questions(URL, DAYS)