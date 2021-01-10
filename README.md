# 15AI Name Maker

This short script is intended to assist anyone preparing a submission for the 
website linked below

https://15.ai/contribute

## Prerequisites

This is only supported on Microsoft Windows platforms and only requires a modern (3.x.x minimum) version of python to be 
installed. 

I suggest installing the linked version, though anything 3.x.x should work
https://www.python.org/downloads/release/python-380/

**Make sure to add python to your windows path and reboot your computer on install
in the advanced install options**

## Usage

Download this project however you like and follow these steps

1) Delete the file named `delete_me.wav` in the `audio_files` directory. This has to be here so I can commit a correctly named directory (audio_files.) 
   It's a fake wav file, open it in notepad for a surprise!
1) Copy your music files into the `audio_files` directory
2) Double click on the main script - `make_audio_path_file.py`
3) A file called `report.txt` will appear in the same directory and contain your results

You may also run this in command line by `cd`ing into this projects directory and running

* `python make_audio_path_file.py`

## License

This program is licensed to you under the GNU-GPL (https://www.gnu.org/licenses/gpl-3.0.en.html) with the
stipulation that it is not used for evil purposes.
