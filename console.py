#!/usr/bin/python3
""" command line interpreter or console """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Prompt for HBNB console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ exits the console """
        # equivalent to CTRL-D
        return True

    def do_quit(self, arg):
        """exit the program (Quit Command)"""
        # quit 
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
