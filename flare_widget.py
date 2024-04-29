import logging
import os
import shutil
import tkinter as tk
from collections import defaultdict
from tkinter import font

import content
import palette

import main
from gptrando.main import self

TAG_BOLD = '>BOLD'
TAG_ITALIC = '>ITALIC>'
TAG_COMMENT = '>COMMENT'
TAG_VARIABLE = '>VARIABLE'
TAG_CONSTANT = '>CONSTANT'
TAG_FUNCTION = '>FUNCTION'
TAG_KEYWORD = '>TAG_KEYWORD'
TAG_STRING = '>STRING'  # TODO: Add support for other string types (e.g. multi-line strings)TAG_STRING)
TAG_NUMBER = '>NUMBER'  # TODO: Add support for other number types (e.g. floating point numbers)TAG_NUMBER)
TAG_URL = '>URL'  # TODO: Add support for other URL types (e.g. email addresses)TAG_URL)
TAG_EMAIL = '>EMAIL'  # TODO: Add support for other email types (e.g. email addresses)TAG_EMAIL)
TAG_CODE = '>CODE'  # TODO: Add support for other code types (e.g. code blocks)TAG_CODE)
TAG_HTML = '>HTML'  # TODO: Add support for other HTML types (e.g. HTML tags)TAG_HTML)
TAG_CSS = '>CSS'  # TODO: Add support for other CSS types (e.g. CSS selectors)TAG_CSS)
TAG_JS = '>JS'  # TODO: Add support for other JS types (e.g. JS functions)TAG_JS)
TAG_SQL = '>SQL'  # TODO: Add support for other SQL types (e.g. SQL queries)TAG_SQL)
TAG_JSON = '>JSON'  # TODO: Add support for other JSON types (e.g. JSON objects)TAG_JSON)
TAG_XML = '>XML'  # TODO: Add support for other XML types (e.g. XML elements)TAG_XML)
TAG_YAML = '>YAML'  # TODO: Add support for other YAML types (e.g. YAML documents)TAG_YAML)
TAG_MARKDOWN = '>MARKDOWN'  # TODO: Add support for other Markdown types (e.g. Markdown elements)TAG_MARKDOWN)
TAG_LATEX = '>LATEX'  # TODO: Add support for other LaTeX types (e.g. LaTeX equations)TAG_LATEX)
TAG_ASCII = '>ASCII'  # TODO: Add support for other ASCII types (e.g. ASCII art)TAG_ASCII)
TAG_UNICODE = '>UNICODE'  # TODO: Add support for other Unicode types (e.g. Unicode characters)TAG_UNICODE)
TAG_BINARY = '>BINARY'  # TODO: Add support for other binary types (e.g. binary data)TAG_BINARY)
TAG_IMAGE = '>IMAGE'  # TODO: Add support for other image types (e.g. image files)TAG_IMAGE)
TAG_AUDIO = '>AUDIO'  # TODO: Add support for other audio types (e.g. audio files)TAG_AUDIO)
TAG_VIDEO = '>VIDEO'  # TODO: Add support for other video types (e.g. video files)TAG_VIDEO)
TAG_FILE = '>FILE'  # TODO: Add support for other file types (e.g. file paths)TAG_FILE)
TAG_DIRECTORY = '>DIRECTORY'  # TODO: Add support for other directory types (e.g. directory paths)TAG_DIRECTORY)
TAG_DATE = '>DATE'  # TODO: Add support for other date types (e.g. date strings)TAG_DATE)
TAG_TIME = '>TIME'  # TODO: Add support for other time types (e.g. time strings)TAG_TIME)
TAG_TIMESTAMP = '>TIMESTAMP'  # TODO: Add support for other timestamp types (e.g. timestamp strings)TAG_TIMESTAMP)
TAG_DATETIME = '>DATETIME'  # TODO: Add support for other datetime types (e.g. datetime strings)TAG_DATETIME)
TAG_PHONE = '>PHONE'  # TODO: Add support for other phone types (e.g. phone numbers)TAG_PHONE)
TAG_IP = '>IP'  # TODO: Add support for other IP types (e.g. IP addresses)TAG_IP)
TAG_MAC = '>MAC'  # TODO: Add support for other MAC types (e.g. MAC addresses)TAG_MAC)
TAG_UUID = '>UUID'  # TODO: Add support for other UUID types (e.g. UUID strings)TAG_UUID)
TAG_HASH = '>HASH'  # TODO: Add support for other hash types (e.g. hash strings)TAG_HASH)
TAG_SIGNATURE = '>SIGNATURE'  # TODO: Add support for other signature types (e.g. signature strings)TAG_SIGNATURE)
TAG_ENCRYPTED = '>ENCRYPTED'  # TODO: Add support for other encrypted types (e.g. encrypted strings)TAG_ENCRYPTED)
TAG_DECRYPTED = '>DECRYPTED'  # TODO: Add support for other decrypted types (e.g. decrypted strings)TAG_DECRYPTED)
TAG_COMPRESSED = '>COMPRESSED'  # TODO: Add support for other compressed types (e.g. compressed strings)TAG_COMPRESSED)
TAG_DECOMPRESSED = '>DECOMPRESSED'  # TODO: Add support for other decompressed types (e.g. decompressed
# strings)TAG_DECOMPRESSED)
TAG_ENCODED = '>ENCODED'  # TODO: Add support for other encoded types (e.g. encoded strings)TAG_ENCODED)
TAG_DECODED = '>DECODED'  # TODO: Add support for other decoded types (e.g. decoded strings)TAG_DECODED)
logger = logging.getLogger(__name__)

