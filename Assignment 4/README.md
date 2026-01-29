# Assignment 4

This folder contains two Python tasks about file operations.

## Task 1 - Reading from a File

This program reads the first two lines from a file called sample.txt.

It uses a try-except block to handle errors. First it tries to open the file in read text mode ('rt'). Then it reads the first line and stores it, then reads the second line and stores it.

After that it prints both lines with labels.

If the file doesn't exist, it catches the FileNotFoundError and prints a message saying the file wasn't found instead of crashing.

## Task 2 - Writing and Appending to a File

This program writes to a file, appends more text to it, then reads everything back.

First it opens a file called output.txt in write text mode ('wt'). It asks you to enter some text, then writes that text to the file with a newline at the end. It prints a success message.

Then it opens the same file again but in append text mode ('at'). It asks for more text and adds it to the end of the file (doesn't overwrite what was already there). Prints another success message.

Finally it opens the file in read text mode ('rt') and reads all the content. It prints the final content so you can see everything that's in the file.
