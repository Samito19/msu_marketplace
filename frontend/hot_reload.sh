#!/bin/bash

# Find the Brave browser window
BRAVE_WINDOW_ID=$(xdotool search --onlyvisible --class brave-browser)

# Send the signal to reload the page
xdotool windowactivate $BRAVE_WINDOW_ID
xdotool key --window $BRAVE_WINDOW_ID "Ctrl+r"
