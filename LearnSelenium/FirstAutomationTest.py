from selenium import webdriver
from selenium.webdriver.common.by import By
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


# 221002 不生不滅．相好莊嚴其身－菩薩行…第71集《維摩詰經》…#北大聖玄 #覺曦軒 (56:21)
chrome_conn('https://www.youtube.com/watch?v=8bos67pGPLY', 100, 400)

# 220919 關鍵出擊－文殊八字精要…第3集《關鍵出擊》…#北大聖玄#覺曦軒 (10:12)
# chrome_conn('https://www.youtube.com/watch?v=YeWu9gP8zP8', 100, 203)

# 221006 癱瘓餘生…16集《視頻化·微享－节庆篇》…#北大聖玄 #覺曦軒 (11:06)
# chrome_conn('https://www.youtube.com/watch?v=QZU6NGVp0nw', 30, 221)

# 221005 聖人就在你左右…第82集《5分鐘·奇葩&閨蜜》…#北大聖玄 #覺曦軒 (6:33)
# chrome_conn('https://www.youtube.com/watch?v=ygUYq9aiWno', 30, 195)

# 221004 賀重陽－AI時尚老人·智慧之巔…18集《視頻化·微享－节庆篇》…#北大聖玄 #覺曦軒 (5:43)
# chrome_conn('https://www.youtube.com/watch?v=-fews4ag4Ec', 30, 170)

# 221003 解套．機器人迷思…第13集《煩惱·DUCK不必》…#北大聖玄 #覺曦軒 (6:49)
# chrome_conn('https://www.youtube.com/watch?v=CtyYndah2Xs', 30, 200)

# 220925 行止觀．不墮寂滅－菩薩行…第70集《維摩詰經》…#北大聖玄 #覺曦軒 (1:25:59)
# chrome_conn('https://www.youtube.com/watch?v=hmzXUkHW4Yg', 100, 400)

# 221001 離言內證．高能量－師父證量…第9集《提月點燈－話創異》…#北大聖玄 #覺曦軒 (14:06)
# chrome_conn('https://www.youtube.com/watch?v=hPNtprmd494', 30, 210)

# 220930 止觀不二－境智冥一…第13-7集《視·聖玄語露》…#北大聖玄 #覺曦軒 (5:18)
# chrome_conn('https://www.youtube.com/watch?v=IiznvsolMmE', 30, 158)

# 220929 起早鳴享－秘笈…14集《視頻化·微享》…#北大聖玄 #覺曦軒 (9:20)
# chrome_conn('https://www.youtube.com/watch?v=hNZuoshv584', 30, 186)

# 220928 舐犢情深－師恩難報…15集《視頻化•微享－節慶篇》…#北大聖玄 #覺曦軒 (4:57)
# chrome_conn('https://www.youtube.com/watch?v=W2YEXKorwzs', 30, 148)

# 220926 解套．高知迷思…第12集《煩惱．DUCK 不必》…#北大聖玄 #覺曦軒
# chrome_conn('https://www.youtube.com/watch?v=QM0c7u_gDHs', 30, 220)

# 220918 行八正道．樂求佛道－菩薩行…第69集《維摩詰經》…#北大聖玄 #覺曦軒 (1:17:41)
# chrome_conn('https://www.youtube.com/watch?v=iG-uPAH4Z6A', 100, 480)

# 220923 與佛相應－ 佛佛相通．經經相應…13-5集《視頻化·聖玄語露》…#北大聖玄 #覺曦 (9:03)
# chrome_conn('https://www.youtube.com/watch?v=Dx-Ha7iN-T0', 30, 180)

# 逆向開展自己…第81集《5分鐘·奇葩&閨蜜》…#北大聖玄 #覺曦軒 (9:24)
# chrome_conn('https://www.youtube.com/watch?v=0iGannSJujE', 30, 187)

# 透視異次元－生命存在…06集《視頻化·異次元－解密》…#北大聖玄#覺曦軒 (9:56)
# chrome_conn('https://www.youtube.com/watch?v=Zb6wwKCxMR4', 30, 198)

# 220803 關鍵時刻．出奇制勝…文殊八字真言－簡介…北大．聖玄主講 (10:12)
# chrome_conn('https://www.youtube.com/watch?v=AdgbapI5l6c', 20, 260)

# 220919 重責大任．捨我其誰…第2集《奇蜜．爆破》…#北大聖玄 #覺曦軒 (9:28)
# chrome_conn('https://www.youtube.com/watch?v=Vqrfp1Yhzik', 30, 188)

