import pytest
import  logging

log = logging.getLogger(__name__)
filehandler = logging.FileHandler("test.log")
format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")

filehandler.setFormatter(format)

log.addHandler(filehandler)
log.setLevel(logging.INFO)


def test_display_out(input_data):
      log.info("Hello world , this is %s and url is %s"%(input_data[0], input_data[1]))

#class level
@pytest.mark.usefixtures("input_data")
class Test_Demo:
    #when we need input from fixture , it should also be passed as argument to funtion in class
    def test_display_class(self, input_data):
        print("\n Hello "+ input_data[0] + ' Url is :'+ input_data[1])
    def test_simple_class(self):
        print("\nThis is simple class fun")

#parameterised fixture
@pytest.mark.usefixtures("input_data_param")
class Test_Fix:
    def test_param(self, input_data_param):
        print("This is %s"%input_data_param)