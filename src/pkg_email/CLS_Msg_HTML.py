import datetime as dt

from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

import pkg_email.config_module as config_email
import pkg_common.utils as ut

class CLS_Msg_HTML():

    def __init__(self):
        self.message = MIMEMultipart()
        self.message.add_header('Content-Type','text/html')
        self.sender_email = ''
        self.sender_password = ''
        self.subject = ''
        self.receiver_email = ''
        self.content_html = ""


    def set_subject(self, txt_subject):
        self.subject = txt_subject
        self.message['Subject'] = txt_subject

    
    def set_receiver(self, txt_receiver):
        self.receiver_email = txt_receiver
        self.message['To'] = ','.join(txt_receiver)

    
    def add_content_html(self, content_html_to_add):
        self.content_html += content_html_to_add
        #self.content_html += "fsfasda"

    
    def add_attachment(self, attachment_to_add):
        self.message.attach(attachment_to_add)
    
        
    def send_email_gmail(self):
        self.sender_email = "markets.reporting@gmail.com"
        self.sender_password = ""
        self.message['From'] = 'SRM Analytics'
        #self.message['To'] = 'Reporting Distribution List'
        #self.message['To'] = ', '.join(self.receiver_email)
        self.message.attach(MIMEText(self.content_html , 'html', 'utf-8'))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            #server.login(self.sender_email, self.sender_password)
            server.login(self.sender_email, ut.get_parameters(0))
            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())
            server.quit()
        #print('Email Gmail sent.')

    def send_email_idb(self):
        self.sender_email = 'bloomrmp@iadb.org'
        self.sender_password = ''
        # mudar funcao2
        self.message['From'] = 'bloomrmp@iadb.org'
        #self.message['To'] = ', '.join(self.receiver_email)
        self.message.attach(MIMEText(self.content_html , 'html', 'utf-8'))

        with smtplib.SMTP('smtp.office365.com',587) as server:
            server.ehlo()
            server.starttls()
            #server.login(self.sender_email, self.sender_password)
            server.login(self.sender_email, ut.get_parameters(1))
            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())
            server.quit()
        #print('Email IDB sent.')

    def save_html_file(self):
        file_html = open(f"{config_email.path_output_folder}/{self.subject.replace('|','-')}.html", "w")
        file_html.write(self.content_html)
        file_html.close()