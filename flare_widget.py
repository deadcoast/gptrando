import logging
import tkinter as tk
from collections import defaultdict
from tkinter import font

import main

TAG_BOLD = 'bold'
TAG_ITALIC = 'italic'


class FlareTextExtension(tk.Frame):
    """
    An advanced Flare widget that provides a rich set of features for content display and interaction within the HEAT UP editor.
    """

    def __init__(
            self,
            master: tk.Misc | None = None,
            cnf=None,
            *,
            x_focus_val: main.TakeFocusValue = 1):
        """
        Initialize the FlareTextExtension object.

        Args:
            master (tk.Misc | None): The master widget.
            cnf: The configuration options.
            x_focus_val (TakeFocusValue): The x focus value.
        """
        if cnf is None:
            cnf = {}
        super().__init__(master, **cnf)
        self.x_focus_val = x_focus_val
        self.text_widget = None
        self.parent = None
        self.palette = None
        self.bold_font = font.Font(family='Courier New', size=12, weight='bold')
        self.italic_font = font.Font(family='Courier New', size=12, slant='italic')

    def init(self, parent, content='', palette=None, font_family='Courier New', font_size=12, **kwargs):
        """
        Initialize the object.

        Args:
            parent: The parent object.
            content: The content of the object.
            palette: The palette of the object.
            font_family: The font family to use.
            font_size: The font size to use.
            **kwargs: Additional keyword arguments.
        """
        super().init(parent, **kwargs)

        self.set_parent(parent)
        self.set_palette(palette)
        self.create_text_widget(font_family, font_size, **kwargs)
        self.place_text_widget()

        try:
            self.text_widget.grid(row=0, column=0, sticky="nsew")
        except tk.TclError as e:
            logging.error(f'Error creating or placing text widget: {e}')

    def set_parent(self, parent):
        """
        Set the parent object.

        Args:
            parent: The parent object.
        """
        self.parent = parent

    def set_palette(self, palette):
        """
        Set the palette of the object.

        Args:
            palette: The palette of the object.
        """
        self.palette = palette or {}

    def create_text_widget(self, font_family, font_size, **kwargs):
        """
        Create the text widget.

        Args:
            font_family: The font family to use.
            font_size: The font size to use.
            **kwargs: Additional keyword arguments.
        """
        self.text_widget = tk.Text(self, font=font.Font(family=font_family, size=font_size), wrap=tk.WORD)

    def setup_text_formatting(self):
        """
        Configures the various text formatting options for the Flare widget.
        """
        self.text_widget.tag_configure(TAG_BOLD, font=self.bold_font)
        self.text_widget.tag_configure(TAG_ITALIC, font=self.italic_font)

        self.text_widget.bind('<Control-b>', self.toggle_bold)
        self.text_widget.bind('<Control-i>', self.toggle_italic)

    def toggle_bold(self, event):
        """
        Toggles the bold formatting for the selected text.
        """
        self.toggle_formatting(TAG_BOLD)

    def toggle_italic(self, event):
        """
        Toggles the italic formatting for the selected text.
        """
        self.toggle_formatting(TAG_ITALIC)

    def toggle_formatting(self, tag):
        """
        Generic method to toggle the specified text formatting tag.
        """
        start, end = self.text_widget.tag_ranges('sel')
        if start is not None and end is not None:
            if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
                self.text_widget.tag_remove(tag, start, end)
            else:
                self.text_widget.add_tag(tag, start, end)

    def set_content(self, content):
        """
        Sets the content of the Flare widget.
        """
        try:
            self.text_widget.delete('1.0', tk.END)
            self.text_widget.insert('1.0', content)
        except Exception as e:
            print(f'Error setting content: {e}')

    def get_content(self):
        """
        Retrieves the current content of the Flare widget.
        """
        try:
            return self.text_widget.get('1.0', tk.END).strip()
        except Exception as e:
            print(f'Error getting content: {e}')

    def apply_palette(self):
        """
        Applies the specified color palette to the Flare widget.
        """
        default_palette = defaultdict(lambda: '#303030')
        default_palette |= self.palette

        self.text_widget.configure(
            background=default_palette['secondary'],
            foreground=default_palette['primary'],
            insertbackground=default_palette['tertiary']  # Cursor color for HEAT UP editor text widget
        )

    def clear_content(self):
        """
        Clears the content of the Flare widget.
        """
        self.text_widget.delete('1.0', tk.END)

    def place_text_widget(self):
        """
        Places the text widget in the parent object.
        """
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(1, weight=0)
        self.parent.grid_columnconfigure(1, weight=0)
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        self.text_widget.grid(row=1, column=1, sticky="nsew")
        self.text_widget.grid_propagate(False)
        self.text_widget.grid_rowconfigure(0, weight=1)
        self.text_widget.grid_columnconfigure(0, weight=1)
        self.text_widget.grid_rowconfigure(1, weight=0)
        self.text_widget.grid_columnconfigure(1, weight=0)
        self.text_widget.grid_rowconfigure(2, weight=0)
        self.text_widget.grid_columnconfigure(2, weight=0)
        self.text_widget.grid_rowconfigure(3, weight=0)
        self.text_widget.grid_columnconfigure(3, weight=0)
        self.text_widget.grid_rowconfigure(4, weight=0)
        self.text_widget.grid_columnconfigure(4, weight=0)
        self.text_widget.grid_rowconfigure(5, weight=0)
        self.text_widget.grid_columnconfigure(5, weight=0)
        
    def set_focus(self):
        """
        Sets the focus on the Flare widget.
        """
        self.text_widget.focus_set()
        self.text_widget.focus_force()
        self.text_widget.focus()

    def close(self):
        """
        Closes the Flare widget.
        """
        self.destroy()
        self.text_widget = None
        self.parent = None
        self.palette = None
        self.bold_font = None
        self.italic_font = None
# Path: gptrando/flare_widget.py
# Compare this snippet from gptrando/file_handler_parser.py:CustomExtractionError.__repr__:
#     def __repr__(self):
#         return f'CustomExtractionError("{self.message}")' 
#         ...
#     def __iadd__(self, other):
#         self.message += other.message
#         return self
#
# class ChatLogParser.extract_code:
#     def __init__(self, content):
#         return re.findall(r"```(.*?)```", content, re.DOTALL)
#     ...
#     def extract_code(self, content):
#         return re.findall(r"```(.*?)```", content, re.DOTALL)
#         ...
#     def extract_code(self, content):
#         return re.findall(r"```(.*?)```", content, re.DOTALL)
#         ...
