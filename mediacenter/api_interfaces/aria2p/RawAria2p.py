import aria2p


class Aria2p:
    def __init__(self):
        self.aria2 = aria2p.API(
            aria2p.Client(
                host="http://192.168.1.200",
                port=6800,
                secret=""
            )
        )
