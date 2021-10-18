import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/explicit_wait2.html"

try:

    browser = webdriver.Chrome()

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get(link)

    option = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button=browser.find_element_by_id("book")
    button.click()

   # driver = webdriver.Chrome()  # <- Путь до файла хромдрайвера
   # driver.get(link)
   # Ваш код, который заполняет обязательные поля

   # input1 = driver.find_element_by_css_selector("input.form-control:nth-child(2)")
   # input1.send_keys("Ivan")
   # input2 = driver.find_element_by_css_selector("input.form-control:nth-child(4)")
    #input2.send_keys("Ivanov")
   # input3 = driver.find_element_by_css_selector("input.form-control:nth-child(6)")
    #input3.send_keys("Ivanov@mail.ru")

   # current_dir = os.path.abspath(os.path.dirname(__file__))
    #file_path = os.path.join(current_dir, "111A.txt")
   # elements = driver.find_elements_by_css_selector("#file")

   # print(file_path)

   # elements.send_keys(file_path)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

   # // javascript
 #   button = driver.find_element_by_tag_name("button")
 #   driver.execute_script("return arguments[0].scrollIntoView(true);", button)
 #   button.click()

  #  input1 = driver.find_element_by_css_selector("#answer")
  #  input1.send_keys(y)


  #  y_element = driver.find_element_by_css_selector("#num2")
  #  y = y_element.text
  #  x = x_element.text
  #  a = int(x)+int(y)
  #  str(a)

#    from selenium.webdriver.support.ui import Select

#    Select = Select(driver.find_element_by_tag_name("select"))
 #   Select.select_by_isible_text(a)# ищем элемент с текстом "Python"

 #   driver.find_element_by_tag_name("select").click()
 #   driver.find_element_by_css_selector(f"[value='{a}']").click()

  #  input1 = driver.find_element_by_css_selector("#answer")
  #  input1.send_keys(a)

  #  option1 = driver.find_element_by_css_selector("#robotCheckbox")
  #  option1.click()

   # option2 = driver.find_element_by_css_selector("#robotsRule")
  #  driver.execute_script("return arguments[0].scrollIntoView(true);", option2)
  #  option2.click()

    # Отправляем заполненную форму
  #  button = driver.find_element_by_css_selector("button.btn")
   # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
   # time.sleep(1)

  #  alert = driver.switch_to.alert
  # alert.accept()

  #  new_window = driver.window_handles[1]
  #  driver.switch_to.window(new_window)

  #  x_element = driver.find_element_by_css_selector("#input_value")
   # x = x_element.text
   # y = calc(x)

  #  input1 = driver.find_element_by_css_selector("#answer")
  #  input1.send_keys(y)

   # button = driver.find_element_by_css_selector("button.btn")
   # button.click()
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
 #   assert "Congratulations! You have successfully registered!" == welcome_text


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
