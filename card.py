class Card:

    def __init__(self, type, value):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type.upper()

    def get_value(self):
        return self.__value.upper()