# stormpath-export

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
