from Bio import SeqIO
from Bio.Blast import NCBIXML
import os

"""
This function takes an .xml input file from a blast search and helps to visualize the results, providing information about the sequence that matched, the lenght of said sequence and its e-value.

Arguments:
input_file > filepath to the .xml file with the blast search results
e_value_tresh > treshold for the e-values to display.
"""
def sequence_ev_parser(input_file, e_value_tresh):
    
    assert e_value_tresh != 0
    assert os.path.exists(input_file), 'input filepath does not exist'
    
    parsed = NCBIXML.read(open(input_file))
    alignment_set = parsed.alignments
    for individual_alignment in alignment_set:
        for hsp in individual_alignment.hsps:
            if hsp.expect < e_value_tresh:
                print('****Alignment****')
                print('sequence:', individual_alignment.title)
                print('length:', individual_alignment.length)
                print('e value:', hsp.expect)
                print(hsp.query[0:75] + '...')
                print(hsp.match[0:75] + '...')
                print(hsp.sbjct[0:75] + '...')