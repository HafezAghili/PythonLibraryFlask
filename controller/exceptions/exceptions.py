class AccessDeniedError(Exception):
    def __init__(self):
        super().__init__("Wrong Username or Password")


class NoUsernameError(Exception):
    def __init__(self):
        super().__init__("No User found")


class DuplicateUsernameError(Exception):
    def __init__(self):
        super().__init__("Duplicate Username")


class NoBookError(Exception):
    def __init__(self):
        super().__init__("No Book found")
