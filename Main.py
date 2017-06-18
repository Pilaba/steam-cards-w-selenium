"""
Program made by poche
09/01/2017
automatizando la exploracion de cromos
1.- THIS SCRIPT NEED ACCESS TO IMAP IN YOUR GMAIL ACCOUNT
2.- AND NEED A DRIVER FOR WEB BROWSER OF YOUR PREFERENCE IN YOUR PATH SYSTEM 
HERE WE USE https://github.com/operasoftware/operachromiumdriver/releases
3.- Need selenium API -- "pip install selenium"  if fatal error appears use  "python -m pip install selenium"
"""

from selenium import webdriver
import time

driver = webdriver.Opera() #Se utilizara opera
#driver = webdriver.Opera(executable_path="PATH/TO/WEBDRIVER/FOR/OPERA")
driver.implicitly_wait(30) #Tiempo de espera implicito para la busqueda de elementos

#Credenciales STEAM
user="###"
passw="###"

print("entrando al login con la cuenta %s"%(user))
driver.get("https://store.steampowered.com//login/")

hoja=driver.find_element_by_name("logon")
hoja.find_element_by_id("input_username").send_keys(user)
hoja.find_element_by_id("input_password").send_keys(passw)
hoja.submit()

#Credenciales correo gmail
correo = "###"
password = "###"
print("buscando correo en: %s"%(correo))

from Project import stemCode

while True:
    time.sleep(2)
    Obj = stemCode.SteamCode(correo,password)
    codigo = Obj.CheckSteamCode()
    print("Remitente: %s \nAsunto: %s\nHora: %s" % (Obj.get_From(), Obj.get_subject().decode("utf-8"), Obj.get_date()))
    if(codigo==False):
        print("CORREO INCORRECTO!");
        continue
    else:
        break
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


