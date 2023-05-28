"""Contains the class Vaccination Appointment"""
from datetime import datetime
from uc3m_care.data.attribute.attribute_cancelation_type import CancelationType
from uc3m_care.data.attribute.attribute_reason import Reason
from uc3m_care.data.attribute.attribute_date_signature import DateSignature
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.storage.appointments_json_store import AppointmentsJsonStore
from uc3m_care.parser.cancel_json_parser import CancelJsonParser
from uc3m_care.storage.vaccination_json_store import VaccinationJsonStore
from uc3m_care.storage.cancel_json_store import CancelJsonStore

#pylint: disable=too-many-instance-attributes
class VaccinationCancel():
    """Class representing an appointment  for the vaccination of a patient"""

    def __init__(self, date_signature , cancelation_type , reason ):
        self.__cancelation_type = CancelationType(cancelation_type).value
        self.__reason = Reason(reason).value
        self.__date_signature = DateSignature(date_signature).value

    @classmethod
    def create_cancel(cls, input_file):
        """Metodo encargado de crear una cancelacion para una cita predefinida"""
        my_cancel = CancelJsonParser(input_file)
        date_signature = my_cancel.json_content[my_cancel.DATE_SIGNATURE_KEY]
        json_appointment = VaccinationJsonStore()
        vacunados = json_appointment.find_item(date_signature)
        if vacunados is not None:
            raise VaccineManagementException("Error: El paciente ya ha sido vacunado")
        new_cancel = cls(
            my_cancel.json_content[my_cancel.DATE_SIGNATURE_KEY],
            my_cancel.json_content[my_cancel.CANCELATION_TYPE_KEY],
            my_cancel.json_content[my_cancel.REASON_KEY])

        return new_cancel

    def update_appointment(self, cancel):
        """Metodo encargado de actualizar el contenido de la cita en caso de ser necesario"""
        my_store = AppointmentsJsonStore()
        my_date = self.validate_appointment(my_store)
        if cancel.cancelation_type == "Final":
            my_store_cancel = CancelJsonStore()
            my_store_cancel.add_item(cancel)
        my_store.modificar_item(my_date, cancel.cancelation_type)

    def validate_appointment(self, my_store):
        """Metodo encargado de validar la cita"""
        my_date = my_store.find_item(self.__date_signature)
        if my_date is None:
            raise VaccineManagementException("Error: La cita no existe")
        if my_date["_VaccinationAppointment__isCancel"] == "Final":
            raise VaccineManagementException("La cita ya ha sido cancelada anteriormente")
        appointment_date = my_date["_VaccinationAppointment__appointment_date"]
        justnow = datetime.utcnow()
        today = datetime.timestamp(justnow)
        date_float = datetime.strptime(appointment_date, "%Y-%m-%d")
        date_float = datetime.timestamp(date_float)
        if date_float <= today:
            raise VaccineManagementException("Error: La fecha de la cita ya ha pasado")
        return my_date

    @property
    def date_signature(self):
        """devuelve el attr date_signature"""
        return self.__date_signature

    @date_signature.setter
    def date_signature(self, value):
        """setter correspondiente al attr date_signature"""
        self.__date_signature = DateSignature(value).value

    @property
    def cancelation_type(self):
        """devuelve el attr cancelation_type"""
        return self.__cancelation_type

    @cancelation_type.setter
    def cancelation_type(self, value):
        """setter correspondiente al attr cancelation_type"""
        self.__cancelation_type = CancelationType(value).value

    @property
    def reason(self):
        """devuelve el attr reason"""
        return self.__reason

    @reason.setter
    def reason(self, value):
        """setter correspondiente al attr reason"""
        self.__reason = Reason(value).value
