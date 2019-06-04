# pytest-selenium

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


### D) Verify that an error message is displayed after submitting the Pocket 'log in' form with no password.

Test Steps:
1. Navigate to '/automation'.
2. Click the 'share on Pocket' button.
3. Enter a username.
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
