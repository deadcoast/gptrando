import tkinter as tk
from tkinter import font
from typing import Any, Literal

from PIL.Image import new
from PIL.ImageColor import colormap
from colorama import Cursor
from fig import container
from pyasn1.compat.octets import null

from gptrando.main import TakeFocusValue, Relief


class FlareTextExtension(tk.Frame):
    """
    An advanced Flare widget that provides a rich set of features for content display and interaction within the HEAT UP editor.
    """

    def __init__(
            self,
            master: tk.Misc | None = None,
            cnf=None,
            *,
            background: str = ...,
            bd: tk = ...,
            bg: str = ...,
            border: tk = ...,
            borderwidth: tk = ...,
            cursor: Cursor = ...,
            height: tk = ...,
            x_focus_val: TakeFocusValue = 1,
            visual=None,
            class_=None):
        """
        Initialize the FlareTextExtension object.

        Args:
            master (tk.Misc | None): The master widget.
            cnf: The configuration options.
            background (str): The background color.
            bd (tk): The border width.
            bg (str): The background color.
            border (tk): The border style.
            borderwidth (tk): The border width.
            cursor (Cursor): The cursor style.
            height (tk): The height of the widget.
            x_focus_val (TakeFocusValue): The x focus value.
            visual: The visual style.
            class_: The class style.
        """
        super().__init__(master, cnf, null, background, bd, bg, border, borderwidth, class_, colormap, container,
                         cursor, height)
        self.x_focus_val = x_focus_val
        self.visual = visual
        if cnf is None:
            cnf = {}
        self.text_widget = None
        self.parent = None
        self.palette = None

    def init(self, parent, content='', palette=None, **kwargs):
        super().init(parent, **kwargs)

        self.parent = parent
        self.palette = palette or {}
        self.text_widget = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def setup_text_formatting(self):
        """
        Configures the various text formatting options for the Flare widget.
        """
        bold_font = font.Font(family='Courier New', size=12, weight='bold')
        italic_font = font.Font(family='Courier New', size=12, slant='italic')

        self.text_widget.tag_configure('bold', font=bold_font)
        self.text_widget.tag_configure('italic', font=italic_font)

        self.text_widget.bind('<Control-b>', self.toggle_bold)
        self.text_widget.bind('<Control-i>', self.toggle_italic)

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
            self.text_widget.tag_add(tag, start, end)

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

    def apply_palette(self):
        """
        Applies the specified color palette to the Flare widget.
        """
        self.text_widget.configure(
            background=self.palette.get('secondary', '#303030'),
            foreground=self.palette.get('primary', '#505050'),
            insertbackground=self.palette.get('tertiary', '#202020')  # Cursor color for HEAT UP editor text widget
        )
