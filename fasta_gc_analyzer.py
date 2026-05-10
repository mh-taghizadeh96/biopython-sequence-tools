with open ("example.fasta") as file:
    lines = file.readlines()
    header = lines[0].strip()
    sequence = lines[1].strip()
    print ("Sequence:", sequence)
    print ("Length:", len(sequence))
    gc_content = (sequence.count ("G") + sequence.count ("C")) / len(sequence) *100
    if gc_content > 60 :
        print ("High GC Content!")
    else:
        print ("GC Content:", gc_content, "%")
