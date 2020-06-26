latitude_coefficient = 5.4
longitude_coefficient = 6

class Location:
    latitude = ["", None]  # [direction {N, S, E, W}, value]
    longitude = ["", None]   # [direction {N, S, E, W}, value]
    tolerance = None

    def __init__(self, latitude = None, longitude = None, tolerance = None):
        if latitude:
            self.latitude = self.toDegreeDecimalMinutes(latitude, 1)
        if longitude:
            self.longitude  = self.toDegreeDecimalMinutes(longitude, 2)
        if tolerance:
            self.tolerance = tolerance 

    def getTransformedLocation(self):
        """ Main driver function.
            Gives transformed location to be used in key construction process
        """
        return [transform_location(self.latitude[0], self.latitude[1]), transform_location(self.latitude[0], self.latitude[1])]

    def getAdjacentQuadrants(self):
        return createAjacentQuadrants(transform_location(self.latitude[0], self.latitude[1]), transform_location(self.latitude[0], self.latitude[1]))

    def transformLocation(location_dir, location_value):
        location_value = location_value * 10000
        if location_dir == "N" or location_dir == "S":
            return includeLocationSign(location_dir, location_value / (self.tolerance * latitude_coefficient))
        else: 
            return includeLocationSign(location_dir, location_value / (self.tolerance * longitude_coefficient))

    def includeLocationSign(location_dir, location_value):
        return (location_dir == "N" or location_dir == "W") ? location_value : -1 * location_value


    def createAdjacentQuadrants(latitude_val, longitude_val):
        adjacentQuadrants = []  # list containing all the possible quadrants
        directions = [1, -1, 0]
        for x in directions:
            for y in directions:
                adjacentQuadrants.append([latitude_val + x, longitude_val + y])
        return adjacentQuadrants

    def toDegreeDecimalMinutes(self, location_value, location_type):
        """Convert location values
        """
        result_location = ["", 0.0]
        if location_value < 0 and location_type == 1:
            location_sign = "S"
            location_value = location_value * -1
        elif location_value < 0 and location_type == 2:
            location_sign = "W"
            location_value = location_value * -1
        elif location_value > 0 and location_type == 1:
            location_sign = "N"
        elif location_value > 0 and location_type == 2:
            location_sign = "E"
        result_location[0] = location_sign
        result_location[1] = location_value
        # TODO: convert result_location to degrees & minutes
        return result_location