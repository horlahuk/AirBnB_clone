#!/usr/bin/python3
"""
    The command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    __classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quits the console """
        return True

    def do_EOF(self, arg):
        """ Quits the console """
        return True

    def emptyline(self):
        """ Do nothing when enter is pressed """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(f"{arg[0]}")()
            print(new_obj.id)
        storage.save()

    def do_show(self, args):
        """
            Prints the string representation of an instance based
            on the class name and id
        """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{arg[0]}.{arg[1]}"])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{arg[0]}.{arg[1]}"]

        storage.save()

    def do_all(self, args):
        """
            Prints all string representation of all instances based
            or not on the class name
        """
        arg = args.split()

        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])

        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if k.startswith(arg[0])])

    def do_update(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
