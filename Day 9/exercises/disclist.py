# Travel Log (Dictionary in List) : Day 9 Exercise 2

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, visited, city):
    travel_log.append({
        "country" : country_name,
        "visits" : visited,
        "cities" : city,
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(f"{travel_log} \n")
