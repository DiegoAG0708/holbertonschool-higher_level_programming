#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and saves them to a file as JSON.
"""

import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise start with empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend list with command-line arguments
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, filename)
