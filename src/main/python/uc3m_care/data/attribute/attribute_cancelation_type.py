"""Class for the attribute CancelationType"""
from uc3m_care.data.attribute.attribute import Attribute

# pylint: disable=too-few-public-methods


class CancelationType(Attribute):
    """Class for the attribute CancelationType"""
    _validation_pattern = r"(Final|Temporal)"
    _validation_error_message = "Cancelation type is nor valid"
