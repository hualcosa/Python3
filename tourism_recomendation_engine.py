# Return the index of a certain destination
def get_destination_index(destination):
  return destinations.index(destination);

# Return the index of traveler location in the destinations list
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# Adds an attraction to the list of attractions
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
  except ValueError:
    print("This destination is not among the list of destinations")
    return

# 
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_the_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_the_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
    
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for attraction in traveler_attractions:
    if attraction is traveler_attractions[-1]:
      interests_string += attraction + "."
    else:
    	interests_string += attraction + ", "
  return interests_string

# Create the list of destinantions we're going to be using
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. Erin is in China right now, hopefully we can find some good places to show her. 
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Create a list of attractions
attractions = [[] for dest in destinations]

# test calls
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_traveler_location(test_traveler))
#print(attractions)

# Addding a few interesting places to go...
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Testing find_attractions function
la_arts = find_attractions("Los Angeles, USA", ["art"])
#print(la_arts)

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
wilkes_china = get_attractions_for_traveler(test_traveler)
print(smills_france)
print(wilkes_china)



