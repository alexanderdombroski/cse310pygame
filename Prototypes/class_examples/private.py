class Example:
    def __init__(self):
        self.public_property = "I am accessible from anywhere."
        self.__private_property = "I am only accessible within the class."

    def public_method(self):
        return "This is a public method."

    def __private_method(self):
        return "This is a private method."