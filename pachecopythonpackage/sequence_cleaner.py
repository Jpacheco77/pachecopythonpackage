import dendropy

def sequence_cleanup(sequence_set, out_file, taxon, gene):
    assert taxon == sequence_set[taxon], 'the taxon is not present in the dataset'
    assert gene == sequece_set[taxon.gene]
    #assert end and beginning
    
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence[int(gene[0]) : int(gene[1])]
    ofile = open(outfile, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
    
    assert os.path.getsize(out_file) > 0
    

