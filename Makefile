JUPYTER = jupyter

markdown:
	$(JUPYTER) nbconvert *.ipynb --to markdown --ExtractOutputPreprocessor.enabled=False
