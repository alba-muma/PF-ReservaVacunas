"""Class for the attribute Date appointment"""
from datetime import datetime
import re
from uc3m_care.data.attribute.attribute import Attribute
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
# pylint: disable=too-few-public-methods


class DateAppointment(Attribute):
    """Class for the attribute PatientId"""
    _validation_error_message = "La fecha no es valida"
    _validation_pattern = r"[0-9]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$"
    _validation_error_message2 = "El formato de la fecha no es valido"

    def _validate(self, attr_value):
        """overrides the validate method to include the validation of  UUID values"""
        registration_type_pattern = re.compile(self._validation_pattern)
        res = registration_type_pattern.fullmatch(attr_value)
        if not res:
            raise VaccineManagementException(self._validation_error_message2)
        justnow = datetime.utcnow()
        today = datetime.timestamp(justnow)
        date_float = datetime.strptime(attr_value, "%Y-%m-%d")
        date_float = datetime.timestamp(date_float)
        if date_float <= today:
            raise VaccineManagementException(self._validation_error_message)
        return str(attr_value)
