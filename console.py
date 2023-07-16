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
        """
            Updates an instance based on the class name and id by 
            adding or updating attribute (save the change into the
            JSON file)
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
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            object_class = arg[0]
            object_id = arg[1]
            object_key = object_class + "." + object_id
            obj = storage.all()[object_key]

            attribute_name = arg[2]
            attribute_value = arg[3]

            if attribute_value[0] == '"':
                attribute_value = attribute_value[1:-1]
            if hasattr(obj, attribute_name):
                type_ = type(getattr(obj, attribute_name))
                if type_ in [str, float, int]:
                    attribute_value = type_(attribute_value)
                    setattr(obj, attribute_name, attribute_value)
            else:
                setattr(obj, attribute_name, attribute_value)

            storage.save()

    def default(self, args):
        """retrieve all instances of a class"""
        arg = args.split('.')

        if arg[0] in self.__classes:
            if arg[1] == "all()":
                self.do_all(arg[0])
            elif arg[1] == "count()":
                list_ = [v for k, v in storage.all().items() if k.startswith(arg[0])]
                print(len(list_))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
