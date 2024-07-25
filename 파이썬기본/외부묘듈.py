import requests
from bs4 import BeautifulSoup

# url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
# html = requests.get(url).text
# soup = BeautifulSoup(html, "html.parser")
# print(soup)

url = "https://comic.naver.com/webtoon/weekday"
html = requests.get(url)
html.raise_for_status()

soup = BeautifulSoup(html.text, "lxml")
cartoons = soup.find_all('a', attrs={"class" : "title"})
for cartoon in cartoons:

    title = cartoon.get_text()

    link = cartoon["href"]

    print(title,"https://comic.naver.com" + link)