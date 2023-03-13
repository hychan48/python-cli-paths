# python-cli-paths
Trying out python cli / paths


https://github.com/google/python-fire


```bash
# in another project
poetry init

poetry shell

cd ../python-cli-paths/dist
# easier to use local path i guess
# add 
[tool.poetry.dependencies]
my-package = { file = "path/to/wheel.whl" }

poetry remove 
```


```bash
# want:
pli hello param

# current:
python path_hello.py param


# https://stackoverflow.com/questions/59286983/how-to-run-a-script-using-pyproject-toml-settings-and-poetry
poetry update # after updating pyproject.toml
# dont need to update in another scirpt yet
poetry run my_package_cli
# probably need to add an alias or something
#https://github.com/python-poetry/poetry/issues/2496

#rename poetry perhaps?
# check rasa imo
```