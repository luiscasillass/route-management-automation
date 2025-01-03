# this program contains confidential information belonging to JARO Freight. Any unauthorized alteration, 
# misuse, or distribution of this data will result in penalties
import requests
import pandas as pd


BASE_URL = 'https://BASE_URL'
COLLECTION = 'routes'
API_TOKEN = 'API_KEY'


def route_exists(origin, destination):
    filter_query = f"origin='{origin}' && destination='{destination}'"
    response = requests.get(
        f"{BASE_URL}/collections/{COLLECTION}/records",
        headers={
            'Authorization': f'Bearer {API_TOKEN}'
        },
        params={
            'filter': filter_query
        }
    )
    data = response.json()
    return data['totalItems'] > 0  

# function to create route
def create_route(route):
    response = requests.post(
        f"{BASE_URL}/collections/{COLLECTION}/records",
        headers={
            'Authorization': f'Bearer {API_TOKEN}',
            'Content-Type': 'application/json'
        },
        json=route
    )
    return response.json()


csv_file = 'routes.csv'  
df = pd.read_csv(csv_file)


for index, row in df.iterrows():
    origin = row['origin']
    destination = row['destination']
    distance_km = row['distance_km']
    origin_lat = row['origin_lat']
    origin_lon = row['origin_lon']
    destination_lat = row['destination_lat']
    destination_lon = row['destination_lon']
    
    if not route_exists(origin, destination):
        route = {
            "origin": origin,
            "destination": destination,
            "distance_km": distance_km,
            "origin_lat": origin_lat,
            "origin_lon": origin_lon,
            "destination_lat": destination_lat,
            "destination_lon": destination_lon
        }
        result = create_route(route)
        print(f"Ruta creada: {result}")
    else:
        print(f"Ruta ya existe: {origin} -> {destination}")

print("Proceso completado.")
