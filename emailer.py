import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(address: str="", subj: str="", msg: str=""):
    """
    Meant to send an email given a recipient, subject, and message.
    """
    if len(address) == 0 or len(msg) == 0:
        raise Exception("Invalid arguments to form email.")
    
    # Email Message Formatting
    mimemsg = MIMEMultipart()
    mimemsg['Subject'] = subj
    mimemsg.attach(MIMEText(msg))

    # Email Client
    email = os.environ['EMAIL']
    password = os.environ['PASSWORD']
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(user=email, password=password)
    s.sendmail(from_addr=email, to_addrs=address, msg=mimemsg.as_string())

    return


def generate_workout_email_message(nomen: str, exercises: list[str]) -> str:
    """
    Meant to take in a list of exercises and generate the workout email's message.
    """
    greeting = f"Hello {nomen},\n\nWe hope this email finds you well, and ready to work out!\n\nYour workout today will be:\n"
    bulleted_list = "\n".join(f"- {element}" for element in exercises)
    closing = f"\nHave a great workout and an even better day!\n\nBest,\nYour Workout Care Team"

    return greeting + bulleted_list + closing


if __name__=="__main__":
    msg = generate_workout_email_message("Matt", ["Exercise 1", "Exercise 2"])
    print(msg)
