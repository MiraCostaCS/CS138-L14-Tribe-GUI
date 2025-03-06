"""
TribeRecord
--------------------------------
- tribe_name : string
- history : string
- location : string
- population : int
- date_of_colonization : string
- active : boolean
- current_location : string
- current_population : int
--------------------------------
__init__(name, history, location, population, date_of_colonization, active)
set
__str__()
set_tribe_name(tribe_name)
set_history(history)
set_location(location)
set_population(population)
set_date_of_colonization(date_of_colonization)
set_active(active)
set_current_location(current_location)
set_current_population(current_population)
get_tribe_name()
get_history()
get_location()
get_population()
get_date_of_colonization()
get_active()
get_current_location()
get_current_population()
"""


class TribeRecord:

    def __init__(
        self,
        name,
        history,
        location,
        population,
        date_of_colonization,
        active,
        current_location,
        current_population,
    ):
        self.__tribe_name = name
        self.__history = history
        self.__location = location
        self.__population = population
        self.__date_of_colonization = date_of_colonization
        self.__active = active
        self.__current_location = current_location
        self.__current_population = current_population

    def __str__(self):
        all = f"Tribe Name: {self.__tribe_name}, "
        all += f"History: {self.__history}, "
        all += f"Location: {self.__location}, "
        all += f"Population: {self.__population}, "
        all += f"Date of Colonization:{self.__date_of_colonization}, "
        all += f"Active: {self.__active}, "
        all += f"Current Location: {self.__current_location}, "
        all += f"Current Population: {self.__current_population}"
        return all


# Remaining methods are missing