# 220913 行七覺分．分別佛智慧－菩薩行…第68集《維摩詰經》…#北大聖玄 #覺曦軒 (1:25:57)
# chrome_conn('https://www.youtube.com/watch?v=0vZq1_McyuM', 60, 480)

# 220917 人生最重要的一課…第80集《5分鐘．奇葩 & 閨蜜》…#北大聖玄 #覺曦軒 (5:49)
# chrome_conn('https://www.youtube.com/watch?v=aLKvImVhWXA', 30, 173)

# 220916 轉身不斷念－文殊法教…13-5集《視頻化‧聖玄語露》…#北大聖玄 #覺曦軒 (8:46)
# chrome_conn('https://www.youtube.com/watch?v=ewD9CChd1Gw', 20, 175)

# 220914 睡眠即作戰－少睡．少惛沈…第79集《5分鐘·奇葩 & 閨蜜》…#北大聖玄#覺曦軒 (9:07)
# chrome_conn('https://www.youtube.com/watch?v=GyJFTeuXhtk', 10, 182)

# 220828 行五根．分別利鈍－菩薩行…第66集《維摩詰經》…#北大聖玄 #覺曦軒 (1:11:17)
# chrome_conn('https://www.youtube.com/watch?v=A0udmAPbF6A', 60, 480)

# 220912 解套．月圓心團圓…第11集《煩惱．DUCK 不必》…#北大聖玄 #覺曦軒 (6:10)
# chrome_conn('https://www.youtube.com/watch?v=j_K9b01KQjk', 10, 184)

# 220911 覺曦軒．金秋禮贊…01集《節慶視頻》…#北大聖玄 #覺曦軒 (2:37)
# chrome_conn('https://www.youtube.com/watch?v=tBg7-BG-gV0', 10, 155)

# 220910 千江映月・虛實之間－中秋祝福…13集《視頻化•微享》…#北大聖玄 #覺曦軒 (4:49)
# chrome_conn('https://www.youtube.com/watch?v=cqyUZp0NdZI', 10, 144)

# 220909 真愛無限－無緣大慈．同體大悲…第13-4集《視頻化·聖玄語露》…#北大聖玄 #覺曦軒 (6:05)
# chrome_conn('https://www.youtube.com/watch?v=O4KziXOXRYU', 10, 182)

# 220908 超度亡靈－生命教育…第11集《視頻化．微享》…#北大聖玄 #覺曦軒 (12:16)
# chrome_conn('https://www.youtube.com/watch?v=chhu_xACpUQ', 10, 240)

# 220907 與世界首富對話－人生四悟…第78集《5分鐘·奇葩 & 閨蜜》…#北大聖玄#覺曦軒 (7:37)
# chrome_conn('https://www.youtube.com/watch?v=BF5bK7YZwCM', 10, 226)

# 220906 正確詮釋－四種存在力量…05集《視頻化·異次元－解密》…#北大聖玄#覺曦軒 (7:18)
# chrome_conn('https://www.youtube.com/watch?v=o6XiFOlwy0E', 10, 218)

# 220905 解套．悲秋綜合症…第10集《煩惱．DUCK 不必》…#北大聖玄 #覺曦軒 (5:48)
# chrome_conn('https://www.youtube.com/watch?v=MWnrtdz5yH0', 20, 173)

# 220902 在平凡中．照見不平凡…第13-3集《視頻化－聖玄語錄》…#北大聖玄 #覺曦軒 (6:30)
# chrome_conn('https://www.youtube.com/watch?v=aTwHZwV3gAM', 10, 194)

# 220901 超越時空－古今對話…第66-21集《視頻化．教學相長》…#北大聖玄 #覺曦軒 (13:13)
# chrome_conn('https://www.youtube.com/watch?v=0yBNJfAKj98', 10, 263)

# 220831 選擇我所愛－愛我所選擇…第77集《5分鐘·奇葩 & 閨蜜》…#北大聖玄#覺曦軒 (5:58)
# chrome_conn('https://www.youtube.com/watch?v=5qQ5EH88Igk', 10, 178)

# 220830 苦海無邊－提月點燈…第12集《提月點燈－話創異》…#北大聖玄 #覺曦軒 (13:42)
# chrome_conn('https://www.youtube.com/watch?v=pUCkbYlRlew', 10, 272)

