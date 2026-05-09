dna = "ATGGGCCCTTAA"
l = len(dna)
print ("Length:", l)
g = dna.count("G")
print ("G Count:", g)
#GC Content
c = (dna.count("C"))
gc = ((g + c) / l *100)
print ("GC Content:", gc)