%%capture
# The line above suppresses output. If there are errors, remove it.
# Execute this cell once to install and update all needed packages. Could take a while, please wait until this process is finished before continuing.
# When the cell is finished, the [*] to the left of the cell turns into a number, e.g. [1].
import sys
!{sys.executable} -m pip install git+https://github.com/SemWebNotebooks/Jupyter-RDFify.git -U
# The line below installs the python graphviz interface together with the grahpviz binaries.
# If you do not use anaconda, you need to install graphviz by hand and add it to your path as well as install the graphviz
# interface with pip (pip install graphviz)
!conda install --override-channels --yes --prefix {sys.prefix} -c conda-forge python-graphviz