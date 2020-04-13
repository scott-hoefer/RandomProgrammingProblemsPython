'''
Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km 
length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to it's nearest space station.

For example, there are n = 3 cities and m = 1 of them has a space station, city 1. They occur consecutively along a route. City 2 is 2-1 = 1 unit away and city 3 is 3 - 1 = 2 units away. City 1 is 0 units from its nearest space station as one is located there.
The maximum distance is therefore 2.

.

Function Description

It should return an integer that represents the maximum distance any city is from the nearest space station.

flatlandSpaceStations has the following parameter(s):

    n: the number of cities
    c: an integer array that contains the indices of cities with a space station, 

    1-based indexing
    There will be at least 1 city with a space station.
    No city has more than one space station.

Output Format

Print an integer denoting the maximum distance that an astronaut in a Flatland city would need to travel to reach the nearest space station.

Sample Input 0

n = 5
c = [0,  4]

c0(S) <--> c1 <--> c2 <--> c3 <--> c4(S)
Sample Output 0

2

'''
# This has a runtime of O(nlogn) due to the sorting, not sure if its optimal
def flatlandSpaceStations(num_of_cities, stations):
    num_of_stations = len(stations)
    stations_sorted = sorted(stations)
    # stations_sorted[0] will give you the distance from the first city to the first space station
    # distance from last city to last space station is number of cities - (last space station index + 1) (I add one since its 0 based indexing)
    maxDistance = max(stations_sorted[0], num_of_cities - (stations_sorted[-1] + 1))

    for i in range(1, num_of_stations):
        # d is the distance between 2 space stations
        d = stations_sorted[i] - stations_sorted[i-1]
        # taking the floor of the distance between the 2 stations will give you the distance to the nearest space station
        maxDistance = max(d//2, maxDistance)

    return maxDistance

if __name__ == '__main__':
    n = 99992
    c = [90467, 18058, 99109, 48463]
    space_answer = flatlandSpaceStations(n, c)
    print('The answer to space stations is {} for n={}, c={}'.format(space_answer, str(n), str(c)))