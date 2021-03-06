# -*- coding: utf-8 -*-
"""Module for constructing <caption> tag."""

from __future__ import absolute_import

from ...lib.utils import validate_attribute_values
from ...templates.html.tags import caption

ATTRIBUTES = {
    'align': {
        'description': 'Defines the alignment of the caption',
        'values': ['left', 'right', 'top', 'bottom']
    }
}


class Caption(object):
    """Class for constructing caption tag.

    Args:
        align (str): Defines the alignment of the caption.
        text (str): Specifies the caption text.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.2.0
        Renamed the method construct_tag to construct.
    """
    def __init__(self, align=None, text=None):
        self.tag = 'caption'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  attribute_value=align,
                                  default_values=ATTRIBUTES['align']['values'])
        self.values = {'align': align, 'text': text}

    def construct(self):
        """Returns the constructed caption tag <caption>."""
        return caption.render(self.values)
