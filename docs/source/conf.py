# -*- coding: utf-8 -*-


import os

# Add any Sphinx extension module names, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
import sys

import importlib_metadata

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../../"))

source_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(source_dir, "ext"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "numpydoc",
    "sphinx_multiversion",
    "sphinx_sitemap",
    "sphinx_gallery.gen_gallery",
]

# default url is a dummy for local build
html_baseurl = os.environ.get(
    "GITHUB_PAGES_URL", f"file://{os.path.dirname(source_dir)}/build/html/"
)
sitemap_locales = ["en"]
sitemap_url_scheme = "{link}"

numpydoc_show_class_members = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# Disabling generation of docs on different branches to use tags only
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"
smv_branch_whitelist = r"^main$"
smv_latest_version = r"^main$"

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "iohub"
copyright = "2023. Chan Zuckerberg Biohub. All rights reserved"
release = importlib_metadata.version("iohub")

json_url = f"{html_baseurl}/main/_static/switcher.json"
if "dev" in release or "rc" in release:
    # json_url = "_static/switcher.json"
    version_match = "latest"
else:
    version_match = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output --------------------------------------------------

html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "show_toc_level": 2,
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "iohub"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "resources/1.png"


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# emoji favicon code adapted from:
# https://twitter.com/LeaVerou/status/1241619866475474946
html_favicon = (
    "data:image/svg+xml,"
    "<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>"
    r"<text y=%22.9em%22 font-size=%2290%22>💾</text>"
    "</svg>"
)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["sidebar-nav-bs"]}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "iohubdoc"

numpydoc_show_class_members = False

# sphinx-gallery config
sphinx_gallery_conf = {
    "examples_dirs": "../examples",
    "gallery_dirs": "auto_examples",
    "download_all_examples": False,
    # "filename_pattern": "/run_",
    "min_reported_time": 2,
    "show_signature": False,
}
