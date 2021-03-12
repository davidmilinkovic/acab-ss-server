# Screenshot server

The goal of this project is to extract messages from several selected Viber groups and determine few different parameters such as which group was the message been sent into, time of the delivery, etc.

This is the first part of the bigger project - A police patrol locating platform. Extracted data would be sent to the external server, which would map the messages to the exact locations on the map.

With the lack of Viber API, we resorted to an unconventional way of extracting viber messages - we used python mouse control tools to select messages and copy the texts, as well as determine the the current group from the screenshot.

## groupNameExtraction.py

This scipt screenshots the viber interface, crops the image while focusing on the group with latest messages and applies integrated text recognition model to extract the name of the group from the image

## scroller.py

Description...

## main.py
Description...
