import sys
import pandas as pandas
import http.client
import json


def unwrap(time):
    if time[0] is "'":
        time = time[1:len(time)]

    if time[-1] is "'":
        time = time[0:len(time) - 1]

    return time


def set_requests_body(db):
    out_list = []

    for index, row in db.iterrows():
        event = {
            "title": row["title"],
            "coordinates": row["coordinates"],
            "description": row["description"],
            "startTime": unwrap(row["startTime"]),
            "endTime": unwrap(row["endTime"]),
            "price": row["price"],
            "peopleCount": row["peopleCount"]
        }
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
