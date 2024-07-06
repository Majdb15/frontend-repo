class Client:
    def __init__(self):
        self.server_ip = None

    def set_server_ip(self, ip):
        self.server_ip = ip

    def print_server_ip(self):
        print(f'Server IP Address: {self.server_ip}')