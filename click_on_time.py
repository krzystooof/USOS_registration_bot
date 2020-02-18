import time
from selenium import webdriver
from datetime import datetime

driver = webdriver.Firefox()
user_login = "enter your login in .py file"
user_password = "enter your password in .py file"
login_address = "https://usosweb.amu.edu.pl/kontroler.php?_action=logowaniecas/index"
home_address = "https://usosweb.amu.edu.pl/kontroler.php?_action=dla_stud/rejestracja/kalendarz"


def click_button(target_time):
    while target_time > time.time():
        pass

    button_type = "submit"
    button_value = "Rejestruj"
    xpath = "//input[@type='" + button_type + "' and @value='" + button_value + "']"
    button = driver.find_element_by_xpath(xpath)
    button.click()
    print("Przycisk nacisniety o " + str(datetime.now().time()))


def login_usos(adress, login, password):
    driver.get(adress)

    input_type = "text"
    input_name = "username"
    xpath = "//input[@type='" + input_type + "' and @name='" + input_name + "']"
    site_input = driver.find_element_by_xpath(xpath)
    site_input.send_keys(login)

    input_type = "password"
    input_name = "password"
    xpath = "//input[@type='" + input_type + "' and @name='" + input_name + "']"
    site_input = driver.find_element_by_xpath(xpath)
    site_input.send_keys(password)

    button_type = "submit"
    button_name = "submit"
    button_class = "btn btn-sm btn-outline-secondary"
    xpath = "//button[@class='" + button_class + "' and @name='" + button_name + "']"
    button = driver.find_element_by_xpath(xpath)
    button.click()


def set_location(address):
    driver.get(address)
    print("Jesli logowanie sie nie powiodlo wpisz 'login'")
    print("Jesli logowanie sie powiodlo przejdz do strony rejestracji (kliknij koszyk) i wpisz 'zrobione'")
    user_input = input()
    if user_input == "zrobione":
        pass
    elif user_input == "login":
        login_usos(login_address, user_login, user_password)
        set_location(address)
    else:
        print("Nie rozumiem: " + user_input)
        set_location(address)


def get_target_time():
    user_input = input("Podaj date rozpoczecia rejestracji (np 19:56:43): ")
    try:
        target_time = datetime.today()
        user_datetime = datetime.strptime(user_input, "%H:%M:%S")
        target_time = datetime.combine(target_time, user_datetime.time())
    except ValueError:
        print("Data ma zly format!")
        return get_target_time()
    return target_time.timestamp()


if __name__ == '__main__':
    login_usos(login_address, user_login, user_password)
    set_location(home_address)
    click_button(get_target_time())
