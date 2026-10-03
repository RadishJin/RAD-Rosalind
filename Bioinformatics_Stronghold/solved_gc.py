from modulefiles import parse_rosalind_fasta, calc_x_content

with open("data/rosalind_gc.txt", "r") as f:
    raw = f.read()

# test
# raw = """
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

seq_dict = parse_rosalind_fasta(raw)

max_id, max_seq = max(
    seq_dict.items(),
    key = lambda item: calc_x_content(item[1], "GC")
)
max_gc = calc_x_content(max_seq, "GC")

print(max_id); print(f'{max_gc*100:.6f}')






