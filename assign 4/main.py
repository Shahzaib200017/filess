from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")

driver.find_element_by_id("username").send_keys("F2019065229")

driver.find_element_by_id("password").send_keys("*Shahzaib171100*")

driver.find_element_by_id("loginbtn").click()

Sub = driver.find_elements_by_class_name("list-group-item list-group-item-action  ")

subject_list = []

for s in range(len(Sub)):

    print(subject_list.append(Sub[s].text))