import Areaperi
import pytest

@pytest.mark.areasqarearectperirect
def testareaofsquare():
    sides= 4
    result = Areaperi.areaofsquare(sides)
    assert result == sides**2
@pytest.mark.areasqarearectperirect
def testperimeterofrectangle():
    length = 10
    breadth = 2
    result = Areaperi.perimeterofrectangle(length,breadth)
    assert result == 2*(length+breadth)
@pytest.mark.areasqarearectperirect
def testareaofectangle():
    length = 10
    breadth = 2
    result = Areaperi.areaofrectangle(length,breadth)
    assert result == length*breadth