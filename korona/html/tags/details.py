# -*- coding: utf-8 -*-
"""Module for constructing <details> tag."""

from ...templates.html.tags import details_tag


class Details(object):
    """Class for constructing details tag.

    Args:
        open (bool): Specifies that the details should be visible (open) to
            the user.
        text (str): Specifies the details text. (As in
            <details>{text}</details>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, open=False, text=None):
        self.tag = 'details'
        self.values = {'open': open, 'text': text}

    def construct(self):
        """Returns the constructed details tag <details></details>."""
        return details_tag.render(self.values)