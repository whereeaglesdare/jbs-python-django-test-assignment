import urllib.request
import json

def send_http_request(delay_sec):
    with urllib.request.urlopen('https://httpbin.org/delay/{}'.format(str(delay_sec))) as response:
        html = response.read()
    data = json.loads(html.decode('utf-8'))
    return data