# Define the TakeFocusValue enum
TakeFocusValue = tk.IntVar
TakeFocusValue.set = TakeFocusValue.set
TakeFocusValue.get = TakeFocusValue.get
TakeFocusValue.toggle = TakeFocusValue.toggle


def set_take_focus_value(value, take_focus_value):
    """
    Set the value of TakeFocusValue.

    Parameters:
    - value: the new value to set
    - take_focus_value: the global variable to set the value

    Returns:
    bool: True if the operation was successful, False otherwise
    """
    try:
        take_focus_value.set(int(value))
        return True
    except TypeError:
        logging.error("Value must be an integer.")
        return False
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False


def get_take_focus_value():
    try:
        return TakeFocusValue.get(self.x_focus_val)
    except (tk.TclError, ValueError, TypeError, AttributeError):
        logging.error("Error getting TakeFocusValue.")
        return None
    except NameError:
        logging.error("Value must be an integer.")
        return None
    except Exception as e:
        # Handle the exception here
        print(f"An error occurred when getting the TakeFocusValue: {e}")

    return None


def toggle_take_focus_value(self, take_focus_value):
    """
    Toggle the value of take_focus_value.

    Args:
        take_focus_value (tkinter.IntVar): The variable to toggle.

    Returns:
        None
    """
    try:
        take_focus_value.set(not take_focus_value.get())
    except (tk.TclError, ValueError, TypeError, AttributeError):
        logging.error("Error toggling take_focus_value.", exc_info=True)
    except Exception as e:
        # Handle the specific exceptions that can be handled
        if isinstance(e, (ValueError, TypeError, AttributeError, tk.TclError)):
            # Handle specific exception
            logging.error("Value must be an integer.")
        else:
            # Reraise the exception for unhandled cases
            raise

    return None


