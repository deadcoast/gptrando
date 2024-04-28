
import tkinter as tk
from tkinter import font


class InlineSearchManager:
    def __init__(self):
        self.find_next = self.find_next
        self.find_previous = self.find_previous
        self.perform_search = self.perform_search
        self.add_search_highlight = self.add_search_highlight
        self.clear_search_highlights = self.clear_search_highlights
        self.hide_search_bar = self.hide_search_bar
        self.prompt_search_query = self.prompt_search_query
        self.setup_search_bar = self.setup_search_bar
        self.setup_bindings = self.setup_bindings
        self.search_query = ""
        self.search_index = "1.0"
        self.search_highlights = []

    def hide_search_bar(self):
        self.search_bar.pack_forget()
        self.clear_search_highlights()

    def prompt_search_query(self, event=None):
        self.search_bar.pack(side=tk.TOP, fill=tk.X)
        self.search_bar.focus_set()

    def find_next(self):
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

    def find_previous(self):
        if self.search_query:
            self.search_index = self.text_widget.search(self.search_query, self.search_index, stopindex="1.0",
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
                self.search_index = tk.END
                self._display_message("No more occurrences found.")

    def perform_search(self, event=None):
        self.search_query = self.search_bar.get()
        self.search_index = "1.0"
        self.clear_search_highlights()
        self.find_next()

    def _display_message(self, message):
        self.status_bar.config(text=message)

    def add_search_highlight(self, start, end):
        self.text_widget.tag_add("search_highlight", start, end)
        self.search_highlights.append((start, end))

    def clear_search_highlights(self):
        for start, end in self.search_highlights:
            self.text_widget.tag_remove("search_highlight", start, end)
        self.search_highlights = []

    def setup_search_bar(self):
        self.search_bar = tk.Entry(self, font=font.Font(family='Courier New', size=12), width=30)
        self.search_bar.pack(side=tk.TOP, fill=tk.X)
        self.search_bar.bind("<Return>", self.perform_search)

    def setup_bindings(self):
        self.text_widget.bind("<Control-f>", self.prompt_search_query)
        self.text_widget.bind("<Control-n>", self.find_next)
        self.text_widget.bind("<Control-p>", self.find_previous)
        self.text_widget.bind("<Control-Return>", self.perform_search)

        self.text_widget.bind("<Control-s>", self.save_file)
        self.text_widget.bind("<Control-o>", self.open_file)

        self.text_widget.bind("<Control-q>", self.close)

    def close(self, event=None):
        self.master.destroy()

    def save_file(self, event=None):
        self.master.save_file()

    def open_file(self, event=None):
        self.master.open_file()

    def apply_palette(self):
        self.text_widget.configure(
            background=self.palette.get('secondary', '#303030'),
            foreground=self.palette.get('primary', '#505050'),
            insertbackground=self.palette.get('tertiary', '#202020')
        )

        self.search_bar.configure(
            background=self.palette.get('secondary', '#303030'),
            foreground=self.palette.get('primary', '#505050'),
            insertbackground=self.palette.get('tertiary', '#202020')
        )

        self.status_bar.configure(
            background=self.palette.get('secondary', '#303030'),
            foreground=self.palette.get('primary', '#505050')
        )

        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.search_bar.pack(side=tk.TOP, fill=tk.X)

        self.text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.apply_palette_and_init()

    def init(self, text_widget):
        self.text_widget = text_widget

        self.search_query = ""
        self.search_index = "1.0"
        self.search_highlights = []
        self.setup_search_bar()
        self.setup_bindings()

        self.apply_palette()

        self.apply_palette_and_init()
        self._display_message("Ready")

        self.text_widget.focus_set()

        self.master.protocol("WM_DELETE_WINDOW", self.close)

        self.master.mainloop()

    def apply_palette_and_init(self):
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.text_widget.tag_configure(
            "search_highlight", background=self.palette.get('tertiary', '#202020')
        )
        self.apply_palette()

    def setup_menu_bar(self):
        pass

    def setup_status_bar(self):
        pass

    def setup_text_formatting(self):
        pass


    """
    Provides advanced inline search functionality for the HEAT UP editor.
    """

    def pack(self, side, fill, expand):


    def hide_search_bar(self):
        """
        Hides the search bar.
        """
        self.search_bar.pack_forget()
        self.clear_search_highlights()

    def show_search_bar(self):
        """
        Shows the search bar.
        """
        self.search_bar.pack(side=tk.TOP, fill=tk.X)
        self.search_bar.focus_set()

    def prompt_search_query(self, event):
        """
        Prompts the user to enter a search query.
        """
        self.show_search_bar()
        self.search_bar.delete(0, tk.END)

    def find_next(self):
        pass

    def find_previous(self):
        pass

    def perform_search(self, event):

        pass


def init(self, text_widget):
    self.text_widget = text_widget


self.search_query = ""
self.search_index = "1.0"
self.search_highlights = []
self.setup_search_bar()
self.setup_bindings()


def setup_search_bar(self):
    """
    Configures the search bar widget.
    """
    self.search_bar = tk.Entry(self, font=font.Font(family='Courier New', size=12), width=30)
    self.search_bar.pack(side=tk.TOP, fill=tk.X)
    self.search_bar.bind("<Return>", self.perform_search)


def perform_search(self, event=None):
    """
    Performs the inline search based on the user's query.
    """
    self.search_query = self.search_bar.get()
    self.search_index = "1.0"
    self.clear_search_highlights()
    self.find_next()