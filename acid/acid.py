""" https://www.mrsec.psu.edu/sites/mrsec.psu.edu/files/dnas_secret_code.pdf """
dd = {'AAA': 'a', 'CAA': 'q', 'GAA': 'G', 'TAA': 'W',
      'AAC': 'b', 'CAC': 'r', 'GAC': 'H', 'TAC': 'X',
      'AAG': 'c', 'CAG': 's', 'GAG': 'I', 'TAG': 'Y',
      'AAT': 'd', 'CAT': 't', 'GAT': 'J', 'TAT': 'Z',
      'ACA': 'e', 'CCA': 'u', 'GCA': 'K', 'TCA': '1',
      'ACC': 'f', 'CCC': 'v', 'GCC': 'L', 'TCC': '2',
      'ACG': 'g', 'CCG': 'w', 'GCG': 'M', 'TCG': '3',
      'ACT': 'h', 'CCT': 'x', 'GCT': 'N', 'TCT': '4',
      'AGA': 'i', 'CGA': 'y', 'GGA': 'O', 'TGA': '5',
      'AGC': 'j', 'CGC': 'z', 'GGC': 'P', 'TGC': '6',
      'AGG': 'k', 'CGG': 'A', 'GGG': 'Q', 'TGG': '7',
      'AGT': 'l', 'CGT': 'B', 'GGT': 'R', 'TGT': '8',
      'ATA': 'm', 'CTA': 'C', 'GTA': 'S', 'TTA': '9',
      'ATC': 'n', 'CTC': 'D', 'GTC': 'T', 'TTC': '0',
      'ATG': 'o', 'CTG': 'E', 'GTG': 'U', 'TTG': ' ',
      'ATT': 'p', 'CTT': 'F', 'GTT': 'V', 'TTT': '.', }

b = []
n = 3

with open('acid.txt', 'r') as infile:
    encoded = infile.read()
    b = [encoded[i:i+n] for i in range(0, len(encoded), n)]

b = [dd[i] for i in b]
b = str.encode(''.join(b))
with open('acid', 'wb') as acid:
    acid.write(b)