# 220829 起死回生…第11集《提月點燈－話創異》…#北大聖玄 #覺曦軒 (12:44)
# chrome_conn('https://www.youtube.com/watch?v=rcqqQMJPjKo', 10, 254)

# 220821 四正勤如意足、不捨精進－菩薩行…第65集《維摩詰經》…#北大聖玄 #覺曦軒 (1:24:04)
# chrome_conn('https://www.youtube.com/watch?v=w_kh7ZBHQJI', 20, 480)

# 220826 般若智．世間智－交叉對話…第13-2集《視頻化－聖玄語錄》…#北大聖玄 #覺曦軒 (8:41)
# chrome_conn('https://www.youtube.com/watch?v=8fXsWKlC430', 20, 240)

# 220825 酷酷雲端女郎—風情萬種…05集《視頻化·微享》…#北大聖玄 #覺曦軒 (5:38)
# chrome_conn('https://www.youtube.com/watch?v=8CVrkRc8klY', 20, 165)

# 220824 馬斯克傳奇－即創．創異…第76集《5分鐘．奇葩 & 閨蜜》…#北大聖玄#覺曦軒 (8:31)
# chrome_conn('https://www.youtube.com/watch?v=mDx2o0bNXdo', 20, 170)

# 220822 解套．社會陷阱…第9集《煩惱．DUCK 不必》…#北大聖玄 #覺曦軒 (5:12)
# chrome_conn('https://www.youtube.com/watch?v=1gMevADcjD4', 20, 154)

# 220819 世間無常－科學會通 …13-1集《視頻化－聖玄語錄》…#北大聖玄 #覺曦軒 (5:43)
# chrome_conn('https://www.youtube.com/watch?v=RBrjW5WMnjw', 10, 170)

# 220814 行四念處．不離身受心法－菩薩行…第64集《維摩詰經》…#北大聖玄 #覺曦軒** (1:20:27)
# chrome_conn('https://www.youtube.com/watch?v=a4aLxrkdam4', 10, 480)

# 220817 走投無路．出奇制勝－馬斯克秘笈…75集《5分鐘·奇葩&閨蜜》…#北大聖玄#覺曦軒 (10:00)
# chrome_open('https://www.youtube.com/watch?v=7ojrkRWdhvU', 10, 190)

# 220816 探密－異次元物語…04集《視頻化·異次元－解密》》…#北大聖玄#覺曦軒 (13:10)
# chrome_conn('https://www.youtube.com/watch?v=dqGfFAJyV3c', 10, 300)

# 220915 解套·畢業就是失業…第8集《煩惱·DUCK不必》修三…#北大聖玄#覺曦軒 (5:30)
# chrome_conn('https://www.youtube.com/watch?v=BQ1O_K4ZTRI', 10, 160)

# 220807 不貪著、不隨順－菩薩行…第63集《維摩詰經》…#北大聖玄 #覺曦軒 (1:16:00)
# chrome_conn('https://www.youtube.com/watch?v=DOCLDnu3LjE', 10, 500)

# 220813 新奢華－全心奢華…第74集《5分鐘·奇葩&閨蜜》…#北大聖玄#覺曦軒 (6:49)
# chrome_conn('https://www.youtube.com/watch?v=XuqjFXVATxY', 10, 200)

# 220812 慶盂蘭盆．贊中元－跨領域對話…10集《視頻化·微享－節慶》…#北大聖玄 #覺曦軒 (11:08)
# chrome_conn('https://www.youtube.com/watch?v=TpZjCJlWigw', 10, 250)

# 220810 破壞性創新－實操落地…第73集《5分鐘·奇葩&閨蜜》…#北大聖玄#覺曦軒 (7:01)
# chrome_conn('https://www.youtube.com/watch?v=C1uiJrPx2pQ', 10, 200)

# 220809 移居火星－科學巨人評析…第3集《視頻化．異次元－解密》…#北大聖玄#覺曦軒 (9:19)
# chrome_conn('https://www.youtube.com/watch?v=3O7OCFnaf3I', 10, 140)

# 220731 見菩提相而取證－增上慢人…第62集《維摩詰經》…#北大聖玄 #覺曦軒 (1:50:08)
# chrome_conn('https://www.youtube.com/watch?v=fGsIxQ1e_yA', 10, 500)

# 220806 腦科學－禪定vs.腦波…第71集《5分鐘·奇葩&閨蜜》…#北大聖玄#覺曦軒 (6:07)
# chrome_conn('https://www.youtube.com/watch?v=bX6Yw_sL7mw', 10, 180)

