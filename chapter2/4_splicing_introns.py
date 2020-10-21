DNA_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = DNA_seq[:63]
exon2 = DNA_seq[90:]
print(f"The coding sequence of the given DNA sequence is {exon1 + exon2}.")


coding = len(exon1 + exon2)

coding_percentage = (coding / len(DNA_seq)) * 100
print(f"{round(coding_percentage, 2)}% of the DNA sequence is coding.")


new_DNA = exon1 + (DNA_seq[63:90]).lower() + exon2
print(new_DNA)
