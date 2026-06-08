class City:
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
    def add_facility(self, facility_name):
        self.facilities.append(facility_name)
    def add_demographic(self, group_name, population):
        self.demographics[group_name] = population 
    def city_summery(self):
        return f"City Name: {self.name}\n\nFacilities: {self.facilities}\n\nDemographics: {self.demographics}"
        
