# Print a message to the screen.
message = "The message says 'Hello!'"
print(message)

message = "But now it says " + '"Goodbye!"'
print(message)

multiline_message = "This message\nis in two lines!"
print(multiline_message)

prefix = "AAA"
suffix = "GGG"
my_dna = prefix + "ATGC"
my_dna += suffix
print("my_dna: " + my_dna)
# print("my_dna:", my_dna)

my_dna_length = len(my_dna)
print("my_dna: " + str(my_dna_length) + " characters")
# print("my_dna:", my_dna_length, "characters")

my_dna = "ATGC"
print(my_dna.lower())

protein = "vlspadktnv"
print(protein.replace("v", "y"))
print(protein.replace("vls", "ymt"))
print(protein)

print(protein[3:5])
print(protein[0:6])
print(protein[0:60])
# print(protein[0:])

first_residue = protein[0]
print(first_residue)

protein = "vlspadktnv"
valine_count = protein.count("v")
lsp_count = protein.count("lsp")
tryptophan_count = protein.count("w")

print("valines:", valine_count)
print("lsp:", lsp_count)
print("tryptophan:", tryptophan_count)

print("first 'p' is at", protein.find("p"))
print("first 'kt' is at", protein.find("kt"))
print("there is no 'w' ->", protein.find("w"))
