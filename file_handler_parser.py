import logging
import os
import re


def parse_and_save_file(self, file_path):
    with open(file_path, "r") as file:
        content = file.read()
    # Parse the content and extract Python code and Markdown code
    python_code, markdown_code = self.extract_code(content)
    # Determine the appropriate subdirectory based on file type
    if python_code:
        subdir = os.path.join(self.parsed_directory, ".python")
    else:
        subdir = os.path.join(self.parsed_directory, ".md")
    os.makedirs(subdir, exist_ok=True)
    # Save the extracted code to new files
    self.save_code(
        python_code,
        os.path.join(
            subdir, f"{os.path.splitext(os.path.basename(file_path))}.py"
        ),
    )
    self.save_code(
        markdown_code,
        os.path.join(
            subdir, f"{os.path.splitext(os.path.basename(file_path))}.md"
        ),
    )


def save_code(self, code, file_path):
    if not code:
        return
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Write the code to the file
    with open(file_path, "w") as file:
        file.write(code)

    print(f"Saved code to {file_path}")

    self.display_message(f"Saved code to {file_path}")


def extract_code(self, content: str) -> tuple:
    """
    Extracts Python and Markdown code from the content.
    Args:
        content (str): The content to extract code from.
    Returns:
        tuple: A tuple containing the extracted Python code and Markdown code.
        :param content: 
        :param self: 
    """
    if not isinstance(content, str):
        raise ValueError("Content must be a string.")

    try:
        python_code = self.python_code_pattern(content)
        markdown_code = self.markdown_code_pattern(content)

        # Remove code block delimiters from extracted code snippets
        python_code = [code.strip("```") for code in python_code]
        markdown_code = [code.strip("```") for code in markdown_code]

        return python_code, markdown_code
    except Exception as e:
        print(f"Error extracting code: {e}")


def python_code_pattern(self, content: str) -> list:
    return re.findall(r"```python\n(.*?)```", content, re.DOTALL)


def markdown_code_pattern(self, content):
    return re.findall(r"```(.*?)```", content, re.DOTALL)


PYTHON_CODE_PATTERN = re.compile(r"```python\n(.*?)```")
MARKDOWN_CODE_PATTERN = re.compile(r"```(.*?)```")


class CustomExtractionError(Exception):
    
    def __init__(self, message: str):
        """
        Initialize the CustomExtractionError instance.

        Args:
            message (str): The error message.
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return f'CustomExtractionError("{self.message}")'

    def __call__(self):
        return f"{self.message}!"

    def __add__(self, other):
        return f"{self.message}**{other.message}**"

    def __mul__(self, other):
        return self.message * other + "!" * other

    def __rmul__(self, other):
        return other.message * self.message + "!!"

    def __radd__(self, other):
        return other.message + self.message

    def __iadd__(self, other): 
        self.message += other.message
        return self


class ChatLogParser:

    def extract_code(self, content):
        """
        Extracts Python and Markdown code from the chat log content.
            Args:
                content (str): The chat log content.

            Returns:
                tuple: A tuple containing the extracted Python code and Markdown code.
        """
        if not content:
            raise ValueError("Content must not be None or empty.")

        try:
            code_pattern = re.compile(r"```(.*?)```|```python\n(.*?)```")
            code = code_pattern.findall(content)
            python_code = [c[1] for c in code if c[1]]
            markdown_code = [c[0] for c in code if c[0]]

            return python_code, markdown_code
        except Exception as e:
            logging.exception("Error occurred during code extraction.")
            raise CustomExtractionError("Failed to extract code from chat log.") from e
