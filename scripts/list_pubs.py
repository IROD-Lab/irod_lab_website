import os
import glob
from pybtex.database import parse_string

def clean_and_parse(filename):
    """
    Reads the file as text first, removes duplicate 'doi =' lines inside entries,
    and then parses it. This prevents pybtex from crashing on Zotero exports.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    seen_fields = set()
    inside_entry = False

    for line in lines:
        stripped = line.strip().lower()

        # Detect start of a new entry
        if stripped.startswith("@"):
            seen_fields = set()
            inside_entry = True
            cleaned_lines.append(line)
            continue

        # Check for duplicates inside an entry
        if inside_entry and "=" in stripped:
            field_part = stripped.split("=")[0].strip()
            
            # If it is a DOI and we already saw one, skip this line
            if field_part == "doi":
                if "doi" in seen_fields:
                    continue 
                seen_fields.add("doi")
        
        cleaned_lines.append(line)

    return parse_string("\n".join(cleaned_lines), bib_format='bibtex')

def render_pubs(bib_file, author_highlight=None):
    if not os.path.exists(bib_file):
        print(f"**Error:** Could not find bibliography file: `{bib_file}`")
        return

    try:
        bib_data = clean_and_parse(bib_file)
    except Exception as e:
        print(f"**Error parsing bib file:** {e}")
        return

    # 1. Define Categories
    categories = {
        "Journal Articles": ["article"],
        "Conference Papers": ["inproceedings", "proceedings"],
        "Books and Chapters": ["book", "incollection"],
        "Theses": ["phdthesis", "mastersthesis"]
    }

    # 2. Sort entries by year first
    all_entries = sorted(bib_data.entries.items(), 
                         key=lambda x: x[1].fields.get('year', '0000'), 
                         reverse=True)

    # 3. Iterate through categories and print
    for cat_name, types in categories.items():
        # Filter entries for this category
        cat_entries = [e for e in all_entries if e[1].type.lower() in types]
        
        if not cat_entries:
            continue

        print(f"### {cat_name}")
        
        for key, entry in cat_entries:
            year = entry.fields.get('year', 'n.d.')
            title = entry.fields.get('title', 'Untitled').replace("{", "").replace("}", "")
            
            # Smart Venue Detection
            venue = entry.fields.get('journal', 
                        entry.fields.get('booktitle', 
                            entry.fields.get('publisher', 
                                entry.fields.get('school', 'Preprint'))))
            
            doi = entry.fields.get('doi', '')
            doi_str = f" [[Link](https://doi.org/{doi.replace('https://doi.org/', '')})]" if doi else ""
            
            # Format Authors
            authors = []
            for person in entry.persons.get('author', []):
                # Handle cases where first_names or last_names might be empty
                fname = person.first_names[0] if person.first_names else ""
                lname = person.last_names[0] if person.last_names else ""
                name = f"{fname} {lname}".strip()
                
                if author_highlight and author_highlight in name:
                    name = f"**{name}**"
                authors.append(name)
            
            author_str = ", ".join(authors)

            # Print the final Markdown Bullet
            print(f"1. {author_str} ({year}). **{title}.** *{venue}*.{doi_str}")
        print("\n") # Add space between sections

def get_current_page_title():
    qmd_files = glob.glob("*.qmd")
    if not qmd_files: return None
    target_file = qmd_files[0]
    with open(target_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("title:"):
                return line.split(":", 1)[1].strip().strip('"').strip("'")
    return None

def render_auto():
    clean_name = get_current_page_title()
    bib_files = glob.glob("*.bib")
    if not bib_files:
        print("*No bibliography found in this folder.*")
        return
    for bib in bib_files:
        render_pubs(bib, author_highlight=clean_name)