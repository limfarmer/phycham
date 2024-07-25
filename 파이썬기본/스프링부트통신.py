# 통신하는 모듈 임포트
# import requests
import json

import requests

data = {
    "id" : "곰돌이 사육사",
    "pw" : "1234",
}
# JSON 데이터를 스프링부트 서버로 전송하기
url = " http://localhost:8111/auth/python"
headers = {"Content-Type": "application/json"}
response = requests.post(url,data=json.dumps(data), headers=headers)

if response.status_code == 200 :
    print(response)
else :
    print("데이터 전송 실패 , 응답코드 : ", response.status_code)