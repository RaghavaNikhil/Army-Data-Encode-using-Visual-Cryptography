import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

class Email_Sender:
    def __init__(self):
        self.email = "imageshare2020@gmail.com"
        self.password = "imageshare2020@anits"

        # All code in __init__ is taken from stack overflow
        self.server = smtplib.SMTP('smtp.gmail.com', 587) # 587 is port no of smtp
        self.server.ehlo() # stolen code
        self.server.starttls() # stolen code
        self.server.login(self.email, self.password) # login

    def send_email(self, to_email_id, share_path):
        mail = MIMEMultipart() # MIME because image and text are present. dict() returned
        mail['From'] = self.email # from email
        mail['To'] = to_email_id # to email
        mail['Subject'] = "Your Share Of Image" # Subject

        message = ("Dear Share Holder,",
                "Your Share Of Image is Attached ,If you agree mailback Image to Admin")
        body = "\n\n".join(message) # Creating body of message

        mail.attach(MIMEText(body, 'plain')) # Attach the body as plain text to mail. mail is MIMEMultipart()

        attachment_name = share_path.split('/')[-1] # extracting last part in the path to get filename
        attachment = open(share_path, "rb") # reading file in rb mode to preserve image nature

        part = MIMEBase('application', 'octet-stream') # MIME base with octet stream is default
        part.set_payload((attachment).read()) # setting the payload with attachment
        encoders.encode_base64(part) # encoding the image to octect stream
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_name)

        mail.attach(part) # attaching image to original email
        text = mail.as_string() # get stringified mail

        self.server.sendmail(self.email, to_email_id, text) # send email


# sshankarsingh.16.cse@anits.edu.in
# raghuu14@gmail.com
# onlinecse99@gmail.com
# mvraghavanikhil.16.cse@anits.edu.in
# ksaisankar.16.cse@anits.edu.in
# bnikhil.16.cse@anits.edu.in
# balu88861@gmail.com
# dsganeshpatnaik.16.cse@anits.edu.in
# gjagadish.cse@anits.edu.in