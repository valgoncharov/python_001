import pytest

def test_first():
    pass

def test_first1():
    assert 1 == 1

def test_second():
    assert 1 == 2, "Единица не должна быть равна двойке"

@pytest.fixture(scope='session', autouse=True)
def before_all(request):
    print("Called before al tests " + request.node.name)

    @pytest.fixture()
    def driver():
        pass

    @pytest.fixture()
    def config():
        pass

    @pytest.fixture()
    def firefox(driver, config):
        return ""
