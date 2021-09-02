
class UnexpectedValueTypeError(Exception):
    """Custom exception to be raised if the script finds a value type that was no t expected
    
    Attributes:
        -file_name = Name of the file where the script found the error.
        -column_name = Name of the column where the script found the error.
        -line_number = Line number where the script found the error.
        -expected_type = The value type that the user expected to find in that column.
        -actual_value = Actual value found by the script.
        
    """

    def __init__(self, file_name, column_name, line_number, expected_type, actual_value):
        self.file_name = file_name
        self.column_name = column_name
        self.line_number = line_number
        self.expected_type = expected_type
        self.actual_value = actual_value
        
        super().__init__(f'Error found at "{file_name}", in column "{column_name}", at line {line_number}. Expected {expected_type} got "{actual_value}"')


class WrongCategoryError(Exception):
    """Custom exception to be raised if the user does not choose any of the value type categories available to choiced.
    
    Attributes:
        -choiced: The category that the user choiced.
    """

    def __init__(self, choiced):
        self.choiced = choiced
        
        super().__init__(f'You should choose one of the available categories (S I, F, N, B). "{choiced.upper()}" is not available.')




