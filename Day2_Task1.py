dna = "ATGGCCATTAGGGGTAAATAA"
genetic_code = {"ATG": "M", "GCC": "A", "ATT": "I", "AGG": "R", "GGT": "G", "AAA": "K", "TAA": "*"}
protein = ""
for i in range(0, len(dna), 3):
    codon = dna[i : i+3]
    print ("Reading Codon:", codon)
    if codon in genetic_code:
        amino_acid = genetic_code[codon]
        if amino_acid == "*":
            break
        protein += amino_acid
print("Protein:", protein)