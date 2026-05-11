seq = input()
seq = seq.upper()
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
dna = Seq(seq)
print ("Sequence:", dna)
print ("Length:" , len(dna))
if gc_fraction(dna) > 0.5 :
    print ("GC Content:", gc_fraction(dna) * 100, "%", "(High GC Genome!)")
else :
    print ("GC Content:", gc_fraction(dna) * 100, "%")
print ("Complement:", dna.complement())
print ("Reverse Complement:", dna.reverse_complement())
print ("RNA:", dna.transcribe())
print ("Protein:", dna.translate(to_stop = True))
