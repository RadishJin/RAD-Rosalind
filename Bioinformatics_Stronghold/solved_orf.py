from modulefiles import parse_rosalind_fasta, find_pattern

from Bio.Seq import Seq # 번역기 가져오기

with open("data/rosalind_orf.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# """

line = list(parse_rosalind_fasta(raw).values())[0]

seq = Seq(line)
rev = seq.reverse_complement()

prot_list = []
for i in range(3):
    prot_list.append(str(seq[i:].translate()))
    prot_list.append(str(rev[i:].translate()))
# print(prot_list)

aa = []
for prot in prot_list:
    pat = find_pattern("M[A-Z*]*?\*", prot)
    if len(pat):
        aa.extend(pat)
aa = set(aa)

for a in aa:
    print(a[:-1])