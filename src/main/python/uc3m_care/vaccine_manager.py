"""Module """

from uc3m_care.data.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.data.vaccination_appointment import VaccinationAppointment
from uc3m_care.data.vaccination_cancel import VaccinationCancel


class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""

    # pylint: disable=invalid-name
    class __VaccineManager:
        def __init__(self):
            pass

        # pylint: disable=too-many-arguments
        # pylint: disable=no-self-use
        def request_vaccination_id(self, patient_id,
                                    name_surname,
                                    registration_type,
                                    phone_number,
                                    age):
            """Register the patient into the patients file"""
            my_patient = VaccinePatientRegister(patient_id,
                                                    name_surname,
                                                    registration_type,
                                                    phone_number,
                                                    age)

            my_patient.save_patient()
            return my_patient.patient_sys_id

        def get_vaccine_date(self, input_file, date):
            """Gets an appointment for a registered patient"""
            my_sign = VaccinationAppointment.create_appointment_from_json_file(input_file, date)
            # save the date in store_date.json
            my_sign.save_appointment()
            return my_sign.date_signature

        def vaccine_patient(self, date_signature):
            """Register the vaccination of the patient"""
            appointment = VaccinationAppointment.get_appointment_from_date_signature(date_signature)
            return appointment.register_vaccination()

        def cancel_appointment(self, input_file):
            """Este metodo anula una cita predefinida"""
            my_cancel = VaccinationCancel.create_cancel(input_file)
            my_cancel.update_appointment(my_cancel)
            return my_cancel.date_signature

    __instance = None

    def __new__(cls):
        if not VaccineManager.__instance:
            VaccineManager.__instance = VaccineManager.__VaccineManager()
        return VaccineManager.__instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)
