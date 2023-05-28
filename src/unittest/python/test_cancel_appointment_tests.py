"""Tests for cancel_appointment method"""
from unittest import TestCase
from freezegun import freeze_time
from uc3m_care import VaccineManager
from uc3m_care import JSON_FILES_RF2_PATH, JSON_FILES_FP_PATH
from uc3m_care import AppointmentsJsonStore
from uc3m_care import PatientsJsonStore
from uc3m_care import VaccinationJsonStore
from uc3m_care import CancelJsonStore
from uc3m_care import VaccineManagementException

param_not_ok = [("test2_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test3_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test4_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test5_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test6_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test7_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test8_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test9_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test10_not_ok.json", "Bad label cancelation_type"),
                ("test11_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test12_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test13_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test14_not_ok.json", "Bad label reason"),
                ("test15_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test16_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test17_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test18_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test19_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test20_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test21_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test22_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test23_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test24_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test25_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test26_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test27_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test28_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test29_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test30_not_ok.json", 'JSON Decode Error - Wrong JSON Format'),
                ("test31_not_ok.json", 'JSON Decode Error - Wrong JSON Format'),
                ("test32_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test33_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test34_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test35_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test36_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test37_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test38_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test39_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test40_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test41_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test42_not_ok.json", "Bad label date_signature"),
                ("test43_not_ok.json", "Bad label date_signature"),
                ("test44_not_ok.json", "Bad label date_signature"),
                ("test45_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test46_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test47_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test48_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test49_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test50_not_ok.json", "date_signature format is not valid"),
                ("test51_not_ok.json", "date_signature format is not valid"),
                ("test52_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test53_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test54_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test55_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test56_not_ok.json", "Bad label cancelation_type"),
                ("test57_not_ok.json", "Bad label cancelation_type"),
                ("test58_not_ok.json", "Bad label cancelation_type"),
                ("test59_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test60_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test61_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test62_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test63_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test64_not_ok.json", "Cancelation type is nor valid"),
                ("test65_not_ok.json", "Cancelation type is nor valid"),
                ("test66_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test67_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test68_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test69_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test70_not_ok.json", "Bad label reason"),
                ("test71_not_ok.json", "Bad label reason"),
                ("test72_not_ok.json", "Bad label reason"),
                ("test73_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test74_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test75_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test76_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test77_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test78_not_ok.json", "reason is nor valid"),
                ("test79_not_ok.json", "reason is nor valid"),
                ("test80_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test81_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test82_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test83_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test84_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test85_not_ok.json", "date_signature format is not valid"),
                ("test86_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test87_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test88_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test89_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test90_not_ok.json", "Cancelation type is nor valid"),
                ("test91_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test92_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test93_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test94_not_ok.json", "JSON Decode Error - Wrong JSON Format"),
                ("test95_not_ok.json", "reason is nor valid"),
                ("test96_not_ok.json", "JSON Decode Error - Wrong JSON Format")]

