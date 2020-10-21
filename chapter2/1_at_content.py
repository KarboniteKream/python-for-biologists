DNA_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

num_AT = DNA_seq.count("A") + DNA_seq.count("T")
AT_content = (num_AT / len(DNA_seq)) * 100

print(f"The AT content of the given DNA sequence is {round(AT_content, 2)}%.")
