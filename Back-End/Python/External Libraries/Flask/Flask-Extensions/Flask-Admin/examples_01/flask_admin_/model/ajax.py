#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect, warnings
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

DEFAULT_PAGE_SIZE = 10


class AjaxModelLoader(object):

    def __init__(self, name, options):
        self.name = name
        self.options = options
    
    def format(self, model):
        raise NotImplementedError()
    
    def get_one(self, pk):
        raise NotImplementedError()

    def get_list(self, query, offset=0, limit=DEFAULT_PAGE_SIZE):
        raise NotImplementedError()