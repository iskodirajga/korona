# -*- coding: utf-8 -*-
"""Module for constructing description tags <dd>, <dl>, <dt>."""

from ...templates.html.tags import dd_tag, dl_tag, dt_tag


class DD(object):
    """Class for constructing dd tag.

    Args:
        text (str): Specifies the dd text. (As in <dd>{text}</dd>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        self.tag = 'dd'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed dd tag <dd></dd>."""
        return dd_tag.render(self.values)


class DL(object):
    """Class for constructing dl tag.

    Args:
        text (str): Specifies the dl text. (As in <dl>{text}</dl>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        self.tag = 'dl'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed dl tag <dl></dl>."""
        return dl_tag.render(self.values)


class DT(object):
    """Class for constructing dt tag.

    Args:
        text (str): Specifies the dt text. (As in <dt>{text}</dt>)

    .. versionadded:: 0.2.0
    """
    def __init__(self, text=None):
        self.tag = 'dt'
        self.values = {'text': text}

    def construct(self):
        """Returns the constructed dt tag <dt></dt>."""
        return dt_tag.render(self.values)