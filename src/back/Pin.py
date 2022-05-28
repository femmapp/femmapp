from Value import Value

class Pin:
    """
    Class that represents a pin in the application map. It has a 
    """

    __num_categories = 11

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value_id):
        value, id = value_id
        if (self._author_id == id):
            self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value_id):
        value, id = value_id
        if (self._author_id == id):
            self._description = value

    @property
    def author_id(self):
        return self._author_id

    @property
    def attributes(self):
        return self._attributes

    @property
    def coordinates(self):
        return (self._latitude, self._longitude)

    @coordinates.setter
    def coordinates(self, latitude_longitude_id):
        latitude, longitude, id = latitude_longitude_id
        if (self._author_id == id):
            self._latitude, self._longitude = latitude, longitude
    
    def __init__(self, id, name, description, author_id, latitude, longitude, attributes=[[0] * 2 ] * __num_categories):
        self._id = id
        self._name = name
        self._description = description
        self._author_id = author_id
        self._attributes = attributes
        self._latitude = latitude
        self._longitude = longitude

    def __getitem__(self, id):
        if id < 11:
            return self._attributes[key]
        else:
            return None
    