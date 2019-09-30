def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2)) 


class RNAStructure:
    ''' Class to model a RNA dot bracket notation structure'''
    def __init__(self , vienna):
        lines = vienna.split('\n')
        self.name = lines[0].strip()
        self.sequence = lines[1].strip()
        self.structure = lines[2].strip()
        self.basepairs = sorted(self.parse_basepairs(lines[2].strip()))


    def parse_basepairs(self, dotbracket):
        stack = []
        bp5 = []
        bp3 = []
        for i , char in enumerate( dotbracket ):
            if char == '(':
                stack.append(i)
                bp5.append(i)
            elif char == ')':
                j = stack.pop()
                bp3.append(i)
        #yield(j,i)
        if not stack:
            bp3.reverse()
            return(listOfTuples(bp5, bp3))
        else: print("Error: inconsistency detected at the input dot bracket notation")
