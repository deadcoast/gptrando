import logging
import re
import tkinter
import tkinter as tk
from collections import namedtuple
from tkinter import font

from gptrando.flare_widget import FlareTextExtension
from gptrando.inline_search_manager import InlineSearchManager

Palette = namedtuple('Palette', ['secondary', 'primary', 'tertiary'])


class PaletteManager:
    def __init__(self, text_widget):
        assert text_widget is not None and isinstance(text_widget,
                                                      tk.Text), ("text_widget must be an instance of ExpectedClass "
                                                                 "and cannot be None")
        self._palette = Palette('#303030', '#505050', '#202020')
        self.text_widget = text_widget

    class PaletteManager:
        color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')

        def validate_color(self, color):
            """
            Validates a color value to ensure it is a valid hex color code.
            """
            if color is None:
                raise ValueError("color cannot be None")
            if not isinstance(color, str):
                raise TypeError("color must be a string")
            if not self.color_regex.match(color):
                raise ValueError(f"Invalid color value: {color}. Please provide a valid hex color code starting with "
                                 f"'#' followed by 3 or 6 hexadecimal digits.")

    def apply_palette(self):
        """
        Applies the specified color palette to the Flare WidgetTest.
        """
        if self.text_widget is None:
            raise ValueError("text_widget cannot be None")
        if not self._palette:
            return False
        try:
            self.text_widget.configure(
                background=self._palette.secondary,
                foreground=self._palette.primary,
                insertbackground=self._palette.tertiary
            )
        except ValueError:
            logging.error("Error applying Palette to Text Widget", exc_info=True)
        else:
            return True

    def update_palette(self, palette):
        """
        Updates the color palette.
        """
        required_attributes = ['secondary', 'primary', 'tertiary']
        if not all(hasattr(palette, attr) for attr in required_attributes):
            return False
        if not isinstance(palette, Palette):
            raise ValueError("palette must be an instance of the 'Palette' class")
        self._palette = palette
        self.apply_palette()


color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')


