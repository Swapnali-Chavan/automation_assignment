from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
timeout = 5

def open_website():
    driver = webdriver.Chrome(executable_path="C:\\Users\\schava\\Downloads\\chromedriver.exe")
    # driver.get("http://10.100.171.218:3000")
    driver.get("http://localhost:3000/")
    return driver

def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//label[text()='Email']/../div//input")
    username_field.send_keys(username)
    time.sleep(1)
    password_field = driver.find_element(By.XPATH, "//label[text()='Password']/..//div//input")
    password_field.send_keys(password)
    time.sleep(1)
    login_button = driver.find_element(By.XPATH, '//div/button[text()="Login"]')
    login_button.click()
    time.sleep(timeout)

def check_if_name_is_present(driver,search_name):
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(search_name)
    arr_elements = []
    for _ in range(3):
        name_elements = driver.find_elements(By.XPATH, '//div[@data-field="name" and @role="cell"]/div')
        arr_elements.extend([i.text for i in name_elements])
        last_element = name_elements[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", last_element)
        time.sleep(1)

def scroll_to_top(driver):
    action = ActionChains(driver)
    print("Scrolling to top")
    while True:
        for_parent_of_first = driver.find_elements(By.XPATH, "//div[@data-rowindex = '1']")
        res = driver.find_elements(By.XPATH, '//div[@data-field="name"]/div[text()]')
        action.scroll_to_element(res[0]).perform()
        if for_parent_of_first:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "1"]/div[@data-field="name"]/div[text()]')
            break
        time.sleep(timeout)

def check_sort_asc(driver):
    element_to_hover = driver.find_element(By.XPATH, "//div[@aria-label='Name']")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(1)
    sort_button = driver.find_element(By.XPATH, "(//div//button[@aria-label='Sort'])[1]")
    sort_button.click()
    time.sleep(1)
    arr_list = []
    while True:
        name_elements = driver.find_elements(By.XPATH, "//div[@data-field='name' and @data-colindex='0']//div")
        current_elements = [i.text for i in name_elements]
        time.sleep(1)
        arr_list.extend(current_elements)
        last_element = name_elements[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", last_element)
        # Break out of the loop if all elements have been collected
        if len(arr_list) >= 20:  
            break
    is_sorted_ascending = current_elements == sorted(current_elements)
    print("Column is sorted in ascending order:", is_sorted_ascending)

def check_sort_desc(driver):
    element_to_hover = driver.find_element(By.XPATH, "//div[@aria-label='Name']")
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(1)
    sort_button = driver.find_element(By.XPATH, "(//div//button[@aria-label='Sort'])[1]")
    sort_button.click()
    time.sleep(1)
    arr_list = []
    while True:
        name_elements = driver.find_elements(By.XPATH, "//div[@data-field='name' and @data-colindex='0']//div")
        current_elements = [i.text for i in name_elements]
        time.sleep(1)
        arr_list.extend(current_elements)
        time.sleep(1)
        last_element = name_elements[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", last_element)
        time.sleep(1)
        # Break out of the loop if all elements have been collected
        if len(arr_list) >= 20:  
            break
    is_sorted_descending = current_elements == sorted(current_elements, reverse=True)
    print("Column is sorted in descending order:", is_sorted_descending)

if __name__ == "__main__":
    driver = open_website()
    time.sleep(2)
    print("Website open")
    login(driver, 'swapnali@gmail.com', 'abc1234')
    print("User is logged in application")
    check_if_name_is_present(driver, "ric")
    print("User is searching")
    scroll_to_top(driver)
    check_sort_asc(driver)
    scroll_to_top(driver)
    check_sort_desc(driver)