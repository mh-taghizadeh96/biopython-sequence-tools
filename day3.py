def hello() : #Defining a function
    print ("Hello Bioinformatics")
hello()

def print_sequence(dna) : #Function with input
    print(dna)
print_sequence("ATGCGT")

def get_length(dna) : #Return value
    return len(dna)
length = get_length("ATGC")
print(length)

#GC Function
def gc_content(dna) :
    g = dna.count ("G")
    c = dna.count ("C")
    gc = (g+c) / len(dna) *100
    return gc
seq1 = "ATGTGCAGCGAGCT"
print ("GC Content:" , gc_content (seq1))

#Multiple Functions
print (get_length(seq1))
print (gc_content(seq1))

#FASTA files
file = open ("example.fasta") #open() opens file for reading
content = file.read ()
print (content)
file.close ()

#How to separate header of a fasta file (>) and its content (sequence)?
file = open ("example.fasta")
lines = file.readlines()
header = lines[0]
sequence = lines[1]
print (header)
print (sequence)
file.close()

#First FASTA Ananlyzer
def gc_content (dna) :
    g = dna.count ("G")
    c = dna.count ("C")
    gc = (g + c) / len(dna) * 100
    return gc
file = open ("example.fasta")
lines = file.readlines()
header = lines[0].strip()
sequence = lines[1].strip()
file.close()
result = gc_content (sequence)
print ("Header:", header)
print ("Sequence:", sequence)
print ("Length:", len(sequence))
print ("GC Content:", result)

#Modern Python Style!
with open("example.fasta") as file:
    lines = file.readlines()
    header = lines[0].strip()
    sequence = lines[1].strip()
    print (sequence) #This method does not need a file.close and closes the file automatically
