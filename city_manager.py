class city:
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
