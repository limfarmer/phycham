from bs4 import BeautifulSoup

# html = '''
#     <html>
#     <table border=1>
#         <tr>
#             <td> 항목 </td>
#             <td> 2013 </td>
#             <td> 2014 </td>
#             <td> 2015 </td>
#         </tr>
#         <tr>
#             <td> 매출액 </td>
#             <td> 100 </td>
#             <td> 200 </td>
#             <td> 300 </td>
#         </tr>
#     </table>
# </html>
# '''
# # 'html.parser' : 기본 parser 파이썬에서 제공하며 기본적으로 느림
# soup = BeautifulSoup(html, 'html.parser')
# result = soup.select('td')
# for e in result :
#     print(e.text)

html = '''
    <ul>
    <li> 100 </li> 
    <li> 200 </li>
</ul> 
<ol>
    <li> 300 </li> 
    <li> 400 </li>
</ol>
'''
soup = BeautifulSoup(html, 'html5lib')
result = soup.select('li:nth-child(1)')
for e in result :
    print(e.text)