class ThemeManager:
    """
    A class that manages the themes for the text editor.
    """

    def __init__(self):
        self.handle_exit = None
        self.handle_preview = None
        self.theme_manager = None
        self.text_extension = None
        self.handle_export_code = None
        self.handle_run_code = None
        self.handle_decrease_indentation = None
        self.handle_increase_indentation = None
        self.handle_merge_lines = None
        self.handle_toggle_comment = None
        self.handle_wrap_text = None
        self.handle_number_lines = None
        self.handle_remove_duplicates = None
        self.handle_format_code = None
        self.handle_convert_to_uppercase = None
        self.handle_convert_to_lowercase = None
        self.handle_trim_whitespace = None
        self.handle_sort_lines = None
        self.handle_convert_case = None
        self.handle_uncomment = None
        self.handle_duplicate = None
        self.handle_comment = None
        self.handle_justify = None
        self.handle_align_center = None
        self.handle_align_right = None
        self.handle_align_left = None
        self.handle_underline = None
        self.handle_italic = None
        self.handle_bold = None
        self.handle_replace = None
        self.handle_print = None
        self.handle_new = None
        self.handle_quit = None
        self.handle_open = None
        self.handle_save = None
        self.handle_search_previous = None
        self.handle_search_next = None
        self.handle_find = None
        self.handle_redo = None
        self.handle_undo = None
        self.handle_select_all = None
        self.handle_cut = None
        self.handle_paste = None
        self.handle_copy = None
        self.handle_mouse_click = None
        self.handle_right_click = None
        self.handle_key_press = None
        self.inline_search_manager = InlineSearchManager()
        self.KEY_COMBINATION = "<Control-f>"
        self.hide_search_bar = self.inline_search_manager.hide_search_bar
        self.find_previous = self.inline_search_manager.find_previous
        self.find_next = self.inline_search_manager.find_next
        self.perform_search = self.inline_search_manager.perform_complex_search
        self.prompt_search_query = self.inline_search_manager.prompt_search_query
        self.search_index = 1.0
        self.search_highlights = []
        self.search_close_button = tk.Button()
        self.search_prev_button = tk.Button()
        self.search_entry = tk.Entry()
        self.text_widget = tk.Text()
        self.search_bar = tk.Frame()
        self.text_widget = tk.Text()
        self.search_next_button = tk.Button()
        self.text_widget = tk.Text()
        self.init()
        self.setup_menu_bar()
        self.setup_text_area()
        self.setup_bindings()
        self.setup_search_bar()
        self.setup_inline_search_manager()

        self.load_snippets()

        self.text_widget.focus_set()

        self.mainloop()

        self.save_snippets()

        self.close()

        self.destroy()

        self.quit()

    def setup_search_bar(self):
        """
        Creates the search bar UI elements and integrates them into the editor.
        """
        self.search_bar = tk.Frame(self.text_widget)
        self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.search_entry = tk.Entry(self.search_bar, font=font.Font(family='Courier New', size=12))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.search_entry.bind("<Return>", self.perform_search)

        self.search_next_button = tk.Button(self.search_bar, text="Next", command=self.find_next)
        self.search_next_button.pack(side=tk.LEFT, padx=5)

        self.search_prev_button = tk.Button(self.search_bar, text="Previous", command=self.find_previous)
        self.search_prev_button.pack(side=tk.LEFT, padx=5)

        self.search_close_button = tk.Button(self.search_bar, text="Close", command=self.hide_search_bar)
        self.search_close_button.pack(side=tk.LEFT, padx=5)

    def setup_bindings(self):
        """
        Binds keyboard shortcuts for invoking the inline search functionality.
        """
        try:
            if self.prompt_search_query is not None:
                self.text_widget.bind_all("<Control-f>", self.prompt_search_query)
                self.text_widget.bind_all("<Control-g>", self.display_search_feedback)
        except tkinter.TclError as e:
            logging.error(f"Error binding keyboard shortcut: {e}")
            logging.exception("Exception occurred during binding:")

    def KEY_COMBINATION(self):
        """
        Binds the keyboard shortcut for invoking the inline search functionality.
        """
        try:
            if self.KEY_COMBINATION not in self.text_widget.bindtags():
                self.text_widget.bind(self.KEY_COMBINATION, self.prompt_search_query)
        except Exception as e:
            logging.exception(f"Error occurred during binding: {e}")
            raise e

    def display_search_feedback(self, event):
        """
        Displays feedback to the user when the search functionality is invoked.
        """
        logging.info("Search functionality invoked")  # Suggestion 1
        try:
            return self.search_button_depressed(event)
        except Exception as e:
            logging.error(f"Error occurred during search functionality: {e}")  # Suggestion 2
            # Handle the exception appropriately, e.g. display an error message to the user

        self.clear_search_feedback()  # Suggestion 7

    def search_button_depressed(self, event):
        # Add code to display a message or change the UI to indicate search functionality invocation
        event_type = event.type  # Suggestion 5
        if event_type == "click":
            print("Clicked on search button")
        elif event_type == "search":
            print("Search functionality invoked")
        else:
            print("Unknown event type")

        # Update UI to highlight the searched text
        self.highlight_searched_text("searched_text")
        self.search_index = "1.0"
        self.clear_search_highlights()
        self.search_index = "1.0"
        self.clear_search_highlights()
        self.search_index = "1.0"
        self.clear_search_highlights()
        return "Search functionality invoked successfully."  # Suggestion 3

    def highlight_searched_text(self, search_text):
        """
        Highlights the searched text in the text editor.
        :param search_text: The text to be searched and highlighted.
        :return: True if the text was found and highlighted, False otherwise.
        """
        try:
            self.clear_search_highlights()  # Clear previous search highlights
            searched_text = search_text
            text_content = self.text_widget.get("1.0", "end-1c")
            start_index = text_content.find(searched_text)
            while start_index >= 0:
                end_index = start_index + len(searched_text)
                self.text_widget.tag_add("search_highlight", f"1.0 + {start_index}c", f"1.0 + {end_index}c")
                start_index = text_content.find(searched_text, end_index)
            self.text_widget.tag_config("search_highlight", background="yellow")
            return True
        except Exception as e:
            logging.error(f"Error occurred during search and highlight process: {e}")
            return False

    def clear_search_feedback(self):
        """
        Clears the search feedback by removing any search highlights.
        """
        # Add code to clear the search feedback
        pass

    def setup_menu_bar(self):
        pass

    def init(self):
        pass

    def setup_inline_search_manager(self):
        pass

    def load_snippets(self):
        pass

    def save_snippets(self):
        pass

    def close(self):
        pass

    def quit(self):
        pass

    def mainloop(self):
        pass

    def destroy(self):
        # Clean up resources or close connections here
        # ...
        self.text_widget.destroy()
        self.inline_search_manager.destroy()
        self.text_extension.destroy()
        self.theme_manager.destroy()

    def setup_text_area(self):
        """
        Set up the text area WidgetTest.
        """
        self.text_widget = tk.Text(font=font.Font(family='Courier New', size=12))
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        initial_content = "Enter your text here..."
        self.text_widget.insert(tkinter.END, initial_content)
        self.text_widget.bind("<Key>", self.handle_key_press)
        self.text_widget.bind("<Button-1>", self.handle_mouse_click)
        self.text_widget.bind("<Button-3>", self.handle_right_click)
        self.text_widget.bind("<Control-c>", self.handle_copy)
        self.text_widget.bind("<Control-x>", self.handle_cut)
        self.text_widget.bind("<Control-v>", self.handle_paste)
        self.text_widget.bind("<Control-a>", self.handle_select_all)
        self.text_widget.bind("<Control-z>", self.handle_undo)
        self.text_widget.bind("<Control-y>", self.handle_redo)
        self.text_widget.bind("<Control-f>", self.handle_find)
        self.text_widget.bind("<Control-g>", self.handle_search_next)
        self.text_widget.bind("<Shift-Control-g>", self.handle_search_previous)
        self.text_widget.bind("<Control-s>", self.handle_save)
        self.text_widget.bind("<Control-o>", self.handle_open)
        self.text_widget.bind("<Control-q>", self.handle_quit)
        self.text_widget.bind("<Control-n>", self.handle_new)
        self.text_widget.bind("<Control-p>", self.handle_print)
        self.text_widget.bind("<Control-h>", self.handle_replace)
        self.text_widget.bind("<Control-b>", self.handle_bold)
        self.text_widget.bind("<Control-i>", self.handle_italic)
        self.text_widget.bind("<Control-u>", self.handle_underline)
        self.text_widget.bind("<Control-l>", self.handle_align_left)
        self.text_widget.bind("<Control-r>", self.handle_align_right)
        self.text_widget.bind("<Control-e>", self.handle_align_center)
        self.text_widget.bind("<Control-j>", self.handle_justify)
        self.text_widget.bind("<Control-Shift-/>", self.handle_comment)
        self.text_widget.bind("<Control-/>", self.handle_uncomment)
        self.text_widget.bind("<Control-Shift-d>", self.handle_duplicate)
        self.text_widget.bind("<Control-Shift-c>", self.handle_convert_case)
        self.text_widget.bind("<Control-Shift-s>", self.handle_sort_lines)
        self.text_widget.bind("<Control-Shift-t>", self.handle_trim_whitespace)
        self.text_widget.bind("<Control-Shift-l>", self.handle_convert_to_lowercase)
        self.text_widget.bind("<Control-Shift-u>", self.handle_convert_to_uppercase)
        self.text_widget.bind("<Control-Shift-f>", self.handle_format_code)
        self.text_widget.bind("<Control-Shift-o>", self.handle_remove_duplicates)
        self.text_widget.bind("<Control-Shift-n>", self.handle_number_lines)
        self.text_widget.bind("<Control-Shift-w>", self.handle_wrap_text)
        self.text_widget.bind("<Control-Shift-a>", self.handle_toggle_comment)
        self.text_widget.bind("<Control-Shift-m>", self.handle_merge_lines)
        self.text_widget.bind("<Control-Shift-i>", self.handle_increase_indentation)
        self.text_widget.bind("<Control-Shift-d>", self.handle_decrease_indentation)
        self.text_widget.bind("<Control-Shift-r>", self.handle_run_code)
        self.text_widget.bind("<Control-Shift-e>", self.handle_export_code)
        self.text_widget.bind("<Control-Shift-p>", self.handle_preview)
        self.text_widget.bind("<Control-Shift-q>", self.handle_exit)
        self.text_widget.bind("<Control-Shift-s>", self.handle_save_as)
        self.text_widget.bind("<Control-Shift-h>", self.handle_replace_all)
        self.text_widget.bind("<Control-Shift-b>", self.handle_toggle_bold)
        self.text_widget.bind("<Control-Shift-i>", self.handle_toggle_italic)
        self.text_widget.bind("<Control-Shift-u>", self.handle_toggle_underline)
        self.text_widget.bind("<Control-Shift-l>", self.handle_toggle_align_left)
        self.text_widget.bind("<Control-Shift-r>", self.handle_toggle_align_right)
        self.text_widget.bind("<Control-Shift-e>", self.handle_toggle_align_center)
        self.text_widget.bind("<Control-Shift-j>", self.handle_toggle_justify)
        self.text_widget.bind("<Control-Shift-/>", self.handle_toggle_comment)
        self.text_widget.bind("<Control-Shift-/>", self.handle_toggle_comment)

    def clear_search_highlights(self):
        """
        Removes the 'search_highlight' tag from all text in the text_widget if it exists.
        Logs the success or failure of the operation.
        Resets the search_index to 1.0 after clearing the highlights.
        Returns a boolean value indicating whether the operation was successful or not.
        """
        try:
            if "search_highlight" in self.text_widget.tag_names():
                self.text_widget.tag_remove("search_highlight", "1.0", "end")
                self.search_index = "1.0"
                logging.info("Search highlights cleared successfully.")
                return True
            else:
                logging.info("No search highlights found.")
                return False
        except Exception as e:
            logging.error(f"Error occurred while clearing search highlights: {e}")
            return False


