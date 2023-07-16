#!/usr/bin/python3
"""
    Serializes instances to a JSON file and deserializes
    JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Deserializes JSON file to objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_data = json.load(file)
                for obj in obj_data.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(f"{cls_name}")(**obj))
        except FileNotFoundError:
            return
