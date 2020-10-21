# Relativno glede na to, kje je TA (0_lesson.py) file.
# OZIROMA iz kjer pozenes program.

# desktop
# |- lessons
#    |- 0_lesson.py
# |- files
#    |- dna.txt

# v- smo v terminalu
# $ (desktop): python3 lessons/0_lesson.py

# ------------------------------------------------------------------------------

# ko bos delala sama, imej vse v mapi "chapter3" (brez presledkov)
# ko klices open(), uporabi tako kot tukaj, da bo "play" gumb delal
my_file = open("chapter3/dna.txt")

# to izpise samo informacije o datoteki, ne pa direktno vsebine
# print(my_file)

# za izpis CELOTNE vsebine
vsebina = my_file.read()
print("<" + vsebina + ">")

# vsakic ko preberemo vsebino, zelimo se "spucati" besedilo
# stran damo prazne vrstice in presledke na zacetku in koncu
vsebina = vsebina.lstrip("\n")
vsebina = vsebina.rstrip("\n")
print("<" + vsebina + ">")

#                             palica se zvrne k naslednji crki
#                             forward slash
moja_datoteka = open("chapter3/vrstice.txt")
vrstice = moja_datoteka.read()

print("<" + vrstice + ">")

# "representation", izpise kar je "dejansko" v spremenljivki
print(repr(vrstice))

#                        backward slash
vrstice = vrstice.strip("\n")
print(repr(vrstice))

# lstrip, rstrip in strip (l+r) odstrani N znakov iz cistega zacetka oz cistega konca stringa
# ce strip() nima argumentov npr. strip(), odstrani presledke, nove vrstice itd

#                  tabulator
sporocilo = "    \n\t    tami rada   programira!          \n\n\n\n\n".strip()
print("<" + sporocilo + ">") # -> "<tami rada   programira!>"

# ali na kratko:
vsebina = open("chapter3/dna.txt").read().strip()
#         ------------------------ vrne "nekaj" tipa file, na katerem lahko klicemo read()
#         ------------------------------- vrne "nekaj" tipa string, na katerem lahko klicemo strip()
# vse skupaj lahko "ovijemo" z len(), da dobimo dolzino vsebine (fajla) -> "nekaj" tipa int(eger), kar lahko potem shranimo v spremenljivko, ki bo tipa int
# torej lahko nizamo funkcije, dokler imamo ustrezen tip
# npr: dolzina = len("\n\ntami!!!".strip()) + len("klemen" + "julijan") + 3
# opomba: len("\n") == 1
# opomba: = je "assignment" (spremenljivki dolocimo vrednost), == pomeni enacenje (equals)
print(vsebina)
print() # da imamo prazno vrstico




# PISANJE V DATOTEKE                                                        mode (read)
input_file = open("chapter3/dna.txt") # enako kot: open("chapter3/dna.txt", "r")
print(input_file)

#                                         mode (write)
# opomba: 'w' (write): prepise obstojeco vsebino
#                      -> vsakic ko zapres datoteko, program staro vsebino overwrite z novo
#         'a' (append): pripne obstojeci vsebini (redko uporabljamo!)
#                       -> nova vsebina se doda stari (na konec datoteke), kot da pises diplomo
output_file = open("chapter3/output.txt", "w")
output_file.write("klemen\n") # write() ni tako kot print(), zato sprejme samo en argument write("klemen", "\n") bo napaka: "TypeError: write() takes exactly one argument (2 given)"
output_file.write("tami\n")
output_file.write("mami\n")
output_file.write("ati\n")
output_file.close() # ko nehas pisati v datoteko, jo vedno zapri! ce pozabis close() in program crkne med izvajanjem, ni nujno, da se vse shrani/zapise

#                                         mode (append)
output_file = open("chapter3/output.txt", "a")
output_file.write("darjan\n")
output_file.close()
