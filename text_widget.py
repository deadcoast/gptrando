import tkinter as tk
import tk
import search_bar_handler
from search_bar_handler import SearchBarHandler

from .theme_manager import ThemeManager
from self_setup_menu_bar import MenuBar



class TextWidgetError(Exception):
    """
    A custom exception class for text widget errors.
    """

    def __init__(self, message):
        """
        Initialize the TextWidgetError object.

        Args:
            message (str): The error message.
        """
        self.message = message

    def __str__(self):
        """
        Return the error message as a string.

        Returns:
            str: The error message.
        """
        return self.message

    def __repr__(self):
        """
        Return a string representation of the TextWidgetError object.

        Returns:
            str: A string representation of the TextWidgetError object.
        """
        return f'TextWidgetError({repr(self.message)})'


class TextWidget(tk.Widget):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.text_widget = None

    def setup_text_area(self):
        """
        Sets up the text WidgetTest.
        """
        if self.text_widget is not None:
            self.text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        return self.text_widget

    def toggle_formatting(self, tag):
        ranges = self.text_widget.tag_ranges('sel')
        if ranges is None:
            return
        start, end = ranges
        if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
            self.text_widget.tag_remove(tag, start, end)
        else:
            self.text_widget.add_tag(tag, start, end)

    def set_content(self, content):
        """
        Sets the content of the Flare WidgetTest.
        """
        if self.text_widget is None:
            return
        if not isinstance(content, str):
            raise ValueError("content must be a string")
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', content)

    def get_content(self):
        """
        Retrieves the current content of the Flare WidgetTest.
        """
        if self.text_widget is None:
            raise TextWidgetError("text_widget cannot be None in the get_content method")

        return self.text_widget.get('1.0', 'end-1c').strip()


def setup_menu_bar(self, menu_bar):
    """
    Set up the menu bar with the specified options.

    Parameters:
    - self: the instance of the class
    - menu_bar: The menu bar object to be set up. It should be an instance of the `MenuBar` class.

    Returns:
    - The created menu bar
    """
    if not isinstance(menu_bar, MenuBar):
        raise TypeError("menu_bar must be an instance of MenuBar")

    try:
        # Code to setup the menu bar
        ...
    except Exception as e:
        # Handle the exception
        print(f"Error setting up menu bar: {str(e)}")
        return menu_bar, False

    return menu_bar, True


def toggle_underline(self, event):
    """
    Toggles the underline formatting for the selected text.
    :param self:
    :param event:
    :return:
    """
    self.toggle_formatting('underline'),


def toggle_strike(self, event):
    """
    Toggles the strike-through formatting for the selected text.
    :param self:
    :param event:
    :return:
    """
    self.toggle_formatting('strike'),


def toggle_code(self, event):
    """
    Toggles the code formatting for the selected text.
    :param self:
    :param event:
    :return:
    """
    self.toggle_formatting('code')


def toggle_color(self, event):
    """
    Toggles the color formatting for the selected text.
    """
    self.toggle_formatting('color'),


def toggle_link(self, event):
    """
    Toggles the link formatting for the selected text.
    """
    self.toggle_formatting('link'),


def toggle_code_block(self, event):
    """
    Toggles the code block formatting for the selected text.
    """
    self.toggle_formatting('code_block'),


def toggle_quote(self, event):
    """
    Toggles the quote formatting for the selected text.
    """
    self.toggle_formatting('quote'),


def toggle_list(self, event):
    """
    Toggles the list formatting for the selected text.
    """
    self.toggle_formatting('list')


def toggle_bold(self, event):
    """
    Toggles the bold formatting for the selected text.
    """
    self.toggle_formatting('bold')


def toggle_italic(self, event):
    """
    Toggles the italic formatting for the selected text.
    """
    self.toggle_formatting('italic')


def toggle_formatting(self, tag):
    """
    Generic method to toggle the specified text formatting tag.
    """
    start, end = self.text_widget.tag_ranges('sel')
    if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
        self.text_widget.tag_remove(tag, start, end)
    else:
        self.text_widget.add_tag(tag, start, end)


def set_content(self, content):
    """
    Sets the content of the Flare WidgetTest.
    """
    self.text_widget.delete('1.0', tk.END)
    self.text_widget.insert('1.0', content)


def get_content(self):
    """
    Retrieves the current content of the Flare WidgetTest.
    """
    if self.text_widget is None:
        raise ValueError("text_widget cannot be None")

    # Get the current content of the Flare WidgetTest
    return self.text_widget.get('1.0', 'end-1c').strip()