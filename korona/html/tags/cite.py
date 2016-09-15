# -*- coding: utf-8 -*-
"""Module for constructing <cite> tag."""

from ...templates.html.tags import cite_tag


class Cite(object):
    """Class for constructing cite tag.

    Args:
        text (str): Specifies the citation text.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, text):
        self.tag = 'cite'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed cite tag <cite>."""
        return cite_tag.render(self.values)