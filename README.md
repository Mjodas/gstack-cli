# Gstack-cli

This is a set of simple scripts made to quickly access Google services such as Google Calendar and Drive.

**Features:**
- [x] add calendar events.
- [x] list calendar events.
- [ ] simple google drive tasks. Add, remove, list files etc.
- [ ] ?

**Todo:**
- [] handle input errors.
- [] parse dates in not so lazy way.

# Setup

1. Retrieve API key and credential file from https://developers.google.com/. API key need calendar and drive access.
2. Set credential file path in paths.py
3. Add alias to the scripts in .bash_profile.

Example on alias:

alias addcal="python3 /Users/Mjods/Documents/development/gstack-cli/add_event.py"

alias lscal="python3 /Users/Mjods/Documents/development/gstack-cli/list_events.py"
