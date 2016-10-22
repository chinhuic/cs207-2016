

from pytest import fixture
from mymath import myaverage, mymedian


@fixture
def input_data():
    return dict(b=[4,5,6], a=['a', 1,2])

# input data is the output of the data
def test_with_fixture(input_data):
    assert myaverage(input_data['b']) == 5
    assert mymedian(input_data['b']) == 5