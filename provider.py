import sys

import pandas as pandas
from pip._vendor import requests


def set_requests_body(db):
    out_dict = {}
    for index, row in db.iterrows():
        out_dict.update(
            title=row["title"],
            description=row["description"],
            coordinates=row["coordinates"],
            startTime=row["startTime"],
            endTime=row["endTime"],
            price=row["price"],
            peopleCount=row["peopleCount"])

    body = {
        "events": out_dict
    }
    return body


def set_response(url, body):
    try:
        r = requests.post(url=url, data=body)
        print(r)
    except Exception as s:
        print(s)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Ошибка. Слишком мало параметров.")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Ошибка. Слишком много параметров.")
        sys.exit(1)
    path = sys.argv[1]
    url = sys.argv[2]
    events = pandas.read_excel(path)
    body = set_requests_body(events)
    set_response(url, body)
