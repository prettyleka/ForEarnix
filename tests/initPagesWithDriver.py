from SeleniumInfra.infra import SeleniumInfra
from pages.BasePage import BasePage
import init

class InitPagesWithDriver:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra().driver
        self.bp = BasePage()