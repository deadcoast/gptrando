import tkinter as tk
from collections import defaultdict
from tkinter import font

from gptrando.main import TakeFocusValue

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
            x_focus_val: TakeFocusValue = 1):
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

    def init(self, parent, content='', palette=None, **kwargs):
        super().init(parent, **kwargs)

        if parent is not None:
            self.parent = parent
        self.palette = palette or {}
        self.text_widget = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_widget.grid(row=0, column=0, sticky="nsew")

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
        default_palette.update(self.palette)

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
