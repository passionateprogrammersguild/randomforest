from .node import *

class InvalidArgumentException(Exception):
    pass

def _validate(isfeature, isylabel):
    exceptions = []
    if type(isfeature) != type([]):
        exceptions.append("must supply a list as the first argument")

    if type(isylabel) != type([]):
        exceptions.append("must supply a list as the second argument")

    if type(isfeature) == type([]) and len(isfeature) == 0:
        exceptions.append("must supply a non-empty list as the first argument")

    if type(isylabel) == type([]) and len(isfeature) == 0:
        exceptions.append("must supply a non-empty list as the second argument")
    
    if len(exceptions) > 0:
        raise InvalidArgumentException('\n'.join(exceptions))

def _compute(total, count, f, y, p1, p2):

    if p1(f):
        total +=1

        if p2(y):
            count +=1

    return total, count
    

def _getTotalAndCount(isfeature, isylabel, p1):
    total = 0
    count = 0
    
    p2 = lambda x: x == 1

    #compute the percentage where the value is 0 and the corresponding ylabel is 1    
    for i, f in enumerate(isfeature):
        y = isylabel[i]

        total, count = _compute(total, count, f, y, p1, p2)
    
    return total, count

def _getNode(direction, isfeature, isylabel, fn):
    total, count = _getTotalAndCount(isfeature, isylabel, fn)

    if total == 0:
        return None

    return Node(direction, total, count/(total * 1.0))


class Evaluator(object):

    '''
    The feature is a vector of 1/0 for off and on
    The ylabel is a vector of 1/0 for off and on

    We need to compute the metric
    '''
    def evaluate(self, isfeature, isylabel):
        
        _validate(isfeature, isylabel)

        '''
        return a structure of Node
        which has a Direction, number of observations, purity
        '''
        left  = _getNode(LEFT, isfeature, isylabel, lambda x: x == 0)
        right = _getNode(RIGHT, isfeature, isylabel, lambda x: x == 1)

        return left, right