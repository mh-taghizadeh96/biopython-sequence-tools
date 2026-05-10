def count_base (seq) :
    a = seq.count("A")
    g = seq.count("G")
    c = seq.count("C")
    t = seq.count("T")
    print ("A count:", a)
    print ("G count:", g)
    print ("C count:", c)
    print ("T count:", t)

dna = "AGCTGCATCGATCGATCGCTCAGT"
count_base(dna)