def padding(self, PADDING_X=None, PADDING_Y=None):
    """
    Adds padding to the search bar.
    :param self:
    :param PADDING_X:
    :param PADDING_Y:
    :return:
    """
    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=PADDING_X, pady=PADDING_Y)


def setup_inline_search_manager(self):
    """
    Initializes the InlineSearchManager.
    """
    self.inline_search_manager = InlineSearchManager()

    self.inline_search_manager.init(self.text_widget)

    self.inline_search_manager.setup_bindings()

    self.setop_top_inline_search_manager()
    self.hide_search_bar = self.inline_search_manager.hide_search_bar
    self.find_previous = self.inline_search_manager.find_previous
    self.find_next = self.inline_search_manager.find_next
    self.perform_complex_search = self.inline_search_manager.perform_complex_search

    self.prompt_search_query = self.inline_search_manager.prompt_search_query

    self.setop_top_inline_search_manager()


def setop_top_inline_search_manager(self):
    self.inline_search_manager.pack(side=tk.TOP, fill=tk.X, expand=True)

    self.inline_search_manager.apply_palette_and_init()

    self.inline_search_manager.show_search_bar()


def load_snippets(self):
    pass


def save_snippets(self):
    pass


def close(self):
    pass


def quit(self):
    pass


def mainloop(self):
    pass


