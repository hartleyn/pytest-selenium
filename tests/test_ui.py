from helpers import switch_to_new_window
from pages import (
    AutomationPracticePage, 
    ComplicatedPage, 
    SearchResultsPage,
    LostPasswordPage,
    PocketLoginPage,
)


"""
    Verify that an error message is displayed after
    submitting the contact form with a missing captcha value.

    Test Steps:
    1. Navigate to '/complicated-page'.
    2. Enter a username, password, and message.
    3. Submit the form.

    Expected Result:
    An error message stating that the Captcha value is missing
    is displayed.
"""
def test_submit_contact_form_no_captcha(chrome_driver):
    page = ComplicatedPage(chrome_driver, root_uri='https://www.ultimateqa.com')
    page.get('/complicated-page')
    page.contact_form_name_field.send_keys('Guy One')
    page.contact_form_email_field.send_keys('test@test.com')
    page.contact_form_message_field.send_keys('This is a message!')
    page.contact_form_submit_button.click()

    assert(page.contact_form_missing_info_div.is_displayed())
    assert(page.contact_form_missing_info_first_in_list.text == 'Captcha')


"""
    Verify that a keyword search can be executed successfully.

    Test Steps:
    1. Navigate to '/automation'.
    2. Enter a keyword in the search field.
    3. Execute the search.

    Expected Result:
    Search result page is rendered. Top search result contains
    the keyword.
"""
def test_execute_search(chrome_driver):
    page = AutomationPracticePage(chrome_driver, root_uri='https://www.ultimateqa.com')
    page.get('/automation')
    page.search_field.send_keys('landing page')
    page.search_submit_button.click()

    page = SearchResultsPage(chrome_driver)

    assert('landing page' in page.first_result_link.text.lower())


"""
    Verify that an error message is displayed after submitting
    the 'forgot password' form with an unknown username.

    Test Steps:
    1. Navigate to '/complicated-page'.
    2. Click the 'forgot your password?' link.
    3. Enter an unknown username. 
    2. Submit the form.

    Expected Result:
    An error message stating that the username is unknown is
    displayed.
"""
def test_forgot_password_bad_username(chrome_driver):
    page = ComplicatedPage(chrome_driver, root_uri='https://www.ultimateqa.com')
    page.get('/complicated-page')
    page.login_form_forgot_password_link.click()

    page = LostPasswordPage(chrome_driver)
    page.username_field.send_keys('bad_username')
    page.get_new_password_button.click()

    assert(page.no_account_error_message_div.is_displayed())
    assert('There is no account with that username' in page.no_account_error_message_div.text)


"""
    Verify that an error message is displayed after submitting
    the Pocket 'log in' form with no password.

    Test Steps:
    1. Navigate to '/automation'.
    2. Click the 'share on Pocket' button.
    3. Enter a username.
    4. Click the password field (to activate 'log in' button).
    5. Submit the form.

    Expected Results:
    An error message stating that the 'password' value is too
    short is displayed.
"""
def test_pocket_login_no_password(chrome_driver):
    page = AutomationPracticePage(chrome_driver, root_uri='https://www.ultimateqa.com')
    page.get('/automation')
    page.share_on_pocket_button.click()

    switch_to_new_window(chrome_driver)

    page = PocketLoginPage(chrome_driver)
    page.username_field.send_keys('some_username')
    page.password_field.click()
    page.login_button.click()

    assert(page.error_message_buble.is_displayed())
    assert('Please enter at least 6 characters' in page.error_message_buble.text)
