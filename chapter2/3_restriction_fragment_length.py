DNA_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoRI = "GAATTC"

num_res_site = DNA_seq.count(EcoRI)
res_site = DNA_seq.find(EcoRI)

frag1 = DNA_seq[:res_site + 1]
frag2 = DNA_seq[res_site + 1:]

print(f"The sequence of fragment 1 is {frag1}, and the sequence of fragment 2 is {frag2}.")
