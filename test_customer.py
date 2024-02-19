"""Módulo de pruebas para la clase Customer."""
import unittest
import os
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Clase que contiene pruebas unitarias para la clase Customer."""

    def setUp(self):
        """Configura un cliente para las pruebas."""
        self.customer = Customer("John Doe", "john@example.com")

    def tearDown(self):
        """Elimina el archivo de cliente después de las pruebas."""
        self.customer.delete_file()

    def test_save_and_load_customer(self):
        """Prueba guardar y cargar detalles del cliente."""
        self.customer.save_to_file()
        loaded_customer = Customer.load_from_file("John Doe")
        self.assertIsNotNone(loaded_customer)
        self.assertEqual(loaded_customer.name, "John Doe")
        self.assertEqual(loaded_customer.email, "john@example.com")

    def test_delete_customer_file(self):
        """Prueba eliminar el archivo de cliente."""
        self.customer.save_to_file()
        self.assertTrue(os.path.exists("John Doe.json"))
        self.customer.delete_file()
        self.assertFalse(os.path.exists("John Doe.json"))

    def test_special_characters_in_name(self):
        """Prueba para guardar y cargar un cliente con nombre especial."""
        customer = Customer("John !@# Doe", "john@example.com")
        customer.save_to_file()
        loaded_customer = Customer.load_from_file("John !@# Doe")
        self.assertIsNotNone(loaded_customer)
        self.assertEqual(loaded_customer.name, "John !@# Doe")

    def test_delete_nonexistent_customer_file(self):
        """Prueba para eliminar un archivo de cliente que no existe."""
        customer = Customer("Nonexistent Customer", "email@example.com")
        self.assertFalse(os.path.exists("Nonexistent Customer.json"))
        customer.delete_file()

    def test_load_from_file_handles_file_not_found_error(self):
        """Prueba para verific que load_from_file maneje FileNotFoundError."""
        loaded_customer = Customer.load_from_file("Nonexistent Customer")
        self.assertIsNone(loaded_customer)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
