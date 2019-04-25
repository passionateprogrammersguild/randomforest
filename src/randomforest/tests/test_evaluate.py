'''
The intent of the test is to create an instance of the DecisionTree
'''
import pytest

from randomforest.evaluator import Evaluator, InvalidArgumentException

@pytest.fixture
def evaluator():
    return Evaluator()

def test_list_must_be_provided(evaluator):
    with pytest.raises(InvalidArgumentException):
        evaluator.evaluate(1,2)

def test_empty_list(evaluator):
    with pytest.raises(InvalidArgumentException):
        evaluator.evaluate([],[])

def test_leftnodeisnone(evaluator):
    left, right = evaluator.evaluate([1],[1])
    assert left == None

    assert right.purity == 1.0

def test_rightnodeisnone(evaluator):
    left, right = evaluator.evaluate([0],[1])
    assert right == None

    assert left.purity == 1.0    
    