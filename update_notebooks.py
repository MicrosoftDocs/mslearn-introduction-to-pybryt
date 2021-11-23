import nbformat as nbf
import os
import pybryt

from glob import glob
from otter.assign.solutions import strip_solutions_and_output, SOLUTION_CELL_TAG
from otter.assign.utils import add_tag


def remove_notebook_solutions(nb_path, write_path):
    nb = nbf.read(nb_path, nbf.NO_CONVERT)
    nb.cells = [add_tag(c, SOLUTION_CELL_TAG) if c.cell_type == "code" else c for c in nb.cells]
    nb = strip_solutions_and_output(nb)
    nbf.write(nb, write_path)


def main():
    ref_notebooks = glob("*-ref.ipynb")
    for ref in ref_notebooks:        
        print(f"Creating stripped version of {ref}")
        nb_path = os.path.splitext(ref)[0][:-4] + ".ipynb"
        remove_notebook_solutions(ref, nb_path)

    all_notebooks = glob("*.ipynb")
    for nb_name in all_notebooks:
        nb = nbf.read(nb_name, as_version=nbf.NO_CONVERT)
        nb["metadata"]["kernelspec"]["name"] = "conda-env-py37_default-py"
        nbf.write(nb, nb_name)


if __name__ == "__main__":
    main()
