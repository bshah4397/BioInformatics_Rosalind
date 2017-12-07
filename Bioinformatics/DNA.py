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
    return ((countC+countG)*100.00/total)