# Trip-Planner
This Python script utilizes the Foursquare API to create a travel plan for a given city and duration of stay. It searches for tourist attractions in the specified city and then generates a random travel plan for the specified number of days.

# How It Works:

1. The script starts by importing the necessary modules: requests, json, and random.

2. The search_attractions(city) function sends a request to the Foursquare API to search for tourist attractions in the given city. It uses the "tourist" query and sorts the results by rating.

3. The generate_travel_plan(attractions, days_staying) function creates a travel plan by randomly selecting 3 attractions for each day of the specified duration.

4. The script gets user input for the city and the number of days staying using the input() function.

5. It then calls the search_attractions(city) function to get a list of attractions in the city.

6. Using the generate_travel_plan() function, it generates a travel plan with randomly selected attractions for each day.

7. The script displays the generated travel plan in a readable format using print() statements.
