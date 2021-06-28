import unittest



def distanceNeighborhood(pattern, distance):
#=If we remove the first symbol of Pattern (denoted FirstSymbol(Pattern)) (pattern[0]??),
# then we will obtain a (k − 1)-mer that we denote by Suffix(Pattern) (pattern[1:]??).
    if distance == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = []
    #suffixPattern = pattern[1:]
    suffixPattern = pattern[1:]
    suffixNeighbors = distanceNeighborhood(suffixPattern, distance)

    for suffixNeighbor in suffixNeighbors:
        if is_distance_less_than(suffixPattern, suffixNeighbor, distance):
            for nucleotide in {'A', 'C', 'G', 'T'}:
                    neighbor =  nucleotide+suffixNeighbor
                    neighborhood.append(neighbor)
        else:
            firstSymbol = pattern[0]
            neighborhood.append(firstSymbol + suffixNeighbor)
    # newNeighborhood = []
    # for neighbor in neighborhood:
    #     if is_distance_not_greater_than(pattern, neighbor, distance):
    #         newNeighborhood.append(neighbor)
    return neighborhood












def getDistanceOptions(char):
    if char == 'A':
        return ['T', 'C', 'G']
    if char == 'T':
        return ['A', 'C', 'G']
    if char == 'C':
        return ['A', 'T', 'G']
    if char == 'G':
        return ['A', 'T', 'C']

def distance(array_1, array_2):

    if (len(array_1) != len(array_2)):
        raise Exception("sizes are not equal")

    distance = 0

    for i in range(len(array_1)):
        if array_1[i] != array_2[i]:
            distance = distance + 1

    return distance

def is_distance_not_greater_than(array_1, array_2, max_distance):
    if (len(array_1) != len(array_2)):
        raise Exception("sizes are not equal")

    distance = 0

    for i in range(len(array_1)):
        if array_1[i] != array_2[i]:
            distance = distance + 1
            if distance > max_distance:
                return False
    return True

def is_distance_less_than(array_1, array_2, distance):
    if (len(array_1) != len(array_2)):
        raise Exception("sizes are not equal")

    distance = 0

    for i in range(len(array_1)):
        if array_1[i] != array_2[i]:
            distance = distance + 1
            if distance >= distance:
                return False
    return True



