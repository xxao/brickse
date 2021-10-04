#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import brickse

# Before you can start this example be sure to fill in following variables with
# your specific values:

API_KEY = "key"
USER_TOKEN = "token"
USER_NAME = "username"
USER_PASSWORD = "password"

# init Brickse tool
bs = brickse.Brickse(API_KEY, USER_TOKEN, silent=True)

# if user token is not provided on init you can get it later to access user data
# bs.login(USER_NAME, USER_PASSWORD)

print("Get sets:")
data = bs.get_sets(year=2012, theme="The Hobbit")
print(data)
print()

print("Get set:")
data = bs.get_set(set_number=79003)
print(data)
print()

print("Get set instructions:")
data = bs.get_set_instructions(set_number=79003)
print(data)
print()

print("Get themes:")
data = bs.get_themes()
print(data)
print()

print("Get subthemes:")
data = bs.get_subthemes("The Hobbit")
print(data)
print()

print("Get user's sets:")
data = bs.get_users_sets(year=2012, theme="The Hobbit", owned=True)
print(data)
print()

print("Get user's minifigs:")
data = bs.get_users_minifigs("Sparrow", owned=True)
print(data)
print()
