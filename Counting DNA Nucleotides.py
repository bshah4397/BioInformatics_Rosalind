def Nucleotide_Count(dna):
    '''
    Counting the Nucleotide bases in the entire DNA Sequence
    :param dna:
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


print(Nucleotide_Count("AGTTCCCTGGGTTGCGGCCTTGTGGTAGGCGAAATGCGATGGGTATGGCGCATATTTAGCATTCAACTTCAGAGGCGGAGGGTGAGCTTCAACCGTACTACCTCGCCCTAGCGGAACAGTCAATTGTCGGCTGATCACTATTTGCGGGAGCTTACCGCAGGTTCAATAGTCATAGCGTAGAAGTATCTTAACGCCCATATTATCAAGGACCCAGCGAGCGAAGTTGAAGCGTCATAAAGCCACCCAATCGCTGATAATTTCGGCACGGATTGGCACACAGCTTGTCGGTCAAAACAGACGATTTTGACATCTTTACCATAGGGCTCTCATACCTCTACGCAGACCGTGGAATATTATCGGTTAGCCTATCAAGTGAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAAAAAAAAAAAGATCCTTCGGGTATCCTACTGGCCCTCCGTCGGCACCTCCCCCGGGGTATGGTTAACAACGCTCTTCTCGGTACAAGACCCGCATGTTATTCCAAACGTCGTCAATCCCACGTGACCTTTAATTGAAACTTGGGGCCGGTCCTCTTTGCTTTTATGACGTTCGGGACTTGAAGGTGTAAATCCTTTCTCCCTGAAATTACAGATTAGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGACTATCTTGGGAGTTAGTCAGCTGTAGTGTATGCTAATCCGCTTGAGCTCTTGTCCGTTGACAGTGCTTCGGCGACTGGAAAATGAAGCTCAAGCTCGGAGTGCAACGAGGGTCCTTTTCGCTAGCGGGAAATTTGTCGCGGTAACGGCTGCCAGCCAGCGGCACCTTCACCAGGTTTGACAGTCCACGGAAATCATACTTGTGAGGATC"))