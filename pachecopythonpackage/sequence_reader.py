import dendropy
import os

def sequence_reader(filepath):
    
    assert os.path.exist(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
    path=filepath, 
    schema="phylip"
)
   
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
