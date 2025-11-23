import re
import os

# Configuration
MY_NAME = "Your Name" # Update this to your name to bold it in the author list
BIB_FILE = "_data/references.bib"
YML_FILE = "_data/publications.yml"
BIB_OUTPUT_DIR = "assets/bibs"

def parse_bibtex(bib_content):
    """
    Simple BibTeX parser.
    Assumes standard format, one field per line.
    """
    entries = []
    current_entry = {}

    # Match @type{key,
    entry_start_pattern = re.compile(r'@(\w+)\{([^,]+),')
    # Match field = {value} or field = "value"
    field_pattern = re.compile(r'\s*(\w+)\s*=\s*[\{"](.*)[\}"]\s*,?')

    lines = bib_content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue

        start_match = entry_start_pattern.match(line)
        if start_match:
            if current_entry:
                entries.append(current_entry)
            current_entry = {
                'type': start_match.group(1),
                'key': start_match.group(2),
                'raw_bib': [line]
            }
            continue

        if line == '}' and current_entry:
            current_entry['raw_bib'].append(line)
            entries.append(current_entry)
            current_entry = {}
            continue

        if current_entry:
            current_entry['raw_bib'].append(line)
            field_match = field_pattern.match(line)
            if field_match:
                key = field_match.group(1).lower()
                value = field_match.group(2)
                current_entry[key] = value

    if current_entry:
        entries.append(current_entry)

    return entries

def format_authors(author_str):
    """
    Format author list.
    1. Split by ' and '.
    2. Bold MY_NAME.
    3. Join with ', '.
    """
    if not author_str:
        return ""

    authors = author_str.split(' and ')
    formatted_authors = []

    for author in authors:
        author = author.strip()
        if MY_NAME in author:
            if author.startswith(MY_NAME):
                author = author.replace(MY_NAME, f"<strong>{MY_NAME}</strong>")
            else:
                author = author.replace(MY_NAME, f"<strong>{MY_NAME}</strong>")
        formatted_authors.append(author)

    return ", ".join(formatted_authors)

def generate_single_bib(entry, output_dir):
    """
    Generate single bib file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"{entry['key']}.bib"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(entry['raw_bib']))

    return f"/{output_dir}/{filename}"

def main():
    if not os.path.exists(BIB_FILE):
        print(f"Error: {BIB_FILE} not found.")
        return

    with open(BIB_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = parse_bibtex(content)
    yml_data = []

    for entry in entries:
        yml_entry = {}

        # Required fields
        yml_entry['title'] = entry.get('title', 'No Title')
        yml_entry['authors'] = format_authors(entry.get('author', ''))

        # Optional fields
        if 'url' in entry: yml_entry['url'] = entry['url']
        if 'code' in entry: yml_entry['code'] = entry['code']
        if 'page' in entry: yml_entry['page'] = entry['page']
        if 'image' in entry: yml_entry['image'] = entry['image']
        if 'notes' in entry: yml_entry['notes'] = entry['notes']
        if 'tags' in entry: yml_entry['tags'] = entry['tags']

        # Conference/Journal
        if 'booktitle' in entry:
            yml_entry['conference'] = entry['booktitle']
        elif 'journal' in entry:
            yml_entry['conference'] = entry['journal']

        # Generate single bib file link
        bib_link = generate_single_bib(entry, BIB_OUTPUT_DIR)
        yml_entry['bibtex'] = bib_link

        yml_data.append(yml_entry)

    # Write YAML
    with open(YML_FILE, 'w', encoding='utf-8') as f:
        f.write("main:\n")
        for entry in yml_data:
            f.write(f"  - title: \"{entry['title']}\"\n")
            f.write(f"    authors: \"{entry['authors']}\"\n")

            for key in ['url', 'code', 'page', 'image', 'notes', 'tags', 'conference', 'bibtex']:
                if key in entry:
                    val = entry[key]
                    val = val.replace('"', '\\"')
                    f.write(f"    {key}: \"{val}\"\n")
            f.write("\n")

    print(f"Successfully generated {YML_FILE} from {BIB_FILE}")
    print(f"Generated {len(entries)} entries.")

if __name__ == "__main__":
    main()
