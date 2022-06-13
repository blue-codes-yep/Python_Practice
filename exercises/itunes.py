import json  # Can import json to make json more readiable.
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()


response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=3&term=" + sys.argv[1])

# Print out the contents of the search

print(json.dumps(response.json(), indent=2))


# Grabs the track name from the results key in search api for itunes.

o = response.json()

for result in o["results"]:
    print(result["trackName"])
