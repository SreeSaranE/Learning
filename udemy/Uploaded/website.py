import csv
import requests
from http import HTTPStatus
from fake_useragent import UserAgent

def get_web(csv_path):
    website = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[0] or 'http://' not in row[0]:
                website.append(f"https://{row[0]}")
            else:
                website.append(row[1])

        return website

def get_user_agent():
    ua = UserAgent()
    return ua.firefox

def status_description(status_code):
    for value in HTTPStatus:
        if status_code == value:
            description = f"({value} {value.name}) {value.description}"
            return description
        
    return "^^^ Unknown Status!"

def check_web(website, user_agent):
    try:
        code = requests.get(website, headers={'user_agent': user_agent}).status_code
        print(website, status_description(code))
    except Exception:
        print(f"Could get information of {website}")

def main():
    sites = get_web('udemy/website.csv')
    user_agent = get_user_agent()
    for site in sites:
        check_web(site, user_agent)

if __name__ == '__main__':
    main()