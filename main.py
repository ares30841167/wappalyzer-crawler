import os
import time
import pyautogui


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def init_chrome_driver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': f"{os.path.join(os.getcwd(), 'export')}"}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_extension('wappalyzer.crx')
    chrome_options.add_argument('--force-dark-mode')
    chrome_options.add_argument("--lang=zh_TW")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    return driver


# Pin the "Wappalyzer" extension to the toolbar
def pin_extension_to_toolbar() -> None:
    # Open the extension menu
    find_and_click('icons/extensions.png')

    # Click the "pin to toolbar" button
    find_and_click('icons/pin.png')

    # Close the extension menu
    find_and_click('icons/extensions.png')


# Find the related part matching the given image on the scrren and click it
def find_and_click(img: str, offsetX: float = 0, offsetY: float = 0) -> None:
    # Initial variables
    cnt = 0
    loc = None

    # Wait until the image appear on the screen
    while (loc == None):
        # If try over {cnt} times, raise an exception
        if (cnt >= 10):
            raise Exception(
                f'Can\'t found {img} on the screen over {cnt} times')

        try:
            # Locate the image on the screen
            x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            # Click it
            pyautogui.click(x + offsetX, y + offsetY)
            # Wait for a while to simulate the human behavior
            time.sleep(0.18)
            break
        except Exception as e:
            # If the image not found, add the counter and give a hint message
            print(f'Still not found image: {img}')
            cnt += 1
            time.sleep(1)


# Export the data from the wappalyzer extension and save them to the folder
def fetch_wappalyzer_data(url_list: list[str]) -> None:
    # Iterate through all the URLs in the URL list
    first_time = True
    for url in url_list:
        # Go to the target website
        driver.get(url)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//body")))

        # Wait for 30 seconds to ensure all the data is being collected
        time.sleep(30)

        # Click wppalyzer extension
        find_and_click('icons/extensions.png', -40)

        # Click the export button
        find_and_click('icons/wappalyzer_export.png')

        # If this is the first website
        if (first_time):
            # Click the allow button to allow download file
            time.sleep(1.2)
            pyautogui.press('left')
            pyautogui.press('enter')

            # Click wppalyzer extension
            find_and_click('icons/extensions.png', -40)

            # Click the export button
            find_and_click('icons/wappalyzer_export.png')

            # Declare already not the first time
            first_time = False

        # Click the empty area to close the extension
        find_and_click('icons/text_hint.png')


if __name__ == '__main__':
    # Init the chrome driver
    driver = init_chrome_driver()

    # Close the page opened by the wappalyzer plugin
    WebDriverWait(driver, 30).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    driver.close()

    # Go to the initial page
    driver.switch_to.window(driver.window_handles[0])

    # Pin the extension to the toolbar
    pin_extension_to_toolbar()

    # Import all the URLs from the file
    with open('website_url_list.txt', encoding='utf-8') as f:
        url_list = f.readlines()

    # Export the data from the wappalyzer extension
    fetch_wappalyzer_data(url_list)
