# -*- coding: utf-8 -*-
#
# hydromt_sfincs documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 24 15:19:00 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shutil
import hydromt
import hydromt_sfincs
from distutils.dir_util import copy_tree

here = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(here, "..")))


def remove_dir_content(path: str) -> None:
    for root, dirs, files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
    if os.path.isdir(path):
        shutil.rmtree(path)


# -- Project information -----------------------------------------------------

project = "HydroMT SFINCS"
copyright = "Deltares"
author = "Dirk Eilander"

# The short version which is displayed
version = hydromt_sfincs.__version__

# # -- Copy notebooks to include in docs -------
# if os.path.isdir("_examples"):
#     remove_dir_content("_examples")
# os.makedirs("_examples")
# copy_tree("../examples", "_examples")

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "nbsphinx",
]

autosummary_generate = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"
# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "_static/hydromt-icon.svg"
autodoc_member_order = "bysource"  # overwrite default alphabetical sort
autoclass_content = "both"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["theme-deltares.css"]
html_theme_options = {
    "show_nav_level": 2,
    "navbar_align": "content",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deltares/hydromt_sfincs",  # required
            "icon": "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",
            "type": "url",
        },
        {
            "name": "SFINCS",
            "url": "https://sfincs.readthedocs.io/",
            "icon": "_static/sfincs_logo_mHv_icon.ico",
            "type": "local",
        },
        {
            "name": "Deltares",
            "url": "https://www.deltares.nl/en/",
            "icon": "_static/deltares-blue.svg",
            "type": "local",
        },
    ],
    "external_links": [
        {
            "name": "HydroMT core",
            "url": "https://deltares.github.io/hydromt/latest/index.html",
        },
    ],
    "logo": {
        "text": "HydroMT SFINCS",
    },
    "navbar_end": ["navbar-icon-links"],  # remove dark mode switch
}


html_context = {
    "github_url": "https://github.com",  # or your GitHub Enterprise interprise
    "github_user": "Deltares",
    "github_repo": "hydromt_sfincs",
    "github_version": "main",  # FIXME
    "doc_path": "docs",
    "default_mode": "light",
}

remove_from_toctrees = ["_generated/*"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     "**": [
#         "relations.html",  # needs 'show_related': True theme option to display
#         "searchbox.html",
#     ]
# }

nbsphinx_allow_errors = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "hydromt_sfincs_doc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "hydromt_sfincs.tex",
        "HydroMT sfincs plugin Documentation",
        [author],
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "hydromt_sfincs", "HydroMT SFINCS plugin Documentation", [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "hydromt_sfincs",
        "HydroMT sfincs plugin Documentation",
        author,
        "HydroMT sfincs plugin",
        "Miscellaneous",
    ),
]

# -- INTERSPHINX -----------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    # "numba": ("https://numba.pydata.org/numba-doc/latest", None),
    # "matplotlib": ("https://matplotlib.org/stable/", None),
    # "dask": ("https://docs.dask.org/en/latest", None),
    "rasterio": ("https://rasterio.readthedocs.io/en/latest", None),
    "geopandas": ("https://geopandas.org/en/stable", None),
    "xarray": ("https://docs.xarray.dev/en/stable", None),
    "hydromt": ("https://deltares.github.io/hydromt/latest/", None),
}

# -- NBSPHINX --------------------------------------------------------------

# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None).split('\\')[-1].split('/')[-1] %}

.. TIP::

    .. raw:: html

        <div>
            For an interactive online version click here: 
            <a href="https://mybinder.org/v2/gh/Deltares/hydromt_sfincs/main?urlpath=lab/tree/examples/{{ docname|e }}" target="_blank" rel="noopener noreferrer"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg"></a>
        </div>
"""
