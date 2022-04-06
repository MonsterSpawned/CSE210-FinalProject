# An internal error to be used by the game.
class InternalErrorException(Exception):
    pass

# The user did something stupid.
class UserErrorException(Exception):
    pass

# The developer did something stupid.
class HowIsThisPossibleException(Exception):
    pass