"""Módulo de pruebas para la clase reservation."""
import unittest
import os
from reservation import Reservation
from customer import Customer
from hotel import Hotel


class TestReservation(unittest.TestCase):
    """Clase que contiene pruebas unitarias para la clase Reservation."""

    def setUp(self):
        """Configura una reserva para las pruebas."""
        self.customer = Customer("Jane Smith", "jane@example.com")
        self.hotel = Hotel("Hotel XYZ", "Ciudad ABC", 50)
        self.reservation = Reservation(self.customer, self.hotel)

    def tearDown(self):
        """Elimina el archivo de reserva después de las pruebas."""
        self.reservation.delete_file()

    def test_save_and_load_reservation(self):
        """Prueba guardar y cargar detalles de la reserva."""
        self.reservation.save_to_file()
        loaded_reservation = Reservation.load_from_file("Jane Smith",
                                                        "Hotel XYZ")
        self.assertIsNotNone(loaded_reservation)
        self.assertEqual(loaded_reservation.customer.name, "Jane Smith")
        self.assertEqual(loaded_reservation.hotel.name, "Hotel XYZ")
        self.assertEqual(loaded_reservation.hotel.rooms_available, 50)

    def test_delete_reservation_file(self):
        """Prueba eliminar el archivo de reserva."""
        self.reservation.save_to_file()
        self.assertTrue(
    os.path.exists("Jane Smith_Hotel XYZ_reservation.json"))
        self.reservation.delete_file()
        self.assertFalse(os.path.exists("Jane Smith_Hotel"
                                        "XYZ_reservation.json"))

    def test_special_customer_and_hotel(self):
        """Prueba para guardar y cargar una reser con clie y hot espcial."""
        special_customer = Customer("Jane !@# Smith", "jane@example.com")
        special_hotel = Hotel("Special Hotel",
                              "City with special characters", 20)
        reservation = Reservation(special_customer, special_hotel)
        reservation.save_to_file()
        loaded_reservation = Reservation.load_from_file("Jane !@# Smith",
                                                        "Special Hotel")
        self.assertIsNotNone(loaded_reservation)
        self.assertEqual(loaded_reservation.customer.name, "Jane !@# Smith")
        self.assertEqual(loaded_reservation.hotel.name, "Special Hotel")

    def test_delete_nonexistent_reservation_file(self):
        """Prueba para eliminar un archivo de reserva que no existe."""
        reservation = Reservation(Customer("Nonexistent Customer",
                                           "email@example.com"),
                                  Hotel("Nonexistent Hotel", "City", 5))
        self.assertFalse(os.path.exists("Nonexistent Customer_Nonexistent"
                                        "Hotel_reservation.json"))
        reservation.delete_file()


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
