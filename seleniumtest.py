from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
print("hello, Eric 3")



driver = webdriver.Remote(
	command_executor='http://selenium-hub:4444/wd/hub',
	desired_capabilities=DesiredCapabilities.CHROME)
