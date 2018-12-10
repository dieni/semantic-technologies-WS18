# from django.db import models
import sys, os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
src_path = os.path.join(src_path, 'platform')
sys.path.append(src_path)
from platform_class import Platform



# Create your models here.
class Controller():
    pass