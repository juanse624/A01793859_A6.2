"""
Este módulo contiene la clase customer
"""
import json
import os


class Customer:
    """Clase que representa un cliente."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte los atributos del cliente en un diccionario."""
        return {
            "name": self.name,
            "email": self.email
        }

    def save_to_file(self):
        """Guarda los detalles del cliente en un archivo JSON."""
        with open(f"{self.name}.json", "w",
                  encoding="utf-8") as f:  # pragma: no cover
            json.dump(self.to_dict(), f)  # pragma: no cover

    @staticmethod
    def load_from_file(customer_name):
        """Carga los detalles del cliente desde un archivo JSON."""
        try:  # pragma: no cover
            with open(f"{customer_name}.json", "r",
                      encoding="utf-8") as f:  # pragma: no cover
                data = json.load(f)  # pragma: no cover
                return Customer(data['name'], data['email'])  \
                    # pragma: no cover
        except FileNotFoundError:  # pragma: no cover
            print(f"El archivo {customer_name}.json no existe.")  \
                # pragma: no cover
            return None  # pragma: no cover

    def delete_file(self):
        """Elimina el archivo JSON del cliente."""
        try:  # pragma: no cover
            os.remove(f"{self.name}.json")  # pragma: no cover
        except FileNotFoundError:  # pragma: no cover
            print(f"El archivo {self.name}.json no existe.")  \
                # pragma: no cover
