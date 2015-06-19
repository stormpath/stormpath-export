# stormpath-export

Easily export your Stormpath user data.

![Box Sketch](https://github.com/rdegges/stormpath-export/raw/master/assets/box-sketch.jpg)


## Purpose

[Stormpath](http://stormpath.com/) is one of my favorite API companies.  They
provide a scalable, simple, and secure user accounts API platform which makes
building scalable systems simple.

Whenever I talk to people about using Stormpath, the same question invariably
comes up:  "Is it easy to export my user data out of Stormpath?  Or am I locked
in?"

Up until now, the answer has been "Yes!  But only if you contact them about it."

With `stormpath-export`, however, you can easily back up all your Stormpath user
data instantly!

`stormpath-export` will:

- Grab all Stormpath data you've stored, and dump it to JSON files locally.
- Dumps data into a local directory structure which makes intuitive sense
  (groups are located in the groups directory, etc.).
- Each object gets it's own JSON file generated.  This makes it easy to look at
  the filesystem and extract the information you need.

`stormpath-export` makes it easy to:

- Download a copy of all your user data.
- Back up your user data (Stormpath has their own backups of course, but you can
  never be too safe).
- Migrate user data out of Stormpath.


## Installation

Installing `stormpath-export` is simple -- just use
[pip](http://www.pip-installer.org/en/latest/)!

Once you have pip installed on your computer, you can run the following to
install the latest release of `stormpath-export`:

```console
$ pip install -U stormpath-export
```

That's it :)


## Usage

Before you can export all your Stormpath data, you'll need to configure
`stormpath-export` and give it your Stormpath API credentials.  To do this,
simply run:

```console
$ stormpath-export configure
```

On the command line.  This will prompt you for some basic information, then
store your credentials in the local file `~/.stormy`.

Next, to run a backup job, you can run:

```console
$ stormpath-export
```

This will export all your Stormpath data and dump it into a new directory named
`stormpath-exports`.  If you'd like to specify your own backup location, you can
do so by adding a path -- for instance:

```console
$ stormpath-export ~/Desktop/stormpath-exports
```

When exporting your data, you should see output similar to the following:

```console
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
```

**NOTE**: Depending on how many applications, groups, directories, and accounts
you have, this process may take a while.

Once the process is finished, you can navigate the JSON files in the export
directory, which will contain all your Stormpath data.

For full usage information, run `stormpath-export -h`:

```console
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
```


## Help

Need help?  Can't figure something out?  If you think you've found a bug, please
open an issue on the GitHub issue tracker.

Otherwise, [shoot me an email](mailto:r@rdegges.com)!


## Changelog

v0.0.6 06-18-2015

    - Completely re-doing export structures -- much more sane now.
    - Adding IDs, hrefs, and all fields to all backups.
    - Still needs to support Social / ID site / Verification templates.

v0.0.5 05-28-2015

    - Making the application export back up directory mappings.

v0.0.4: 05-27-2015

    - Backing up customData for all resource types.
    - Upgrading dependencies.

v0.0.3: 06-19-2014

    - Making application export include directory name for clarity.

v0.0.2: 06-08-2014

    - Fixing bug with groups.
    - Adding support for custom data exporting.
    - Including new Stormpath SDK.

v0.0.1: 12-14-2013

    - First super-beta release of the project. WOO.
