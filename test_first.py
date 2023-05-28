from urllib import request


def test_first():
    pass


def test_first():
    assert 1 == 1


def test_second():
    assert 1 == 2, "Единица не должна быть равна двойке"


import pytest


@pytest.fixture()
def before_each():
    print("Called before each test" + request.node.name)

    def test_first1(before_each):
        assert 1 == 1


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
