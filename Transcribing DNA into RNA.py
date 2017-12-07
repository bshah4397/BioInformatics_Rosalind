def DNA_to_RNA(fileLocation):
    '''
    Converting DNA -> RNA
    :param fileLocation:
    :return: rna
    '''
    file = open(fileLocation,'r')
    dna = file.read()
    file.close()
    rna = dna.replace('T','U')
    return rna
