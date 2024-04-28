def setup_bindings(self):
    """
    Configures the keyboard shortcuts for the inline search functionality.
    """
    self.text_widget.bind("<Control-f>", self.prompt_search_query)
    self.text_widget.bind("<Control-n>", self.bar_find_next)
    self.text_widget.bind("<Control-p>", self.find_previous)
