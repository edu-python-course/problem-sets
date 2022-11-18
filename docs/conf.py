# This is a configuration file for the Sphinx documentation generator.
# It is used only to check documentation build in place.
# Major documentation will be generated within another project using another
# configuration.

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../src"))
project_copyright = \
    f"{datetime.now().year}, Python training course authors and contributors"
extensions = [
    "sphinx.ext.autodoc",
]
add_module_names = False
source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
exclude_patterns = []
suppress_warnings = []
language = "en"
html_theme_options = {
    "nosidebar": True,
}
