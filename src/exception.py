import sys
from logger import logging

def error_message_details(e: Exception, error_detail:sys) -> str:
    """Return the error message details."""
    exc_type, exc_value, exc_tb = sys.exc_info()
    return f"Exception type: {exc_type.__name__}, Message: {str(exc_value)}, Traceback: {exc_tb.tb_frame.f_code.co_filename}, Line: {exc_tb.tb_lineno}"

class CustomException(Exception):
    """Custom exception class to handle exceptions in the application."""
    def __init__(self, error_message, error_detail: sys) -> None:
        """Initialize the custom exception with a message and the original error."""
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
        self.error_detail = error_detail

    def __str__(self) -> str:
        """Return the string representation of the exception."""
        return f"{self.error_message}"
    
    
