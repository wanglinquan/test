from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({'name':'BAIDUID','value':'7CB3C547740B64736D0ADBC1EFBAF760:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'pNRXJMU0pPdVo1QXdIWWdJdkE1QkFSLUgyV1dNRVh4T2VheDJ1M09RODdPTHRaTVFBQUFBJCQAAAAAAAAAAAEAAADxtNI3AAAAAA \
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADurk1k7q5NZcE'})

driver.refresh()

username = driver.find_element_by_class_name("user-name").text
print(username)

driver.quit()

driver.find_element_by_id()