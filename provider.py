import sys
import pandas as pandas
import http.client
import requests
import json


def unwrap(time):
    if time[0] is "'":
        time = time[1:len(time)]

    if time[-1] is "'":
        time = time[0:len(time) - 1]

    return time

def get_coordinates(addr):
    try:
        response = requests.get('https://nominatim.openstreetmap.org/search/{}?format=json&limit=1'.format(addr))
        response_json = response.json()[0]
        lat = response_json['lat']
        lon = response_json['lon']
        return '{};{}'.format(lat, lon)
    except Exception as e:
        return ''


def set_requests_body(db):
    out_list = []

    for index, row in db.iterrows():
        row["coordinates"] = get_coordinates(row["addres"])
        event = {
            "title": row["title"],
            "coordinates": row["coordinates"],
            "description": row["description"],
            "isInfinite": row["isInfinite"],
            "startTime": unwrap(row["startTime"]),
            "endTime": unwrap(row["endTime"]),
            "price": row["price"],
            "peopleCount": row["peopleCount"]
        }
        if row["coordinates"]:
            out_list.append(event)
    body = {
        "events": out_list
    }
    return body


def set_response(url, url_path, body):
    try:
        connection = http.client.HTTPConnection(url)
        json_data = json.dumps(body)
        headers = {'Content-type': 'application/json'}
        connection.request('POST', url_path, json_data, headers)
        response = connection.getresponse()
        print("response: [", response.read().decode(), "]", sep="")
        print("success")
    except Exception as description:
        print(description)


def main():
    if len(sys.argv) < 3:
        print("Error. Too few parameters.")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Error. Too many parameters.")
        sys.exit(1)

    path = sys.argv[1]
    url = sys.argv[2]
    url_path = "/add_events"
    events = pandas.read_excel(path)
    body = set_requests_body(events)
    set_response(url, url_path, body)


if __name__ == "__main__":
    main()
