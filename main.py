import requests
import json
import random


def search_attractions(city):
    url = "https://api.foursquare.com/v3/places/search"
    params = {
        "query": "tourist",
        "near": city,
        "sort": "RATING"
    }

    headers = {
        "accept": "application/json",
        "Authorization": "fsq3z52r98ErSs1N7oNfIDg/L3CtSV12F7w+lXgYg+F/nkY="
    }
    
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data['results']

def generate_travel_plan(attractions, days_staying):
    travel_plan = {}
    for day in range(1, days_staying + 1):
        daily_attractions = random.sample(attractions, k=3)  # Select 2 random attractions for each day
        travel_plan[f'Day {day}'] = daily_attractions

    return travel_plan

# Get user input for city and days staying
city = input("Enter the name of the city: ")
days_staying = int(input("Enter the number of days staying: "))

# Search attractions in the city
attractions = search_attractions(city)


# Generate the travel plan
travel_plan = generate_travel_plan(attractions, days_staying)

# Display the travel plan
print(f"\nTravel Plan for {city}:\n")
for day, attractions in travel_plan.items():
    print(f"{day}:")
    for attraction in attractions:
        print(f"- {attraction['name']}")
    print()