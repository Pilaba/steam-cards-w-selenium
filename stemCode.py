
import time,imaplib,email,re
from email.header import decode_header
from email.header import make_header

class SteamCode():
    sesion=None
    emaildecode=None
    rawmail=None
    def __init__(self,Usuario,Clave):
        self.sesion = imaplib.IMAP4_SSL('imap.gmail.com',993)  # Iniciacion del cliente IMAP  con SSL , se coloca el servidor y su puerto
        self.sesion.login(Usuario, Clave)  # Credenciales del correo de GMAIL
        self.__Main()

    def get_subject(self):
        """Obtiene el asunto del correo
            :param mail: obtiene como parametro el email como si fuera cadena ya codificada en("utf-8")
            :return: asunto del correo
            """
        h = decode_header(self.emaildecode.get('subject'))
        return str(make_header(h)).encode('utf-8')

    def get_From(self):
        """ Obtiene el remitente del correo
            :param mail: Toma como parametro el email como si fuera una cadena
            :return: remitente del correo
            """
        f = decode_header(self.emaildecode.get("From"))
        return str(make_header(f).encode("utf-8"))

    def get_date(self):
        """ obtiene la fecha en que se recibio el correo
            :param mail:  Toma como parametro el email como si fuera una cadena
            :return: fecha del correo
            """
        mdate = email.utils.parsedate(self.emaildecode.get('date'))
        return time.strftime('%Y/%B/%d %I:%M:%S %p', mdate)

    def get_accountName(self):
        if ("Access from new web or mobile device" in self.get_subject().decode()):
            PositionA = self.raw_email.decode().find("Dear")
            corte = self.raw_email.decode()[PositionA+4:PositionA+17]; x=corte.strip()
            return x.strip(",")
        else:
            return False

    def CheckSteamCode(self):
        if ("Access from new web or mobile device" in self.get_subject().decode()):
            PositionA = self.raw_email.decode().find("Here is the Steam Guard code you need to login")
            PositionB = self.raw_email.decode().find("This email was generated because of a login attempt from")
            corte = self.raw_email.decode()[PositionA:PositionB]
            code = re.compile(r'\s\S{4}[A-Z0-9]\s').findall(corte)[0].strip()
            return code
        else:
            return False

    def close(self):
        self.sesion.close()

    def __Main(self):#Metodo Privado
        self.sesion.select("inbox")
        # Result OK, Mails_Data es una tupla de los mails que en la primera posicion guarda los respectivos ID´s de cada correo
        # Search toma como parametro los correos que no se han visto
        result, mails_data = self.sesion.search(None, "(UNSEEN)")
        Lista=mails_data[0].split()#Coloca los IDs en una lista
        if len(Lista)<1: raise Exception("No se encontro el correo")
        result, mail_data = self.sesion.fetch(Lista[-1], "(RFC822)")#Toma el correo mas reciente sin ser visto
        self.raw_email = mail_data[0][1]#Toma el codigo html del correo
        self.emaildecode = email.message_from_string(self.raw_email.decode())#Se decodifica el email
