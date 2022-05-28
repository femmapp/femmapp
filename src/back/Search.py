import pandas as pd
import pyproj
import numpy as np
from geopy.distance import geodesic
from ast import literal_eval
import Levenshtein

PLACES= pd.read_csv('../data/places.tsv', delimiter='\t')

def get_distance_matches(coordinates1,places_coordinates, max_dist):
  #inspiration from https://gis.stackexchange.com/questions/260992/how-do-i-convert-wgs84-lat-long-points-from-degrees-to-meters-in-python
  distance_matches = []
  for place_id, lat, long in places_coordinates:
    coordinates2 = (lat, long)
    distance = geodesic(coordinates1, coordinates2).meters
    if distance < max_dist:
      distance_matches.append(place_id)
  return (distance_matches)

def get_category_matches(categories, distance_matches):
  category_matches = []
  for category in categories:
    for index in distance_matches:
      if PLACES.loc[index].Categories[category][0] != 0:
        category_matches.append(PLACES.loc[index].to_dict())
  #category_matches = [PLACES.loc[index].to_dict() for index in distance_matches if literal_eval(PLACES.loc[index].Categories_Id) & categories]
  #Returns a list of dictionaries
  return(category_matches)
  
def return_match_spots(lat, long, categories, max_dist):
  places_coordinates = list(zip(PLACES["Id"], PLACES["Latitude"], PLACES["Longitude"]))
  distance_matches = get_distance_matches((lat, long), places_coordinates, max_dist)
  category_matches = get_category_matches(categories, distance_matches)
  return(str(category_matches))
  
def query(query_term, categories, max_dist=500):
  if isinstance(query_term, str): #We assume the query term is a name
    query_term = query_term.replace("_"," ")    
    if query_term in PLACES["Name"].values:
      lat = PLACES.set_index("Name").loc[query_term].Latitude
      long = PLACES.set_index("Name").loc[query_term].Longitude
      category_matches = return_match_spots(lat, long, categories, max_dist)
    else:
      category_matches = "This query didn't return any result!"
      for place in PLACES["Name"].values:
        med = Levenshtein.distance(query_term, place)
        if med < 6:
          lat = PLACES.set_index("Name").loc[place].Latitude
          long = PLACES.set_index("Name").loc[place].Longitude
          category_matches = return_match_spots(lat, long, categories, max_dist)
  elif isinstance(query_term, tuple): #We assume those are the latitude and longitude
    lat, long = query_term
    category_matches = return_match_spots(lat, long, categories, max_dist)
  else:
    category_matches = "Please, entry a valid query!"
  return(category_matches)

def main():
  query((41.43050169245379, 2.18336528460343), {0}, 500) #return 0,2
  query((41.43050169245379, 2.18336528460343), {1}, 500) # return 1
  query((41.43050169245379, 2.18336528460343), {2}, 500) # return 0
  query("Jardí de la Julieta",{1}, 200)
  query("Jardi de la Julieta",{2}, 500)
  query("caca",{0}, 500)
  
main()

#http://127.0.0.1:5000/search?lat=41.43050169245379&long=2.18336528460343&dist=500&categories=0