"""Tests for singleton patter"""

import unittest
from uc3m_care import VaccineManager
from uc3m_care.storage.cancel_json_store import CancelJsonStore
from uc3m_care.storage.vaccination_json_store import VaccinationJsonStore
from uc3m_care.storage.patients_json_store import PatientsJsonStore
from uc3m_care.storage.appointments_json_store import AppointmentsJsonStore


class MyTestCase(unittest.TestCase):
    """Tests para el patron singleton"""
    def test_singleton_appointments_json_store(self):
        """test singleton para AppointmentsJsonStore"""
        my_store1 = AppointmentsJsonStore()
        my_store2 = AppointmentsJsonStore()
        my_store3 = AppointmentsJsonStore()
        my_store4 = AppointmentsJsonStore()

        self.assertEqual(my_store1, my_store2)
        self.assertEqual(my_store1, my_store3)
        self.assertEqual(my_store1, my_store4)

    def test_singleton_cancel_json_store(self):
        """test singleton para CancelJsonStore"""
        my_store1 = CancelJsonStore()
        my_store2 = CancelJsonStore()
        my_store3 = CancelJsonStore()
        my_store4 = CancelJsonStore()

        self.assertEqual(my_store1, my_store2)
        self.assertEqual(my_store1, my_store3)
        self.assertEqual(my_store1, my_store4)

    def test_singleton_patients_json_store(self):
        """test singleton para PatientsJsonStore"""
        my_store1 = PatientsJsonStore()
        my_store2 = PatientsJsonStore()
        my_store3 = PatientsJsonStore()
        my_store4 = PatientsJsonStore()

        self.assertEqual(my_store1, my_store2)
        self.assertEqual(my_store1, my_store3)
        self.assertEqual(my_store1, my_store4)

    def test_singleton_vaccination_json_store(self):
        """test singleton para VaccinationJsonStore"""
        my_store1 = VaccinationJsonStore()
        my_store2 = VaccinationJsonStore()
        my_store3 = VaccinationJsonStore()
        my_store4 = VaccinationJsonStore()

        self.assertEqual(my_store1, my_store2)
        self.assertEqual(my_store1, my_store3)
        self.assertEqual(my_store1, my_store4)

    def test_singleton_vaccine_manager(self):
        """test singleton para AppointmentsJsonStore"""
        my_store1 = VaccineManager()
        my_store2 = VaccineManager()
        my_store3 = VaccineManager()
        my_store4 = VaccineManager()

        self.assertEqual(my_store1, my_store2)
        self.assertEqual(my_store1, my_store3)
        self.assertEqual(my_store1, my_store4)


if __name__ == '__main__':
    unittest.main()
