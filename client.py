class Client:
    def __init__(self):
        self.server_ip = None

    def set_server_ip(self, ip):
        self.server_ip = ip

    def print_server_ip(self):
        print(f'Server IP Address: {self.server_ip}')

    def print_config(self):
        print(f'Server IP Address: {self.server_ip}')
        print(f'Database URL: {self.database_url}')
        print(f'Log Level: {self.log_level}')

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.set_server_ip(config.get('ServerIPAddress'))
        self.set_database_url(config.get('DatabaseURL'))
        self.set_log_level(config.get('LogLevel'))

client = Client()
client.load_config()
client.print_config()

##let's test the workflow from fullstack-repo