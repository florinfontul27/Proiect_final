from pages.home_page import HomePage
from time import sleep

def test_search_functionality(browser):
    home_page = HomePage(browser)
    home_page.load_page()
    home_page.type_search_input("samsung")
    home_page.make_a_search()



def test_search_functionality_2(browser):
    home_page = HomePage(browser)
    home_page.load_page()
    home_page.type_search_input("dssdsd")
    sleep(5)
    home_page.make_a_search()
    sleep(5)
    assert 'Ne pare rau, dar pagina cautata nu a fost gasita' in home_page.get_error_message()
    sleep(10)






