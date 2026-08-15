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