import requests
from bs4 import BeautifulSoup

URL = "https://explainshell.com/explain/1/"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/85.0.4183.121 Safari/537.36",
           "accept": "*/*"}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")

    if soup.find("div", class_="span8 offset2") is None:

        command_html = soup.find("div", id="command")

        command_info = command_html.text.split()
        command_info[0] = command_info[0][0:len(command_info[0])-3]

        command_link = command_html.a["href"]

        command_result = " ".join(command_info) + "\nManual: " + command_link
        return command_result

    else:
        return "Nothing found"


def parse(command):
    url_command = URL + command
    html = get_html(url_command)

    if html.status_code == 200:
        return get_content(html.text)
    else:
        return "Sorry. Connection error"
