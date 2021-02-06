#
#   Imagine you have a set of cities that are laid out in a circle, connected by a
#   circular road that runs clockwise. Each city has a gas station that provides
#   gallons of fuel, and each city is some distance away from the next city.
#
#   You have a car that can drive some number of miles per gallon of fuel, and
#   your goal is to pick a starting city such that you can fill up your car with
#   that city's fuel, drive to the next city, refill up your car with that city's
#   fuel, drive to the next city, and so on and so forth until you return back to
#   the starting city with 0 or more gallons of fuel left.
#
#   This city is called a valid starting city, and it's guaranteed that there will
#   always be exactly one valid starting city.
#
#   For the actual problem, you'll be given an array of distances such that city
#   <span>i</span> is <span>distances[i]</span> away from city <span>i + 1</span>.
#   Since the cities are connected via a circular road, the last city is connected
#   to the first city. In other words, the last distance in the
#   <span>distances</span> array is equal to the distance from the last city to
#   the first city. You'll also be given an array of fuel available at each city,
#   where <span>fuel[i]</span> is equal to the fuel available at city
#   <span>i</span>. The total amount of fuel available (from all cities combined)
#   is exactly enough to travel to all cities. Your fuel tank always starts out
#   empty, and you're given a positive integer value for the number of miles that
#   your car can travel per gallon of fuel (miles per gallon, or MPG). You can
#   assume that you will always be given at least two cities.
#   Write a function that returns the index of the valid starting city

def validStartingCity(distances, fuel, mpg):
    milesAvailable = 0
    numberOfCities = len(distances)
    indexOfCityCandidate = 0
    milesRemainingAtCityCandidate = 0

    for cityIndex in range(1, numberOfCities):
        # example: distance from city 2 to city 1 is 5 in array given
        distanceFromPrevCity = distances[cityIndex - 1]
        fuelFromPrevCity = fuel[cityIndex - 1]
        milesAvailable += ((fuelFromPrevCity * mpg) - distanceFromPrevCity)

        if milesAvailable < milesRemainingAtCityCandidate:
            milesRemainingAtCityCandidate = milesAvailable
            indexOfCityCandidate = cityIndex
    return indexOfCityCandidate
