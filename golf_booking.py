from selenium import webdriver
# from competition_util import go_to_competition


class GolfBooking:
    def __init__(self, username, password, competitionDate):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.username = username
        self.password = password
        self.competitionDate = competitionDate

        # Go to website
        self.browser.get('https://www.brsgolf.com/castlerock/members_home.php')

        # Go to log in screen
        book_time_button = self.browser.find_element_by_class_name('book_a_tee_time_button')
        book_time_button.click()

        # Perform login
        user_name_input = self.browser.find_element_by_name('_username')
        password_input = self.browser.find_element_by_name('_password')
        user_name_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = self.browser.find_element_by_name("SUBMIT")
        login_button.click()

        # # Navigate to today's competition booking
        link_to_comp = None
        competitions = self.browser.find_elements_by_class_name('competition_booking_summary_table')
        for comp in competitions:
            if competitionDate in comp.text.encode('ascii', 'ignore'):
                link_to_comp = comp
                break

        link_to_comp.click()

        server_time = self.browser.find_element_by_id('servertime')
        print (server_time)









