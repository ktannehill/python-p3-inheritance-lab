#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._knowledge = knowledge

    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, knowledge):
        if isinstance(knowledge, list) and len(knowledge):
            self._knowledge = knowledge

    def teach(self):
        return random.choice(knowledge)

my_teacher = Teacher("My", "Teacher")
