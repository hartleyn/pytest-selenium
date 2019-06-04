import time


def switch_to_new_window(driver):
    # Pause to allow new window to load 
    time.sleep(5)
    # Retrieve browser window IDs
    windows = driver.window_handles
    # Switch to new window
    driver.switch_to.window(windows[1])

    return driver
