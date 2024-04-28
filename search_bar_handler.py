
import tkinter as tk
from tkinter import font

from gptrando.theme_manager import ThemeManager
from gptrando.inline_search_manager import InlineSearchManager
from gptrando.flare_text_extension import FlareTextExtension
from gptrando.palette_manager import PaletteManager

from .theme_manager import ThemeManager
from .inline_search_manager import InlineSearchManager
from .FlareTextExtension import FlareTextExtension
from .palette_manager import PaletteManager


class NoMoreOccurrencesException:
    pass

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    def __call__(self):
        return self.message


class SearchBar(tk.Entry):  # Custom search bar widget
    """
    A custom search bar widget that can be used to search for text in a text widget.

    Args:
        master: The parent widget.
        **kwargs: Additional keyword arguments to pass to the parent widget.

    Attributes:
        search_bar: The search bar widget.
        toggle_formatting: A method that can be used to toggle text formatting.
        close_search_bar: A method that can be used to close the search bar.
        close: A method that can be used to close the search bar.
        search_index: The index of the current search query.
        search_highlights: A list of tuples containing the start and end indices of search highlights.
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search_bar = tk.Entry(self, font=font.Font(family='Courier New', size=12), width=30)
        self.toggle_formatting = self.toggle_formatting
        self.close_search_bar = self.pack_forget
        self.close = self.close_search_bar
        self.search_index = 1.0
        self.search_highlights = []
        self.text_widget = self.set_text_widget
        self.search_query = ""
        self.setup_search_bar()
        self.setup_text_formatting()
        self.setup_bindings()

        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.master.mainloop()

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.theme_manager = ThemeManager(self.palette_manager)
        self.inline_search_manager = InlineSearchManager(self.text_area)
        self.flare_text_extension = FlareTextExtension(self.text_area)

        self.setup_menu_bar()
        self.setup_bindings()

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.parent = self.parent or self.master  # Use master as parent if not specified
        self.parent.title("HEAT UP Editor")
        self.palette_manager = PaletteManager()
        self.theme_manager = ThemeManager(self.palette_manager)

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.flare_text_extension = FlareTextExtension(self.text_area)
        self.inline_search_manager = InlineSearchManager(self.text_area)

        self._display_message("Ready")

    def setup_menu_bar(self):
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.parent.quit)

        edit_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Edit", menu=edit_menu)
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
        Configures the search bar widget.
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
        Sets the text widget to be searched.
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
            return self._extracted_from_bar_find_next_(new_search_index)
        if wrapped_search_index := self.text_widget.search(
            self.search_query, "1.0", stopindex=self.search_index, backwards=True
        ):
            return self._extracted_from_bar_find_next_(wrapped_search_index)
        else:
            raise NoMoreOccurrencesException("No more occurrences found.")

    # TODO Rename this here and in `bar_find_next`
    def _extracted_from_bar_find_next_(self, arg0):
        end_index = self.text_widget.index(
            f"{arg0}+{self.text_widget.index(arg0, count=len(self.search_query))}c"
        )
        self.add_search_highlight(arg0, end_index)
        return arg0

    def add_search_highlight(self, start, end):
        """
        Adds a search result highlight to the text widget.
        """
        self.text_widget.tag_add("search_highlight", start, end)
        self.search_highlights.append((start, end))

    def set_text_widget(self, text_widget):
        """
        Sets the text widget to be searched.
        """
        self.text_widget = text_widget

    def set_palette(self, palette):
        """
        Applies the specified color palette to the search bar.
        """
        self.configure(
            background=palette.get('secondary', '#303030'),
            foreground=palette.get('primary', '#505050'),
        )

    def find_previous(self):
        """
        Finds the previous occurrence of the search query and highlights it.
        """
        self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex=tk.END, backwards=True)
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

    def tag_add(self, param, start, end):
        pass
        