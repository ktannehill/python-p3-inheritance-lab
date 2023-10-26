#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.knowledge = []
    
    def learn(self, information):
        self.knowledge.append(information)
