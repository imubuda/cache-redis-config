import redis
import os
import yaml

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.file_path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

class RedisConfig:
    def __init__(self, config):
        self.config = config
        self.redis = self.connect()

    def connect(self):
        host = self.config.get('redis', {}).get('host', os.getenv('REDIS_HOST'))
        port = self.config.get('redis', {}).get('port', os.getenv('REDIS_PORT'))
        password = self.config.get('redis', {}).get('password', os.getenv('REDIS_PASSWORD'))
        return redis.Redis(host=host, port=port, password=password)

def get_redis_config(file_path):
    config = Config(file_path)
    return RedisConfig(config)