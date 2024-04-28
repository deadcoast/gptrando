import tkinter as tk
from doctest import master
from hashlib import new
from imaplib import Literal
from os import name
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from typing import Any

import content
from PIL.ImageColor import colormap
from colorama import Cursor
from fontTools.cffLib import width
from numpy.lib.user_array import container
from self import self
from sqlalchemy import null
from sqlalchemy.engine import cursor

from gptrando.flare_widget import FlareTextExtension
from gptrando.inline_search_manager import InlineSearchManager
from gptrando.theme_manager import PaletteManager, ThemeManager


class ScreenUnits:
    pass


class Relief:
    pass


class TakeFocusValue:
    pass


class MainEditor(tk.Frame):

    def __init__(self, main: tk.Misc | None = None, cnf: dict[str, Any] | None = None, *, background: str = ...,
                 bd: ScreenUnits = ..., bg: str = ..., border: ScreenUnits = ..., border_width: ScreenUnits = ...,
                 class_: str = ..., color_map: Literal["new", ""] | tk.Misc = ..., main_container: bool = ...,
                 cursor: Cursor = ..., height: ScreenUnits = ..., highlight_background: str = ...,
                 highlight_color: str = ..., highlight_thickness: ScreenUnits = ..., name: str = ...,
                 x_value: ScreenUnits = ..., pady: ScreenUnits = ..., relief: Relief = ...,
                 take_focus: TakeFocusValue = ..., visual: str | tuple[str, int] = ..., width: ScreenUnits = ...):
        self.text_widget = self.set_text_widget()
        self.palette_manager = PaletteManager()
        self.parent = self.master = main
        if cnf is None:
            cnf = {}
        super().__init__(main, cnf, null, background, bd, bg, border, border_width, class_, color_map, main_container,
                         cursor, height, highlight_background, highlight_color, highlight_thickness, name, x_value, pady,
                         relief, take_focus, visual, width)

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.theme_manager = ThemeManager()
        self.inline_search_manager = InlineSearchManager()
        self.flare_text_extension = FlareTextExtension(self.text_area)

        self.setup_menu_bar()
        self.setup_bindings()

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.parent = self.parent or self.master  # Use main as parent if not specified
        self.palette_manager = PaletteManager(self.text_area)
        self.theme_manager = ThemeManager()

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.flare_text_extension = FlareTextExtension(self.text_area)
        self.inline_search_manager = InlineSearchManager()

        self.setup_menu_bar()
        self.setup_bindings()

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.parent = self.parent
        self.palette = self.palette or {}
        self.text_widget = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        self.setup_text_formatting()
        self.set_content(content)
        self.apply_palette()

        self.setup_text_formatting()
        self.set_content(content)
        self.apply_palette()

    def init(self, parent, background=None, bd=None, bg=None, border=None, borderwidth=None, class_=None, height=None,
             highlightbackground=None, highlightcolor=None, highlightthickness=None, padx=None, pady=None, relief=None,
             takefocus=None, visual=None):
        self.parent = parent
        self.palette = self.palette or {}
        self.text_widget = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        self.setup_text_formatting()
        self.set_content(content)
        self.apply_palette()

        self.setup_text_formatting()
        self.set_content(content)
        self.apply_palette()

        self.text_widget = self.set_text_widget()
        self.palette_manager = PaletteManager()
        self.parent = self.master = master
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, null, background, bd, bg, border, borderwidth, class_, colormap, container,
                         cursor, height, highlightbackground, highlightcolor, highlightthickness, name, padx, pady,
                         relief, takefocus, visual, width)

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.theme_manager = ThemeManager(self.palette_manager)
        self.inline_search_manager = InlineSearchManager(self.text_area)
        self.flare_text_extension = FlareTextExtension(self.text_area)

        self.setup_menu_bar()
        self.setup_bindings()

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.parent = self.parent or self.master  # Use main as parent if not specified
        self.parent.title("HEAT UP Editor")
        self.palette_manager = PaletteManager()
        self.theme_manager = ThemeManager(self.palette_manager)

        self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.flare_text_extension = FlareTextExtension(self.text_area)
        self.inline_search_manager = InlineSearchManager(self.text_area)

        self.setup_menu_bar()
        self.setup_bindings()

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.parent = self.parent
        self.palette = self.palette or {}

    def setup_menu_bar(self):  # Create the menu bar
        """

        """
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
        edit_menu.add_command(label="Find", command=self.find_text)
        edit_menu.add_command(label="Find Next", command=self.bar_find_next)
        edit_menu.add_command(label="Find Previous", command=self.find_previous)
        edit_menu.add_separator()
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all)

        palette_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Palette", menu=palette_menu)
        palette_menu.add_command(label="Load Palette", command=self.load_palette)
        palette_menu.add_command(label="Save Palette", command=self.save_palette)
        palette_menu.add_separator()
        palette_menu.add_command(label="Toggle Palette", command=self.toggle_palette)

        theme_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Load Theme", command=self.load_theme)
        theme_menu.add_command(label="Save Theme", command=self.save_theme)
        theme_menu.add_separator()
        theme_menu.add_command(label="Toggle Theme", command=self.toggle_theme)

        view_menu = tk.Menu(menubar)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Toggle Line Numbers", command=self.toggle_line_numbers)
        view_menu.add_command(label="Toggle Minimap", command=self.toggle_minimap)
        view_menu.add_command(label="Toggle Fullscreen", command=self.toggle_fullscreen)
        view_menu.add_command(label="Toggle Line Wrapping", command=self.toggle_line_wrapping)
        view_menu.add_separator()
        view_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        view_menu.add_command(label="Toggle Palette", command=self.toggle_palette)
        view_menu.add_command(label="Toggle Inline Search", command=self.toggle_inline_search)
        view_menu.add_command(label="Toggle Flare Text", command=self.toggle_flare_text)

        help_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about_dialog)

    def setup_bindings(self):  # Configure keyboard shortcuts
        self.text_area.bind("<Control-f>", self.inline_search_manager.prompt_search_query)
        self.text_area.bind("<Control-n>", self.inline_search_manager.find_next)
        self.text_area.bind("<Control-p>", self.inline_search_manager.find_previous)

    def show_about_dialog(self):  # Display the about dialog
        messagebox.showinfo("About", "HEAT UP Editor\nVersion 1.0\n\nA simple text editor with advanced features.")

    def save_file(self):  # Open a file dialog to save the current file
        if file_path := filedialog.asksaveasfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        ):
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END).strip())
            self.display_message(f"Saved file: {file_path}")

    def _display_message(self, message):  # Display a message in the status bar
        self.parent.status_bar.config(text=message)  # Update the status bar text

    def close(self):
        self.parent.quit()

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

    def apply_palette(self):
        """
        Applies the specified color palette to the Flare widget.
        """
        self.text_widget.configure(
            background=self.palette.get('secondary', '#303030'),
            foreground=self.palette.get('primary', '#505050'),
            insertbackground=self.palette.get('tertiary', '#202020')
        )

        self.apply_palette_and_init()

    def apply_palette_and_init(self):
        """
        Applies the specified color palette to the Flare widget and initializes the FlareTextExtension.
        """
        self.flare_text_extension.apply_palette()
        self.flare_text_extension.init()

    def toggle_flare_text(self):
        """
        Toggles the Flare text extension.
        """
        self.flare_text_extension.toggle_flare_text()

    def toggle_palette(self):
        """
        Toggles the color palette of the text area.
        """
        current_palette = self.palette_manager.current_palette
        self.palette_manager.toggle_palette()
        self.theme_manager.apply_palette(self.text_area, current_palette)

    def toggle_theme(self):
        """
        Toggles the theme of the text area.
        """
        current_theme = self.theme_manager.current_theme
        self.theme_manager.toggle_theme()
        self.theme_manager.apply_theme(self.text_area, current_theme)

    def toggle_line_wrapping(self):
        """
        Toggles the line wrapping mode of the text area.
        """
        current_state = self.text_area.wrap
        self.text_area.wrap = not current_state
        self.text_area.toggle_line_wrapping()

    def toggle_fullscreen(self):
        """
        Toggles the fullscreen mode of the text area.
        """
        current_state = self.text_area.fullscreen
        self.text_area.fullscreen = not current_state
        self.text_area.toggle_fullscreen()

    def toggle_minimap(self):
        """
        Toggles the display of the minimap in the text area.
        """
        current_state = self.text_area.minimap_visible
        self.text_area.minimap_visible = not current_state
        self.text_area.toggle_minimap()

    def toggle_inline_search(self):
        """
        Toggles the inline search bar.
        """
        self.inline_search_manager.toggle_search_bar()

    def toggle_line_numbers(self):
        """
        Toggles the display of line numbers in the text area.
        """
        current_state = self.text_area.linenumbers_visible
        self.text_area.linenumbers_visible = not current_state
        self.text_area.toggle_line_numbers()

    def save_code(self, code, file_path):
        """
        Saves the extracted code to a file.

        Args:
            code (str): The code to be saved.
            file_path (str): The path of the file to save the code.
        """
        if code:
            with open(file_path, "w") as file:
                file.write(code)

    def add_search_highlight(self, start, end):
        """
        Adds a highlight to the search results.
        """
        self.text_widget.add_tag("search_highlight", start, end)
        self.text_widget.tag_config("search_highlight", background="yellow")
        self.search_highlights.append((start, end))

    def extract_code(self, content):
        """
        Extracts Python and Markdown code from the chat log content.
        Args:
            content (str): The chat log content.
        Returns:
            tuple: A tuple containing the extracted Python code and Markdown code.
        """
        python_code_pattern = r"```python\n(.*?)```"
        markdown_code_pattern = r"```(.*?)```"

        python_code = re.findall(python_code_pattern, content, re.DOTALL)
        markdown_code = re.findall(markdown_code_pattern, content, re.DOTALL)

        return python_code, markdown_code

    def open_file(self):
        """
        Opens a file dialog to select a file to open.
        """
        if file_path := filedialog.askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        ):
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
            self.display_message(f"Opened file: {file_path}")

    def save_file(self):
        """
        Opens a file dialog to save the current file.
        """
        if file_path := filedialog.asksaveasfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        ):
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END).strip())
            self.display_message(f"Saved file: {file_path}")

    def setup_bindings(self):
        self.text_area.bind("<Control-f>", self.inline_search_manager.prompt_search_query)

    def open_file(self):
        if file_path := filedialog.askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        ):
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
            self.display_message(f"Opened file: {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END).strip())
            self.display_message(f"Saved file: {file_path}")

    def _display_message(self, message):
        self.parent.status_bar.config(text=message)


if name == "main":
    self = tk.Tk()
    self.geometry("800x600")
    self.status_bar = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    editor = MainEditor(self)
    editor.theme_manager.apply_theme(editor.text_area)
    editor.pack(fill=tk.BOTH, expand=True)
    self.title("HEAT UP Editor")
    self.palette_manager = PaletteManager()
    self.theme_manager = ThemeManager(self.palette_manager)

    self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
    self.text_area.pack(fill=tk.BOTH, expand=True)

    self.flare_text_extension = FlareTextExtension(self.text_area)
    self.inline_search_manager = InlineSearchManager(self.text_area)
    self.palette_manager = PaletteManager()
    self.theme_manager = ThemeManager(self.palette_manager)

    self.mainloop()

    self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
    self.text_area.pack(fill=tk.BOTH, expand=True)

    self.flare_text_extension = FlareTextExtension(self.text_area)
    self.inline_search_manager = InlineSearchManager(self.text_area)
    self.palette_manager = PaletteManager()
    self.theme_manager = ThemeManager(self.palette_manager)

    self.mainloop()

    self.text_area = tk.Text(self, font=font.Font(family='Courier New', size=12), wrap=tk.WORD)
