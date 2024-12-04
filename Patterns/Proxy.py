# Паттерн Proxy предоставляет суррогатный объект, который контролирует доступ к другому объекту.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."


class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def __getattr__(self, name):
        return getattr(self._real_subject, name)

    def request(self):
        print("Proxy: Logging access to RealSubject.")
        return self._real_subject.request()


def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print(proxy.request())  # Output: Proxy: Logging access to RealSubject.
    #         RealSubject: Handling request.


if __name__ == "__main__":
    main()
