dna = "ATGGCCATT"
for base in dna : #First "for" loop
    print (base)

print('G Count') #Counting G bases
g_count=0
for base in dna :
    if base == "G" :
        g_count += 1
print (g_count)

print ('Codon Extraction') #Extracting Codons
for i in range( 0, len(dna), 3) :
    codon = dna[i : i+3]
    print (codon)

genetic_code = {"ATG" : "M", "GCC" : "A", "ATT": "I"} #First Dictionary
print(genetic_code["ATG"])



#First Tranlator
protein = ""
for i in range (0, len(dna), 3):
    codon = dna[i : i+3]
    if codon in genetic_code :
        protein += genetic_code[codon]
print (protein)

#Expanded Dictionary
genetic_code = {"ATG": "M", "GCC": "A", "ATT": "I", "TTT": "F", "TAA": "*"} # "*" means stop codon

#Detecting Stop Codons
dna = "ATGGCCTAA"
protein = ""
for i in range (0, len(dna), 3) :
    codon = dna[i : i+3]
    if codon in genetic_code:
        amino_acid = genetic_code[codon]
        if amino_acid == "*":
            break
        protein += amino_acid
print ("Protein:", protein)

#In order to check whether the codon is inside the dictionary or not, we may use a code like below:
# if codon in genetic_code:
#This returns as True or False, So we may indicate if the program is gonna run or crash
