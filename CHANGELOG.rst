Changelog
=========


v0.4.3-dev
----------

Added
^^^^^

- Added custom exceptions for korona package.
- Added warnings for korona package.
- Added class ``GlobalAttributes()`` for constructing HTML global attributes.

Changed
^^^^^^^

- Moved all the HTML tag attributes from ``html/root/attributes.py`` to their
  respective tag files.
- Moved all the global attributes from ``html/root/attributes.py`` to
  ``html/root/global_attributes.py``.

- In the class for constructing ``anchor`` tag:

  - The user can be displayed with warnings for charset attribute.
  - Used custom exceptions for all the attributes.
  - Changed the name of the method from ``validate_values()`` to
    ``validate_attribute_values()``.

Removed
^^^^^^^

- Removed ``html/root/attributes.py``.
- Removed ``validate_values()`` method from both ``html.tags.anchor.A()`` and
  ``html.tags.button.Button()`` classes.

v0.4.2 (2016-09-24)
-------------------

Added
^^^^^

- Added classes for building some of the tags:

  - ``<input>``


v0.4.1 (2016-09-16)
-------------------

Changed
^^^^^^^

- Moved all the templates for html tags from ``templates/html/tags.py`` to ``templates/html/tags/``


v0.4.0 (2016-09-15)
-------------------

Added
^^^^^

- Added classes for building some of the tags:

  - ``<html></html>``
  - ``<i></i>``
  - ``<iframe></iframe>``
  - ``<img>``

Changed
^^^^^^^

- Moved all the classes for constructing tags to separate files for easy accessibility.


v0.3.1 (2016-09-05)
-------------------

Added
^^^^^

- Added validation for URL strings in constructing the tags.


v0.3.0 (2016-09-04)
-------------------

Added
^^^^^

- Added classes for building some of the tags:

  - ``<h1></h1>``
  - ``<h2></h2>``
  - ``<h3></h3>``
  - ``<h4></h4>``
  - ``<h5></h5>``
  - ``<h6></h6>``
  - ``<head></head>``
  - ``<header></header>``
  - ``<hr>``


v0.2.0 (2016-09-03)
-------------------

Added
^^^^^

- Added classes for building some of the tags:

  - ``<colgroup></colgroup>``
  - ``<dd></dd>``
  - ``<del></del>``
  - ``<details></details>``
  - ``<dialog></dialog>``
  - ``<div></div>``
  - ``<dl></dl>``
  - ``<dt></dt>``
  - ``<embed>``
  - ``<fieldset></fieldset>``
  - ``<figure></figure>``
  - ``<footer></footer>``
  - ``<form></form>``
  - ``<frame>``
  - ``<frameset></frameset>``


v0.1.0 (2016-08-28)
-------------------

Added
^^^^^

- First release.
- Added classes for building some of the tags:

  - ``<a></a>``
  - ``<abbr></abbr>``
  - ``<acronym></acronym>``
  - ``<address></address>``
  - ``<area>``
  - ``<article></article>``
  - ``<b></b>``
  - ``<base>``
  - ``<button></button>``
  - ``<canvas></canvas>``
  - ``<caption></caption>``
  - ``<cite></cite>``
