# Use "genomic_dna.txt"

genomic_DNA = open("genomic_dna.txt", "r")
genomic_DNA = genomic_DNA.read().strip()

coding = genomic_DNA[:63] + genomic_DNA[90:]
noncoding = genomic_DNA[63:90]

new_DNA_c = open("coding_DNA.txt", "w")
new_DNA_c.write(coding)
new_DNA_c.close()

new_DNA_nc = open("noncoding_DNA.txt", "w")
new_DNA_nc.write(noncoding)
new_DNA_nc.close()
