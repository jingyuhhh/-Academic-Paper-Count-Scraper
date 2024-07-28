import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict


keywords = ["vr", "ar"]
year_start = 2023
year_end = 2024
data = defaultdict(dict)

for keyword in keywords:
    for year in range(year_start, year_end + 1):
        # IEEE
        # url  =f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={keyword}&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges={year}_{year}_Year"
        # ACM
        url = f"https://dl.acm.org/action/doSearch?AllField={keyword}&expand=all&AfterYear={year}&BeforeYear={year}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Referer': url,
        }


        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        num = soup.find('span', class_='hitsLength').text
        num = int(num.replace(',', ''))
        data[year][keyword] = num

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['year']+keywords)
    for year in range(year_start, year_end + 1):
        writer.writerow([year]+[data[year][keyword] for keyword in keywords])
    