def destroy(self):
    pass


def setup_search_bar(self):
    """
    Initializes the search bar.
    """
    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    self.search_bar.bind("<Return>", self.perform_complex_search)
    self.search_bar.focus_set(
        self.perform_complex_search
    )

    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    self.search_bar.bind("<Return>", self.perform_complex_search)
    self.search_bar.focus_set(
        self.perform_complex_search
    )

    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    self.search_bar.bind("<Return>", self.perform_complex_search)
    self.search_bar.focus_set(
        self.perform_complex_search
    ),

    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5),
    self.search_bar.bind("<Return>", self.perform_complex_search),
    self.search_bar.focus_set(
        self.perform_complex_search
    ),

    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5),
    self.search_bar.bind("<Return>", self.perform_complex_search),
    self.search_bar.focus_set(
        self.perform_complex_search
    ),

    self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5),
    self.search_bar.bind("<Return>", self.perform_complex_search),

    self.search_bar.focus_set(
        self.perform_complex_search
    ),


def setup_snippets(self):
    """
    Initializes the FlareTextExtension.
    """
    self.snippets = FlareTextExtension(master=self, x_focus_val=1)
    return self.snippets


def setup_menu_bar(self):
    self.menu_bar = tk.Menu(self.master)
    self.master.config(menu=self.menu_bar)

    self.file_menu = tk.Menu(self.menu_bar)
    self.menu_bar.add_cascade(label="File", menu=self.file_menu)
    self.file_menu.add_command(label="Open", command=self.open_file)
    self.file_menu.add_command(label="Save", command=self.save_file)
    self.file_menu.add_separator()
    self.file_menu.add_command(label="Exit", command=self.master.quit)

    self.edit_menu = tk.Menu(self.menu_bar)
    self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
    self.edit_menu.add_command(label="Find", command=self.find_text)
    self.edit_menu.add_command(label="Find Next", command=self.bar_find_next)
    self.edit_menu.add_command(label="Find Previous", command=self.find_previous)
    self.edit_menu.add_separator()
    self.edit_menu.add_command(label="Copy", command=self.copy_text)
    self.edit_menu.add_command(label="Cut", command=self.cut_text)
    self.edit_menu.add_command(label="Paste", command=self.paste_text)
    self.edit_menu.add_separator()
    self.edit_menu.add_command(label="Select All", command=self.select_all)

    self.palette_menu = tk.Menu(self.menu_bar)
    self.menu_bar.add_cascade(label="Palette", menu=self.palette_menu)
    self.palette_menu.add_command(label="Default", command=self.set_default_palette)
    self.palette_menu.add_command(label="Dark", command=self.set_dark_palette)
    self.palette_menu.add_command(label="Light", command=self.set_light_palette)

    self.theme_menu = tk.Menu(self.menu_bar)
    self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)
    self.theme_menu.add_command(label="Light", command=self.set_light_theme)
    self.theme_menu.add_command(label="Dark", command=self.set_dark_theme)
    self.theme_menu.add_command(label="Custom", command=self.set_custom_theme)

    self.menu_bar.add_command(label="Help", command=self.show_help)

    self.menu_bar.add_command(label="About", command=self.show_about)

    self.menu_bar.add_command(label="Quit", command=self.master.quit)


