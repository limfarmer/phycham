import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.tiobe.com/tiobe-index/")
# print("응답코드 : ", res.status_code)
#
# if res.status_code == requests.codes.ok :
#     print("정상 응답 입니다.")
# else:
#     print("네트워크 오류 : [에러 코드 " , res.status_code , "]")
#
#soup = BeautifulSoup(res.text, "lxml")
# print(soup.find(attrs={"class" : "notify_area"}))
print("응답코드 : ", res.status_code)

if res.status_code == requests.codes.ok :
    print("정상 응답 입니다.")
else:
    print("네트워크 오류 : [에러 코드 " , res.status_code , "]")

soup = BeautifulSoup(res.text, "html.parser")
#print(res.text)
#webToonList = soup.find('ul', attrs={'class': 'ContentList__content_list'}).find_all('li')
#result = soup.find("li", attrs={"class" : " item"})
list = soup.select("tbody tr td")
print(list[4].text)
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body id ="container">
  <div class="example">example인 div태그 입니다.</div>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <div class="content">
      <p>This is a paragraph2.</p>
      <p>This is another paragraph2.</p>
    </div>
    <div id ="parent">
        <div class ="child">first child</div>
        <div class ="child">second child</div>
        <div class ="child">third child</div>
    </div>
    <a href="https://www.example.com">Link</a>
  </body>
</html>
'''

#soup = BeautifulSoup(html_doc, "html.parser")
# soup.태그이름하면 찾아짐 ex)title/body 등등
# title_tag = soup.title
# #print(title_tag)
#
# # 클래스가 "content"인 div태그 검색 (CSS선택자 이용)
# #div_tags = soup.select('div.content p:nth-child(2)')
# div_tags = soup.select('div.content')
# # for e in div_tags :
# #     print(e.text)
# # href 속성이 있는 모든 a태그 검색
# a_tags = soup.find_all('a',href=True)
# # for a in a_tags:
# #     print(a)
#
# # Tag 객체 다루기 : Tag 객체에서는 요소의 이름, 속성, 내용등을 다룸
# tag_name = title_tag.name
# #print(tag_name)
# # Tag 객체에서 요소의 속성 얻기
# tag_attrs = div_tags[0].attrs
# print(tag_attrs)
#
# # Tag 객체에서 요소의 내용 얻기
# tag_content = div_tags[1].text
# print(tag_content)

#CSS 선택자로 요소 검색하기
# div_tags = soup.select('div.example')
# print(div_tags)
#
# #id 선택자 사용하기
# id_sel = soup.select_one("#container")
# #print(id_sel)
#
# # 자식 태그 선택자
# child_tag = soup.select("#parent > .child")
# print(child_tag)

# 속성으로 요소 검색하기
# attrs = {"class" : "content"}
# el = soup.find_all(attrs =attrs)
# print(el)