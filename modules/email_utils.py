import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import path
from datetime import datetime
import re

def sendemail(sender: str, recipient: str, cc_list: list, file_attachment_paths: list, subject: str, body: str, smtp_server: smtplib.SMTP_SSL, log_file_path: str) -> bool:
    '''
    Sends an email to the specified recipient with optional CC list and file attachments.

    Parameters:
        sender (str): The email address of the sender.
        recipient (str): The email address of the recipient.
        cc_list (list): A list of email addresses to CC.
        file_attachment_paths (list): A list of file paths to attach to the email.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        smtp_server (smtplib.SMTP_SSL): The SMTP server object for sending the email.
        log_file_path (str): The path to the log file for recording email statuses.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    '''
    try:
        # create message
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = recipient
        message["Cc"] = ", ".join(cc_list)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        # attach files
        for file_path in file_attachment_paths:
            with open(file_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={path.basename(file_path)}")
                message.attach(part)
        # sending email
        server.sendmail(sender, [recipient] + cc_list, message.as_string())
        # append in the log.csv [new row entry: recipient email, success, datetime]
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{recipient},success,{datetime.now()}\n")
        return True

    except Exception as e:
        # log/append in the log.csv [new row entry: recipient email, error, datetime, error message]
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{recipient},error,{datetime.now()},{e}\n")
        return False

def isvalidemail(email: str) -> bool:
    '''
    Validates an email address using a regular expression.

    Parameters:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    '''
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None