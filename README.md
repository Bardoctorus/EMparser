# EM Parser - a workaround tool for a lazy content creator

This is a tool that probably noone would ever find useful except me.

You need a file in the **input** dir which is called ems0XX.txt where XX is the ep number

Usage: python3 parser.py EPISODENUMBER YOUTUBELINK "Short introductory paragraph"

EPISODENUMBER: suprisingly, the episode number, it's important you just put in the number with no leading digits as it gets used to create the input file
YOUTUBELINK: just the id part of the link, so Z8mGY9m41C8 for example
"short intro" is exactly that "This week we look at a cat with a really large head"


It spits out text files designed to go in YouTube, Libsyn, and Mailchimp - the latter two as HTML to stop the madness of copying and pasting it all
