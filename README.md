# python-cli-paths
Trying out python cli / paths
asdfasdfasdf

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

Set-Alias -Name pli -Value "poetry run"

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
```ps1

[//]: # https://powershell-guru.com/powershell-tip-35-list-and-remove-a-function/()
[//]: # ( Remove-Item -Path Alias:pli)
Remove-Item -Path Function:pli

[//]: # (function pli&#40;[string]$input_str,[string]$input_str2&#41;)
function pli([string]$input_str)
{
    poetry run my_package_cli $input_str
}
https://seankilleen.com/2020/04/how-to-create-a-powershell-alias-with-parameters/
function Encode-Video([string]$VideoFileName, [string]$OutputFileName)
{
    ffmpeg -i "$VideoFileName" -vcodec h264 -acodec mp2 "$OutputFileName"
}

function Encode-Video([string]$VideoFileName, [string]$OutputFileName)
{
    ffmpeg -i "$VideoFileName" -vcodec h264 -acodec mp2 "$OutputFileName"
}
```