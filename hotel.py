"""
Este módulo contiene la clase hotel
"""
import json
import os


class Hotel:
    """Clase que representa un hotel."""
    def __init__(self, name, location, rooms_available):
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Convierte los atributos del hotel en un diccionario."""
        return {
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available
        }

    def save_to_file(self):
        """Guarda los detalles del hotel en un archivo JSON."""
        if self.name is None or \
           self.location is None or \
           self.rooms_available is None:  # pragma: no cover
            raise TypeError("Los datos del hotel son inválidos")  \
                # pragma: no cover
        with open(f"{self.name}.json", "w",
                  encoding="utf-8") as f:  # pragma: no cover
            json.dump(self.to_dict(), f)  # pragma: no cover

    @staticmethod
    def load_from_file(hotel_name):
        """Carga los detalles del hotel desde un archivo JSON."""
        try:  # pragma: no cover
            with open(f"{hotel_name}.json", "r",
                      encoding="utf-8") as f:  # pragma: no cover
                try:  # pragma: no cover
                    data = json.load(f)  # pragma: no cover
                    return Hotel(data['name'], data['location'],
                                 data['rooms_available'])  # pragma: no cover
                except json.decoder.JSONDecodeError:  # pragma: no cover
                    print(f"El archivo {hotel_name}.json "  # pragma: no cover
                          f"contiene datos no válidos.")
                    return None  # pragma: no cover
        except FileNotFoundError:  # pragma: no cover
            print(f"El archivo {hotel_name}.json no existe.")  \
                # pragma: no cover
            return None  # pragma: no cover

    def delete_file(self):
        """Elimina el archivo JSON del hotel."""
        try:  # pragma: no cover
            os.remove(f"{self.name}.json")  # pragma: no cover
        except FileNotFoundError:  # pragma: no cover
            print(f"El archivo {self.name}.json no existe.")  \
                # pragma: no cover
