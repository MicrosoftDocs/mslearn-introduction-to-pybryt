JUPYTER = jupyter

markdown:
	$(JUPYTER) nbconvert *.ipynb --to markdown --ExtractOutputPreprocessor.enabled=False --TagRemovePreprocessor.remove_cell_tags remove
