# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides ...
=========================
...

Todo:
-----

Links:
------
- https://hevodata.com/learn/airtable-python/
- https://dev.to/matthewvielkind/using-python-and-airtable-3bb7

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import os
import re
import unicodedata
from typing import Any, Dict, List, Union

# Import | Libraries
from jinja2 import (
    Environment,
    FileSystemLoader,
    ChoiceLoader,
    select_autoescape,
)
from pyairtable import (
    Api,
    Base,
    Table,
)

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
DIR_TEMPLATES = os.path.join(DIR_ROOT, "templates")
DIR_EXPORT = os.path.join(DIR_ROOT, "export")

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"


# =============================================================================
# Definitions
# =============================================================================

def slugify(value, allow_unicode=False):
    """
    Taken from:
    https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize(
            "NFKD",
            value,
        ).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]', '", value.lower())
    return re.sub(r"[-\s]+', '-", value).strip("-_")


# Function | Write Template
def write_template(environment, context, template, export_path):
    """
    """

    template = environment.get_template(template)

    with open(export_path, "w") as fh:
        fh.write(template.render(context))


# =============================================================================
# Main
# =============================================================================

def main():
    """
    Main
    ====

    """

    # Jinja | Load Environment
    loader = ChoiceLoader([
        FileSystemLoader(searchpath = DIR_TEMPLATES),
    ])
    env = Environment(loader = loader)

    # Airtable | Load Tables
    api = Api(AIRTABLE_API_KEY)
    datasets = api.all(AIRTABLE_BASE_ID, "datasets")

    # iterate over the datasets
    for dataset in datasets:
        fields = dataset["fields"]
        print(fields)

        slug = slugify(fields["name_display"])

        # template_md = os.path.join(DIR_TEMPLATES, "dataset.md.jinja")
        template_md = os.path.join(DIR_TEMPLATES, "dataset.md")
        template_md = "dataset.md"
        template_json = os.path.join(DIR_TEMPLATES, "dataset.json.jinja")

        file_md = slug + ".md"
        path_md = os.path.join(DIR_EXPORT, "md", file_md)

        write_template(env, fields, template_md, path_md)


if __name__ == "__main__":
    main()
