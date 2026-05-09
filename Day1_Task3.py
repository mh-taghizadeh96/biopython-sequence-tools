dna = input('Please Enter Your Sequence:')
dna = dna.upper()
gc = ((dna.count("G") + dna.count("C")) / len(dna) *100)
if gc > 50 :
    print ("High GC Content!")
else:
    print ("GC Content:", gc)

