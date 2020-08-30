# Inserting of the linked Calendar with all your daily notes

This script does the following:

1) __Keyboard maestro extension as trigger of the script__
2) __Script__

- Scans your daily notes in fixed location (based on regex of file name)
- Create markdown table 
- Add daily notes [[links]] into calendar
- Pushes the linked text back to the clipboard

## Requirements

* Keyboard maestro (Mac OS)
* Python 3 + pip
* [Pyperclip](https://pypi.org/project/pyperclip/) - Note that Mac and Linux may require installation of additional modules as per docs
* [PyYAML](https://pypi.org/project/PyYAML/)

```pip install pyperclip pyyaml```

## Setup

1. Install Keyboard meastro script
2. Open Keyboard maestro and replace PATH with path to your script (```"./Obsidian/Scripts/obs-insert_calendar.py```
2. Copy script ```(obs-insert_calendar.py)``` in fixed folder
3. Open script ```(obs-insert_calendar.py)```in text editor and edit values to fit your settings:
	- __diary_regex__ - change to regex of the names of your daily notes
	- __notes_folder__ - to location of your daily notes folder in Obsidian
4. You can also change additional variables in the script to tweak to Calendar look

## Example

Assuming you had the following daily notes in your Obsidian vault:

- __diary_regex__ =   ```"%d-%b-%y"```
- __notes_folder__ =  ```"/Obsidian/Diary/"```

Your daily notes looks like:

- ```04-Aug-20.md```
- ```05-Aug-20.md```
- ```06-Aug-20.md```

And the following text is typed in Obsidian:

```:2020_08```

After executing the script, it would be replaced with the following:

![](https://github.com/dxcore35/obs-Calendar/blob/master/Calendar.jpg)

## Notes

This tool will help to collect daily notes add insert them in handy calendar with all links to individual note. It was intented to be user with Keyboard maestro app. And also with typing trigger. The script can be easily triggered from terminal as well and it is easy to be adapted to for example AutoHotkey in Windows.
