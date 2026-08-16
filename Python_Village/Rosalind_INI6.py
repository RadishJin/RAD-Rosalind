with open("data/rosalind_ini6.txt", "r") as f:
    raw_data = f.read()

# word_list = raw_data.strip().split()
# count = {}
# for w in word_list:
#     if w in count:
#         count[w] += 1
#     else:
#         count[w] = 1

# for k, v in count.items():
#     print(f"{k} {v}")

from collections import Counter
word_list = raw_data.strip().split()

count = Counter(word_list)

for k, v in count.items():
    print(f"{k} {v}")   

# from collections import Counter : 리스트의 요소를 카운트해주는 모듈
# Counter(리스트) : 리스트의 요소를 카운트해서 딕셔너리 형태로 반환
# .items() : 딕셔너리의 key, value를 튜플 형태로 반환
# for Vari1, Vari2 in dict.items(): : 딕셔너리의 key, value를 각각 변수에 할당