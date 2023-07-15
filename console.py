#!/usr/bin/python3
"""
    The command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
