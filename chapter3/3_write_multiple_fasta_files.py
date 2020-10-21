header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence2 = "actgatcgacgatcgatcgatcacgact"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

sequence3 = sequence3.replace("-", "")

output_file1 = open("ABC123.fasta", "w")
output_file2 = open("DEF456.fasta", "w")
output_file3 = open("HIJ789.fasta", "w")

output_file1.write(f">{header1}\n{sequence1}")
output_file2.write(f">{header2}\n{sequence2.upper()}")
output_file3.write(f">{header3}\n{sequence3}")

output_file1.close()
output_file2.close()
output_file3.close()
