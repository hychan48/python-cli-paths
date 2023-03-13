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
```