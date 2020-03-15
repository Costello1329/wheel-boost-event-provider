import sys
import pandas as pandas
import http.client
import json


def set_requests_body(db):
    out_dict = {}

    for index, row in db.iterrows():
        event = {
            "title": row["title"],
            "coordinates": row["coordinates"],
            "description": row["description"],
            "startTime": row["startTime"],
            "endTime": row["endTime"],
            "price": row["price"],
            "peopleCount": row["peopleCount"]
        }
        out_dict.update(event)
    body = {
        "events": [out_dict]
    }
    return body


def set_response(url, url_path, body):
    try:
        connection = http.client.HTTPConnection(url)
        json_data = json.dumps(body)
        headers = {'Content-type': 'application/json'}
        connection.request('POST', url_path, json_data, headers)
        response = connection.getresponse()
        print(response.read().decode())
        print("success")
    except Exception as description:
        print(description)


def main():
    if len(sys.argv) < 4:
        print("Error. Too few parameters.")
        sys.exit(1)

    if len(sys.argv) > 4:
        print("Error. Too many parameters.")
        sys.exit(1)

    path = sys.argv[1]
    url = sys.argv[2]
    url_path = sys.argv[3]
    events = pandas.read_excel(path)
    body = set_requests_body(events)
    set_response(url, url_path, body)


if __name__ == "__main__":
    main()
