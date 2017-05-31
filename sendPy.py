from twilio.rest import Client
import smtplib

class sendPy(object):

    def sendSMS(to, fro, sid, auth, msg):
        
        #To/From format is "+14155555555"

        client = Client(sid, auth)

        message = client.messages.create(
            to    =  to, 
            from_ = fro,
            body  = msg
            )

        print(message.sid)

    def sendEmail(to, fro, emailPass, message):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fro, emailPass)
         
        server.sendmail(fro, to, message)
        server.quit()

