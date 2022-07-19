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

def chrome_conn(url, iter, timer):
    fail_connect = fail_refresh = 0

    for i in range(0, iter, 1):
        servs = Service(ChromeDriverManager().install())
        opts = Options()
        opts.add_argument('--incognito')
        opts.add_argument('--mute-audio')
        driver = webdriver.Chrome(service=servs, options=opts)
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


# 220622 《10分鐘·奇葩＆閨蜜》第61集; 預立遺囑－臨終關懷; 預立遺囑…時代前沿脈動…跟上得利！
# chrome_conn('https://b.scene.ryxiut.net/s/zCSoSuuy/1657409891884?bt=yxy', 50, 8, 3)
# chrome_conn('https://www.youtube.com/watch?v=mW8HAcnSSkc', 10, 340)
# chrome_conn('https://www.youtube.com/watch?v=mW8HAcnSSkc', 10, 180, 0)

# 220711 《煩惱．DUCK 不必》第6集 解套．臨終恐懼五大事…#北大聖玄#覺曦軒 (5:00)
#chrome_conn('https://www.youtube.com/watch?v=rBpaNnwZZlI', 10, 250)

# 220717 菩提之相－實無有法可知…第60集《維摩詰經》…#北大聖玄 #覺曦軒
# chrome_conn('https://a.scene.ryxiut.net/s/51rLUXBb/1658112651729?bt=yxy', 20, 10)
chrome_conn('https://www.youtube.com/watch?v=2yBiVxmsn1A', 10, 500)

# 220719 異次元探秘—生、死切換…01集《視頻化‧異次元—解密》…#北大聖玄 #覺曦軒 (10:35)
chrome_conn('https://www.youtube.com/watch?v=gcxxb668FFc', 10, 200)

# 220710 觀不生．不入正位－菩薩…第59集《維摩詰經》…#北大聖玄 #覺曦軒
# chrome_conn('https://www.youtube.com/watch?v=R55B_yQASn4', 10, 500)
# chrome_conn('https://www.youtube.com/watch?v=R55B_yQASn4', 10, 200, 0)

# 220717 《視頻化·微享》🌺🌺主題：耕心有成·正道圓成－觀音自在解脫 (4:48)
# chrome_open('https://www.youtube.com/watch?v=UYwuW040ci8', 10, 240)

# 220716 《5分鐘‧奇葩&閨蜜》冷眼紅塵－東方不敗…第68集 (5:42)
# chrome_conn('https://www.youtube.com/watch?v=ml0JabzkPEc', 10, 300)

# 220715《聖玄語露·第14-9集》危機與轉機，瞬間轉念之契機，在於觀照二者來自同一本源 (5:30)
# chrome_conn('https://youtu.be/V790YSRCRzw', 10, 180)

# 220714《微言悅享》🌺🌺主題：起死回生; 成功起死回生…化解醫師魔咒…她多活了19年…有理、有據，有方法！ (9:25)
# chrome_conn('https://www.youtube.com/watch?v=-2Ch2IGIhuc', 10, 200)

# 《異次元—解密》 主題：揭穿－三維空間假相
# chrome_conn('https://s.eqxiu.cn/s/0lkTXVid', 50, 10, 3)
#chrome_conn('https://a.scene.ryxiut.net/s/0lkTXVid/1656467885377', 50, 8, 3)

# 均衡身心靈‧妙法出奇制勝 第6集《10分鐘·奇葩&閨蜜》  主題：出奇制勝－世間+ 出世間法
#chrome_conn('https://c.scene.ryxiut.net/s/9mUa5tLm/', 50, 8, 3)

# 對立的統一—煩惱即菩提…第67集《5分鐘‧奇葩&閨蜜》…#北大聖玄#覺曦軒 (6:34)
# chrome_conn('https://www.youtube.com/watch?v=Zxa8RMDfehk', 10, 180, 0)
# chrome_conn('https://www.youtube.com/watch?v=Zxa8RMDfehk', 10, 390, 0)

# 220712 第一名《視頻化·教學相長》…第59集教學🌺🌺主題：勘破迷霧－跨界融合 (13:42)
# chrome_conn('https://www.youtube.com/watch?v=zGs3O1fPv4Y', 10, 180, 0)

# 220703 《跨領域－重磅對話》…時代前沿對話！ 第58集 《維摩詰經》…全球直播教學視頻 🌺🌺🌺主題：無相、無作、無起－菩薩行
# chrome_conn('https://www.youtube.com/watch?v=E11unQn9bvk', 10, 500, 0)
# chrome_conn('https://v.eqxiu.cn/s/K40QrnS1?bt=yxy', 20, 10, 3)

# 220709 《10分鐘·奇葩＆閨蜜》第66集; 主題：解套－命運束縛，突破心理學極限…解套命運束縛！
# chrome_conn('https://www.youtube.com/watch?v=gwyllM0vMS4', 10, 365, 0)

# 220708 《聖玄語露·第14-8集》 小聰明，製造歧異; 大智慧，和諧解套歧異！
#chrome_conn('https://www.youtube.com/watch?v=2NiJppBBXVU', 10, 276, 0)

