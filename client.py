import os
import yaml

class Client:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
    
    def load_config(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    
    def run(self):
        server_ip = self.config.get('ServerIPAddress', 'localhost')
        run_localhost = self.config.get('run_localhost', False)
        
        if run_localhost:
            print(f"Running on localhost with IP: {server_ip}")
        else:
            print(f"Connecting to server at {server_ip}")

if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')  # Adjust the path as needed
    client_instance = Client(config_path)
    client_instance.run()

##