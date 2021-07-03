# Jupyter Notebooks for Teaching Semantic Web Technologies

This repository contains the digital learning materials, scripts and documents employed by the [Chair of Information Systems at RWTH Aachen University](http://dbis.rwth-aachen.de/) to interactively teach Semantic Web Lectures with IPython Jupyter Notebooks.

All notebooks are developed based on [Jupyter-RDFify](https://github.com/SemWebNotebooks/Jupyter-RDFify), our IPython plugin bringing support for Semantic Web Technologies, such as Turtle, SPARQL, ShEx, etc., directly into the Jupyter Notebook ecosystem.

## Contents

File or path | Description
--- | ---
[workflow.pdf](Docs/Workflow/workflow.pdf) | A document describing the process of creating a jupyter notebook assignment and automatically grading it.
[SemWeb_jupyter_guide.pdf](Docs/SemWeb_jupyter_guide/SemWeb_jupyter_guide.pdf) | A document to teach students how to use JupyterHub or a local installation of Jupyter to open notebooks.
[Notebooks](Notebooks/) | This path contains the **student versions** of the SemWebNotebooks, which do **not** include the unit tests used for automatic grading. Please contact `semweb [at] dbis (dot) rwth-aachen {dot} de` if you want to get a copy  the full notebooks.
[moodle_nbgrader](Scripts/moodle_nbgrader) | This is a very slightly changed fork of [moodle_nbgrader by johnhw](https://github.com/johnhw/moodle_nbgrader). These are scripts used to change the moodle submission directory structure to the nbgrader directory structure.
[snippets](Scripts/snippets) | For code snippets used in notebooks or elsewhere.
[Evaluation](Evaluation.ipynb) | A quantitative summary of the [raw evaluation results](Eval_semweb_tool.xlsx) of our user study.

## Submodules & Libs

RDFLib: https://rdflib.readthedocs.io/en/stable/

RDFLib-jsonld: https://github.com/RDFLib/rdflib-jsonld

OWL-RL: https://owl-rl.readthedocs.io/en/latest/

Graphviz: https://graphviz.org
