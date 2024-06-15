from twilio.rest import Client
import os


def generate_workout_text_message(nomen: str, exercises: list[str]) -> str:
    """
    Meant to take in a list of exercises and generate the workout email's message.
    """
    greeting = f"Hi {nomen},\n\nYour workout today will be:\n"
    bulleted_list = "\n".join(f"- {element}" for element in exercises)
    closing = f"\n\nHave a great workout and an even better day!"

    return greeting + bulleted_list + closing


def send_text(recipient: str, msg):
    # need stronger checks here
    if len(recipient) != 11:
        raise Exception("Invalid number")
    if len(msg) == 0:
        raise Exception("Don't send an empty message!")
    # Start Client
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    sender_phone = os.environ['TWILIO_PHONE_NUMBER']
    client = Client(account_sid, auth_token)

    # Send text
    client.api.account.messages.create(
        to=recipient,
        from_=sender_phone,
        body=msg)
    

if __name__=="__main__":
    # print(generate_workout_text_message("Matt", ["Exercise A", "Exercise B"]))
    