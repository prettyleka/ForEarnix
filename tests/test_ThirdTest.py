import pytest as pytest
from ForEarnix.tests.initPagesWithDriver import init

class TestThirdTest:
    def setup_class(self):
        self.initial = init.pageWithDriver()

    def test_ThirdTest(self):
        self.initial.goTo.bp.moveToSite("https://demo.nopcommerce.com/")
        self.initial.goTo.lp.hoverOnNotMobileTab("computers")
        self.initial.goTo.lp.clickOnNitMobileComputerMenuBtns("notebooks")
        sumHiddenIds=self.initial.goTo.pg.sumOfHiddenIds()
        assert sumHiddenIds>5
        self.initial.goTo.seleniumInfra.close()


if __name__ == '__main__':
    import sys, inspect, os

    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    class_name = getattr(sys.modules[__name__], clsmembers[0][0])
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    method_list = [func for func in dir(class_name) if
                   callable(getattr(class_name, func)) and not func.startswith("__") and func.startswith("test")]
    function_dict = {}
    function_dict["0"] = "run all tests"
    for i in range(1, len(method_list) + 1):
        function_dict[str(i)] = method_list[i - 1]
    print(function_dict)
    txt = input("please choose test you want to run or debug and then press enter")
    command = "-v " + module_name + ".py::" + clsmembers[0][0] + "::" + function_dict[txt] + ""
    if txt != "0":
        pytest.main(command.split(" "))
    else:
        pytest.main(["-v", module_name + ".py"])