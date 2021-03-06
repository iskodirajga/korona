# -*- coding: utf-8 -*-
"""Module for constructing <iframe> tag."""


from __future__ import absolute_import

from ...lib.utils import validate_attribute_values, validate_url
from ...templates.html.tags import iframe

ATTRIBUTES = {
    'align': {
        'description': 'Specifies the alignment of an <iframe> '
                       'according to surrounding elements',
        'values': ['left', 'right', 'middle', 'top', 'bottom']
    },
    'frameborder': {
        'description': 'Specifies whether or not to display a border '
                       'around an <iframe>',
        'values': ['1', '0']
    },
    'height': {
        'description': 'Specifies the height of an <iframe>',
        'values': None
    },
    'longdesc': {
        'description': 'Specifies a page that contains a long '
                       'description of the content of an <iframe>',
        'values': None
    },
    'marginheight': {
        'description': 'Specifies the top and bottom margins of the '
                       'content of an <iframe>',
        'values': None
    },
    'marginwidth': {
        'description': 'Specifies the left and right margins of the '
                       'content of an <iframe>',
        'values': None
    },
    'name': {
        'description': 'Specifies the name of an <iframe>',
        'values': None
    },
    'sandbox': {
        'description': 'Enables an extra set of restrictions for the '
                       'content in an <iframe>',
        'values': ['',
                   'allow-forms',
                   'allow-pointer-lock',
                   'allow-popups',
                   'allow-same-origin',
                   'allow-scripts',
                   'allow-top-navigation']
    },
    'scrolling': {
        'description': 'Specifies whether or not to display scrollbars'
                       ' in an <iframe>',
        'values': ['yes', 'no', 'auto']
    },
    'src': {
        'description': 'Specifies the address of the document to embed'
                       ' in the <iframe>',
        'src': None
    },
    'srcdoc': {
        'description': 'Specifies the HTML content of the page to show'
                       ' in the <iframe>',
        'values': None
    },
    'width': {
        'description': 'Specifies the width of an <iframe>',
        'values': None
    }
}


class IFrame(object):
    """Class for constructing <iframe> tag.

    Args:
        align (str): Specifies the alignment of an <iframe> according to
            surrounding elements.
        frameborder (str): Specifies whether or not to display a border around
            an <iframe>.
        height (str): Specifies the height of an <iframe>.
        longdesc (str): Specifies a page that contains a long description of
            the content of an <iframe>.
        marginheight (str): Specifies the top and bottom margins of the
            content of an <iframe>.
        marginwidth (str): Specifies the left and right margins of the content
            of an <iframe>.
        name (str): Specifies the name of an <iframe>.
        sandbox (str): Enables an extra set of restrictions for the content in
            an <iframe>.
        scrolling (str): Specifies whether or not to display scrollbars in an
            <iframe>.
        src (str): Specifies the address of the document to embed in the
            <iframe>.
        srcdoc (str): Specifies the HTML content of the page to show in the
            <iframe>.
        width (str): Specifies the width of an <iframe>.

    .. versionadded:: 0.4.0
    """
    def __init__(self,
                 align=None,
                 frameborder=None,
                 height=None,
                 longdesc=None,
                 marginheight=None,
                 marginwidth=None,
                 name=None,
                 sandbox=None,
                 scrolling=None,
                 src=None,
                 srcdoc=None,
                 width=None):
        self.tag = 'iframe'
        validate_attribute_values(tag=self.tag,
                                  attribute_name='align',
                                  attribute_value=align,
                                  default_values=ATTRIBUTES['align']['values'])
        validate_attribute_values(
            tag=self.tag,
            attribute_name='frameborder',
            attribute_value=frameborder,
            default_values=ATTRIBUTES['frameborder']['values'])
        validate_url(attribute_name='longdesc', url=longdesc)
        self.validate_sandbox(sandbox=sandbox)
        validate_attribute_values(
            tag=self.tag,
            attribute_name='scrolling',
            attribute_value=scrolling,
            default_values=ATTRIBUTES['scrolling']['values'])
        validate_url(attribute_name='src', url=src)
        self.values = {'align': align,
                       'frameborder': frameborder,
                       'height': height,
                       'longdesc': longdesc,
                       'marginheight': marginheight,
                       'marginwidth': marginwidth,
                       'name': name,
                       'sandbox': sandbox,
                       'scrolling': scrolling,
                       'src': src,
                       'srcdoc': srcdoc,
                       'width': width}

    def construct(self):
        """Returns the constructed iframe tag <iframe>."""
        return iframe.render(self.values)

    def validate_sandbox(self, sandbox):
        """Validates sandbox attribute. The value of the sandbox attribute
        can either be just sandbox (then all restrictions are applied), or a
        space-separated list of pre-defined values that will REMOVE the
        particular restrictions.
        """
        if not sandbox:
            return

        parts = sandbox.split(' ')

        for part in parts:
            validate_attribute_values(
                tag=self.tag,
                attribute_name='sandbox',
                attribute_value=part,
                default_values=ATTRIBUTES['sandbox']['values'])
