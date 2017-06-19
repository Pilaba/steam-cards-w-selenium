"""
Program made by Baldemar Alejandres Garcia
09/01/2017
automatizando la exploracion de cromos en las ofertas de steam
1.- THIS SCRIPT NEED ACCESS TO IMAP IN YOUR GMAIL ACCOUNT
2.- NEED A DRIVER FOR WEB BROWSER OF YOUR PREFERENCE IN YOUR PATH SYSTEM OR JUST THE PATH OF THE DRIVER 
HERE WE USE OPERA DRIVER https://github.com/operasoftware/operachromiumdriver/releases PROVIDED IN webDriver\\operadriver
3.- Need selenium API -- "pip install selenium"  if fatal error appears use  "python -m pip install selenium" OR WE JUST 
PROVIDED THE LIBRARY IN THE FOLDER seleniumApi\\Webdriver
"""

from seleniumApi import webdriver
import stemCode
import time

driver = webdriver.Opera(executable_path="Webdriver\\operadriver") #in this proyect we use opera driver
driver.implicitly_wait(30) #Tiempo de espera implicito para la busqueda de elementos

###################Credenciales STEAM
user="###"
passw="###"

print("entrando al login con la cuenta %s"%(user))
driver.get("https://store.steampowered.com//login/")

hoja=driver.find_element_by_name("logon")
hoja.find_element_by_id("input_username").send_keys(user)
hoja.find_element_by_id("input_password").send_keys(passw)
hoja.submit()

###################Credenciales correo gmail
correo = "###"
password = "###"
print("buscando correo en: %s"%(correo))

<<<<<<< HEAD:Codigo/Main.py
=======
from steam-cards-w-selenium-master import stemCode

>>>>>>> 164ca848746e0530c89045fadb3ab1e8bbf9532a:Main.py
while True:
    time.sleep(2)
    Obj = stemCode.SteamCode(correo,password)
    codigo = Obj.CheckSteamCode()
    print("Remitente: %s \nAsunto: %s\nHora: %s" % (Obj.get_From(), Obj.get_subject().decode("utf-8"), Obj.get_date()))
    if(codigo==False):
        print("CORREO INCORRECTO!"); continue
    else: break;
print("Colocando codigo %s"%(codigo))

enter = driver.find_element_by_id("authcode")
enter.send_keys(codigo)
enter.submit()
time.sleep(3)
irSteam = driver.find_element_by_xpath(r"//*[@id='success_continue_btn']/div[1]")
irSteam.click()

#IF YOU WANT A PHONE MESSAGE
"""
from SMS import twilioSMS
twilioSMS().sendSMS("Exito!! Inicio de sesion con '%s'"%(Obj.get_accountName().strip()))
"""
Obj.close()
driver.quit()


