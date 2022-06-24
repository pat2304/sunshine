from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# chrome_service = Service(r"E:\TEMP\selenium\browser_drivers\chromedriver.exe")

# locate the chrome driver
# s = Service('E:/TEMP/selenium/browser_drivers/chromedriver.exe')
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome('E:/TEMP/selenium/browser_drivers/chromedriver.exe')

for i in range(0, 10, 1):
    servs = Service(ChromeDriverManager().install())
    opts = Options()
    opts.add_argument('--incognito')
    driver = webdriver.Chrome(service=servs, options=opts)
    #driver = webdriver.Chrome(service=servs)

    # 《異次元—解密》 主題：揭穿－三維空間假相
    #driver.get('https://s.eqxiu.cn/s/0lkTXVid')
    #time.sleep(5)

    # 外現聲聞身－內秘菩薩行…第56集《維摩詰經》…#北大聖玄 #覺曦軒
    #driver.get('https://www.youtube.com/watch?v=oonruVoXOf0')
    #time.sleep(480)

    # 《跨领域－重磅对话》…时代前沿对话！ 第56集 《维摩诘经》…全球直播教学视频 主题：外现声闻身－内秘菩萨行
    #driver.get('https://v.eqxiu.cn/s/DBGJLWnW')
    #time.sleep(3)

    # 《聖玄語露·第14-6集》生命中最重要的兩天： 出生當天，以及覺悟生命存在意義的那一天。
    driver.get('https://www.youtube.com/watch?v=6qs9wqdmsSM')
    time.sleep(360)
    # driver.get('https://v.eqxiu.cn/s/FlHSB3TW?bt=yxy')

    # 共生·共贏－全球戰疫
    #driver.get('https://v.eqxiu.cn/s/3zW8XTxG')
    #time.sleep(3)

    # Set URL 壯闊中的溫柔—獻給人父
    # driver.get('https://s.eqxiu.cn/s/QEGRw46u')

    # 均衡身心靈‧妙法出奇制勝 第6集《10分鐘·奇葩&閨蜜》  主題：出奇制勝－世間+ 出世間法
    #driver.get('https://c.scene.ryxiut.net/s/9mUa5tLm/')


    # 里外不是人－生死一如
    # driver.get('https://s.eqxiu.cn/s/OzccsTBN')
    # time.sleep(3)


    # driver.maximize_window()
    print(driver.title, ' - ', i+1)
    # time.sleep(3)
    driver.close()
