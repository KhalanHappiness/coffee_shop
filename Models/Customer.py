class Customer:

    def __init__(self, name):
        if not isinstance(name, str) and (name.length >= 1 and name.length <= 15):
            raise TypeError("name must be a string between 1 and 15 characters")
        self.name = name

        pass
    pass