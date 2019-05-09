from selenium import webdriver


class GolfBooking:
    def __init__(self):
        pass

    browser = webdriver.Chrome('/usr/local/bin/chromedriver')

    # Go to website
    browser.get('https://www.brsgolf.com/castlerock/members_home.php')

    # Go to log in screen
    book_time_button = browser.find_element_by_class_name('book_a_tee_time_button')
    book_time_button.click()

    # Perform login
    user_name_input = browser.find_element_by_name('_username')
    password_input = browser.find_element_by_name('_password')
    user_name_input.send_keys(raw_input("Username: "))
    password_input.send_keys(raw_input("Password: "))
    login_button = browser.find_element_by_name("SUBMIT")
    login_button.click()

    # Ask user which competition they would like to navigate to
    competitionList = browser.find_elements_by_class_name('competition_booking_summary_table')
    competitionDict = {i+1: x for i, x in enumerate(competitionList)}

    print 'Competitions are: \n'
    for k, v in competitionDict.iteritems():
        print '[', k, ']\t', v.text.split(',')[0].split(' - ')[1], '-', v.text.split(',')[0].split(' - ')[2]

    compIndex = raw_input('\n\nWhich competition would you like to book? ')
    competitionDict.get(int(compIndex)).click()
