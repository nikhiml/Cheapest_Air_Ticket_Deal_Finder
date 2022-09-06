from twilio.rest import Client
import smtplib


ACCOUNT_SID = 'ACf3edb3f928face31f32db8d81f6a319c'
AUTH_TOKEN = '04bed3ffc85be164e7f9c60c406521db'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

my_email = "****************"
my_password = "**********"


class NotificationManager:
    def __init__(self, all_users):
        self.club_users = all_users
        self.message_flights = {}
        self.user_dict = {}
        self.user_message = ''
        self.mail_subject = ''
        # self.send_message()
        # self.send_mail()

    def create_message(self, cheap_flights_data):
        self.message_flights = cheap_flights_data
        if len(self.message_flights['route']) == 2:
            self.user_message = f"{self.message_flights['route'][0]['cityFrom']} - {self.message_flights['route'][0]['cityTo']}, " \
                                f"leaving on {self.message_flights['route'][0]['local_departure']} and arriving back on " \
                                f"{self.message_flights['route'][1]['local_arrival']} - Total Fare: {self.message_flights['price']} " \
                                f"Booking at https://www.google.co.uk/flights?hl=en#flt={self.message_flights['route'][0]['flyFrom']}." \
                                f"{self.message_flights['route'][0]['flyTo']}.{self.message_flights['route'][0]['local_departure'].split('T', 1)[0]}*" \
                                f"{self.message_flights['route'][1]['flyFrom']}.{self.message_flights['route'][1]['flyTo']}." \
                                f"{self.message_flights['route'][1]['local_departure'].split('T', 1)[0]}"

            self.mail_subject = f"{self.message_flights['route'][0]['cityFrom']} - {self.message_flights['route'][0]['cityTo']}"

        else:
            self.user_message = f"{self.message_flights['route'][0]['cityFrom']} - {self.message_flights['route'][0]['cityTo']} - " \
                                f"{self.message_flights['route'][1]['cityTo']}, leaving on {self.message_flights['route'][0]['local_departure']} " \
                                f"and arriving back {self.message_flights['route'][2]['cityFrom']} - {self.message_flights['route'][2]['cityTo']} -" \
                                f" {self.message_flights['route'][3]['cityTo']} on {self.message_flights['route'][3]['local_arrival']} - " \
                                f"Total Fare: {self.message_flights['price']}"
            self.mail_subject = f"{self.message_flights['route'][0]['cityFrom']} - {self.message_flights['route'][0]['cityTo']} - {self.message_flights['route'][1]['cityTo']} "

        self.send_message()
        self.send_mail()

    def send_message(self):
        message = client.messages.create(body=f"We found a deal for {self.user_message}",
                                              from_='+17473000192', to='************')
        print(message.status)

    def send_mail(self):

        for user in self.club_users['users']:
            to_email = user['email']
            with smtplib.SMTP("smtp.gmail.com") as my_connection:
                my_connection.starttls()
                my_connection.login(user=my_email, password=my_password)
                my_connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject: Flight Deal - "
                                                                                  f"{self.mail_subject} \n\n Dear {user['firstName']} \n {self.user_message}")


