from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class BarCommand(PluginCommand):

    @command
    def do_bar(self, args, arguments):
        """
        ::

          Usage:
                bar -f FILE
                bar FILE
                bar list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