# 220805 文殊睿智－驚艷度眾…14-12集《聖玄語露》…#北大聖玄 #覺曦軒 (5:33)
# chrome_conn('https://www.youtube.com/watch?v=JYhiUNdI8MQ', 10, 165)

# 220804 傳說中的…新瓶舊酒…02集《關鍵出擊》…#北大聖玄#覺曦軒 (8:33)
# chrome_conn('https://www.youtube.com/watch?v=Tp0vS1GNjaE', 10, 240)

# 220725 解套．顛倒夢想…第7集《煩惱．DUCK 不必》…#北大聖玄#覺曦軒 (4:24)
# chrome_conn('https://www.youtube.com/watch?v=Kn4tQ-HxkRw', 10, 200)

# 220802 第一性原理．息災免難－文殊八字…07集《視頻化．微享》…#北大聖玄 #覺曦軒 (7:10)
# chrome_conn('https://www.youtube.com/watch?v=OAXXttgBn7Q', 10, 260)

# 220724 菩提性相空寂－無有可得者…第61集《維摩詰經》…#北大聖玄 #覺曦軒 (1:36:56)
# chrome_conn('https://www.youtube.com/watch?v=0TWTYnv1j3E', 10, 500)

# 220622 《10分鐘·奇葩＆閨蜜》第61集; 預立遺囑－臨終關懷; 預立遺囑…時代前沿脈動…跟上得利！ (5:47)
# chrome_conn('https://b.scene.ryxiut.net/s/zCSoSuuy/1657409891884?bt=yxy', 50, 8, 3)
# chrome_conn('https://www.youtube.com/watch?v=mW8HAcnSSkc', 10, 340)
# chrome_conn('https://www.youtube.com/watch?v=mW8HAcnSSkc', 10, 260)

# 220730 黃金屋．顏如玉－炸開傳統……第三名投稿文《視頻化·教學相長·61-10集》…#北大聖玄#覺曦軒…修一 (16:04)
# chrome_conn('https://www.youtube.com/watch?v=uCr15pAv9OI', 10, 300)

# 220729 仗劍殺佛－甚深意涵…14-11集《聖玄語露》…#北大聖玄 #覺曦軒 (5:21)
# chrome_conn('https://www.youtube.com/watch?v=sK_m0WI89iQ', 10, 220)

# 220728 多頭運作 - 王牌金腦…第二名投稿文《視頻化·教學相長·60-8集》…#北大聖玄#覺曦軒 (14:34)
# chrome_conn('https://www.youtube.com/watch?v=-rvnt8Ec3_c', 10, 300)

# 220727 馬斯克秘笈－夢想落地…第72集《5分鐘·奇葩&閨蜜》…#北大聖玄#覺曦軒 (5:40)
# chrome_conn('https://www.youtube.com/watch?v=34ac3JVi-Kc', 10, 240)

# 220726 光 - 進出異次元介質…第02集《視頻化．異次元－解密》…#北大聖玄 #覺曦軒 (13:15)
# chrome_conn('https://www.youtube.com/watch?v=uvDr70bBCBw', 10, 300)

# 220711 《煩惱．DUCK 不必》第6集 解套．臨終恐懼五大事…#北大聖玄#覺曦軒 (5:00)
# chrome_conn('https://www.youtube.com/watch?v=rBpaNnwZZlI', 10, 250)

# 220717 菩提之相－實無有法可知…第60集《維摩詰經》…#北大聖玄 #覺曦軒 (1:22:14)
# chrome_conn('https://a.scene.ryxiut.net/s/51rLUXBb/1658112651729?bt=yxy', 20, 10)
# chrome_conn('https://www.youtube.com/watch?v=2yBiVxmsn1A', 10, 500)

# 220723 《5分鐘·奇葩＆閨蜜》第70集 主題：困境vs.仙境－一念之間; 思惟昇華…超越一切束縛…困境變仙境！ (6:55)
# chrome_conn('https://www.youtube.com/watch?v=NXlLbuargJE', 10, 260)


# 220722《聖玄語露·第14-9集》🌺🌺🌺無相修慧－四大關鍵意涵 (5:42)
# chrome_conn('https://www.youtube.com/watch?v=ez8olIX-dNY', 10, 240)

