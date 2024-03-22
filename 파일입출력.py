# 파일 쓰기
# score_file = open("./file_name.txt", "w", encoding="utf-8")
# print("수학 : 55",file=score_file)
# print("영어 : 60", file=score_file)
# score_file.write("과학 : 90\n")
# score_file.write("국어 : 100\n")
# score_file.close()

# 파일 읽기
#score_flie = open("file_name.txt","r",encoding="utf-8")
# read() : 파일 내의 모든 내용을 읽어 하나의 문자 열로 반환
# print(score_file.read())
# score_file.close()

# readline() : 한 라인씩 읽어 문자 열로 반환, 파일의 끝에 도달 하면 None 값이 반환
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line, end="")
# score_file.close()

# readlines() : 해당 파일의 모든 라인을 순서대로 읽어들여 리스트로 반환
# lines = score_file.readlines() # 파일의 라인을 리스트로 반환
# for line in lines:
#     print(line,end="")
# score_file.close()

# with : with 구문이 종료 될 때 자동으로 파일을 닫음
# with open("file_name.txt","r",encoding="utf-8") as score_file:
#     lines = score_file.readlines()
#     for line in lines:
#         print(line,end="")

# pickle 직렬화에 관한 키워드

