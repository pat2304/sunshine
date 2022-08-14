from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys as YouKey
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, datetime


# chrome_service = Service(r"E:\TEMP\selenium\browser_drivers\chromedriver.exe")
# locate the chrome driver
# s = Service('E:/TEMP/selenium/browser_drivers/chromedriver.exe')
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome('E:/TEMP/selenium/browser_drivers/chromedriver.exe')

def chrome_open(url, loop, ptime):
    from selenium.webdriver.chrome.service import Service
    # from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    fail_connect = start_point = next_time = total_time = 0

    floop = True

    servs = Service(ChromeDriverManager().install())
    # servs = webdriver.chrome.service.Service(ChromeDriverManager.install())
    # servs = webdriver.chrome.service.Service(ChromeDriverManager().install())
    opts = webdriver.ChromeOptions()
    opts.add_argument('--incognito')
    opts.add_argument('--mute-audio')

    for i in range(0, loop, 1):
        driver = webdriver.Chrome(service=servs, options=opts)
        # driver = webdriver.Chrome(service=servs)

        mouse_act = ActionChains(driver)

        # chrome connect to URL
        try:
            driver.get(url)
            element = driver.find_element(By.XPATH, "//*[@class='ytp-large-play-button ytp-button']")
            element.click()
            # time.sleep(7)

            # time.sleep(10)
            # play_element = driver.find_element(By.XPATH, "//*[@class='ytp-play-button ytp-button']")
            # play_element.click()

            # wait.until(visible((By.ID, '耕心有成·正道圓成－觀音自在解脫…03集《視頻化·微享·》…#北大聖玄 #覺曦軒')))
            # driver.find_element('耕心有成·正道圓成－觀音自在解脫…03集《視頻化·微享·》…#北大聖玄 #覺曦軒').click()
            # video.send_keys(Keys.SPACE)
        except:
            fail_connect += 1
            print('Fail to connect => ', fail_connect)
            driver.refresh()

        # panel = driver.find_element(By.CSS_SELECTOR, 'div.ytp-chrome-controls')
        panel = driver.find_element(By.CSS_SELECTOR, '.ytp-left-controls')
        # panel = driver.find_element(By.ID, 'player-container-inner')
        # play_press = driver.find_element(By.ID, 'movie_player')

        try:
            mouse_act.move_to_element(panel).move_by_offset(10, 10).perform()
            print('Mouse over panel')

        except:
            print('Mouse over fail')

        # Wait 7 secs
        for j in range(0, 7):
            mouse_act.move_to_element(panel).move_by_offset(10, 10).perform()
            time.sleep(1)

        # time.sleep(2)
        # mouse_act.move_to_element(panel).move_by_offset(10, 10).perform()
        # time.sleep(2)
        # mouse_act.move_to_element(panel).move_by_offset(10, 10).perform()
        # time.sleep(2)
        # mouse_act.move_to_element(panel).move_by_offset(10, 10).perform()

        # Skip ads
        try:
            skip_button = driver.find_element(By.CLASS_NAME, 'ytp-ad-skip-button-container')
            skip_button.click()

        except:
            print('Skip button not found')

        # # find play button to pause
        # try:
        #     play_press = driver.find_element(By.ID, 'movie_player')
        #     play_press.send_keys(YouKey.SPACE)
        # except:
        #     print('Play key not found')

        duration = driver.find_elements(By.XPATH, "//span[@class='ytp-time-duration']")[0].text
        # print(duration)

        # Obtain the length of the video in seconds
        try:
            x = time.strptime(duration, '%H:%M:%S')
            total_time = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        except:
            x = time.strptime(duration, '%M:%S')
            total_time = datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        # Check total time in secs
        # print(total_time)

        next_time += ptime

        #        print('Total = ', total_time, 'start = ', start_point, ' next = ', next_time)

        if next_time >= total_time:
            print('Inside if')
            start_point = 0
            next_time = ptime
            floop = True

        print('Total = ', total_time, 'start = ', start_point, ' next = ', next_time)

        if not floop:
            try:
                driver.execute_script('document.getElementsByTagName("video")[0].currentTime=' + str(start_point))

            except:
                print('forwarding fail')

        # Maximize the window
        # driver.maximize_window()

        # Minimized the window if you don't want to be disturbed by pop-up, Youtube is excepted
        # driver.minimize_window()

        print(driver.title, ' - ', i + 1)

        start_point = next_time
        floop = False

        time.sleep(ptime)

        #       for j in range(0, reload, 1):
        #           try:
        #               driver.refresh()
        #               time.sleep(ptime)
        #           except:
        #               fail_refresh += 1
        #               print('Error in Refresh => ', fail_refresh)

        driver.close()


def fox_open(url, loop, timer):
    import os
    os.environ['GH_TOKEN'] = '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'
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
    from webdriver_manager.firefox import GeckoDriverManager

    fail_connect = fail_refresh = 0

    servs = Service(GeckoDriverManager().install())
    opts = webdriver.FirefoxOptions()
    opts.add_argument('-private')
    opts.add_argument('--mute-audio')
    opts.binary_location = r'D:\apps\FirefoxPortable\App\firefox64\firefox.exe'

    for i in range(0, loop, 1):
        # driver = webdriver.Firefox(service=servs, options=opts)
        driver = webdriver.Firefox(service=servs)

        # chrome connect to URL
        try:
            driver.get(url)
            element = driver.find_element(By.XPATH, "//*[@class='ytp-large-play-button ytp-button']")
            element.click()
        except:
            fail_connect += 1
            print('Fail to connect => ', fail_connect)
            driver.refresh()

        # driver.maximize_window()
        print(driver.title, ' - ', i + 1)
        # Minimized the window if you don't want to be disturbed by pop-up, Youtube is excepted
        driver.minimize_window()
        time.sleep(timer)
        #       for j in range(0, reload, 1):
        #           try:
        #               driver.refresh()
        #               time.sleep(timer)
        #           except:
        #               fail_refresh += 1
        #               print('Error in Refresh => ', fail_refresh)

        driver.close()


def edge_open(url, loop, timer):
    from selenium.webdriver.edge.service import Service as EdgeService
    # from selenium.webdriver.chrome.options import Options
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    fail_connect = fail_refresh = 0

    servs = EdgeService(EdgeChromiumDriverManager().install())
    # servs = webdriver.chrome.service.Service(ChromeDriverManager.install())
    # servs = webdriver.chrome.service.Service(ChromeDriverManager().install())
    opts = webdriver.EdgeOptions()
    opts.add_argument('--InPrivate')
    opts.add_argument('--mute-audio')

    for i in range(0, loop, 1):
        driver = webdriver.Edge(service=servs, options=opts)
        # driver = webdriver.Chrome(service=servs)

        # chrome connect to URL
        try:
            driver.get(url)
            element = driver.find_element(By.XPATH, "//*[@class='ytp-large-play-button ytp-button']")
            element.click()
        except:
            fail_connect += 1
            print('Fail to connect => ', fail_connect)
            driver.refresh()

        # driver.maximize_window()
        print(driver.title, ' - ', i + 1)
        # Minimized the window if you don't want to be disturbed by pop-up, Youtube is excepted
        driver.minimize_window()
        time.sleep(timer)
        #       for j in range(0, reload, 1):
        #           try:
        #               driver.refresh()
        #               time.sleep(timer)
        #           except:
        #               fail_refresh += 1
        #               print('Error in Refresh => ', fail_refresh)

        driver.close()
