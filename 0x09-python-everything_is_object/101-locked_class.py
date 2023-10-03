#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, value):
        if attr == "first_name":
            self.__dict__[attr] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{attr}'")
