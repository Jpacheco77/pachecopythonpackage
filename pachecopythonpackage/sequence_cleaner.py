import dendropy
import os

def sequence_cleaner(sequence_set, out_file, taxon, init_gene, end_gene):

    """
    This module takes in a list of sequences in phylip format and then by specifying 
    a taxon as well as a begginning and end posistion for a gene creates a fasta formatted
    file for that gene
    
    sequence set > input filepath sequence in phylip format
    out_file > ouptut filepath for the fasta file
    init_gene > position in the genome for the first nucleotide in a sequence/genome
    end_gene > position in the genome for the last nucleotide in a sequence/genome
    
    """
    
    
    assert type(init_gene) == int, 'initial nucleotide position is not an integer'
    assert type(end_gene) == int, 'final nucleotide position is not an integer'
    
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    
    #for index in my_taxon_sequence:
        #assert taxon == my_taxon_sequence[index], 'the taxon is not present in the dataset'
    
    #assert end_gene < len(my_taxon_sequence[taxon]), 'ending nucleotide exceeds genome lenght'
    
    """
    module still requires an assertion to check the presence of selected taxon and asserting     if the final nucleotide position exceeds the genome size. 
    """
    
    my_taxon_gene = my_taxon_sequence[init_gene : end_gene]
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_gene + "\n")
    ofile.close()
    
    assert os.path.getsize(out_file) != 0
    

