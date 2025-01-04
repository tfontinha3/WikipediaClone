import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
import markdown2 

def list_entries():
    """Returns a list of all entry names."""
    entries = os.listdir('entries')
    entries = [entry[:-3] for entry in entries if entry.endswith('.md')]
    return entries

def get_entry(title):
    """Returns the HTML content of an entry given its title."""
    try:
        with open(f'entries/{title}.md', 'r') as file:
            content = file.read()
            return markdown2.markdown(content)  # Convert Markdown to HTML
    except FileNotFoundError:
        return None

def save_entry(title, content):
    """Saves an entry to disk."""
    with open(f'entries/{title}.md', 'w') as file:
        file.write(content)

