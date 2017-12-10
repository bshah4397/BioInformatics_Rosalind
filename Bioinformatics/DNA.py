def DNAComplement(dna):
    '''
    First Reveresed the DNA sequence and then Complimented the DNA Nucleotides
    :param dna: DNA Sequence String
    :return dnaC:
    '''
    dna = dna[::-1]
    dnaC = dna.replace('C','0')
    dnaC = dnaC.replace('G','C')
    dnaC = dnaC.replace('0', 'G')
    dnaC = dnaC.replace('A', '0')
    dnaC = dnaC.replace('T', 'A')
    dnaC = dnaC.replace('0', 'T')
    return dnaC

def Nucleotide_Count(dna):
    '''
    Counting the Nucleotide bases in the entire DNA Sequence
    :param dna: DNA Sequence String
    :return: countA,countC,countG,countT
    '''
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for i in dna:
        if i == 'A': countA += 1
        if i == 'C': countC += 1
        if i == 'G': countG += 1
        if i == 'T': countT += 1
    return countA, countC, countG, countT

def DNA_to_RNA(dna):
    '''
    Converting DNA -> RNA
    :param dna: DNA Sequence String
    :return: rna
    '''
    rna = dna.replace('T','U')
    return rna

def GCCompute(countG,countC,total):
    '''
    Computing the GC Percentage of a DNA Sequence
    :param countG:
    :param countC:
    :param total: GC Percentage
    :return:
    '''
    return ((countC+countG)*100.00/total)

def HammingDistance(dna1,dna2):
    '''
    Finding the Hamming Distance between two DNA Sequences
    :param dna1: DNA Sequence 1
    :param dna2: DNA Sequence 2
    :return distance: Hamming Distance between DNA1 and DNA2
    '''
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]: distance += 1
    return distance