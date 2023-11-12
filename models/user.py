#!/usr/bin/python3
"""User that inherits from BaseModel"""

import json
from models.base_model import BaseModel


class User(BaseModel):
    """A subclass of BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
