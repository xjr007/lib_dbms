"""
Module containing function templates for tkinter.

Important functions for main.py
"""


class LabelForTk:
    """
    Label.

    Label for tkinter object : Label
    """

    def __init__(self, obj, widget, text, background_colour):
        """
        Initialize.

        Class Label
        """
        self.obj = obj
        self.widget = widget
        self.text = text
        self.background_colour = background_colour

    def style_object(self):
        """
        Create an instace of tkinter Object.

        Label
        """
        return self.obj(self.widget, text=self.text, font=('arial', 12, 'bold'),
                        padx=2, pady=2, bg=self.background_colour)


# def label_for_tk(module, object_type, widget, text, background_colour):
#     """
#     Label.
#
#     Label for tkinter Object : Label
#     """
#     new_label = module.object_type(widget, text=text, font=('arial', 12, 'bold'),
#                                    padx=2, pady=2, bg=background_colour)
#     return new_label
