with open("data/rosalind_ini5.txt", "r") as f:
    raw_data = f.readlines()

str_list = []

for i in range(len(raw_data)):
    if i % 2 != 0:
        str_list.append(raw_data[i].strip())
    else:
        continue

for j in str_list:
    print(f"{j}")

# .readlines() : 파일 전체를 읽어옴, 각 줄을 요소로 갖는 리스트로 반환
# .readline() : 파일 전체를 읽어옴, 한 줄씩 읽어옴, 한 줄을 string으로 반환