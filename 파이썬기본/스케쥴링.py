import schedule #스케쥴 기능을 사용하기 위해 import
import time #일정 시간만큼 대기를 걸기 위해서
import requests #http 동기 통신을 하기 위해서 사용
from bs4 import BeautifulSoup #크롤링 위해 사용

def perform_web_crawling():
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행합니다.")
    perform_web_crawling()

schedule.every().day.at("09:47").do(job)
job1 = schedule.every(1).second.do(job)

while True:
    schedule.run_pending() #대기중인 작업을 수행하는 함수
    time.sleep(1) #1초 대기
