import random

def generate_strand(length):
    nucleotides = ['A', 'C', 'T', 'G']
    return ''.join([random.choice(nucleotides) for _ in range(length)])

def translate_strand(strand):
    typeshi = str.maketrans('ACTG', 'TGAC')
    return strand.translate(typeshi)

def basecount(chain):
    counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for base in chain:
        counts[base] += 1
    return counts

def convert(chain):
    RNA = chain.replace('T', 'U')
    return RNA

length = int(input('How many base pairs would you like there to be? '))
strand = generate_strand(length)
strand2 = translate_strand(strand)

counts = basecount(strand)
print(strand)
print(counts)

counts = basecount(strand2)
print(strand2)
print(counts)

print('CONVERTED RNA STRANDS:')
RNA = convert(strand)
print(RNA)
RNA = convert(strand2)
print(RNA)
