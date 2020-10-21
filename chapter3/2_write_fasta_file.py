header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence2 = "actgatcgacgatcgatcgatcacgact"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

output_file = open("fasta_file.fasta", "w")

sequence3 = sequence3.replace("-", "")

output_file.write(f">{header1}\n{sequence1}\n")
output_file.write(f"\n>{header2}\n{sequence2.upper()}\n")
output_file.write(f"\n>{header3}\n{sequence3}")
output_file.close()
