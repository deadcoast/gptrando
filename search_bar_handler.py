import logging
import tkinter as tk
from tkinter import font

from fig.cli import formatter

from .inline_search_manager import InlineSearchManager
from .theme_manager import theme_manager
from .theme_manager import ThemeManager


class NoMoreOccurrencesException(Exception):
    pass

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    def __call__(self):
        return self.message


def emit_text_widget_set_event(callback=None):
    """
    Emits a text WidgetTest set event and returns a boolean indicating the success of the event emission or callback function call.

    This method is responsible for emitting an event or calling a callback function after the text WidgetTest is set. It should be called after setting the text WidgetTest to perform any necessary actions or updates related to the text WidgetTest.

    Args:
        callback (function, optional): A callback function to be called after the text WidgetTest is set. Defaults to None.

    Returns:
        bool: True if the event was successfully emitted or the callback function was successfully called, False otherwise.
    """
    try:
        # code to emit the event or call the callback function
        if callback:
            callback()
        return True
    except Exception as e:
        print(f"Error occurred during emission of event or calling of callback function: {e}")
        return False


class SearchBar(tk.Entry):  # Custom search bar WidgetTest
    """
    A custom search bar WidgetTest that can be used to search for text in a text WidgetTest.

    Args:
        master: The parent WidgetTest.
        **kwargs: Additional keyword arguments to pass to the parent WidgetTest.

    Attributes:
        search_bar: The search bar WidgetTest.
        toggle_formatting: A method that can be used to toggle text formatting.
        close_search_bar: A method that can be used to close the search bar.
        close: A method that can be used to close the search bar.
        search_index: The index of the current search query.
        search_highlights: A list of tuples containing the start and end indices of search highlights.
    """

    def __init__(self, master, edit_menu=None, menubar=None, **kwargs):
        super().__init__(master, **kwargs)

        self.menubar = tk.Menu(self)
        self.palette_manager = theme_manager()
        self.search_bar = tk.Entry(self, font=font.Font(family='Courier New', size=12), width=30)
        self.toggle_formatting = formatter.toggle_formatting
        self.close_search_bar = self.pack_forget
        self.close = self.close_search_bar
        self.search_index = 1.0
        self.search_highlights = []
        self.text_widget = self.set_text_widget
        self.search_query = ""
        self.setup_search_bar()
        self.setup_text_formatting()
        self.setup_bindings()

        self.main.protocol("WM_DELETE_WINDOW", self.close)
        self.main.mainloop()

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.theme_manager = ThemeManager(self.palette_manager)
        self.inline_search_manager = InlineSearchManager(self.text_area)
        self.flare_text_extension = FlareTextExtension(self.text_area)

        self.setup_menu_bar()
        self.setup_bindings()

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.parent = self.parent or self.master  # Use main as parent if not specified
        self.parent.title("HEAT UP Editor")
        self.palette_manager = theme_manager()
        self.theme_manager = ThemeManager(self.palette_manager)

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.flare_text_extension = FlareTextExtension(self.text_area)
        self.inline_search_manager = InlineSearchManager(self.text_area)

        self._display_message("Ready")

        edit_menu.add_command(label="Undo", command=self.text_area.undo)
        edit_menu.add_command(label="Redo", command=self.text_area.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.text_area.cut)
        edit_menu.add_command(label="Copy", command=self.text_area.copy)
        edit_menu.add_command(label="Paste", command=self.text_area.paste)

        theme_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Themes", menu=theme_menu)
        theme_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        theme_menu.add_command(label="Toggle Palette", command=self.toggle_palette)

        search_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Search", menu=search_menu)
        search_menu.add_command(label="Toggle Inline Search", command=self.toggle_inline_search)
        search_menu.add_command(label="Toggle Flare Text", command=self.toggle_flare_text)

        self._display_message("Ready")

    def setup_bindings(self):
        self.text_area.bind("<Control-f>", self.inline_search_manager.prompt_search_query)
        self.text_area.bind("<Control-n>", self.inline_search_manager.bar_find_next)
        self.text_area.bind("<Control-p>", self.inline_search_manager.find_previous)

        self.text_area.bind("<Control-s>", self.save_file)
        self.text_area.bind("<Control-o>", self.open_file)

        self.text_area.bind("<Control-q>", self.close)

    def setup_search_bar(self):
        """
        Configures the search bar WidgetTest.
        """
        self.search_bar = tk.Entry(self, font=font.Font(family='Courier New', size=12), width=30)
        self.search_bar.pack(side=tk.TOP, fill=tk.X)
        self.search_bar.bind("<Return>", self.perform_search)

    def setup_text_formatting(self):
        """
        Sets up the text formatting for the search bar.
        """
        background_color = '#303030'
        foreground_color = '#505050'
        self.text_widget.tag_configure('search_highlight', background=background_color, foreground=foreground_color)

        self.bind_key_functions()

    def bind_key_functions(self):
        """
        Binds functions to key combinations for the search bar.
        """
        key_functions = {
            '<Control-f>': self.toggle_formatting,
            '<Control-b>': self.toggle_formatting,
            '<Control-i>': self.toggle_formatting,
            '<Control-Return>': self.perform_search,
            '<Control-n>': self.bar_find_next,
            '<Control-p>': self.find_previous
        }

        for key, function in key_functions.items():
            self.text_widget.unbind(key)
            self.text_widget.bind(key, function)

    def setup_bindings(self):
        """
        Configures the keyboard shortcuts for the inline search functionality.
        """
        key_functions = {
            '<Control-s>': self.prompt_search_query,
            '<F3>': self.bar_find_next,
            '<Shift-F3>': self.find_previous,
            '<Return>': self.perform_search,
        }

        for key, function in key_functions.items():
            self.text_widget.unbind(key)
            self.text_widget.bind(key, function)

    def set_text_widget(self, text_widget):
        """
        Sets the text WidgetTest to be searched.
        """
        self.text_widget = text_widget

    def prompt_search_query(self, event):
        """
        Prompts the user for a search query and initiates the search.
        """
        self.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        self.focus_set()

    def hide_search_bar(self):
        """
        Hides the search bar and clears the search highlights.
        """
        self.search_bar.pack_forget()
        self.clear_search_highlights()

    def clear_search_highlights(self):
        """
        Clears all search result highlights and frees up memory.
        """
        self.search_highlights.clear()

    def _display_message(self, message):
        """
        Displays a message in the status bar.
        """
        self.search_bar.pack(side=tk.TOP, fill=tk.X)
        self.search_bar.focus_set()

    def perform_search(self, event):
        """
        Performs the inline search based on the user's query.
        """
        self.search_query = self.search_bar.get()
        self.search_index = "1.0"
        self.clear_search_highlights()
        self.bar_find_next()

    def bar_find_next(self):
        """
        Finds the next occurrence of the search query and highlights it.
        """
        if not self.search_query:
            return
        if new_search_index := self.text_widget.search(
                self.search_query, self.search_index, stopindex=tk.END
        ):
            return self.add_search_highlight(new_search_index)
        if wrapped_search_index := self.text_widget.search(
                self.search_query, "1.0", stopindex=self.search_index, backwards=True
        ):
            return self.add_search_highlight(wrapped_search_index)
        else:
            raise NoMoreOccurrencesException("No more occurrences found.")

    def add_search_highlight(self, arg0):
        end_index = self.text_widget.index(
            f"{arg0}+{self.text_widget.index(arg0, count=len(self.search_query))}c"
        )
        self.add_search_highlight(arg0, end_index)
        return arg0

    def add_search_highlight(self, start, end):
        """
        Adds a search result highlight to the text WidgetTest.
        """
        self.text_widget.tag_add("search_highlight", start, end)
        self.search_highlights.append((start, end))

    def set_text_widget(self, text_widget):
        """
        Sets the text WidgetTest to be searched and validates the text_widget argument.
        Clears any existing state related to the previous text_widget.
        Emits an event or calls a callback function after the text_widget is set.
        Returns self to allow for method chaining.
        """
        if not isinstance(text_widget, tk.Text):
            raise ValueError("Invalid text_widget. Expected a tk.Text object.")

        try:
            self.clear_search_highlights()  # Clear existing search highlights
            self.search_index = "1.0"  # Reset search index
            self.text_widget = text_widget
            emit_text_widget_set_event()  # or self.call_text_widget_set_callback()
        except Exception as e:
            # Handle the exception here (e.g. log the error, display an error message, etc.)
            print(f"Error occurred during assignment of self.text_widget: {e}")

        return self

    def set_palette(self, palette):
        """
        Applies the specified color palette to the search bar.
        """
        DEFAULT_BACKGROUND_COLOR = '#303030'
        DEFAULT_FOREGROUND_COLOR = '#505050'

        background_color = palette.get('secondary', DEFAULT_BACKGROUND_COLOR)
        foreground_color = palette.get('primary', DEFAULT_FOREGROUND_COLOR)

        if isinstance(palette, dict):
            try:
                self.configure(
                    background=background_color,
                    foreground=foreground_color,
                )
            except KeyError:
                # Handle case where palette dictionary does not contain expected keys
                self.configure(
                    background=DEFAULT_BACKGROUND_COLOR,
                    foreground=DEFAULT_FOREGROUND_COLOR,
                )
        else:
            raise ValueError("Invalid palette. Expected a dictionary.")

    def search(self, search_query: str, search_index: str, stopindex: str, backwards: bool = False):
        """
        Searches for the specified search_query in the text WidgetTest.

        Args:
            search_query (str): The query to search for.
            search_index (str): The starting index for the search.
            stopindex (str): The stopping index for the search.
            backwards (bool, optional): Whether to search backwards. Defaults to False.

        Returns:
            str: The result of the search.

        Raises:
            ValueError: If the search_query is not a string.
            ValueError: If the search_index is not a string.
            ValueError: If the stopindex is not a string.
            ValueError: If the backwards is not a boolean.
        """
        if not isinstance(search_query, str):
            raise ValueError("Invalid search_query. Expected a string.")
        if not isinstance(search_index, str):
            raise ValueError("Invalid search_index. Expected a string.")
        if not isinstance(stopindex, str):
            raise ValueError("Invalid stopindex. Expected a string.")
        if not isinstance(backwards, bool):
            raise ValueError("Invalid backwards. Expected a boolean.")

        try:
            return self.text_widget.search(search_query, search_index, stopindex, backwards)
        except Exception as e:
            print(f"Error occurred during search: {e}")

    def find_previous(self):
        """
        Finds the previous occurrence of the search query and highlights it.
        """
        self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex=tk.END,
                                                    backwards=True)
        if self.search_index:
            self.add_search_highlight(
                self.search_index,
                f"{self.search_index}+{len(self.search_query)}c",
            )
            self.search_index = self.text_widget.index(
                f"{self.search_index}+{len(self.search_query)}c"
            )
        else:
            self.search_index = "1.0"
            self._display_message("No more occurrences found.")

    @staticmethod
    def validate_input_parameters(tag, start, end):
        error_messages = []
        if not isinstance(tag, str):
            error_messages.append("Invalid tag. Expected a string for parameter 'tag'.")
        if not isinstance(start, str):
            error_messages.append("Invalid start index. Expected a string for parameter 'start'.")
        if not isinstance(end, str):
            error_messages.append("Invalid end index. Expected a string for parameter 'end'.")
        if error_messages:
            raise ValueError("\n".join(error_messages))
        return True

    def add_tag(self, text_widget, tag, start, end):
        """
        Adds a tag to the specified text WidgetTest from the start index to the end index.

        :param text_widget: The text WidgetTest to add the tag to.
        :param tag: The tag to be added.
        :param start: The start index.
        :param end: The end index.
        :return: The added tag if the operation was successful.
        :raises ValueError: If the tag, start index, or end index is invalid.
        """
        self.validate_input_parameters(tag, start, end)

        try:
            text_widget.tag_add(tag, start, end)
            return tag
        except (tk.TclError, ValueError) as e:
            raise ValueError(f"An error occurred: {e}") from e

    def undo(self):
        """
        Undoes the last action and displays a message indicating the success of the operation.
        """
        try:
            self.text_area.edit_undo()
            self._display_message("Undo successful")
            return True
        except tk.TclError:
            self._display_message("No more actions to undo")
            return False

    def redo(self):
        """
        Redoes the last action.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        try:
            if self.text_area.edit_modified():
                self.text_area.edit_redo()
                self.text_area.edit_reset()
                self._display_message("Redo successful")
                return True
            else:
                self._display_message("No action to redo")
                return False
        except Exception as e:
            logging.error(f"Error occurred during redo operation: {e}")
            return False

    def cut(self):
        """
        Cuts the selected text and returns a boolean indicating success.
        """
        try:
            if self.text_area.tag_ranges(tk.SEL):
                self.text_area.clipboard_clear()
                self.text_area.event_generate("<<Cut>>")
                self._display_message("Text cut successfully.")
                return True
            else:
                self._display_message("No text selected.")
                return False
        except Exception as e:
            logging.error(f"Error occurred during cut operation: {e}")
            return False

    def copy(self):
        """
        Copies the selected text.
        """
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        """
        Pastes the clipboard content.
        """
        try:
            if clipboard_content := self.master.clipboard_get():
                self.text_area.insert(tk.INSERT, clipboard_content)
                self._display_message("Paste successful")
            else:
                self._display_message("Clipboard is empty")
        except tk.TclError as e:
            self._display_message(f"Error occurred during paste operation: {e}")

    def setup_menu_bar(self, edit_menu):
        """
        Sets up the menu bar for the application.

        Args:
            edit_menu: The edit menu to add commands to.
        """
        if edit_menu is None:
            raise ValueError("edit_menu cannot be None.")

        if self.text_area is None:
            raise ValueError("Invalid text_area. Cannot set up menu bar without a valid text_area.")

        try:
            self._extracted_from_setup_menu_bar_15(edit_menu)
        except tk.TclError as e:
            # handle the specific exception
            logging.error(f"An error occurred: {e}")

    # TODO Rename this here and in `setup_menu_bar`
    def _extracted_from_setup_menu_bar_15(self, edit_menu):
        if hasattr(self.text_area, 'undo'):
            edit_menu.add_command(label="Undo", command=self.undo)
        else:
            raise AttributeError("text_area does not have 'undo' method")

        if hasattr(self.text_area, 'redo'):
            edit_menu.add_command(label="Redo", command=self.redo)
        else:
            raise AttributeError("text_area does not have 'redo' method")

        edit_menu.add_separator()

        if hasattr(self.text_area, 'cut'):
            edit_menu.add_command(label="Cut", command=self.cut)
        else:
            raise AttributeError("text_area does not have 'cut' method")

        if hasattr(self.text_area, 'copy'):
            edit_menu.add_command(label="Copy", command=self.copy)
        else:
            raise AttributeError("text_area does not have 'copy' method")

        if hasattr(self.text_area, 'paste'):
            edit_menu.add_command(label="Paste", command=self.paste)
        else:
            raise AttributeError("text_area does not have 'paste' method")


class SearchBarHandler:
    """
    A class to handle the search bar WidgetTest.
    
    Attributes:
        search_bar (tk.Entry): The search bar WidgetTest.
        search_query (str): The search query to be searched for.
        text_widget (tk.Text): The text widget to be searched.
        search_manager (SearchManager): The search manager object.
    """

    def __init__(self, search_bar, search_query):
        self.search_bar = search_bar
        self.search_query = search_query
        self.text_widget = None
        self.search_manager = None

    def set_palette(self, palette):
        """
        Applies the specified color palette to the search bar.
        """
        if not isinstance(palette, dict):
            raise ValueError("Palette must be a dictionary.")
        if 'secondary' not in palette or 'primary' not in palette:
            raise ValueError("Palette must contain 'secondary' and 'primary' keys.")
        self.search_bar.configure(bg=palette['secondary'], fg=palette['primary'])

    def set_text_widget(self, text_widget):
        """
        Sets the text WidgetTest to be searched.
        """
        if isinstance(text_widget, tk.Text):
            self.text_widget = text_widget
        else:
            raise ValueError("Invalid text_widget parameter. Expected tk.Text object.")

    def find_previous(self):
        """
        Finds the previous occurrence of the search query and highlights it.
        """
        self.search_manager.find_previous()

    def find_next(self):
        """
        Finds the next occurrence of the search query and highlights it.
        """
        self.search_manager.find_next()

    def clear_search_highlights(self):
        """
        Clears all search result highlights.
        """
        self.search_manager.clear_search_highlights()

    def set_search_query(self, search_query: str):
        """
        Sets the search query to be searched for.
        """
        self.search_query = search_query

    def get_search_query(self):
        """
        Returns the current search query.
        """
        return self.search_query

    def set_search_index(self, search_index: int):
        """
        Sets the current search index.
        """
        self.search_manager.set_search_index(search_index)

    def get_search_index(self):
        """
        Returns the current search index.
        """
        return self.search_manager.get_search_index()

    def perform_search(self):
        """
        Performs the search query.
        """
        self.search_manager.perform_search()

    def close_search_bar(self):
        """
        Closes the search bar.
        """
        self.search_manager.close_search_bar()

    def hide_search_bar(self):
        """
        Hides the search bar.
        """
        self.search_manager.hide_search_bar()

    def show_search_bar(self):
        """
        Shows the search bar.
        """
        self.search_manager.show_search_bar()
