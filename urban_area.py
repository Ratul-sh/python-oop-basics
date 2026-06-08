class UrbanArea:
    def __init__(self, name, population, area_sq_km):
        self.name = name
        self.population = int(population)
        self.area_sq_km = float(area_sq_km)
    
    def calculate_density(self):
        density = self.population / self.area_sq_km
        return density.__round__()
    def is_megacity(self):
        if self.population > 10000000:
            return True
        else:
            return False
        
city_1 = UrbanArea("Dhaka", 22000000, 306.4)
city_2 = UrbanArea("Tokyo", 37400068, 2194)
city_3 = UrbanArea("Shanghai", 29900000, 6341)
city_4 = UrbanArea("Khulna", 718735, 59.57)
city_5 = UrbanArea("New York City", 8336817, 783.8)
city_6 = UrbanArea("London", 8982000, 1572)

print(UrbanArea.calculate_density(city_5))
print(UrbanArea.is_megacity(city_1))