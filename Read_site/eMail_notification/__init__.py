import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "michal.hvila@gmail.com"
receiver_email = "hvila.michal@gmail.com"
subject_email = "Python mail"

text_email = """\
       Hi,\n
        How are you?\n
        Real Python has many great tutorials:
        www.realpython.com
        """

html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               <a href="http://www.realpython.com">Real Python</a> 
               has many great tutorials.
            </p>
          </body>
        </html>
        """


class Email:
    def __init__(self,subject, sender, receiver, text):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.text = text
    

    def odosli(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender
        message["To"] = self.receiver
    
        
        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(self.text, "plain")
        part2 = MIMEText(self.text, "html")
        
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        message.attach(part2)
        
        
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#        with smtplib.SMTP_SSL("smtp.dwcslovakia.sk", 465) as server:    
            password = input("Type your password and press enter:")
            server.login(self.sender, password)
            server.sendmail(
                self.sender, self.receiver, message.as_string()
            )
        print("Email bol odoslany .....")
 
# ----------------------------------------------------------- 
            
#mail_a = Email(subject_email, sender_email, receiver_email, text_email)
#mail_a.odosli(xlbwwvmcortykbci)



 