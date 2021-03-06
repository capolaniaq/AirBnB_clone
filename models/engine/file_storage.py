#!/usr/bin/python3
"""Module File_storage"""

import json


class FileStorage:
    """ File storage class that serialze instances to a JSON file and
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method that returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Method that sets in __objects the obj with key """
        id_key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({id_key: obj})

    def save(self):
        """ Public method that serializes __objects to the JSON file """
        new_dict = {}
        for key, value in self.all().items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists; otherwise, do nothing
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        new_dict = {}
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    self.all()[key] = obj
        except:
            pass
