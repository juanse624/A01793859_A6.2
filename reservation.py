"""
Este módulo contiene la clase reservation
"""
import json
import os
from customer import Customer
from hotel import Hotel


class Reservation:
    """Clase que representa una reserva."""
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def to_dict(self):
        """Convierte los atributos de la reserva en un diccionario."""
        return {
            "customer": self.customer.to_dict(),
            "hotel": self.hotel.to_dict()
        }

    def save_to_file(self):
        """Guarda los detalles de la reserva en un archivo JSON."""
        with open(f"{self.customer.name}_{self.hotel.name}_reservation.json",
                  "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)

    @staticmethod
    def load_from_file(customer_name, hotel_name):
        """Carga los detalles de la reserva desde un archivo JSON."""
        try:
            with open(f"{customer_name}_{hotel_name}_reservation.json",
                      "r", encoding="utf-8") as f:
                data = json.load(f)
                customer = Customer(data['customer']['name'],
                                    data['customer']['email'])
                hotel = Hotel(data['hotel']['name'], data['hotel']['location'],
                              data['hotel']['rooms_available'])
                return Reservation(customer, hotel)
        except FileNotFoundError:  # pragma: no cover
            print(f"La reserva para {customer_name} en \
                  {hotel_name} no existe.")  # pragma: no cover
            return None  # pragma: no cover

    def delete_file(self):
        """Elimina el archivo JSON de la reserva."""
        try:
            os.remove(f"{self.customer.name}_{self.hotel.name}_"
                      "reservation.json")
        except FileNotFoundError:
            print(f"La reserva para {self.customer.name} en \
                  {self.hotel.name} no existe.")
