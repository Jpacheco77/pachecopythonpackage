from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os

"""
This module performs a blast search with a fasta file.

fasta_path > filepath to the fasta file
results_path > filepath to the .xml output file.

"""
def sequence_blaster(fasta_path, results_path):
 
    assert os.path.exists(fasta_path), 'no such filepath exists'
    
    record = SeqIO.read(fasta_path, format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    
    save_file = open(results_path, "w")
    save_file.write(result_handle.read())
    save_file.close()

    
    assert os.path.getsize(results_path) != 0
    #assert there is no memory leak
    