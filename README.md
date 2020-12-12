# FilenameFixer
Replaces given chars in all filenames contained within a given directory.

## Download:
[macOS Binary](https://github.com/jonathannwinters/FilenameFixer/raw/main/FilenameFixer)

[Windows Binary] **Coming soon

## Help:

usage: FilenameFixer.py [-h] [--version] [-r] [-v] [-l LOG] [-c COPY]
                        [--analyze ANALYZE] [--dirs-only DIRS_ONLY]
                        [--files-only FILES_ONLY]
                        path current_character new_character

Replaces given chars in all filenames contained within a given directory.
NOTE: This program does not yet correct directory names.

positional arguments:
  path                  Specify path to directory.
  current_character     Character to convert from.
  new_character         Character to convert to.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -r, --recursive       Applies the specified character substitution
                        recursively to the file hierarcy rooted at the given
                        path
  -v, --verbose         Causes FilenameFixer to be verbose, showing full file
                        path as they are changed.
  -l LOG, --log LOG     Specify path to write log file.
  -c COPY, --copy COPY  FEATURE NOT YET DEVELOPED: Copies the entire directory
                        structure and contained files to specified locations,
                        replacing the specified character in each file path.
  --analyze ANALYZE     FEATURE NOT YET DEVELOPED: Search for potential
                        problem file and directory names.
  --dirs-only DIRS_ONLY
                        FEATURE NOT YET DEVELOPED: Replaces given character in
                        directory paths only.
  --files-only FILES_ONLY
                        FEATURE NOT YET DEVELOPED: Replaces given character in
                        file names only and does not modify directories.
