from abc import ABC, abstractmethod


# Базовый класс для уведомлений
class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


# Конкретный класс для Email уведомлений
class EmailNotification(Notification):
    def notify(self, message):
        print(f"Sending Email: {message}")


# Конкретный класс для SMS уведомлений
class SMSNotification(Notification):
    def notify(self, message):
        print(f"Sending SMS: {message}")


# Конкретный класс для Push уведомлений
class PushNotification(Notification):
    def notify(self, message):
        print(f"Sending Push Notification: {message}")


# Базовый класс фабрики
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass


# Фабрика для Email уведомлений
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()


# Фабрика для SMS уведомлений
class SMSNotificationFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()


# Фабрика для Push уведомлений
class PushNotificationFactory(NotificationFactory):
    def create_notification(self):
        return PushNotification()


# * * * * * * * * * * * * * * * * * * * * * * * * *
# Клиентский код
def send_notification(factory: NotificationFactory, message: str):
    notification = factory.create_notification()
    notification.notify(message)


def main():
    # Пример использования
    email_from_factory = EmailNotificationFactory()
    sms_from_factory = SMSNotificationFactory()
    push_from_factory = PushNotificationFactory()

    send_notification(email_from_factory, "Hello via Email!")
    send_notification(sms_from_factory, "Hello via SMS!")
    send_notification(push_from_factory, "Hello via Push!")


if __name__ == "__main__":
    main()
