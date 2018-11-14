import dendropy
import os

"""
This function reads in a file in phylip format and returns DnaCharacterMatrix.

filepath > filepath to the file in phylip format.
"""

def sequence_reader(filepath):
    
    assert os.path.exists(filepath), 'no such filepath exists'
    sequence_set = dendropy.DnaCharacterMatrix.get(
    path=filepath, 
    schema="phylip"
)
   
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)