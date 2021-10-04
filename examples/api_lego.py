#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import json
import brickse

# Before you can start this example be sure to fill in following variable with
# your specific value:

API_KEY = "your_key"

# set default token for the whole module
brickse.init(API_KEY)

print("Get sets:")
response = brickse.lego.get_sets(year=2012, theme="The Hobbit")
print(json.loads(response.read()))
print()

print("Get set:")
response = brickse.lego.get_set(set_number=79003)
print(json.loads(response.read()))
print()

print("Get set images:")
response = brickse.lego.get_set_images(9752)
print(json.loads(response.read()))
print()

print("Get set instructions:")
response = brickse.lego.get_set_instructions(9752)
print(json.loads(response.read()))
print()

print("Get set reviews:")
response = brickse.lego.get_set_reviews(9752)
print(json.loads(response.read()))
print()

print("Get themes:")
response = brickse.lego.get_themes()
print(json.loads(response.read()))
print()

print("Get subthemes:")
response = brickse.lego.get_subthemes('The Hobbit')
print(json.loads(response.read()))
print()

print("Get theme years:")
response = brickse.lego.get_theme_years('The Hobbit')
print(json.loads(response.read()))
print()
