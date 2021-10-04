# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

# See the BrickSet API documentation at https://brickset.com/article/52664/api-version-3-documentation

import json
from . import config
from . request import request


def get_sets(query=None, set_id=None, set_number=None, theme=None, subtheme=None, year=None, extended_data=False, page=None, page_size=None, ordering=None, api_key=None):
    """
    Retrieves a list of sets according to search params.
    
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
        
        extended_data: bool
            If set to True, full data are retrieved.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
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
        'extendedData': int(extended_data),
        'pageNumber': page,
        'pageSize': page_size,
        'orderBy': ordering}
    
    params = {k: v for k, v in params.items() if v is not None}
    
    parameters = {
        'params': json.dumps(params),
        'userHash': "",
        'apiKey': api_key}
    
    path = config.API_URL + "getSets"
    
    return request(path, parameters, post=True)


def get_set(set_id=None, set_number=None, extended_data=True, api_key=None):
    """
    Retrieves details about specific set.
    
    Args:
        set_id: int
            BrickSet internal set ID.
        
        set_number: int
            Full set number including variant.
        
        extended_data: bool
            If set to True, full data are retrieved.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if set_number and '-' not in str(set_number):
        set_number = "%s-1" % set_number
    
    return get_sets(
        set_id = set_id,
        set_number = set_number,
        extended_data = extended_data,
        api_key = api_key)


def get_set_images(set_id, api_key=None):
    """
    Retrieves a list of URLs of additional set images for the specified set.
    
    Args:
        set_id: int
            BrickSet internal set ID.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'setID': set_id,
        'apiKey': api_key}
    
    path = config.API_URL + "getAdditionalImages"
    
    return request(path, parameters)


def get_set_instructions(set_id, api_key=None):
    """
    Retrieves a list of instructions for the specified set.
    
    Args:
        set_id: int
            BrickSet internal set ID.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'setID': set_id,
        'apiKey': api_key}
    
    path = config.API_URL + "getInstructions"
    
    return request(path, parameters)


def get_set_reviews(set_id, api_key=None):
    """
    Retrieves user reviews for the specified set.
    
    Args:
        set_id: int
            BrickSet internal set ID.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'setID': set_id,
        'apiKey': api_key}
    
    path = config.API_URL + "getReviews"
    
    return request(path, parameters)


def get_themes(api_key=None):
    """
    Retrieves a list of themes, with the total number of sets in each.
    
    Args:
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'apiKey': api_key}
    
    path = config.API_URL + "getThemes"
    
    return request(path, parameters)


def get_subthemes(theme, api_key=None):
    """
    Retrieves a list of sub-themes for a given theme, with the total number of
    sets in each.
    
    Args:
        theme: str
            Main theme name.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'Theme': theme,
        'apiKey': api_key}
    
    path = config.API_URL + "getSubthemes"
    
    return request(path, parameters, post=True)


def get_theme_years(theme=None, api_key=None):
    """
    Retrieves a list of years for a given theme, with the total number of sets
    in each.
    
    Args:
        theme: str or None
            The theme to limit the set by or None for all.
        
        api_key: str or None
            BrickSet API access key. If set to None the one set by
            brickse.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'Theme': theme or "",
        'apiKey': api_key}
    
    path = config.API_URL + "getYears"
    
    return request(path, parameters, post=True)
