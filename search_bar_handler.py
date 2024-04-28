
import tkinter as tk
from tkinter import font


class SearchBar(tk.Entry):  # Custom search bar widget
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
            '<Control-n>': self.find_next,
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
            '<F3>': self.find_next,
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
        self.find_next()

    def find_next(self):
        """
        Finds the next occurrence of the search query and highlights it.
        """
        if self.search_query:
            self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex=tk.END)
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
        