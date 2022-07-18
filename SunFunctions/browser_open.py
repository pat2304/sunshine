from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as YouKey
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# chrome_service = Service(r"E:\TEMP\selenium\browser_drivers\chromedriver.exe")
# locate the chrome driver
# s = Service('E:/TEMP/selenium/browser_drivers/chromedriver.exe')
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome('E:/TEMP/selenium/browser_drivers/chromedriver.exe')

def chrome_open(url, loop, timer):
    from selenium.webdriver.chrome.service import Service
    # from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    fail_connect = fail_refresh = 0
    servs = Service(ChromeDriverManager().install())
    # servs = webdriver.chrome.service.Service(ChromeDriverManager.install())
    # servs = webdriver.chrome.service.Service(ChromeDriverManager().install())
    opts = webdriver.ChromeOptions()
    opts.add_argument('--incognito')
    opts.add_argument('--mute-audio')

    for i in range(0, loop, 1):
        driver = webdriver.Chrome(service=servs, options=opts)
        # driver = webdriver.Chrome(service=servs)

        # chrome connect to URL
        try:
            driver.get(url)
            wait.until(visible((By.ID, '耕心有成·正道圓成－觀音自在解脫…03集《視頻化·微享·》…#北大聖玄 #覺曦軒')))
            driver.find_element('耕心有成·正道圓成－觀音自在解脫…03集《視頻化·微享·》…#北大聖玄 #覺曦軒').click()
            video.send_keys(Keys.SPACE)
        except:
            fail_connect += 1
            print('Fail to connect => ', fail_connect)
            driver.refresh()

        # driver.maximize_window()
        print(driver.title, ' - ', i + 1)
        # Minimized the window if you don't want to be disturbed by pop-up, Youtube is excepted
#        driver.minimize_window()
        time.sleep(timer)
#       for j in range(0, reload, 1):
#           try:
#               driver.refresh()
#               time.sleep(timer)
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
    #servs = webdriver.chrome.service.Service(ChromeDriverManager().install())
    opts = webdriver.EdgeOptions()
    opts.add_argument('--InPrivate')
    opts.add_argument('--mute-audio')

    for i in range(0, loop, 1):
        driver = webdriver.Edge(service=servs, options=opts)
        #driver = webdriver.Chrome(service=servs)

        # chrome connect to URL
        try:
            driver.get(url)
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
