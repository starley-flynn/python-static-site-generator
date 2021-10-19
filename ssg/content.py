import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping

class Content(Mapping):

    __delimeter = '"^(?:-|\+)'
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, str):
        return str