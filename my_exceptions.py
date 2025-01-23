#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class InvalidInputError(Exception):
    """Исключение для некорректного ввода данных."""
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)

class DatabaseConnectionError(Exception):
    """Исключение для ошибок подключения к базе данных."""
    def __init__(self, message="Failed to connect to the database."):
        super().__init__(message)

class QueryExecutionError(Exception):
    """Исключение для ошибок выполнения запросов."""
    def __init__(self, message="Error occurred during query execution."):
        super().__init__(message)

def validate_string_input(input_value: str, field_name: str) -> str:
    """
    Проверяет строковый ввод на корректность.
    - Удаляет лишние пробелы.
    - Проверяет, что строка не пуста.
    """
    if not isinstance(input_value, str):
        raise InvalidInputError(f"{field_name} must be a string.")
    input_value = input_value.strip()
    if not input_value:
        raise InvalidInputError(f"{field_name} cannot be empty.")
    return input_value

def validate_integer_input(input_value: str, field_name: str) -> int:
    """
    Проверяет ввод на возможность преобразования в целое число.
    """
    if not input_value.isdigit():
        raise InvalidInputError(f"{field_name} must be a valid integer.")
    return int(input_value)

def validate_db_connection(connection) -> None:
    """
    Проверяет, активна ли база данных.
    """
    if connection is None or not connection.is_connected():
        raise DatabaseConnectionError("The database connection is not active.")

