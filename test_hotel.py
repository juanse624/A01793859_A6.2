"""Módulo de pruebas para la clase Hotel."""
import unittest
import os
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Clase que contiene pruebas unitarias para la clase Hotel."""

    def setUp(self):
        """Configura un hotel para las pruebas."""
        self.hotel = Hotel("Hotel ABC", "Ciudad XYZ", 100)

    def tearDown(self):
        """Elimina el archivo de hotel después de las pruebas."""
        self.hotel.delete_file()

    def test_save_and_load_hotel(self):
        """Prueba guardar y cargar detalles del hotel."""
        self.hotel.save_to_file()
        loaded_hotel = Hotel.load_from_file("Hotel ABC")
        self.assertIsNotNone(loaded_hotel)
        self.assertEqual(loaded_hotel.name, "Hotel ABC")
        self.assertEqual(loaded_hotel.location, "Ciudad XYZ")
        self.assertEqual(loaded_hotel.rooms_available, 100)

    def test_delete_hotel_file(self):
        """Prueba eliminar el archivo de hotel."""
        self.hotel.save_to_file()
        self.assertTrue(os.path.exists("Hotel ABC.json"))
        self.hotel.delete_file()
        self.assertFalse(os.path.exists("Hotel ABC.json"))

    def test_special_characters_in_location(self):
        """Prueba para guardar y cargar un hotel con ubicación especial."""
        hotel = Hotel("Hotel Special", "City with special characters !@#", 10)
        hotel.save_to_file()
        loaded_hotel = Hotel.load_from_file("Hotel Special")
        self.assertIsNotNone(loaded_hotel)
        self.assertEqual(loaded_hotel.location,
                         "City with special characters !@#")

    def test_delete_nonexistent_hotel_file(self):
        """Prueba para eliminar un archivo de hotel que no existe."""
        hotel = Hotel("Nonexistent Hotel", "City", 5)
        self.assertFalse(os.path.exists("Nonexistent Hotel.json"))
        hotel.delete_file()  # No debe lanzar excep si el archivo no existe

    def test_invalid_data_handling(self):
        """Prueba para verificar el manejo de datos no válidos."""
        # Intenta cargar un archivo con datos no válidos
        with open("Invalid_Hotel.json", "w",
                  encoding="utf-8") as f:
            f.write("Invalid JSON")
        loaded_hotel = Hotel.load_from_file("Invalid_Hotel")
        self.assertIsNone(loaded_hotel)

        # Intenta guardar con datos no válidos
        invalid_hotel = Hotel(None, None, None)
        with self.assertRaises(TypeError):
            invalid_hotel.save_to_file()

    def test_load_nonexistent_hotel_file(self):
        """Prueba para cargar un archivo de hotel que no existe."""
        loaded_hotel = Hotel.load_from_file("Nonexistent_Hotel")
        self.assertIsNone(loaded_hotel)

    def test_save_with_null_data(self):
        """Prueba para guardar un hotel con datos nulos."""
        null_hotel = Hotel(None, None, None)
        with self.assertRaises(TypeError):
            null_hotel.save_to_file()

    def test_load_invalid_json_file(self):
        """Prueba para cargar un archivo JSON con formato incorrecto."""
        with open("Invalid_JSON_Hotel.json", "w",
                  encoding="utf-8") as f:
            f.write("This is not a valid JSON format")
        loaded_hotel = Hotel.load_from_file("Invalid_JSON_Hotel")
        self.assertIsNone(loaded_hotel)

    def test_delete_nonexistent_file(self):
        """Prueba para eliminar un archivo que no existe."""
        non_existing_hotel = Hotel("Nonexistent Hotel", "City", 5)
        non_existing_hotel.delete_file()


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
