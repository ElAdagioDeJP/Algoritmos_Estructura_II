import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        """
        Lee el contenido del archivo JSON y lo devuelve como un diccionario.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: El archivo {self.file_path} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.file_path} no tiene un formato JSON válido.")
        except Exception as e:
            print(f"Error: {e}")
            return None
        if __name__ == "__main__":
            file_path = "/path/to/your/json/file.json"  # Replace with the actual file path
            reader = JsonReader(file_path)
            json_data = reader.read_json()
            if json_data:
                # Do something with the json_data
                print(json_data)