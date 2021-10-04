# Brickse

The *brickse* library provides a collection of utilities to retrieve various data from
[BrickSet.com](https://brickset.com/) bricks repository. It can be used either as a simple tool, which reads
requested data and converts them into easy-access custom classes or by using the API directly to allow handling the
HTTPResponse in whatever way you want.

Please see the *examples* folder or in-code documentation of classes and functions to learn more about the *brickse*
library capabilities as well as the original documentation of the
[BrickSet API](https://brickset.com/article/52664/api-version-3-documentation).

See also a similar tool for [Rebrickable.com](https://rebrickable.com/) called [rebrick](https://github.com/xxao/rebrick).


## Tool Example

```python
import brickse

# init Brickse tool
bs = brickse.Brickse("your_API_KEY_here", "your_USER_TOKEN_here", silent=True)

# get set info
data = bs.get_set(set_number=6608)
print(data)

# if user token is not provided on init you can get it later to access user data
bs.login("your_username_here", "your_password_here")

# get user sets
data = bs.get_users_sets(owned=True)
print(data)
```

## API Example

```python
import brickse
import json

# init brickse module for general reading
brickse.init("your_API_KEY_here")

# get set info
response = brickse.lego.get_set(set_number=6608)
print(json.loads(response.read()))

# init brickse module including user reading
brickse.init("your_API_KEY_here", "your_USER_TOKEN_here")

# if you don't know the user token you can use your login credentials
brickse.init("your_API_KEY_here", "your_username_here", "your_password_here")

# get user sets
response = brickse.users.get_sets(owned=True)
print(json.loads(response.read()))
```

## Installation

The *brickse* library is fully implemented in Python. No additional compiler is necessary. After downloading the source
code just run the following command from the *brickse* folder:

```$ python setup.py install```

or simply by using pip

```$ pip install brickse```


## Disclaimer

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
