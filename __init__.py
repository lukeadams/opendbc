
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


import os
DBC_PATH = os.path.dirname(os.path.abspath(__file__))
