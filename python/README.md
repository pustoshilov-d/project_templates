## Extensions you have to use:
- Python: [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Black Formatter (code auto formatting): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- Ruff (format and lint): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- Mypy (types checking and lint): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=matangover.mypy)
- autoDocstring (one format for docstings): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- Pylance (intellenge code): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- IntelliCode (intellenge code): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
- Python Indent (Correct Python indentation): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- SSH Remote (ssh): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

[Optional]: 
- Django (snippents): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- Even Better Toml (toml snippents): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)
- Python Extended Snippets (snippents): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=tushortz.python-extended-snippets)
- TODOs (write # TODO: add some feature there): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
- GitLens (shows merge conflicts and line's author): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens-insiders)
- Change Case (change case of selected text): [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=wmaurer.change-case)



### Setup Env

1. Install [mamba](https://github.com/conda-forge/miniforge)
```shell script
wget -P ~/ "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash ~/Mambaforge-$(uname)-$(uname -m).sh
rm Mambaforge-$(uname)-$(uname -m).sh
```
restart a terminal

2. Create environment
```shell script
micromamba env create -y -n new-env -f env.yml
micromamba activate new-env
```

3. Set up git hooks
```shell script
git config --local core.hooksPath .githooks/
```

### Update env
```shell script
micromamba env update -n new-env -f env.yml --prune
```