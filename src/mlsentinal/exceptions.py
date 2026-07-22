"""
Custom made exceptions for MLSentinal SDK for efficient error handling
"""

class MLSentinalError(Exception):
    """
    Base exception
    """
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

    def __str__(self):
        return f"[{self.code}] {self.message}"
    
    
class InvalidAPIKeyError(MLSentinalError):
    """
    Raised when entered API key was wrong
    """

    pass

class AuthenticationError(MLSentinalError):
    """
    When Authentication failes
    """

    pass

class MetricValidationError(MLSentinalError):
    """
    Raised one or more metrics
    """

    pass

class ProjectValidationError(MLSentinalError):
    """
    When project name is invalid
    """

    pass

class ModelValidationError(MLSentinalError):
    """
    When invalid model name
    """

    pass

class MLSentinalConnectionError(MLSentinalError):
    """
    When SDK could not connect the MLSentinal servers
    """

    pass

class MLSentinalServerError(MLSentinalError):
    """
    When server returns error
    """

    pass