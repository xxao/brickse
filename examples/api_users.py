#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import json
import brickse

# Before you can start this example be sure to fill in following variables with
# your specific values:

API_KEY = "key"
USER_TOKEN = "token"
USER_NAME = "username"
USER_PASSWORD = "password"

# set default tokens for the whole module directly
brickse.init(API_KEY, USER_TOKEN)

# OR set default tokens for the whole module by login credentials
# brickse.init(API_KEY, USER_NAME, USER_PASSWORD)

# print("Get user token:")
# response = brickse.users.get_token(USER_NAME, USER_PASSWORD)
# print(json.loads(response.read()))
# print()

print("Get user's sets:")
response = brickse.users.get_sets(year=2012, theme="The Hobbit", owned=True)
print(json.loads(response.read()))
print()

print("Get user's sets notes:")
response = brickse.users.get_sets_notes()
print(json.loads(response.read()))
print()

print("Get user's minifigs:")
response = brickse.users.get_minifigs("Sparrow", owned=True)
print(json.loads(response.read()))
print()

print("Get user's minifigs notes:")
response = brickse.users.get_minifigs_notes()
print(json.loads(response.read()))
print()
