class Brother:
    
    number_of_brothers = 0
    dues_rate = 0
    next_id = 0

    def __init__(self, first_name:str, last_name:str, pledge_class:str, academic_year:str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pledge_class = pledge_class
        self.__academic_year = academic_year
        Brother.number_of_brothers += 0
        self.id = Brother.next_id
        Brother.next_id += 1

    #getters
    def get_first_name(self) -> str:
        return self.__first_name
    
    def get_last_name(self) -> str:
        return self.__last_name

    def get_pledge_class_name(self) -> str:
        return self.__pledge_class

    def get_academic_year(self) -> str:
        return self.__academic_year
    
    def get_dues_rate_name(self) -> str: # this can be used to set custom dues rates for certain brothers because self is used
        return self.dues_rate
    
    @classmethod
    def get_number_of_brothers(cls) -> str:
        return cls.number_of_brothers

    # setters
    def set_first_name(self, first_name:str):
        self.__first_name = first_name
    
    def set_last_name(self, last_name:str):
        self.__last_name = last_name

    def set_pledge_class(self, pledge_class:str):
        self.__pledge_class = pledge_class
    
    def set_academic_year(self, academic_year:str):
        self.__academic_year = academic_year

    #combine first and last name
    def combine_name(self) -> str:
        return '{} {}'.format(self.get_first_name(), self.get_last_name())
    
