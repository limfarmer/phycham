import json
# 인코딩

# customer = {
#     "id" : "dla",
#     "name" : "임정후",
#     "history" : [
#         {"date" : "2024-06-17","product" : "iPhone Xs"},
#         {"date": "2024-06-17","product": "Galaxy S24 Ultra"},
#     ]
# }
#
# json_string = json.dumps(customer)
# print((json_string))

#디코딩
# jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
#     {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
#     {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
# ]}'''
#
# dict = json.loads(jsonString)
#
# print(dict["name"])
# for h in dict["history"]:
#     print(h["date"], h["item"])

# csv파일 방식
# import csv
#
# f = open('output.csv','w', encoding='utf-8', newline='')
# wr = csv.writer(f)
# wr.writerow([1,"안유진", False])
# wr.writerow([2, "장원영", True])
# f.close()