import smtplib

def getSMTPServer(sender: str, password: str) -> smtplib.SMTP_SSL:
    '''
    Creates and returns an SMTP server object for sending emails.

    Parameters:
        sender (str): The email address of the sender.
        password (str): The password or app-specific password for the sender's email account.

    Returns:
        smtplib.SMTP_SSL: The SMTP server object.

    Raises:
        smtplib.SMTPAuthenticationError: If authentication fails.
        Exception: For other SMTP connection errors.
    '''
    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.login(sender, password)
        return smtp_server
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. If you're using Gmail with 2FA,")
        print("Remember to use correct domain when creating smtplib.SMTP_SSL server.\nYou may need to create an App Password: https://myaccount.google.com/apppasswords, tutorial: https://www.youtube.com/watch?v=g_j6ILT-X0k")
        raise
    except Exception as e:
        print(f"SMTP connection error: {e}")
        raise