# 220721 《視頻化·微享》北大尼師 - 大陸情…04集…#北大聖玄 #覺曦軒 (3:19)
# chrome_conn('https://www.youtube.com/watch?v=O3tx5k1fiBY', 10, 180)

# 220720 《5分鐘·奇葩＆閨蜜》第69集🌺🌺主題：對望－明月窗‧裝飾夢; 對望的深度省思－橋上風景‧樓上看 (3:37)
# chrome_conn('https://www.youtube.com/watch?v=4wOjqauZwro', 10, 200)

# 220719 異次元探秘—生、死切換…01集《視頻化‧異次元—解密》…#北大聖玄 #覺曦軒 (10:35)
# chrome_conn('https://www.youtube.com/watch?v=gcxxb668FFc', 10, 200)

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
# chrome_conn('https://a.scene.ryxiut.net/s/0lkTXVid/1656467885377', 50, 8, 3)

# 均衡身心靈‧妙法出奇制勝 第6集《10分鐘·奇葩&閨蜜》  主題：出奇制勝－世間+ 出世間法
# chrome_conn('https://c.scene.ryxiut.net/s/9mUa5tLm/', 50, 8, 3)

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
# chrome_conn('https://www.youtube.com/watch?v=2NiJppBBXVU', 10, 276, 0)

# 220707 《微言悅享》主題：震撼開示—脫胎轉化; 久病床前無孝子…轉化思惟，則雙贏！…震撼開示，不可思議！
# chrome_conn('https://youtu.be/H-lNH__Tznc', 300, 10, 0)

# 《微言悅享》主題：震撼開示—脫胎轉化; 久病床前無孝子…轉化思惟，則雙贏！…震撼開示，不可思議！
# chrome_conn('https://www.youtube.com/watch?v=H-lNH__Tznc', 10, 300, 0)

# 220706 《10分鐘·奇葩＆閨蜜》第65集; 🌺🌺主題：三輪體空－最高階佈施; 三輪體空…無盡福田的代言…最高階的佈施！
# chrome_conn('https://www.youtube.com/watch?v=czDUOUE-UqA', 10, 329, 0)

# 220705 《異次元—解密》🌺🌺主題：念波－透視能力，意識透視能力，人皆有之！…端視念波頻率、強度而論斷。
# chrome_conn('https://v.eqxiu.cn/s/drvgK3JV', 50, 8, 3)

# 220704 解套·死局…人人必修的學分…#煩惱·DUCK不必 🌺🌺 第5集…主題：解套·死局
# chrome_conn('https://www.youtube.com/watch?v=cIrHY-k7wnQ', 10, 264, 0)
# chrome_conn('https://v.eqxiu.cn/s/Psb3JZID?bt=yxy', 10, 10, 3)

# 220626 《跨領域－重磅對話》…時代前沿對話！ 第57集 《維摩詰經》…全球直播教學視頻 主題：雖行於空－植種德本
# chrome_conn('https://www.youtube.com/watch?v=UMNKSNIAt8I', 10, 500)
# chrome_conn('https://s.eqxiu.cn/s/SOcpPeOv', 20, 10)

# 220702 《10分鐘·奇葩＆閨蜜》第64集 主題：生命回顧－導負為正; 重走舊時路…賦予新意義！
# chrome_conn('https://www.youtube.com/watch?v=Pd3qSMDXmNg', 10, 348)

# 220701 《圣玄语露·第14-7集》 生命内在觉醒，是不可替代的永恒真幸福！
# chrome_conn('https://www.youtube.com/watch?v=0iTzkoL9-VY', 10, 240)
# chrome_conn('https://v.eqxiu.cn/s/Aletmrg1', 10, 10)

# 220630 《微言悅享》主題：大臼齒與主人的對話; 大臼齒與主人的親密關係！…有情、非情…來自同一終極本質！
# chrome_conn('https://s.eqxiu.cn/s/BpKCU61d?bt=yxy', 50, 10)

# 220630 DT: 《異次元—解密》主題：見相非相 - 空間扭曲
# chrome_conn('https://s.eqxiu.cn/s/4TQFtLQo', 10, 10)

# 220629 第63集《10分鐘·奇葩＆閨蜜》 🌺🌺主題：臨終關懷－五全照顧 (善生、善終…生死兩無憾！)
# https://www.youtube.com/watch?v=i5vx63X9Ors
# chrome_conn('https://a.scene.ryxiut.net/s/tH1pXUEb/1656457671824', 50, 10)

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


