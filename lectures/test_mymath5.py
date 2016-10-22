from pytest import fixture
import io
#from docs
@fixture
def file_data(request): # The fixture MUST have a 'request' argument
    text = open("test_mymath5.py")

    @request.addfinalizer
    # just to free up memory
    def teardown():
        text.close()
    return text

def test_data_type(file_data):
    assert isinstance(file_data, io.TextIOWrapper)