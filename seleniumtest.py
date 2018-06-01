import os
import time
from selenium import webdriver

print('test start')
driver = webdriver.Remote(
		command_executor='http://172.18.0.9:4444/wd/hub',
		desired_capabilities={
			'browserName': 'firefox',
			'javascriptEnabled': True
		}
	)
driver.get('http://softwaretester.info/')
print('test end')
