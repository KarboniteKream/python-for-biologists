# 1. Preberi DNK iz "dna1.txt".
# 2. Izpisi prvih in zadnjih 12 znakov DNK.
# 3. Deseti in enajsi nukleotid v zaporedju nakazujeta mesto prereza. Mesto se imenuje XY.
# 4. Vsako zaporedje GGG v DNK med dvema nukleotidoma XY zamenjaj z zvezdico. --> Iščemo XYGGGXY, samo GGG se zamenja z zvezdico (pri vseh CTGGGCT).
# 5. Izpisi mesto prve in druge zvezdice v DNK.
# 6. Izpisi stevilo zvezdic.
# 7. Odstrani zvezdice iz zaporedja in poisci razliko v dolzini zacetnega in koncnega DNK.
# 8. Koncno zaporedje shrani v datoteko "new_dna1.txt".

dna = open("dna1.txt", "r")
dna = dna.read().strip().upper()

first12 = dna[0:12]
print(f"Prvih 12 znakov: {first12}")
last12 = dna[(len(dna) - 12):]
print(f"Zadnjih 12 znakov: {last12}")

resite = dna[9] + dna[10]
print(f"Mesto prereza XY je {resite}.")

reseq = resite + "GGG" + resite
reseq_star = resite + "*" + resite
dna = dna.replace(reseq, reseq_star)
print(dna)

star1_index = dna.find("*")
star2_index = dna.find("*", star1_index + 1)
print(f"Prva zvezdica se nahaja na indeksu {star1_index}.")
print(f"Druga zvezdica se nahaja na indeksu {star2_index}.")

num_star = dna.count("*")
print(num_star)

dna_new = dna.replace("*", "")
new_len = len(dna_new)
print(f"Dolžina novega DNA zaporedja je {new_len}.")
old_len = new_len + (3 * num_star)
print(f"Dolžina starega DNA zaporedja je {old_len}.")
print(f"Razlika med dolžinama obeh zaporedij je {old_len - new_len}.")

output_file = open("new_dna1.txt", "w")
output_file.write(dna_new)
output_file.close()
