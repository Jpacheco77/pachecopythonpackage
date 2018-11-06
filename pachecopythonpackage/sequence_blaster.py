def sequence_blaster(fasta_path, results_path):

    from Bio.Blast import NCBIWWW
    from Bio import SeqIO
    import os
    
    assert fasta_path is fast
    
    record = SeqIO.read(fasta_path, format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    
    save_file = open(results_path, "w")
    save_file.write(result_handle.read())
    save_file.close()

    assert os.path.exists(results_path)
    assert os.path.getsize(results_path) != 0
    #assert there is no memory leak
    