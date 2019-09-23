## import Local packages
import sys
from pathlib import Path
sys.path.append(str(Path.home())+'/Documents/PROYECTOS/rnaStrComp/code/src')
from py_packages.dataModel.datamodels import RNAStructure

import unittest


example1 = ''' >sHP
               AAACCCCGUUU
               ((((...))))
            ''' 


class Test1(unittest.TestCase):
    
    def test_basepairs_count(self):
        self.assertEqual( len(RNAStructure(example1).basepairs) , 4)
        
        

if __name__ == '__main__':
    unittest.main()