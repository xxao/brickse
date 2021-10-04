# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import json
import urllib.request
import urllib.error
from . import config
from . import api_lego as lego
from . import api_users as users
from . objects import *


class Brickse(object):
    """Brickse tool."""
    
    
    def __init__(self, api_key=None, user_token=None, silent=False):
        """
        Initializes a new instance of brickse.Brickse class.
        
        Args:
            api_key: str or None
                BrickSet API key. If set to None, module global API key is
                used.
            
            user_token:
                BrickSet user token. If set to None, you need to call login
                method before accessing user account functionality.
            
            silent: bool
                If set to True, all HTTP errors will be silenced and methods
                return None. If set to False, all HTTP errors are raised
                normally.
        """
        
        super().__init__()
        
        self._api_key = api_key
        self._user_token = user_token
        self._silent = silent
    
    
    def login(self, username, password):
        """
        Retrieves user login token, which is used to access user account
        functionality.
        
        Args:
            username: str
                BrickSet login username or email.
            
            password: str
                BrickSet login password.
        
        Returns:
            str or None
                Returns user token or None if login failed.
        """
        
        # send request
        try:
            response = users.get_token(
                username = username,
                password = password,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # set token
        self._user_token = data.get('hash', None)
        
        return self._user_token
    
    
    def get_sets(self, query=None, set_id=None, set_number=None, theme=None, subtheme=None, year=None):
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
        
        Returns:
            (brickse.Collection,) or None
                Sets details.
        """
        
        sets = []
        page = 1
        
        while True:
            
            # send request
            try:
                response = lego.get_sets(
                    query = query,
                    set_id = set_id,
                    set_number = set_number,
                    theme = theme,
                    subtheme = subtheme,
                    year = year,
                    extended_data = True,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create collections
            for item in data['sets']:
                sets.append(Collection.create(item))
            
            # check next page
            if data['matches'] <= len(sets):
                break
            
            # get next page
            page += 1
        
        return sets
    
    
    def get_set(self, set_id=None, set_number=None):
        """
        Retrieves details about specific set.
        
        Args:
            set_id: int
                BrickSet internal set ID.
            
            set_number: int
                Full set number including variant.
        
        Returns:
            brickse.Collection or None
                Set details.
        """
        
        # send request
        try:
            response = lego.get_set(
                set_id = set_id,
                set_number = set_number,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read()).get('sets', None)
        if not data:
            return None
        
        # create set
        return Collection.create(data[0])
    
    
    def get_set_instructions(self, set_id=None, set_number=None):
        """
        Retrieves a list of instructions for the specified set.
        
        Args:
            set_id: int
                BrickSet internal set ID.
            
            set_number: int
                Full set number including variant.
        
        Returns:
            (brickse.Instructions,) or None
                Set instructions.
        """
        
        instructions = []
        
        # get internal ID
        if set_id is None:
            
            collection = self.get_set(set_number=set_number)
            if collection is None:
                return None
            
            set_id = collection.set_id
        
        # send request
        try:
            response = lego.get_set_instructions(
                set_id = set_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read()).get('instructions', None)
        if not data:
            return None
        
        # create instructions
        for item in data:
            instructions.append(Instructions.create(item))
        
        return instructions
    
    
    def get_themes(self):
        """
        Retrieves a list of themes, with the total number of sets in each.
        
        Returns:
            (brickse.Theme,) or None
                Available themes.
        """
        
        themes = []
        
        # send request
        try:
            response = lego.get_themes(
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read()).get('themes', None)
        if not data:
            return None
        
        # create themes
        for item in data:
            themes.append(Theme.create(item))
        
        return themes
    
    
    def get_subthemes(self, theme):
        """
        Retrieves a list of sub-themes for a given theme, with the total number
        of sets in each.
        
        Args:
            theme: str
                Main theme name.
        
        Returns:
            (brickse.Theme,) or None
                Sub-themes.
        """
        
        themes = []
        
        # send request
        try:
            response = lego.get_subthemes(
                theme = theme,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read()).get('subthemes', None)
        if not data:
            return None
        
        # create themes
        for item in data:
            if item['subtheme'] != '{None}':
                themes.append(Theme.create(item))
        
        return themes
    
    
    def get_users_sets(self, query=None, set_id=None, set_number=None, theme=None, subtheme=None, year=None, owned=False, wanted=False):
        """
        Retrieves a list of user sets according to search params.
        
        Args:
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
        
        Returns:
            (brickse.Collection,) or None
                Sets details.
        """
        
        sets = []
        page = 1
        
        while True:
            
            # send request
            try:
                response = users.get_sets(
                    query = query,
                    set_id = set_id,
                    set_number = set_number,
                    theme = theme,
                    subtheme = subtheme,
                    year = year,
                    extended_data = True,
                    page = page,
                    owned = owned,
                    wanted = wanted,
                    api_key = self._api_key,
                    user_token = self._user_token)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create collections
            for item in data['sets']:
                sets.append(Collection.create(item))
            
            # check next page
            if data['matches'] <= len(sets):
                break
            
            # get next page
            page += 1
        
        return sets
    
    
    def get_users_minifigs(self, query=None, owned=False, wanted=False):
        """
        Retrieves a list of minifigs owned/wanted by a user.
        
        Args:
            query: str or None
                Search query to limit the minifigs by.
            
            owned: bool
                If set to True, only the owned minifigs are retrieved.
            
            wanted: bool
                If set to True, only the wanted minifigs are retrieved.
        
        Returns:
            (brickse.Minifig,) or None
                Minifigs details.
        """
        
        minifigs = []
        
        # send request
        try:
            response = users.get_minifigs(
                api_key = self._api_key,
                user_token = self._user_token)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read()).get('minifigs', None)
        if not data:
            return None
        
        # create minifigs
        for item in data:
            minifigs.append(Minifig.create(item))
        
        return minifigs
    
    
    def get_file(self, url):
        """
        Downloads a file from given URL.
        
        Args:
            url: str
                URL of the image to download.
        
        Returns:
            bytes
                Image data.
        """
        
        # make request
        request = urllib.request.Request(url, headers={'User-Agent': 'Brickse Tool'})
        
        # send request
        try:
            response = urllib.request.urlopen(request)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        return response.read()
    
    
    def _on_error(self, error):
        """Process request error."""
        
        if self._silent:
            return
        
        raise error
