class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        obj = {}
        for k, v in self.__dict__.items():
            if k in attrs:
                obj[k] = v
        return obj

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
