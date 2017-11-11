dumbp
=====

A cli tool for my shitty Alcatel A392CC flip phone.

Based on the the CLI tutorial here: https://stormpath.com/blog/building-simple-cli-interfaces-in-python

Usage
-----

Desired functions:

- Sync
  - Sync from phone to local cache for modification
  - sync back to phone once operations are complete
  - Backup phone contents
- music
  - Convert non-mp3 music files to mp3
  - cleanup non-mp3 music files
  - re-write music metadata to format more useful for phone
  - 
- podcast
  - some way to use podcasts on phone?
- ebook
  - is there any point to using this functionality?
- notes
  - maybe sync latest notes from NOTES folder?

There should maybe also be a gnereal update command, which might happend when you just run the tool without any input.




Setup
------

Expects a `.env` file in your project folder.