import requests
from bs4 import BeautifulSoup

def get_csv_range_phone(src='web'):
    if src == 'web':
        url = "https://rossvyaz.gov.ru/about/otkrytoe-pravitelstvo/otkrytye-dannee/reestr-otkrytykh-dannykh"
        html_text = requests.get(url, verify=False).text
        soup = BeautifulSoup(html_text, 'lxml')
        url_csv_range_phone = soup.find('a', text='CSV-DEF-9').get('href')
        arr = requests.get(url_csv_range_phone, verify=False).text
    elif src == 'file':
        f = open("CSV-DEF-9.csv", "r")
        arr = f.read()
    else:
        []
    arr = arr.split('\n')
    arr.pop(0)
    return list(map(lambda s: s.split(';'), arr))


if __name__ == '__main__':
    arr = get_csv_range_phone('file')
    d = set([item[5] for item in arr])
    print(d)
