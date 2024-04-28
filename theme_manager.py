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
        Applies the specified color palette to the Flare widget.
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
        self.hide_search_bar = None
        self.find_previous = None
        self.find_next = None
        self.perform_search = None
        self.inline_search_manager = InlineSearchManager()
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
        self.text_widget.bind("<Control-f>", self.prompt_search_query)

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
        pass


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

        self.inline_search_manager.pack(side=tk.TOP, fill=tk.X, expand=True)

        self.inline_search_manager.apply_palette_and_init()

        self.inline_search_manager.show_search_bar()

        self.hide_search_bar = self.inline_search_manager.hide_search_bar
        self.find_previous = self.inline_search_manager.find_previous
        self.find_next = self.inline_search_manager.find_next
        self.perform_search = self.inline_search_manager.perform_search

        self.prompt_search_query = self.inline_search_manager.prompt_search_query

        self.inline_search_manager.pack(side=tk.TOP, fill=tk.X, expand=True)

        self.inline_search_manager.apply_palette_and_init()

        self.inline_search_manager.show_search_bar()

        self.hide_search_bar = self.inline_search_manager.hide_search_bar
        self.find_previous = self.inline_search_manager.find_previous
        self.find_next = self.inline_search_manager.find_next
        self.perform_search = self.inline_search_manager.perform_search

        self.prompt_search_query = self.inline_search_manager.prompt_search_query

        self.inline_search_manager.pack(side=tk.TOP, fill=tk.X, expand=True)

        self.inline_search_manager.apply_palette_and_init()

        self.inline_search_manager.show_search_bar()

        self.hide_search_bar = self.inline_search_manager.hide_search_bar
        self.find_previous = self.inline_search_manager.find_previous
        self.find_next = self.inline_search_manager.find_next
        self.perform_search = self.inline_search_manager.perform_search

        self.prompt_search_query = self.inline_search_manager.prompt_search_query

        self.inline_search_manager.pack(side=tk.TOP, fill=tk.X, expand=True)

        self.inline_search_manager.apply_palette_and_init()

        self.inline_search_manager.show_search_bar()

        self.hide_search_bar = self.inline_search_manager.hide_search_bar
        self.find_previous = self.inline_search_manager.find_previous
        self.find_next = self.inline_search_manager.find_next
        self.perform_search = self.inline_search_manager.perform_search

        self.prompt_search_query = self.inline_search_manager.prompt_search_query

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

        self.search_bar.bind("<Return>", self.perform_search)

        self.search_bar.focus_set(
            self.perform_search
        )

        self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.search_bar.bind("<Return>", self.perform_search)

        self.search_bar.focus_set(
            self.perform_search
        )

        self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.search_bar.bind("<Return>", self.perform_search)

        self.search_bar.focus_set(
            self.perform_search
        ),

        self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5),

        self.search_bar.bind("<Return>", self.perform_search),

        self.search_bar.focus_set(
            self.perform_search
        ),

        self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5),

        self.search_bar.bind("<Return>", self.perform_search),

        self.search_bar.focus_set(
            self.perform_search
        ),

        self.search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5),

        self.search_bar.bind("<Return>", self.perform_search),

        self.search_bar.focus_set(
            self.perform_search
        ),

    def setup_snippets(self):
        """
        Initializes the FlareTextExtension.
        """
        self.snippets = FlareTextExtension(),

    def setup_text_area(self):
        """
        Sets up the text widget.
        """
        self.text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True),

    def setup_menu_bar(self):
        pass

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
,
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
        Sets the content of the Flare widget.
        """
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', content)

    def get_content(self):
        """
        Retrieves the current content of the Flare widget.
        """
        return self.text_widget.get('1.0', tk.END).strip()

    def setup_menu_bar(self):
        pass

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
        Removes all search result highlights from the text widget.
        :param START_INDEX:
        :param END_INDEX:
        """
        try:
            # Clear the list of search highlights
            self.search_highlights.clear()

            # Remove the search highlight tag from the text widget
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
