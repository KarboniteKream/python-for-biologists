DNA_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

DNA_seq = DNA_seq.replace("A", "t")
DNA_seq = DNA_seq.replace("T", "a")
DNA_seq = DNA_seq.replace("G", "c")
DNA_seq = DNA_seq.replace("C", "g")

new_DNA = DNA_seq.upper()
print(f"The complementing sequence of the given DNA sequence is {new_DNA}.")
