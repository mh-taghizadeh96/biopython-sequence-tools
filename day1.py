print('hello bioinformatics') #print

dna = "ATGCGTAA" #String
print(dna) #Print a string

print(len(dna)) #Lenght function

print (dna [0]) #starting with zero, python gives numbers to each member of a string
print(dna [1])
print(dna [7])

print(dna[0:3]) #Slicing a sequence

print(dna.count("G")) #Count function

g = dna.count("G") #Calculating gc content
c = dna.count("C")
gc_cont = (g + c) / len(dna) *100
print (gc_cont)

complement = dna.replace("A" , "t") #Complement basic method
complement = complement.replace("T" , "a")
complement = complement.replace("G" , "c")
complement = complement.replace("C" , "g")

print(complement.upper())

#First Script
print ('First Script')
dna = "ATGCGCGCTA"
print ("Sequence:", dna)
print ("Length:", len(dna))
print ("G Count:", dna.count("G"))
print ("C count:", dna.count("C"))
gc = (dna.count("G") + dna.count("C") / len(dna) * 100)
print ("GC Content:", gc)
