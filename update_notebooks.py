import nbformat as nbf
import os
import pybryt

from glob import glob
from otter.assign.solutions import strip_solutions_and_output, SOLUTION_CELL_TAG
from otter.assign.utils import add_tag, remove_output


def remove_notebook_solutions(nb):
    nb.cells = [add_tag(c, SOLUTION_CELL_TAG) if c.cell_type == "code" else c for c in nb.cells]
    nb = strip_solutions_and_output(nb)
    return nb


def main():
    ref_notebooks = glob("*-ref.ipynb")
    for ref in ref_notebooks:        
        print(f"Creating stripped version of {ref}")
        nb_path = os.path.splitext(ref)[0][:-4] + ".ipynb"

        nb = nbf.read(ref, as_version=nbf.NO_CONVERT)
        nb = remove_notebook_solutions(nb)
        nb["metadata"]["kernelspec"]["display_name"] = "py37_default"
        nb["metadata"]["kernelspec"]["name"] = "conda-env-py37_default-py"
        remove_output(nb)
        nbf.write(nb, nb_path)


if __name__ == "__main__":
    main()
