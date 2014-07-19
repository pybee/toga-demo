Toga Demo
=========

A demonstration of the capabilities of the Toga widget toolkit.

Quickstart
----------

In your virtualenv, install Toga Demo, and then run it::

    $ pip install toga-demo
    $ toga-demo

This will pop up a GUI window.

Problems using virtualenv under Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toga uses the system native python GTK+3 bindings for display purposes.
However, if you're using a `--no-site-packages` virtualenv, the Python bindings
for GTK won't be in your `PYTHONPATH`.

Unfortunately, you can't `pip install` GTK+ bindings, so you have to use a
workaround. To make the system GTK+ bindings available to your virtualenv,
symlinking the `gi` module from the system dist-packages directory into your
virtualenv's site-packages:

    $ cd <your virtualenv dir>/lib/python2.7/site-packages
    $ ln -si /usr/lib/python2.7/dist-packages/gi

Community
---------

Toga Demo is part of the `BeeWare suite`_. You can talk to the community through:

 * `@pybeeware on Twitter`_

 * The `BeeWare Users Mailing list`_, for questions about how to use the BeeWare suite.

 * The `BeeWare Developers Mailing list`_, for discussing the development of new features in the BeeWare suite, and ideas for new tools for the suite.

Contributing
------------

If you experience problems with Toga Demo, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _BeeWare suite: http://pybee.org
.. _Read The Docs: http://toga-demo.readthedocs.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _BeeWare Users Mailing list: https://groups.google.com/forum/#!forum/beeware-users
.. _BeeWare Developers Mailing list: https://groups.google.com/forum/#!forum/beeware-developers
.. _log them on Github: https://github.com/pybee/toga-demo/issues
.. _fork the code: https://github.com/pybee/toga-demo
.. _submit a pull request: https://github.com/pybee/toga-demo/pulls