class CancelAppointmentTests(TestCase):
    """Class for testing get_vaccine_date"""

    @freeze_time("2022-03-08")
    def test_cancel_appointment_no_ok_parameter2(self):
        """tests no ok"""
        my_manager = VaccineManager()
        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()
        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_date = "2022-03-18"
        my_manager.get_vaccine_date(file_test, my_date)
        for file_name, expected_value in param_not_ok:
            with self.subTest(test=file_name):
                hash_original = file_store_cancel.data_hash()
                cancel_test = JSON_FILES_FP_PATH + file_name
                # check the method
                with self.assertRaises(VaccineManagementException) as c_m:
                    my_manager.cancel_appointment(cancel_test)
                self.assertEqual(c_m.exception.message, expected_value)

                # read the file again to compare
                hash_new = file_store_cancel.data_hash()

                self.assertEqual(hash_new, hash_original)

    @freeze_time("2022-03-08")
    def test2_not_ok(self):
        """test not ok"""
        cancel_test = JSON_FILES_FP_PATH + "test1_2_not_ok.json"
        my_manager = VaccineManager()

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        hash_original = file_store_cancel.data_hash()
        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test)
        hash_new = file_store_cancel.data_hash()
        self.assertEqual(c_m.exception.message, "Error: La cita no existe")
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2022-03-08")
    def test3_not_ok(self):
        """test not ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancel_test = JSON_FILES_FP_PATH + "test1_3_not_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-10"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        my_manager.cancel_appointment(cancel_test)
        hash_original = file_store_cancel.data_hash()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test)
        hash_new = file_store_cancel.data_hash()
        self.assertEqual(c_m.exception.message, "La cita ya ha sido cancelada anteriormente")
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2022-03-08")
    def test4_0_setup(self):
        """test para añadir un paciente y crear una cita"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-10"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)

    @freeze_time("2022-04-08")
    def test4_1_not_ok(self):
        """test not ok"""
        cancel_test = JSON_FILES_FP_PATH + "test1_3_not_ok.json"
        my_manager = VaccineManager()

        # first , prepare my test , remove store patient
        file_store_date = AppointmentsJsonStore()
        file_store_cancel = CancelJsonStore()

        hash_original = file_store_cancel.data_hash()
        hash_original_appointment = file_store_date.data_hash()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test)

        hash_new = file_store_cancel.data_hash()
        hash_new_appointment = file_store_date.data_hash()
        self.assertEqual(c_m.exception.message, "Error: La fecha de la cita ya ha pasado")
        self.assertEqual(hash_new, hash_original)
        self.assertEqual(hash_new_appointment, hash_original_appointment)

    @freeze_time("2022-03-10")
    def test4_2_0_setup(self):
        """test necesario para el proceso de cancelacion"""
        my_manager = VaccineManager()
        value = "9afeeb8121b9cd285347b319836c238c268f84c7979c61984e2c001550a07522"
        my_manager.vaccine_patient(value)

    @freeze_time("2022-03-08")
    def test4_2_1_not_ok(self):
        """test que evalua si un paciente ha sido vacunado o no para poder cancelar la cita"""
        cancel_test = JSON_FILES_FP_PATH + "test1_2_not_ok.json"
        my_manager = VaccineManager()
        # check store_date
        file_store_cancel = CancelJsonStore()
        hash_original = file_store_cancel.data_hash()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test)
        hash_new = file_store_cancel.data_hash()
        self.assertEqual(c_m.exception.message, "Error: El paciente ya ha sido vacunado")
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2022-03-08")
    def test5_ok(self):
        """test ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancel_test = JSON_FILES_FP_PATH + "test1_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        #first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular","+34123456789","6")
        #check the method
        my_manager.get_vaccine_date(file_test , my_date)
        #check store_date
        value = my_manager.cancel_appointment(cancel_test)
        appointment = file_store_date.find_item(value)
        self.assertEqual("Temporal", appointment["_VaccinationAppointment__isCancel"])
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-03-08")
    def test6_ok(self):
        """test ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancel_test = JSON_FILES_FP_PATH + "test1_1_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        value = my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        value = my_manager.cancel_appointment(cancel_test)
        appointment = file_store_date.find_item(value)
        self.assertEqual("Final", appointment["_VaccinationAppointment__isCancel"])
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-04-08")
    def test7_not_ok_vl_reason(self):
        """test not ok valores limite del string de reason"""
        file_test = JSON_FILES_RF2_PATH + "test_new_3.json"
        # Cancelacion con un string en reason que posee 1 caracter
        cancel_test = JSON_FILES_FP_PATH + "test1_4_not_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-04-09"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        hash_original = file_store_cancel.data_hash()
        my_manager.get_vaccine_date(file_test, my_date)
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test)
        hash_new = file_store_cancel.data_hash()
        self.assertEqual(c_m.exception.message, "reason is nor valid")
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2022-04-08")
    def test8_not_ok_vl_reason(self):
        """test not ok valores limite del string de reason"""
        file_test = JSON_FILES_RF2_PATH + "test_new_3.json"
        # Json que contiene un string en reason formado por 101 caracteres
        # (superior al limite establecido)
        cancel_test = JSON_FILES_FP_PATH + "test1_5_not_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-04-11"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        hash_original = file_store_cancel.data_hash()
        my_manager.get_vaccine_date(file_test, my_date)
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test)
        hash_new = file_store_cancel.data_hash()
        self.assertEqual(c_m.exception.message, "reason is nor valid")
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2022-03-08")
    def test9_ok_vl_reason(self):
        """test ok valores limite del string de reason"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        # El string de reason introducido posee 3 caracteres
        cancel_test = JSON_FILES_FP_PATH + "test1_5_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        value = my_manager.cancel_appointment(cancel_test)
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-03-08")
    def test10_ok_vl_reason(self):
        """test ok valores limite del string de reason"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        # El string de reason introducido posee 2 caracteres (limite inferior)
        cancel_test = JSON_FILES_FP_PATH + "test1_2_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        value = my_manager.cancel_appointment(cancel_test)
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-03-08")
    def test11_ok_vl_reason(self):
        """test ok valores limite del string de reason"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        # El string de reason introducido posee 100 caracteres (limite superior)
        cancel_test = JSON_FILES_FP_PATH + "test1_3_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        value = my_manager.cancel_appointment(cancel_test)
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-03-08")
    def test12_ok_vl_reason(self):
        """test ok valores limite del string de reason"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        # El string de reason introducido posee 99 caracteres
        cancel_test = JSON_FILES_FP_PATH + "test1_4_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        value = my_manager.cancel_appointment(cancel_test)
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-03-08")
    def test13_ok(self):
        """test ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancel_test = JSON_FILES_FP_PATH + "test1_ok.json"
        cancel_test2 = JSON_FILES_FP_PATH + "test1_3_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-18"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        value = my_manager.cancel_appointment(cancel_test)
        appointment = file_store_date.find_item(value)
        value = my_manager.cancel_appointment(cancel_test2)
        appointment = file_store_date.find_item(value)
        self.assertEqual("Final", appointment["_VaccinationAppointment__isCancel"])
        self.assertEqual(value, "62ca69e8aad4b24d8588117e58b3524ffe18dac510306a9f2c3aeb5039f3afa6")

    @freeze_time("2022-03-08")
    def test14_not_ok(self):
        """test not ok"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        cancel_test = JSON_FILES_FP_PATH + "test14_1_not_ok.json"
        cancel_test2 = JSON_FILES_FP_PATH + "test14_2_not_ok.json"
        my_manager = VaccineManager()
        my_date = "2022-03-10"

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        file_store_cancel = CancelJsonStore()
        file_store_cancel.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        my_manager.get_vaccine_date(file_test, my_date)
        # check store_date
        my_manager.cancel_appointment(cancel_test)
        hash_original = file_store_cancel.data_hash()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.cancel_appointment(cancel_test2)
        hash_new = file_store_cancel.data_hash()
        self.assertEqual(c_m.exception.message, "La cita ya ha sido cancelada anteriormente")
        self.assertEqual(hash_new, hash_original)
