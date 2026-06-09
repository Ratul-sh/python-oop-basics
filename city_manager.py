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
        City.city_database[self.name] = self
    def add_facility(self, facility_name):
        self.facilities.append(facility_name)
    def add_demographic(self, group_name, population):
        self.demographics[group_name] = population 
    def city_summery(self):
        return f"City Name: {self.name}\n\nFacilities: {self.facilities}\n\nDemographics: {self.demographics}"

        
while True:
    x = int(input("What Do You Want to Do?\n\n1. Add Facility\n2. Add Demographic\n3. View Summery\n4. Exit\n\n"))
    if x == 1:
        print("Here are the Cities. Please Select One from the Beloww\n")
        for i in range(len(City.city_database)):
            print(i)
        city_name
        a = list(input("Enter The Facility Name: "))
        City.add_facility(a)
    elif x == 2:
        City.add_demographic()
    elif x == 3:
        City.city_summery()
    elif x == 4:
        break
    else:
        print('You Gave Wrong input. Choose from the Number 1 - 4')


# --- TESTING AREA ---

khulna = City("Khulna", "Bangladesh")
# print(khulna.name)           # Expected output: Khulna
# print(khulna.facilities)     # Expected output: []

khulna = City("Khulna", "Bangladesh")
khulna.add_facility("Hospital")
khulna.add_facility("Park")
# print(khulna.facilities)

khulna.add_demographic("Male", 50000)
# print(khulna.demographics)   # Expected output: {'Male': 50000}

# print(City.city_summery(khulna))
