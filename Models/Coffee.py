class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) and name.length >= 3:
            raise TypeError("name must be a string with at least three characters")
        self.name = name
        pass
    pass