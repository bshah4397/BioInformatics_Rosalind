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
