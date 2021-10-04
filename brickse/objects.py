# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import re

# define constants
INSTRUCTIONS_VERSION_PATTERN = re.compile("(?:vers|V|v).?(\d\d)")
INSTRUCTIONS_PARTS_PATTERN = re.compile("(?:\s|-)([0-9]{1,2})/([0-9]{1,2})(?:\s|$)")


class _Entity(object):
    """Provides a base class for all objects."""
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Entity."""
        
        # set given attributes
        for name, value in attrs.items():
            if hasattr(self, name):
                setattr(self, name, value)
            else:
                raise AttributeError("Attribute not found! --> %s" % name)
    
    
    def __repr__(self):
        """Gets debug string representation."""
        
        return "%s(%s)" % (self.__class__.__name__, self.__str__())


class Collection(_Entity):
    """Represents a BrickSet set."""
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of brickse.Collection."""
        
        self.set_id = None
        self.number = None
        self.variant = None
        
        self.name = None
        self.category = None
        self.group = None
        self.theme = None
        self.subtheme = None
        
        self.year = None
        self.released = None
        
        self.image_url = None
        
        super().__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return "SET ID: %s (%s), %s" % (self.set_id, self.number, self.name)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of brickse.Collection from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from BrickSet
        
        Returns:
            brickse.Collection
                Initialized collection.
        """
        
        # create collection
        return Collection(
            set_id = data['setID'],
            number = data['number'],
            variant = data['numberVariant'],
            name = data['name'],
            year = data['year'],
            category = data['category'],
            group = data['themeGroup'],
            theme = data['theme'],
            subtheme = data.get('subtheme', None),
            released = data['released'],
            image_url = data['image'].get('imageURL', None))


class Theme(_Entity):
    """Represents a BrickSet set theme definition."""
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of brickse.Theme."""
        
        self.name = None
        self.parent = None
        self.subthemes = None
        self.sets = None
        self.year_from = None
        self.year_to = None
        
        super().__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return "Theme: %s (%s)" % (self.name, self.parent)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of brickse.Theme from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from BrickSet.
        
        Returns:
            brickse.Theme
                Initialized theme.
        """
        
        # create sub-theme
        if 'subtheme' in data:
            return Theme(
                parent = data['theme'],
                name = data['subtheme'],
                sets = int(data['setCount']),
                year_from = int(data['yearFrom']),
                year_to = int(data['yearTo']))
        
        # create theme
        return Theme(
            name = data['theme'],
            subthemes = data.get('subthemeCount', None),
            sets = int(data['setCount']),
            year_from = int(data['yearFrom']),
            year_to = int(data['yearTo']))


class Instructions(_Entity):
    """Represents a BrickSet set instructions definition."""
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of brickse.Instructions."""
        
        self.description = None
        self.url = None
        self.version = None
        self.part = None
        self.parts = None
        
        super().__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return "Instructions: %s (%s)" % (self.description, self.url)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of brickse.Instructions from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from BrickSet.
        
        Returns:
            brickse.Instructions
                Initialized instructions.
        """
        
        # get description
        descr = data.get('description', None)
        version = None
        part = None
        parts = None
        
        # get version
        if descr:
            
            # get version
            match = INSTRUCTIONS_VERSION_PATTERN.search(descr)
            if match:
                version = f"V{match.group(1)}"
            elif descr[-3:] in (" IN", " NA"):
                version = descr[-2:]
            
            # get parts
            match = INSTRUCTIONS_PARTS_PATTERN.search(descr)
            if match:
                part = int(match.group(1))
                parts = int(match.group(2))
        
        # create instructions
        return Instructions(
            description = descr,
            url = data['URL'],
            version = version,
            part = part,
            parts = parts)


class Minifig(_Entity):
    """Represents a BrickSet minifig."""
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of brickse.Minifig."""
        
        self.minifig_id = None
        self.name = None
        self.category = None
        
        self.owned_in_sets = None
        self.owned_loose = None
        self.owned_total = None
        self.wanted = None
        
        super().__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return "MINIFIG ID: %s, %s" % (self.minifig_id, self.name)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of brickse.Collection from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from BrickSet
        
        Returns:
            brickse.Minifig
                Initialized minifig.
        """
        
        # create minifig
        return Minifig(
            minifig_id = data['minifigNumber'],
            name = data['name'],
            category = data['category'],
            owned_in_sets = data['ownedInSets'],
            owned_loose = data['ownedLoose'],
            owned_total = data['ownedTotal'],
            wanted = data['wanted'])
