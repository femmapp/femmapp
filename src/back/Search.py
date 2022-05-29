import pandas as pd
import pyproj
import numpy as np
from geopy.distance import geodesic
from ast import literal_eval

PLACES= pd.read_csv('src/data/places.tsv', delimiter='\t')

def get_distance_matches(coordinates1,places_coordinates, max_dist):
  #inspiration from https://gis.stackexchange.com/questions/260992/how-do-i-convert-wgs84-lat-long-points-from-degrees-to-meters-in-python
  distance_matches = []
  for place_id, lat, long in places_coordinates:
    coordinates2 = (lat, long)
    distance = geodesic(coordinates1, coordinates2).meters
    if distance < max_dist:
      distance_matches.append(place_id)
  return (distance_matches)
  
def return_match_spots(lat, long, categories, max_dist):
  places_coordinates = list(zip(PLACES["Id"], PLACES["Latitude"], PLACES["Longitude"]))
  distance_matches = get_distance_matches((lat, long), places_coordinates, max_dist)
  category_matches = [index for index in distance_matches if literal_eval(PLACES.loc[index].Categories_Id) & set(categories)]
  print(category_matches)
  
def query(query_term, categories, max_dist=500):
  if isinstance(query_term, str): #We assume the query term is a name
    # TODO: Include levenstein distance
    lat = PLACES.set_index("Name").loc[query_term].Latitude
    long = PLACES.set_index("Name").loc[query_term].Longitude
    return_match_spots(lat, long, categories, max_dist)
  elif isinstance(query_term, tuple): #We assume those are the latitude and longitude
    lat, long = query_term
    return_match_spots(lat, long, categories, max_dist)
  else:
    print("This query didn't return any result!")

def main():
  query((41.43050169245379, 2.18336528460343), {0}, 500) #return 0,2
  query((41.43050169245379, 2.18336528460343), {1}, 500) # return 1
  query((41.43050169245379, 2.18336528460343), {2}, 500) # return 0
  query("Jardí de la Julieta",{1}, 200)

main()