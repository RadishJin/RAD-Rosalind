# FASTA = """

# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT

# """

# RAW = FASTA

with open("data/rosalind_gc.txt", "r") as f:
    RAW = f.read()

L = RAW.strip().splitlines()

def parse(n: list) -> dict:
    seq = {}
    current_id = ""
    for line in n:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            seq[current_id] = ""
        else:
            seq[current_id] += line
    return(seq)

seq = parse(L)

max_id = ""
max_gc = -1.0

for id, sequence in seq.items():
    gc_val = ((sequence.count("G") + sequence.count("C"))/len(sequence)) *100
    if gc_val > max_gc:
        max_id = id
        max_gc = gc_val

print(f"{max_id}\n{max_gc:.6f}")



