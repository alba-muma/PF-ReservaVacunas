"""Subclass of JsonStore for managing the Patients store"""
from uc3m_care.storage.json_store import JsonStore
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH

class CancelJsonStore():
    """Clase encargada de las cancelaciones de las citas deseadas"""
    # pylint: disable=invalid-name
    class __CancelJsonStore(JsonStore):
        """Subclass of JsonStore for managing the VaccinationLog"""
        _FILE_PATH = JSON_FILES_PATH + "cancel_json.json"
        _ID_FIELD = ""

    __instance = None

    def __new__(cls):
        if not CancelJsonStore.__instance:
            CancelJsonStore.__instance = CancelJsonStore.__CancelJsonStore()
        return CancelJsonStore.__instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)