def setup_text_formatting(self):
    self.theme_manager = ThemeManager()
    self.text_area = tkinter.Text()
    self.text_area.pack(fill=tk.BOTH, expand=True)
    self.setup_bindings()


def init(self):
    pass


def setup_text_area(self):
    pass


def setup_inline_search_manager(self):
    pass


def load_snippets(self):
    pass


def mainloop(self):
    pass


def save_snippets(self):
    pass


def close(self):
    pass


def destroy(self):
    pass


def quit(self):
    pass


SEARCH_HIGHLIGHT_TAG = "search_highlight"


def clear_search_highlights(self, START_INDEX=None, END_INDEX=None):
    """
    Removes all search result highlights from the text WidgetTest.
    :param START_INDEX:
    :param END_INDEX:
    """
    try:
        # Clear the list of search highlights
        self.search_highlights.clear()

        # Remove the search highlight tag from the text WidgetTest
        self.text_widget.tag_remove(self.SEARCH_HIGHLIGHT_TAG, START_INDEX, END_INDEX)
    except ValueError as e:
        # Log the error details
        logging.error("Error removing search highlight", exc_info=True)
        return False
    except tk.TclError as e:
        # Log the error details
        logging.error("Error removing search highlight", exc_info=True)
        return False
    return True


def add_search_highlight(self, search_index, param):
    """
    Adds a highlight to the search results.
    """
    if search_index is None or param is None:
        return False
    try:
        self.text_widget.add_tag("search_highlight", search_index, param)
    except Exception as e:
        logging.error("Error adding search highlight", exc_info=True)
    else:
        try:
            self.search_highlights.append((search_index, param))
        except ValueError as e:
            logging.error("Error Searching with Highlight", exc_info=True)
            return False
        else:
            return True


def hide_search_bar(self):
    """
    Hides the search bar and clears the search highlights.
    """
    self.search_bar.pack_forget()
    self.clear_search_highlights()

    def __init__(self):
        self.text_widget = tkinter.Text()
        self.search_bar = tkinter.Entry()
        self.search_index = 1.0
        self.search_highlights = []
        self.search_query = ""
        self.setup_search_bar()
        self.setup_text_formatting()
        self.setup_bindings()
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.master.mainloop()
        self.text_area = tkinter.Text()
        self.theme_manager = ThemeManager()
        self.inline_search_manager = InlineSearchManager()
        self.flare_text_extension = FlareTextExtension()
        self.setup_menu_bar()
        self.setup_bindings()
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.parent = self.parent or self.master
        self.parent.title("HEAT UP Editor")
        self.palette_manager = PaletteManager(text_widget=self.text_area)
        self.theme_manager = ThemeManager()
        self.text_area = tkinter.Text()
        self.theme_manager = ThemeManager()
        self.text_area = tkinter.Text()
        self.text_area.pack(fill=tk.BOTH, expand=True)
