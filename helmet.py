from .const import HelmetType

NUM_OF_HELMETS = 5


def choose_helmet_type(type_name: str):
    return HelmetType(type_name)
