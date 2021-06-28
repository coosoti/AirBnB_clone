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

    def do_help(self, args):
        """command lists all help details for each command """
        cmd.Cmd.do_help(self, args)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