class FlareTextExtension(tk.Frame):
    def __init__(
            self,
            master: tk.Misc | None = None,
            cnf=None,
            *,
            x_focus_val: main.TakeFocusValue = 1):
        super().__init__(master, cnf=cnf)
        self.x_focus_val = x_focus_val
        self.bold_font = font.Font(family='Helvetica', size=12, weight='bold')
        self.italic_font = font.Font(family='Helvetica', size=12, slant='italic')
        self.palette = defaultdict(lambda: '#505050')
        self.text_widget = None
        self.parent = None

    def create_text_widget(self, font_family, font_size, **kwargs):
        self.text_widget = tk.Text(self, font=font.Font(family=font_family, size=font_size), wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        self.text_widget.focus_set()

    def set_content(self, content):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', content)

    def get_content(self):
        return self.text_widget.get('1.0', tk.END).strip()

    def clear_content(self):
        self.text_widget.delete('1.0', tk.END)

    def toggle_formatting(self, tag):
        try:
            start, end = self.text_widget.tag_ranges('sel')
            if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
                self.text_widget.tag_remove(tag, start, end)
            else:
                self.text_widget.tag_add(tag, start, end)
        except Exception as e:
            logger.error(f'Error toggling formatting: {e}')

    def apply_palette(self):
        self.text_widget.configure(
            background=self.palette['secondary'],
            foreground=self.palette['primary'],
            insertbackground=self.palette['tertiary']
        )

    def set_palette(self, primary, secondary, tertiary):
        self.palette['primary'] = primary
        self.palette['secondary'] = secondary
        self.palette['tertiary'] = tertiary

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent  # Return the parent object

    def set_focus(self):
        self.text_widget.focus_set()
        self.text_widget.focus_force()
        self.text_widget.focus()  # Set the focus on the text WidgetTest

    def init(self, parent, content, palette, font_family, font_size):
        pass


# List of supported text formatting tags with an example of how to use them.

# List of supported text formatting tags with an example of how to use them.
# Example usage of the toggle_formatting method:
class WidgetTest(FlareTextExtension):
    widget = FlareTextExtension()
    widget.init(parent=widget, content='This is a test message.', palette=None, font_family='Courier New', font_size=12)

    def toggle_formatting(self, tag):
        try:
            start, end = self.text_widget.tag_ranges('sel')
            if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
                self.text_widget.tag_remove(tag, start, end)
            else:
                self.text_widget.tag_add(tag, start, end)
        except Exception as e:
            logger.error(f'Error toggling formatting: {e}')

    def apply_palette(self):
        self.text_widget.configure(
            background=self.palette['secondary'],
            foreground=self.palette['primary'],
            insertbackground=self.palette['tertiary']
        )

    def place_text_widget(self):
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.text_widget.grid_rowconfigure(0, weight=1)
        self.text_widget.grid_columnconfigure(0, weight=1)

    def set_palette(self, primary, secondary, tertiary):
        self.palette['primary'] = primary
        self.palette['secondary'] = secondary
        self.palette['tertiary'] = tertiary

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent  # Return the parent object

    def set_focus(self):
        self.text_widget.focus_set()
        self.text_widget.focus_force()
        self.text_widget.focus()  # Set the focus on the text WidgetTest

    def get_focus(self):
        return self.text_widget.focus_get()

    def set_content(self, content):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', content)

    def get_content(self):
        return self.text_widget.get('1.0', tk.END).strip()

    def clear_content(self):
        self.text_widget.delete('1.0', tk.END)

    def toggle_formatting(self, tag):
        try:
            start, end = self.text_widget.tag_ranges('sel')
            if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
                self.text_widget.tag_remove(tag, start, end)
            else:
                self.text_widget.tag_add(tag, start, end)
        except Exception as e:
            logger.error(f'Error toggling formatting: {e}')

    def place_text_widget(self):
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


WidgetTest.create_text_widget('Courier New', 12),
WidgetTest.set_content('This is a test message.'),
WidgetTest.apply_palette(self)
WidgetTest.set_palette('#FFFFFF', '#000000', '#000000')
WidgetTest.init(parent=WidgetTest,
                content='This is a test message.',
                palette=None,
                font_family='Courier New',
                font_size=12)
WidgetTest.set_palette('primary', 'secondary', 'tertiary')
WidgetTest.set_parent(self)
WidgetTest.set_focus()
WidgetTest.set_content('This is a test message.')
WidgetTest.apply_palette(self)
WidgetTest.set_palette('#FFFFFF', '#000000', '#000000')
WidgetTest.set_parent(self)
WidgetTest.set_palette('primary', 'secondary', 'tertiary')
WidgetTest.set_parent(self)
WidgetTest.set_content('This is a test message.')
WidgetTest.toggle_formatting(self, 'bold')
WidgetTest.toggle_formatting(self, 'italic')
WidgetTest.toggle_formatting(self, 'underline')
WidgetTest.toggle_formatting(self, 'strikethrough' or 'strike')
WidgetTest.toggle_formatting(self, 'code')
WidgetTest.toggle_formatting(self, 'variable')
WidgetTest.toggle_formatting(self, 'constant')
WidgetTest.toggle_formatting(self, 'function')
WidgetTest.toggle_formatting(self, 'keyword')
WidgetTest.toggle_formatting(self, 'string')
WidgetTest.toggle_formatting(self, 'number')
WidgetTest.toggle_formatting(self, 'url')
WidgetTest.toggle_formatting(self, 'email')
WidgetTest.toggle_formatting(self, 'code')
WidgetTest.toggle_formatting(self, 'html')
WidgetTest.toggle_formatting(self, 'css')
WidgetTest.toggle_formatting(self, 'js')
WidgetTest.toggle_formatting(self, 'sql')
WidgetTest.toggle_formatting(self, 'json')
WidgetTest.toggle_formatting(self, 'xml')
WidgetTest.toggle_formatting(self, 'yaml')
WidgetTest.set_palette(primary='#FFFFFF', secondary='#000000', tertiary='#000000')
WidgetTest.set_parent(self)
WidgetTest.set_content('This is a test message.')
WidgetTest.set_palette('primary', 'secondary', 'tertiary')
WidgetTest.set_palette(primary='#FFFFFF', secondary='#000000', tertiary='#000000')


# create function for zettelkasten note sorting and connection
class Zettelkasten:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.zettelkasten_notes = self.get_zettelkasten_notes()

    def get_zettelkasten_notes(self):
        return [note for note in os.listdir(self.folder_path) if note.endswith('.md')]

    def sort_zettelkasten_notes(self):
        self.zettelkasten_notes.sort()

    def connect_zettelkasten_notes(self):
        for i in range(len(self.zettelkasten_notes) - 1):
            note1 = self.zettelkasten_notes[i]
            note2 = self.zettelkasten_notes[i + 1]
            self.connect_notes(note1, note2)

    def connect_notes(self, note1, note2):
        with open(os.path.join(self.folder_path, note1), 'a') as f:
            f.write(f'\n\n[[{note2}]]')

        with open(os.path.join(self.folder_path, note2), 'a') as f:
            f.write(f'\n\n[[{note1}]]')

    def disconnect_notes(self, note1, note2):
        with open(os.path.join(self.folder_path, note1), 'w') as f:
            f.write('')

        with open(os.path.join(self.folder_path, note2), 'w') as f:
            f.write('')

    def disconnect_zettelkasten(self):
        self.disconnect_zettelkasten_notes()
        self.sort_zettelkasten_notes()
        self.connect_zettelkasten_notes()

    def connect_zettelkasten(self):
        self.connect_zettelkasten_notes()
        self.sort_zettelkasten_notes()
        self.disconnect_zettelkasten_notes()

    def sort_zettelkasten(self):
        self.sort_zettelkasten_notes()
        self.disconnect_zettelkasten_notes()
        self.connect_zettelkasten_notes()

    def get_zettelkasten(self):
        self.sort_zettelkasten()
        self.connect_zettelkasten()
        self.disconnect_zettelkasten()

    def get_zettelkasten_notes(self):
        return [note for note in os.listdir(self.folder_path) if note.endswith('.md')]

    def connect_zettelkasten_notes(self):
        for i in range(len(self.zettelkasten_notes) - 1):
            note1 = self.zettelkasten_notes[i]
            note2 = self.zettelkasten_notes[i + 1]
            self.connect_notes(note1, note2)

    def disconnect_zettelkasten_notes(self):
        for i in range(len(self.zettelkasten_notes) - 1):
            note1 = self.zettelkasten_notes[i]
            note2 = self.zettelkasten_notes[i + 1]
            self.disconnect_notes(note1, note2)

    def delete_zettelkasten_notes(self):
        for note in self.zettelkasten_notes:
            os.remove(os.path.join(self.folder_path, note))

    def delete_zettelkasten_folder(self):
        shutil.rmtree(self.folder_path)

    def create_zettelkasten_folder(self):
        os.makedirs(self.folder_path)

    def create_zettelkasten_notes(self):
        for i in range(10):
            with open(os.path.join(self.folder_path, f'note{i}.md'), 'w') as f:
                f.write(f'# Note {i}\n\nThis is note {i}.')

    def create_zettelkasten(self):
        self.create_zettelkasten_folder()
        self.create_zettelkasten_notes()

    def delete_zettelkasten(self):
        self.delete_zettelkasten_notes()
        self.delete_zettelkasten_folder()

    def connect_zettelkasten(self):
        self.connect_zettelkasten_notes()

    def disconnect_zettelkasten(self):
        self.disconnect_zettelkasten_notes()

    def sort_zettelkasten(self):
        self.sort_zettelkasten_notes()

    def connect_zettelkasten_and_sort(self):
        self.connect_zettelkasten()
        self.sort_zettelkasten()

    def disconnect_zettelkasten_and_sort(self):
        self.disconnect_zettelkasten()
        self.sort_zettelkasten()

    def connect_zettelkasten_and_sort_and_disconnect(self):
        self.connect_zettelkasten_and_sort()
        self.disconnect_zettelkasten()


# Path: gptrando/flare_widget.py


class FlareTextExtension(tk.Frame):
    """
    An advanced Flare WidgetTest that provides a rich set of features for content display and interaction within the HEAT UP editor.
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
            master (tk.Misc | None): The master WidgetTest.
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
        self.set_parent(parent)
        self.set_palette(palette)
        self.create_text_widget(font_family, font_size, **kwargs)
        self.set_content(content)  # Set the content to the text_widget
        self.place_text_widget()

        if self.text_widget is not None:
            try:
                self.text_widget.grid(row=0, column=0, sticky="nsew")
            except tk.TclError as e:
                logging.error(f'Error creating or placing text WidgetTest: {e}')
                raise

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
        Create the text WidgetTest.

        Args:
            font_family: The font family to use.
            font_size: The font size to use.
            **kwargs: Additional keyword arguments.
        """
        self.text_widget = tk.Text(self, font=font.Font(family=font_family, size=font_size), wrap=tk.WORD)

    def setup_text_formatting(self):
        """
        Configures the various text formatting options for the Flare WidgetTest.
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
        try:
            start, end = self.text_widget.tag_ranges('sel')
            if self.text_widget.tag_names(start) and tag in self.text_widget.tag_names(start):
                self.text_widget.tag_remove(tag, start, end)
            else:
                self.text_widget.add_tag(tag, start, end)
        except Exception as e:
            logging.error(f'Error toggling formatting: {e}')

    def set_content(self, content):
        """
        Sets the content of the Flare WidgetTest.
        """
        try:
            self.text_widget.delete('1.0', tk.END)
            self.text_widget.insert('1.0', content)
        except (tk.TclError, tk.TextError) as e:
            logging.error(f'Error setting content: {e}')

    def get_content(self):
        """
        Retrieves the current content of the Flare WidgetTest.
        """
        try:
            return self.text_widget.get('1.0', tk.END).strip()
        except (tk.TclError, tk.TextError) as e:
            logging.error(f'Error getting content: {e}')

    def apply_palette(self):
        """
        Applies the specified color palette to the Flare WidgetTest.
        """

        def get_default_color():
            return '#303030'

        default_palette = defaultdict(get_default_color)
        default_palette |= self.palette

        self.text_widget.configure(
            background=default_palette['secondary'],
            foreground=default_palette['primary'],
            insertbackground=default_palette['tertiary']  # Cursor color for HEAT UP editor text WidgetTest
        )

    def clear_content(self):
        """
        Clears the content of the Flare WidgetTest.
        """
        self.text_widget.delete('1.0', tk.END)

    def place_text_widget(self):
        """
        Places the text WidgetTest in the parent object.
        """
        for i in range(6):
            self.parent.grid_rowconfigure(i, weight=1)
            self.parent.grid_columnconfigure(i, weight=1)
        self.text_widget.grid(sticky="nsew")
        self.text_widget.grid_propagate(False)
        for i in range(6):
            self.text_widget.grid_rowconfigure(i, weight=1)
            self.text_widget.grid_columnconfigure(i, weight=1)

    def set_focus(self):
        """
        Sets the focus on the Flare WidgetTest.
        """
        self.text_widget.focus_set()
        self.text_widget.focus_force()
        self.text_widget.focus()

    def close(self):
        """
        Closes the Flare WidgetTest.
        """
        self.destroy()
        del self.text_widget
        del self.parent
        del self.palette
        del self.bold_font
        del self.italic_font
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
