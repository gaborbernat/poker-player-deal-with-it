import json
import urllib


def rank(cards):
    import requests

    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': '*/*'}
    d = urllib.urlencode([('cards', json.dumps(cards))])
    r = requests.get('http://rainman.leanpoker.org/rank', headers=headers, data=d)
    print(r.text)


if __name__ == '__main__':
    cards = [
        {"rank": "5", "suit": "diamonds"},
        {"rank": "6", "suit": "diamonds"},
        {"rank": "7", "suit": "diamonds"},
        {"rank": "7", "suit": "spades"},
        {"rank": "8", "suit": "diamonds"},
        {"rank": "9", "suit": "diamonds"}
    ]
    rank(cards)