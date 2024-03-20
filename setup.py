#!/usr/bin/env python

from distutils.core import setup

setup(name='Activetigger',
      version='0.0.6',
      description='Active Tigger in Python',
      author='Émilien Schultz',
      author_email='emilien.schultz@gmail.com',
      url='https://github.com/emilienschultz/pyactivetigger',
      packages=['activetigger'],
      py_modules = ['api', 'server','widget',"datamodels","functions","models"],
      install_requires=["fastapi[all]",
		"requests",
		"uvicorn",
		"argparse",
		"datasets",
		"fasttext",
		"ipywidgets",
		"IPython",
		"numpy",
		"pandas",
		"pyarrow",
		"torch",
		"transformers[torch]",
		"sentence_transformers",
		"typing-inspect",
		"typing_extensions",
		"spacy",
		"pyyaml",
		"protobuf",
		"umap-learn",
		"distinctipy",
		"python-jose[cryptography]",
		"bcrypt",
		"plotly",
		"matplotlib",
		"scikit-learn"]
     )
