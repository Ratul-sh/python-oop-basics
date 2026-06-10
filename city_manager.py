class City:
    city_database = {}
    def __init__(self, name, country, facilities = None, demographics = None):
        self.name = name
        self.country = country
        if facilities is None:
            self.facilities = []
        else:
            self.facilities = facilities
        if demographics is None:
            self.demographics = {}
        else:
            self.demographics = demographics
        City.city_database[self.name.lower()] = self  
    def add_facility(self, facility_name):
        self.facilities.append(facility_name)
    def add_demographic(self, group_name, population):
        group_name = group_name.capitalize()
        self.demographics[group_name] = population 
    def city_summary(self):
        return f"City Name: {self.name}\n\nFacilities: {self.facilities}\n\nDemographics: {self.demographics}"
    @classmethod
    def del_database_element(cls, city_name):
        del cls.city_database[city_name]
    @classmethod
    def add_city(cls, name, country):
        cls(name, country)

        
while True:
    available_Cities = list(City.city_database.keys())
    print("Wwelcome To The System.\nThese Are The Current City.\n\n", available_Cities)
    x = int(input("What Do You Want to Do?\n\n1. Add A City?\n2. Add Facility\n3. Add Demographic\n4. View Summary\n5. Delete a City\n6. Exit\n\n"))
    if x == 1:
        a = str(input("Enter The City Name: ")).lower()
        b = str(input("Enter The Country Name: "))
        City.add_city(a, b)
        print("congratulations. Your City Has Beeen added")
        # print(City.city_summery(City.city_database[a]))
        print(City.city_database[a].city_summery())
    elif x == 2:
        select_city_for_facility = str(input('Enter The City Name: ')).lower()
        select_facility = str(input("Enter The Facility You Want to input: ")).capitalize()
        # City.add_facility(City.city_database[select_city], select_facility)
        if select_city_for_facility in City.city_database:
            City.city_database[select_city_for_facility].add_facility(select_facility)
        else:
            print("The City You Entered Is Currently Unavailabe. Or U Might Have Entered The Wrong Spelling.")
            print(f"Available Cities:\n{available_Cities}")
    elif x == 3:
        select_city_for_demographics = str(input('Enter The City Name: ')).lower()
        select_group_name = str(input("Enter The Group Name: ")).capitalize()
        select_population = int(input("Enter The Population Number: "))
        if select_city_for_demographics in City.city_database:
            City.city_database[select_city_for_demographics].add_demographic(select_group_name, select_population)
        else:
            print("The City You Entered Is Currently Unavailabe. Or U Might Have Entered The Wrong Spelling.")
            print(f"Available Cities:\n{available_Cities}")
    elif x == 4:
        select_city_for_summary = str(input('Enter The City Name: ')).lower() 
        if select_city_for_summary in City.city_database:
            print(City.city_database[select_city_for_summary].city_summary())
        else:
            print("The City You Entered Is Currently Unavailabe. Or U Might Have Entered The Wrong Spelling.")
            print(f"Available Cities:\n{available_Cities}")
    elif x == 5:
        select_city_for_delete = str(input('Enter The City Name: ')).lower()
        if select_city_for_delete in City.city_database:
            City.del_database_element(select_city_for_delete)
        else:
            print("The City You Entered Is Currently Unavailabe. Or U Might Have Entered The Wrong Spelling.")
            print(f"Available Cities:\n{available_Cities}")
    elif x == 6:
        break
    else:
        print('You Gave Wrong input. Choose from the Number 1 - 6')


# --- TESTING AREA ---

City("Khulna", "Bangladesh")
# # print(khulna.name)           # Expected output: Khulna
# # print(khulna.facilities)     # Expected output: []

# khulna = City("Khulna", "Bangladesh")
# khulna.add_facility("Hospital")
# khulna.add_facility("Park")
# # print(khulna.facilities)

# khulna.add_demographic("Male", 50000)
# # print(khulna.demographics)   # Expected output: {'Male': 50000}

# # print(City.city_summery(khulna))
