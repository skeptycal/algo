#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" fileinput_example.py """
import fileinput
import sys
import time
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

# Establish the RSS and channel nodes
rss = Element('rss',
              {'xmlns:dc': "http://purl.org/dc/elements/1.1/",
               'version': '2.0'})
channel = SubElement(rss, 'channel')
title = SubElement(channel, 'title')
title.text = 'Sample podcast feed'
desc = SubElement(channel, 'description')
desc.text = 'Generated for PyMOTW'
pubdate = SubElement(channel, 'pubDate')
pubdate.text = time.asctime()
gen = SubElement(channel, 'generator')
gen.text = 'https://pymotw.com/'

for line in fileinput.input(sys.argv[1:]):
    mp3filename = line.strip()
    if not mp3filename or mp3filename.startswith('#'):
        continue
    item = SubElement(rss, 'item')
    title = SubElement(item, 'title')
    title.text = mp3filename
    encl = SubElement(item, 'enclosure',
                      {'type': 'audio/mpeg',
                       'url': mp3filename})

rough_string = tostring(rss)
reparsed = minidom.parseString(rough_string)
print(reparsed.toprettyxml(indent="  "))

""" References:

https://pymotw.com/3/fileinput/

Converting M3U files to RSS
An example of a filter is m3utorss, a program to convert a set of MP3 files into an RSS feed that can be shared as a podcast. The inputs to the program are one or more m3u files listing the MP3 files to be distributed. The output is an RSS feed printed to the console. To process the input, the program needs to iterate over the list of filenames and

- Open each file.
- Read each line of the file.
- Figure out if the line refers to an mp3 file.
- If it does, add a new item to the RSS feed.
- Print the output.

All of this file handling could have been coded by hand. It is not that complicated and, with some testing, even the error handling would be right. But fileinput handles all of the details, so the program is simplified.

The input() function takes as argument a list of filenames to examine. If the list is empty, the module reads data from standard input. The function returns an iterator that produces individual lines from the text files being processed. The caller just needs to loop over each line, skipping blanks and comments, to find the references to MP3 files.

Here is the complete program.

##########################################################################
This sample input file contains the names of several MP3 files.

```bash
# sample_data.m3u
# This is a sample m3u file
episode-one.mp3
episode-two.mp3
```

Running fileinput_example.py with the sample input produces XML data using the RSS format.

##########################################################################
$ python3 fileinput_example.py sample_data.m3u

<?xml version="1.0" ?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>Sample podcast feed</title>
    <description>Generated for PyMOTW</description>
    <pubDate>Sun Mar 18 16:20:44 2018</pubDate>
    <generator>https://pymotw.com/</generator>
  </channel>
  <item>
    <title>episode-one.mp3</title>
    <enclosure type="audio/mpeg" url="episode-one.mp3"/>
  </item>
  <item>
    <title>episode-two.mp3</title>
    <enclosure type="audio/mpeg" url="episode-two.mp3"/>
  </item>
</rss>
"""
