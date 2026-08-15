with open("rosalind_ini2.txt", "r") as f:
    raw_data = f.read()

clean_data = raw_data.strip()
numbers_str = clean_data.split()
a, b = map(int, numbers_str)

print(f"{a**2 + b**2}")