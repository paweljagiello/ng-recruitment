from selenium import webdriver
import pytest

#Tests if correct message is shown when name field is left empty.
def test_required_field_username():
    name = "Adam"
    email = "testest@test.pl"
    password = "Qwerty123"

    driver = webdriver.Chrome()
    #Website prepared by me - sample registration form for this task.
    driver.get("http://boogie-town.pl/netguru_example_registration_form/")

    field_name = driver.find_element_by_id("text-WPw5th")
    field_name.send_keys(name)

    field_email = driver.find_element_by_id("text-EAu5dZ")
    field_email.send_keys(email)

    field_password = driver.find_element_by_xpath('//*[@id="text-APOuTW"]')
    field_password.send_keys(password)

    field_password_confirm = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[1]/div/form/div[1]/div/div[6]/input")
    field_password_confirm.send_keys(password)

    confirm = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[1]/div/form/div[4]/div/button")
    confirm.click()

    message = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[1]/div/form/div[1]/div/div[2]/ul/li").text
    assert message == "This value is required."


#Tests if password is encrypted after typing it.
def test_password_encryption():
    password = "Qwerty123"

    driver = webdriver.Chrome()
    # Website prepared by me - sample registration form for this task.
    driver.get("http://boogie-town.pl/netguru_example_registration_form/")

    field_password = driver.find_element_by_xpath('//*[@id="text-APOuTW"]')
    field_password.send_keys(password)
    text1 = field_password.text

    field_password_confirm = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[1]/div/form/div[1]/div/div[6]/input")
    field_password_confirm.send_keys(password)
    text2 = field_password_confirm.text

    assert text1 == "" and text2 == ""