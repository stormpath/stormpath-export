stormpath-export
================

Easily export your Stormpath user data.


.. image:: https://img.shields.io/pypi/v/stormpath-export.svg
    :alt: stormpath-export Release
    :target: https://pypi.python.org/pypi/stormpath-export

.. image:: https://img.shields.io/pypi/dm/stormpath-export.svg
    :alt: stormpath-export Downloads
    :target: https://pypi.python.org/pypi/stormpath-export

.. image:: https://api.codacy.com/project/badge/grade/d7904abc80dc40a39e8b1850f10000ea
    :alt: stormpath-export Code Quality
    :target: https://www.codacy.com/app/r/stormpath-export

.. image:: https://img.shields.io/travis/stormpath/stormpath-export.svg
    :alt: stormpath-export Build
    :target: https://travis-ci.org/stormpath/stormpath-export

.. image:: https://github.com/rdegges/stormpath-export/raw/master/assets/box-sketch.png
    :alt: Box Sketch


Purpose
-------

`Stormpath`_ is one of my favorite API services. They provide a scalable,
simple, and secure user management API which makes building scalable systems
simple.

Whenever I talk to people about using `Stormpath`_, the same question
invariably comes up: "Is it easy to export my user data out of Stormpath?  Or
am I locked in?"

Up until now, the answer has been "Yes! But only if you contact them about it."

With ``stormpath-export``, however, you can easily back up all your Stormpath
user data instantly!

``stormpath-export`` will:

- Grab all Stormpath data you've stored, and dump it to JSON files locally.
- Dump data into a local directory structure which makes intuitive sense
  (*groups are located in the groups directory, etc.*).
- Each object gets it's own JSON file generated. This makes it easy to look at
  the file system and extract the information you need.

``stormpath-export`` makes it easy to:

- Download a copy of all your user data.
- Back up your user data (*Stormpath has their own backups of course, but you
  can never be too safe*).
- Migrate user data out of Stormpath.


Installation
------------

Installing ``stormpath-export`` is simple -- just use `pip`_!

Once you have pip installed on your computer, you can run the following to
install the latest release of ``stormpath-export``:

.. code-block:: console

    $ pip install -U stormpath-export

That's it :)


Usage
-----

Before you can export all your `Stormpath`_ data, you'll need to configure
``stormpath-export`` and give it your Stormpath API credentials. To do this,
simply run:

.. code-block:: console

    $ stormpath-export configure

This will prompt you for some basic information, then store your credentials
in the local file ``~/.stormy``.

NOTE: If you are using Stormpath Enterprise, please enter
``https://enterprise.stormpath.io/v1`` when prompted for the Base URL.  This
instructs the export tool to talk to the Stormpath Enterprise environment.

Next, to initiate a backup job, you can run:

.. code-block:: console

    $ stormpath-export

This will export all your Stormpath data, and dump it into a new directory
named ``stormpath-exports``. If you'd like to specify your own backup location,
you can do so by adding a path -- for instance:

.. code-block:: console

    $ stormpath-export ~/Desktop/stormpath-exports

When exporting your data, you should see output similar to the following:

.. code-block:: console

    === Exporting all application data...
    - Exporting application: Stormpath
    === Done!

    === Exporting all directory data...
    - Exporting directory: Stormpath Administrators
    - Exporting directory: testdirectory
    === Done!

    === Exporting all group data...
    - Exporting group: Administrators
    === Done!

    === Exporting all account data...
    - Exporting account: r@rdegges.com
    === Done!

.. note::
    Depending on how many applications, groups, directories, organizations, and
    accounts you have, this process may take a while.

Once the process is finished, you can navigate the JSON files in the export
directory, which will contain all your Stormpath data.

For full usage information, run ``stormpath-export -h``:

.. code-block:: console

    $ stormpath-export -h
    stormpath-export
    ----------------

    Easily export your Stormpath (https://stormpath.com/) user data.

    Usage:
      stormpath-export configure
      stormpath-export [(<location> | -l <location> | --location <location>)]
      stormpath-export (-h | --help)
      stormpath-export --version

    Options:
      -h --help  Show this screen.
      --version  Show version.

    Written by Randall Degges <http://www.rdegges.com/>.


Help
----

Need help? Can't figure something out? If you think you've found a bug, please
open an issue on the `Github issue tracker`_.

Otherwise, `shoot us an email`_.


Changelog
---------

**0.1.1**: 10-17-2016

- Supporting ``--base-url`` argument.
- Making the tool Python 3 compatible.

**0.1.0**: 03-16-2016

- Supporting API key exports.
- Supporting Organization exports.
- Fixing documentation.
- Updating Stormpath dependency.

**0.0.9**: 06-19-2015

- Fixing version information.

**0.0.8**: 06-19-2015

- Supporting private deployments.

**0.0.7**: 06-18-2015

- Supporting Account API key backups.

**0.0.6**: 06-18-2015

- Completely re-doing export structures -- much more sane now.
- Adding IDs, hrefs, and all fields to all backups.
- Still needs to support Social / ID site / Verification templates.

**0.0.5**: 05-28-2015

- Making the application export back up directory mappings.

**0.0.4**: 05-27-2015

- Backing up customData for all resource types.
- Upgrading dependencies.

**0.0.3**: 06-19-2014

- Making application export include directory name for clarity.

**0.0.2**: 06-08-2014

- Fixing bug with groups.
- Adding support for custom data exporting.
- Including new Stormpath SDK.

**0.0.1**: 12-14-2013

- First super-beta release of the project. WOO.


.. _Stormpath: https://stormpath.com/ "Stormpath"
.. _pip: http://pip.readthedocs.org/en/stable/ "pip"
.. _Github issue tracker: https://github.com/stormpath/stormpath-export/issues "stormpath-export Issue Tracker"
.. _shoot us an email: mailto:support@stormpath.com "Stormpath Support"