class TestStringMethods(unittest.TestCase):

    def test_distance_1(self):
            distance_ = distance('CCGAAGCAATTGAAACCCCCCCGGCCTGGGAGGCGCAAAAATCTGACCTCTTTGTGAGTTGACCACTTAATTTATGTCTGACCACGAGAAGGGCTACTGATTTGGTACGTCGGGTCATGACCCCCAGTTCTTAGCCGCCTGCTCCAATCTCTGACTTGTTTATCGAGGGGATGGAGTAACGAAATGCGATTCGCCCGCTCAGGCCAAGGTATATATTTGAGTAGCGGAAGGTTGCACTACCTACAACCACGGCACACCGGCACGTTGTCGTGCCCTGGCGGCCTGCGCACTTTCGCCACTGTCAAGTACGACTTCCCAAGCTCAACCAACATTCATAATCCGGTGCAATTCATACCGTATCATCGTGCTATAAGCGACGCCGATTCTCGGGGCCTGATAATTGAGACTGGACTACATAGTGGGTGCCCTCTCTGCGAGTAAGTGACGGAACAACGGAGATCAGGGACCAAATGGTAGCAAAACAGATCGAGGTACACGCAGGTAGCTGTCCGTGGAGTAGACCGCGCTTAGCGTCTGTTAGAGTATCATCGGGGTATTAGACACAGGAACCTCTATGCTGTTAAAAGGCCATACCCCGTAATTGTGCAAATTTGTTACGTTCAAATCTACGCAGTGAGGGTCCTAAGGTGATGGCAGGGATTGGAACTTCTCCGCTGGCTCTTAGATTACTTAGCCAGTCTACCCTCGAAGATACAAATCCTTCCACCAGAGGGAGCTCATTGAAATTCATTCCATGCTACTCGACCGCGCGTATGGGTGCGGGGCTCTATGGGATCTAACTCGATCCTTCAGAGTCCTTATTCAAATGCATTTCCGTCCCCGTATGTTTCGACGAAGCCGAAGCCCAAACCCTGGGATGGACGAATTAAGGACAGTACAGGCAATAGTGTTCTCCCATACTCGGAACAGACGCCTCATTTTTTCGCGAAATCGATCTGGGTTGGAAGAAGTTCCAGTGCAGAGTTCCTATCACACAATTCGTTCTCGGGGCTTCCGGCCCATAAGCGATACTACTGTCTTTGCGAGCTAACGATTACATTCGGGGGAACTTAGCTCGGACTGGACCAGGTACATGATCCAAAGCGCGATGTCTGTCTGTTACCCTCACCGCCGCTCTTTTATCGGGTA',
                                'GCGTAGTAGGTTCGCGTACCTAGTTCCGCCGAAAAGACAAAGGAGAAGGGAATGCTCCTAGTAGTTTCAGTCTAGCAAACATGTTATAACGCTAACTGTGTGCTGCAAAAAGGATTTGAACCCAAATTTTAAAGCGCTGATCGACAGAACGCTGTTGAAGAGGCGATGGTACTGAGATTCCCCAGAAACCACCTCCGCGCTATGTGCTCAAGACAACCCGCATTCGTTTTTACTAGATTTGGAGCCGAGTTGTGATTTGGATATTTTCACATAAGACCGAGCAGGAAATATACCTTGTTGCAGCTATTGACCCCGTTCTCTCGGAAATCCATGGAATAGTCTTCGGATATTCGTACCAATGGGCGCGATGTTGCGATAAGAGAGCACATTTCATTAAGTGGTGCTCCGCCGCTAAGATGGGAAGGGGCGAGTCTATCGCAGCATCGAAGGCTGAGTTGGCCATTGCCGAGAGTATACATATTTACGATCACACTCGCATAGTCCCACGCATTACGTCCGAGATAGTATGTCCCAATGCAACCTAAAGCCGCGAGATTCCCTAAGGAGAAAATTAAACACTGGAAATTAGGTGATGCTACATCCCATGGACACTTTCGGAACAATATCGGTGACACACATCATCCGTGATCCCGTGATATTTCATCCATGGAGAGAGTATGGTTTTACTACACCTGGTCTAGGCCAAGCCTAACCCCCTGTTCATCCGTTTTATACGAGTATTACCTTGACGACCATAGAGGATAGACTCGGTATCCCGCACACTCTACACACACGACTTAATCCGCTCCACGACCTTCCTAGCGATCTTTGGCGCAGCCGGTTCGCGTATTTTACGACCAACTCGATGGATCCCAATTATCCCCCTGGTAGTGCCCCTCCGCCTGAGAATTCGACGGGCGAGGTCCGGGGGACCGACATAGAGTGGAATGCTTCTTTCCGGGATAACACGTGATTGACATAAAAATGTAGGGCAGATAGGCATCGTTAGCACCTCTCTCCTTGCTGCACTGCGTTTATCGATCGAATTCAAGACTTGTGCATGTTGAAAACAACCTCGCGTTATCCCTGCTATTTGCTTCAGAGCCGTAGGAGGGGACCATGCGTGAGTCCTCCTGAGCAACCTCAATT')
            self.assertEqual(distance_, 844)

    def test_distance_2(self):
            distance_ = distance('CAATCCTCATGGCGTAATTGAATGTTTACTCCGTGGAAGGCAGCTTTTCGGGCACATTCCGCGCGTGACCCTTACTTGGCTGCAGGTTTCACAACCATTAGGAAATAAGTGACCGGACTATCAACGCTTAGTGTATTGATACTCAATCTTGTGCCAACGGGCGCGTAAGATCTATCATGCATTACGATCTGCTATGAGGCGTCGACAGGAATGAAAGACCTTACCTGACTCAACCTTAGGCGACTGTTATCATAAAGTCTCGCGAATATCTTAGAAACAGCGTGGAGCCCAGGGTGAGGCTCCGACATGCAATCATCGACAGGAGGATGTCGGTAACGACACACAAAGGGCAGACGGGCACTCCCACGTCTATCGTTGTAGGGCGTTAATGGATCGTGTGCCTTTAGCGTAACAAACACTCTACCGCGTAGACCCCTCTAAGTAGTTACTTGGTTCGAGGGAGTCACATATCTATACAACTGCACTTGCAACGTACAGGCAAGGCTCTTTCTCTTTAGAGCTTTGAACTAAATTTGCAGTATTGAAAAGGGTGTGTGGCGGGGATAGATCCTCTTGATACGATCGATGCGAAAGGACTACTCCGTAGATTACAATAGCACATAAGAATATAACCCCGGGCACCCATCGCTGGTTGGGATATCCGTTAGCTAACTACGCGCAGTAAAAAGGGCCTTAATTGAACGCCTCCTGATATTGGGGCTTTCACTCCAGATAGGAGGGGTTCGGTGCCTGTCTTATCTCTTGCGACAGTATCGATTTTGTTGCGCAAACCGGTATGCCTCTCAATTAAAGCTCTCCTTAGAATTCCTAATCATCGTAGTATCTTGCGCGCTACTTCCGCAGCTGGACAGATATGTAAAGAGTTTAAGACGAGGAAATCCGCTCGAACTTGGGTTTGACTAATTGGCTTTCCAACACTACCGTTTAGTCATGTGTAGACTACAAGGCCGGGGAGAATGACTGAACAAGGGTTAGTGAGTAA',
                             'CGAGGCCCATCCCAGGACGACCGCGTCTAACATGCTTATAGCTCTATAATCATAAAGACTCTTCCTCTGCACAAGCACAACGCTACTATACAGGGGGGTTTGCATCCATATTAGCGCGATCTCTAGGTGTAGTGACCATCGCCCATGTGGTCCCCCCAGAGCTGGAACCGGAGTGTTCAGCTCTCCGACGTTGGTGTAGAATTAGCGCAACTGTCCCGGCCGCAAACTTACCCTTGAAGTCGGGTCTACGTTAGAAGTAGCCGGTGCGGGAGGGTAATCAAGATGTCTTCACCTCGCATTTCCTGTTGGGCACATGTAGTGAGAAAGGATATTGCTAGCTCACGTCAGTCGAGATGGGACCTCGCTGAGCTTCTTCCAAAAAGGCAAACCCGGATCTGAAGGTTGACGAGTAAATGCAGACGTAGCACCGTCTCTGGTCAAGTCAGAACATGACCGACGTGGTTACTGTAACTCTACGAGCGATTGTCCGCTTTTGCCTTGGTGCCCGGTCACCTTTTAAGGACTCACCATCGGGAATTGGTGAGACCTAAGATCGATGAAAAGTCTGAAAACCAAGATGCCAAATATTAAACCCTACGGGTCCTTCTCCAATTATAAAACCGGGGTCACGTTAAGGTTTGTTCGCACACTCGGCCAAACTAGGAAATCCTAGAGCCATCCGAGTTAACACGTGTAAACCTCTATAGAAAAGCCCACCCTTCCGCAGTCATACCCGCTATGCCGTCTTAGTGAGGGGCGTTATTATAATACTAGCTGGGGGTCAAGCCATATAGCTCCGGCTGAGTCACATCACGCCGTCTGAGTTATTGTGCAGAATCTGTATATAACCCCATCCATTACACTTACAGTCTCCTTCATCGCGACCTCCAAGAGAGCAACTAGACTTACATACAACTGGTAACCGATCCTAATTAGATTCGCGACAAGATTGAGTGGTGGTAGCGCCCGCAACGAGTTCCCTAAGCAACTCTATCATCAACAG')

            self.assertEqual(distance_, 757)

    def test_neighborhood_1(self):
        n = distanceNeighborhood("AC", 1)
        self.assertCountEqual(n, ['CC', 'TC', 'GC', 'AC', 'AT', 'AG', 'AA'])


    def test_neighborhood_2(self):
        n = distanceNeighborhood("GGCCCAGAG", 3)
        self.assertCountEqual(n, ['ACC', 'ACT', 'CCA', 'TCA', 'ACA', 'GCA', 'ATA', 'AAA', 'AGA', 'ACG'])

if __name__ == '__main__':
    unittest.main()



