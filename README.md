## An introduction to Python Selenium testing.

[![YouTube Video](https://i9.ytimg.com/vi/jstptPq5YxU/mq2.jpg?sqp=CMip2-cF&rs=AOn4CLD89JACj-0xXZa-9sKsEmh_018how)](https://www.youtube.com/watch?v=jstptPq5YxU)

### What is this?

A quick demonstration of Selenium-based testing using Python. The tests were written using the Pytest testing framework. Pytest uses test discovery to run all 'test_' prefixed functions in 'test_' prefixed files. The test suite performs a series of functional tests on the user interface of UltimateQA.com. 

### What techniques will I see?

Some of the automation techniques on display include:
* URL navigation
* Interacting with forms
* Clicking buttons
* Interacting with pop-up windows
* Result validation using ```assert``` statements
* 'Page Object Model' design pattern implementation

### Why is this important? How is it used?

Automated browser tests are often utilized within the continuous integration pipeline of agile development teams. Running automated tests prior to accepting code changes helps ensure ongoing build stability; a practice known as test driven development (TDD).

### What does 'Page Object Model' mean?

As previously mentioned, this test suite employs the page object model (POM) design pattern. POM calls for an individual class to be created for each webpage. The class contains the various page elements for a given webpage as attributes. Methods for performing operations on the webpage's elements may also be added to the class. POM makes test maintenance easier by separating the test code from page-specific logic.

### Where can I find more information?

Pytest Documentation: https://docs.pytest.org/en/latest/index.html

Test Collection in Pytest: https://docs.pytest.org/en/latest/goodpractices.html#test-discovery

Unofficial Python Selenium Documention: https://selenium-python.readthedocs.io/api.html

Official Documentation: https://seleniumhq.github.io/selenium/docs/api/py/api.html

More on POM: https://selenium-python.readthedocs.io/page-objects.html

---

## Test Cases

### A) Verify that an error message is displayed after submitting the contact form with a missing captcha value.

Test Steps:
1. Navigate to '/complicated-page'.
2. Enter a username, password, and message.
3. Submit the form.

Expected Result:
An error message stating that the Captcha value is missing
is displayed.


### B) Verify that a keyword search can be executed successfully.

Test Steps:
1. Navigate to '/automation'.
2. Enter a keyword in the search field.
3. Execute the search.

Expected Result:
Search result page is rendered. Top search result contains
the keyword.


### C) Verify that an error message is displayed after submitting the 'forgot password' form with an unknown username.

Test Steps:
1. Navigate to '/complicated-page'.
2. Click the 'forgot your password?' link.
3. Enter an unknown username. 
2. Submit the form.

Expected Result:
An error message stating that the username is unknown is
displayed.


### D) Verify that an error message is displayed after submitting the Pocket 'log in', pop-up form with no password.

Test Steps:
1. Navigate to '/automation'.
2. Click the 'share on Pocket' button.
3. In the pop-up window, enter a username.
4. Click the password field (to activate 'log in' button).
5. Submit the form.

Expected Results:
An error message stating that the 'password' value is too
short is displayed.

---

## Usage

Run the following commands in a Terminal window:

1. ```bash
   pip install requirements.txt
   ```
2. ```bash
   pytest
   ```


NOTE: Requires a ChromeDriver installation: http://chromedriver.chromium.org/downloads.
