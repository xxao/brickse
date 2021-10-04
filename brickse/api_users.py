# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

# See the BrickSet API documentation at https://brickset.com/article/52664/api-version-3-documentation

import json
from . import config
from . request import request, assert_user_token


def get_token(username, password, api_key=None):
    """
    Retrieves user token to be used for authorizing actions.
    
    Args:
        username: str
            BrickSet registration username or email.
        
        password: str
            BrickSet registration password.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'username': username,
        'password': password,
        'apiKey': api_key}
    
    path = config.API_URL + "login"
    
    return request(path, parameters, post=True)


def check_token(token, api_key=None):
    """
    Checks user token to be used for authorizing actions.
    
    Args:
        token: str
            BrickSet user token.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'userHash': token,
        'apiKey': api_key}
    
    path = config.API_URL + "checkUserHash"
    
    return request(path, parameters, post=True)


def get_sets(query=None, set_id=None, set_number=None, theme=None, subtheme=None, year=None, owned=False, wanted=False, extended_data=False, page=None, page_size=None, ordering=None, user_token=None, api_key=None):
    """
    Retrieves a list of user sets according to search params.
    
    Args:
        query: str
            Search term for set number, name, theme and subtheme.
        
        set_id: int
            BrickSet internal set ID.
        
        set_number: int
            Full set number including variant.
        
        theme: str, int or (int,)
            Theme name or ID(s).
        
        theme: str, int or (int,)
            Sub-theme name or ID(s).
        
        year: int or (int,)
            Release year(s).
        
        owned: bool
            If set to True, owned sets are retrieved only.
        
        wanted: bool
            If set to True, wanted sets are retrieved only.
        
        extended_data: bool
            If set to True, full data are retrieved.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        user_token: str or None
            BrickSet API user token. If set to None the one set by
            brickse.init() is used.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if set_number and '-' not in str(set_number):
        set_number = "%s-1" % set_number
    
    params = {
        'query': query,
        'setID': set_id,
        'setNumber': set_number,
        'theme': theme,
        'subtheme': subtheme,
        'year': year,
        'owned': int(owned),
        'wanted': int(wanted),
        'extendedData': int(extended_data),
        'pageNumber': page,
        'pageSize': page_size,
        'orderBy': ordering}
    
    params = {k: v for k, v in params.items() if v is not None}
    
    parameters = {
        'params': json.dumps(params),
        'userHash': assert_user_token(user_token),
        'apiKey': api_key}
    
    path = config.API_URL + "getSets"
    
    return request(path, parameters, post=True)


def get_sets_notes(user_token=None, api_key=None):
    """
    Retrieves a list of notes for the sets owned by a user.
    
    Args:
        user_token: str or None
            BrickSet API user token. If set to None the one set by
            brickse.init() is used.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'userHash': assert_user_token(user_token),
        'apiKey': api_key}
    
    path = config.API_URL + "getUserNotes"
    
    return request(path, parameters, post=True)


def get_minifigs(query=None, owned=False, wanted=False, user_token=None, api_key=None):
    """
    Retrieves a list of minifigs owned/wanted by a user.
    
    Args:
        query: str or None
            Search query to limit the minifigs by.
        
        owned: bool
            If set to True, only the owned minifigs are retrieved.
        
        wanted: bool
            If set to True, only the wanted minifigs are retrieved.
        
        user_token: str or None
            BrickSet API user token. If set to None the one set by
            brickse.init() is used.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    params = {
        'query': query,
        'owned': int(owned),
        'wanted': int(wanted)}
    
    params = {k: v for k, v in params.items() if v is not None}
    
    parameters = {
        'params': json.dumps(params),
        'userHash': assert_user_token(user_token),
        'apiKey': api_key}
    
    path = config.API_URL + "getMinifigCollection"
    
    return request(path, parameters, post=True)


def get_minifigs_notes(user_token=None, api_key=None):
    """
    Retrieves a list of notes for the minifigs owned by a user.
    
    Args:
        user_token: str or None
            BrickSet API user token. If set to None the one set by
            brickse.init() is used.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'userHash': assert_user_token(user_token),
        'apiKey': api_key}
    
    path = config.API_URL + "getUserMinifigNotes"
    
    return request(path, parameters, post=True)
