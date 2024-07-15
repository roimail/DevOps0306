from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
#driver.get("https://github.com")
driver.get("file:///home/roy/Downloads/tip_calc/index.html")

billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
driver.find_element(by="id", value="peopleamt").send_keys("8")
driver.find_element(by="id", value="musicQual").send_keys("1")
driver.find_element(by="id", value="calculate").click()

expected = "2.88"
actual = driver.find_element(by="id", value="tip").text

# can use if/else
if expected != actual:
    print("failed")
else:
    print("passed")

# or alternatively use assert (it get boolean, if true it continues, otherwise it BREAKS code)
assert expected == actual, "Not what was expected"

sleep(5)