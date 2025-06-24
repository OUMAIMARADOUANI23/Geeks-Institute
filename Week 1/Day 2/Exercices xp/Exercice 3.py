brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

print("Zara's clients are: ",brand['type_of_clothes'])

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")

print("Last international competitor:", brand["international_competitors"][-1])

print("Major colors in the US:", brand["major_color"]["US"])

print("Number of keys in brand dictionary:", len(brand))
print(brand)

print("All keys in brand dictionary:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1999,
    "number_stores": 10000 }

brand.update(more_on_zara)
print("Updated brand dictionary:" ,brand)
for key, value in brand.items():
   print(key, ":", value)
