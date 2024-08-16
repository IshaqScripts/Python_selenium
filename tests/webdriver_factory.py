from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
#from selenium.webdriver.opera.service import Service as OperaService

class WebDriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name.lower() == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        elif browser_name.lower() == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service)
        elif browser_name.lower() == 'edge':
            service = EdgeService(EdgeChromiumDriverManager().install())
            return webdriver.Edge(service=service)
        elif browser_name.lower() == 'opera':
            service = OperaService(OperaDriverManager().install())
            return webdriver.Opera(service=service)
        elif browser_name.lower() == 'safari':
            return webdriver.Safari()
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")
