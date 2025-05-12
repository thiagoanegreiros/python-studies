from typing import Protocol


class NotificationChannel(Protocol):
    def send_notification(self, destiny: str, message: str): ...


class EmailNotification(NotificationChannel):
    def send_notification(self, destiny: str, message: str):
        print(f'Sending this message though email to {destiny} - {message}')


class PhoneNotification(NotificationChannel):
    def send_notification(self, destiny: str, message: str):
        print(f'Sending this message though phone to {destiny} - {message}')


class NotificationService():
    def __init__(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel
    
    def send(self, destiny: str, message: str):
        self.notification_channel.send_notification(destiny, message)


ns_email = NotificationService(EmailNotification())
ns_email.send('test@test.com', 'My email message')


ph_email = NotificationService(PhoneNotification())
ph_email.send('1166889933', 'My sms message')
