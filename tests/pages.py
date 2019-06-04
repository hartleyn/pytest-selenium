from page_objects import PageObject, PageElement


class AutomationPracticePage(PageObject):
    search_field = PageElement(id_='s')
    search_submit_button = PageElement(id_='searchsubmit')
    big_page_link = PageElement(link_text='Big page with many elements')
    navigation_bar = PageElement(id_='et-top-navigation')
    share_on_pocket_button = PageElement(xpath='//*[@id="post-507"]/div/div[2]/div/div/ul/li[3]/a')
    email_notification_form_email_field = PageElement(id_='subscribe-field-blog_subscription-2')
    email_notification_form_submit_button = PageElement(name='jetpack_subscriptions_widget')
    email_notification_form_success_message_div = PageElement(css='#blog_subscription-2 > div')
    email_notification_form_success_message = PageElement(css='#blog_subscription-2 > div > p')


class ComplicatedPage(PageObject):
    section_of_buttons_first_button = PageElement(xpath='//*[@id="et-boc"]/div/div/div[3]/div[1]/div[1]/a')
    login_form_forgot_password_link = PageElement(xpath='//*[@id="et-boc"]/div/div/div[7]/div[2]/div[2]/div[2]/form/p[3]/a')
    login_form_login_button = PageElement(xpath='//*[@id="et-boc"]/div/div/div[7]/div[2]/div[2]/div[2]/form/p[4]/button')
    contact_form_name_field = PageElement(id_='et_pb_contact_name_0')
    contact_form_email_field = PageElement(id_='et_pb_contact_email_0')
    contact_form_message_field = PageElement(id_='et_pb_contact_message_0')
    contact_form_submit_button = PageElement(css='#et_pb_contact_form_0 > div.et_pb_contact > form > div > button')
    contact_form_missing_info_div = PageElement(css='#et_pb_contact_form_0 > div.et-pb-contact-message')
    contact_form_missing_info_first_in_list = PageElement(xpath='//*[@id="et_pb_contact_form_0"]/div[1]/ul[1]/li[1]')


class SearchResultsPage(PageObject):
    first_result_link = PageElement(css='#post-5008 > h2 > a')


class LostPasswordPage(PageObject):
    username_field = PageElement(id_='user_login')
    get_new_password_button = PageElement(id_='wp-submit')
    no_account_error_message_div = PageElement(id_='login_error')


class PocketLoginPage(PageObject):
    username_field = PageElement(id_='field-1')
    password_field = PageElement(id_='field-2')
    login_button = PageElement(css='#login-page-login-container > div > form > input')
    error_message_buble = PageElement(xpath='//*[@id="login-page-login-container"]/div/form/div[2]/span/span[1]')
