
from uuid import uuid4
class Coffee:
   def __init__(self, size, name, coffee_type):
       self.size = size
       self.name = name
       self.type = coffee_type
       self.id = uuid4()