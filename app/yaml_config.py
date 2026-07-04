import yaml
import os

class YamlUtilities():
    def __init__(self, path):
        self.path = path

    def deserializer(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                data = yaml.safe_load(file)
                return data
        else:
            return None
    
    def Serializer(self, text):
         with open(self.path, 'w') as file:
            yaml.safe_dump(text, file)
            return "Success"

            