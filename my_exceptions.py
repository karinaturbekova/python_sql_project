class InvalidInputError(Exception):
    """Exception for invalid input data."""
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)

class DatabaseConnectionError(Exception):
    """Exception for database connection errors."""
    def __init__(self, message="Failed to connect to the database."):
        super().__init__(message)

class QueryExecutionError(Exception):
    """Exception for query execution errors."""
    def __init__(self, message="Error occurred during query execution."):
        super().__init__(message)

def validate_string_input(input_value: str, field_name: str) -> str:
    """
    - Removes extra spaces.
    - Checks that the string is not empty.
    """
    input_value = input_value.strip()
    if not input_value:
        raise InvalidInputError(f"{field_name} cannot be empty.")
    return input_value

def validate_integer_input(input_value: str, field_name: str) -> int:
    """
    Validates input for conversion to an integer.
    """
    if not input_value.isdigit():
        raise InvalidInputError(f"{field_name} must be a valid integer.")
    return int(input_value)

def validate_db_connection(connection) -> None:
    """
    Checks if the database connection is active.
    """
    if connection is None or not connection.is_connected():
        raise DatabaseConnectionError("The database connection is not active.")
