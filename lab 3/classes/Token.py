class Token:
    # A token consists of a type and an optional value.
    def __init__(self, type, value=None):
        self.type = type  # The type of the token (from TokenType)
        self.value = value  # The value of the token (relevant for integers)

    # Representation of the Token instance for debugging and testing.
    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"
