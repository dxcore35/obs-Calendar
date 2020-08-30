#!/bin/bash/python3

import pyperclip
import calendar
import re
import sys
from datetime import datetime as dt
from datetime import timedelta
import pathlib

#//////////////// SETTINGS ///////////////////

diary_regex = "!!!!MODIFY!!!!!"  # Daily notes pattern in Obsidian, pattern need to be standard regex pattern, it is not same as in Obsidian!
notes_folder = "!!!!MODIFY!!!!!" # Daily notes folder

# Trigger setting

trigger = sys.argv[1] # Clipboard from Keyboard maestro
trigger_regex = ":%Y_%m" # Trigger regex - same as regex for typing trigger in Keyboard Meastro
 
# Calendar settings
empty_days = " -  "                       # Define what will be inserted for days not in month
calendar.setfirstweekday(calendar.MONDAY) # Define start of the week

#/////////////////////////////////////////////

note_date = dt.strptime(trigger, trigger_regex)
year = int(note_date.strftime("%Y"))
month =int(note_date.strftime("%m"))
month_text = note_date.strftime("%B")

def Check_Status(day, notes_folder ,file):
    file = pathlib.Path(notes_folder + file + ".md")
    if not file.exists ():
        return "✎︎"
    else:
        return str(day)
    
def Stringify(input_seq, seperator):
    return seperator.join(input_seq)

# Markdow the month heading
month_header = "## " + month_text + "\n\n"

# Markdow the result headers
List_header = []
table_header = calendar.weekheader(3)
table_header = re.sub("(\w{3})", "|"+ r" \1" + "", table_header)

List_header.append(month_header)
List_header.append(table_header + "|\n")
List_header.append("|-----|-----|-----|-----|-----|-----|----|")

def Add_Obsidian_Links(date, day):
    return "| [[" + str(date) + "\|" + Check_Status(day, notes_folder,date) + "]]"

List_row = []
for row in calendar.monthcalendar(year,month):
    
    for days in row:
        day_string = '%d'%days

        if int(day_string) is 0:
            day_string = "|" + empty_days
        else:
            month_text = note_date.strftime("%B")
            year = note_date.strftime("%Y")
            day = str(day_string)
            
            day_string = dt.strptime(day +"-"+ month_text +"-" + year , "%d-%B-%Y")
            day_string = dt.strftime(day_string, diary_regex)  # Convert to user regex
            day_string = Add_Obsidian_Links(day_string, day)
        
        List_row.append(day_string)
    List_row.append('|\n')
    
Calendar = Stringify(List_header,' ') + "\n"
Calendar = Calendar + Stringify(List_row,' ')

# PRINT CALENDAR (WHEN RUNNING IN TERMINAL)
print(Calendar)              

# COPY TO CLIPBOARD
pyperclip.copy(Calendar)
pyperclip.paste