# 220707 《微言悅享》主題：震撼開示—脫胎轉化; 久病床前無孝子…轉化思惟，則雙贏！…震撼開示，不可思議！
# chrome_conn('https://youtu.be/H-lNH__Tznc', 300, 10, 0)

# 《微言悅享》主題：震撼開示—脫胎轉化; 久病床前無孝子…轉化思惟，則雙贏！…震撼開示，不可思議！
# chrome_conn('https://www.youtube.com/watch?v=H-lNH__Tznc', 10, 300, 0)

# 220706 《10分鐘·奇葩＆閨蜜》第65集; 🌺🌺主題：三輪體空－最高階佈施; 三輪體空…無盡福田的代言…最高階的佈施！
#chrome_conn('https://www.youtube.com/watch?v=czDUOUE-UqA', 10, 329, 0)

# 220705 《異次元—解密》🌺🌺主題：念波－透視能力，意識透視能力，人皆有之！…端視念波頻率、強度而論斷。
#chrome_conn('https://v.eqxiu.cn/s/drvgK3JV', 50, 8, 3)

# 220704 解套·死局…人人必修的學分…#煩惱·DUCK不必 🌺🌺 第5集…主題：解套·死局
# chrome_conn('https://www.youtube.com/watch?v=cIrHY-k7wnQ', 10, 264, 0)
#chrome_conn('https://v.eqxiu.cn/s/Psb3JZID?bt=yxy', 10, 10, 3)

# 220626 《跨領域－重磅對話》…時代前沿對話！ 第57集 《維摩詰經》…全球直播教學視頻 主題：雖行於空－植種德本
#chrome_conn('https://www.youtube.com/watch?v=UMNKSNIAt8I', 10, 500)
# chrome_conn('https://s.eqxiu.cn/s/SOcpPeOv', 20, 10)

# 220702 《10分鐘·奇葩＆閨蜜》第64集 主題：生命回顧－導負為正; 重走舊時路…賦予新意義！
#chrome_conn('https://www.youtube.com/watch?v=Pd3qSMDXmNg', 10, 348)

# 220701 《圣玄语露·第14-7集》 生命内在觉醒，是不可替代的永恒真幸福！
#chrome_conn('https://www.youtube.com/watch?v=0iTzkoL9-VY', 10, 240)
#chrome_conn('https://v.eqxiu.cn/s/Aletmrg1', 10, 10)

# 220630 《微言悅享》主題：大臼齒與主人的對話; 大臼齒與主人的親密關係！…有情、非情…來自同一終極本質！
#chrome_conn('https://s.eqxiu.cn/s/BpKCU61d?bt=yxy', 50, 10)

# 220630 DT: 《異次元—解密》主題：見相非相 - 空間扭曲
#chrome_conn('https://s.eqxiu.cn/s/4TQFtLQo', 10, 10)

# 220629 第63集《10分鐘·奇葩＆閨蜜》 🌺🌺主題：臨終關懷－五全照顧 (善生、善終…生死兩無憾！)
# https://www.youtube.com/watch?v=i5vx63X9Ors
#chrome_conn('https://a.scene.ryxiut.net/s/tH1pXUEb/1656457671824', 50, 10)

# 220628 《異次元—解密》信息場奧秘…進入信息場…有方法！ 主題：適者生存－信息場成長與演化
# chrome_conn('https://v.eqxiu.cn/s/0RWASSU5', 50, 10)

# 220627 解套．全方位貧窮…第4集《煩惱．DUCK 不必》…#北大聖玄#覺曦軒
# chrome_conn('https://www.youtube.com/watch?v=B6yBfgAbsHU', 10, 195)
# chrome_conn('https://s.eqxiu.cn/s/cuGXZIcC?bt=yxy', 20, 10)

# 220618 外現聲聞身－內秘菩薩行…第56集《維摩詰經》…#北大聖玄 #覺曦軒
# chrome_conn('https://www.youtube.com/watch?v=oonruVoXOf0', 20, 480)

# 220617 《跨领域－重磅对话》…时代前沿对话！ 第56集 《维摩诘经》…全球直播教学视频 主题：外现声闻身－内秘菩萨行
# chrome_conn('https://v.eqxiu.cn/s/DBGJLWnW', 10, 10)

# 220625 - 《10分鐘·奇葩＆閨蜜》 臨終關懷起源—人性需求
# chrome_conn('https://www.youtube.com/watch?v=CjCG4lx8DD8', 10, 290)
# chrome_conn('https://v.eqxiu.cn/s/4gOU847g?bt=yxy', 10, 10)

# 《聖玄語露·第14-6集》生命中最重要的兩天： 出生當天，以及覺悟生命存在意義的那一天。
# chrome_conn('https://www.youtube.com/watch?v=6qs9wqdmsSM', 10, 10)
# chrome_conn'https://v.eqxiu.cn/s/FlHSB3TW?bt=yxy'. 10. 10)

# 共生·共贏－全球戰疫
# chrome_conn('https://v.eqxiu.cn/s/3zW8XTxG', 10, 10)

# Set URL 壯闊中的溫柔—獻給人父
# chrome_conn('https://s.eqxiu.cn/s/QEGRw46u', 10, 10)


# 里外不是人－生死一如
# driver.get('https://s.eqxiu.cn/s/OzccsTBN')
# time.sleep(3)


