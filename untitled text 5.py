s = 'ATGGAGGGTCAACGCTGGCTGCCGCTGGAGGCCAATCCCGAGGTCACCAACCAGTTTCTTAAACAATTAGGTCTACATCCTAACTGGCAATTCGTTGATGTATATGGAATGGATCCTGAACTCCTTAGCATGGTACCAAGACCAGTCTGTGCAGTCTTACTTCTCTTTCCTATTACAGAAAAGTATGAAGTATTCAGAACAGAAGAGGAAGAAAAAATAAAATCTCAGGGACAAGATGTTACATCATCAGTATATTTCATGAAGCAAACAATCAGCAATGCCTGTGGAACAATTGGACTGATTCATGCTATTGCAAACAATAAAGACAAGATGCACTTTGAATCTGGATCAACCTTGAAAAAATTCCTGGAGGAATCTGTGTCAATGAGCCCTGAAGAACGAGCCAGATACCTGGAGAACTATGATGCCATCCGAGTTACTCATGAGACCAGTGCCCATGAAGGTCAGACTGAGGCACCAAGTATAGATGAGAAAGTAGATCTTCATTTTATTGCATTAGTTCATGTAGATGGGCATCTCTATGAATTAGATGGGCGGAAGCCATTTCCAATTAACCATGGTGAAACTAGTGATGAAACTTTATTAGAGGATGCCATAGAAGTTTGCAAGAAGTTTATGGAGCGCGACCCTGATGAACTAAGATTTAATGCGATTGCTCTTTCTGCAGCATAG'


print(len(s))

count = 0
for i in range(len(s) - 1):
    if s[i] == 'C' and s[i+1] == 'G':
        count += 1

print (count)

print (s[:3])




            
            
           
                      
            