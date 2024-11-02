# Flask Project

An Document Intelligence powered bt Azure and flask.

## TL;DR

Make sure you have conda/mamba and node/nvm installed, and run:

```bash
nvm install && nvm use
npm install && npm run webpack
mamba env create
mamba activate wordle
python webapp.py --path ./path/to/file.txt              # In production mode or 
python webapp.py --debug --path ./words/default.txt     # In debug mode
```

## List of dependencies

<details> <!-- markdownlint-disable-line MD033 -->

[package.json]: package.json
[environment.yml]: environment.yml

### Python dependencies

|Package            |Version        |Channel        |Settings         |Remarks                |
|:------------------|:--------------|:--------------|:----------------|:---------------------:|
|python             |>=3.12.0       |conda-forge    |[environment.yml]|                       |
|flask              |>=3.0          |conda-forge    |[environment.yml]|                       |
|waitress           |>=3.0          |conda-forge    |[environment.yml]|                       |

### Javascript dependencies

|Package            |Version        |Channel        |Settings         |Remarks                |
|:------------------|:--------------|:--------------|:----------------|:---------------------:|
|typescript         |>=5.5          |npm            |[package.json]   |                       |
|sass               |>=1.77         |npm            |[package.json]   |                       |
|webpack            |>=5.93         |npm            |[package.json]   |                       |

</details>

## Install Python dependencies

- Install [miniconda](docs/miniconda.md) if needed
- Install [mamba](docs/mamba.md) if needed

### With YAML configuration

```bash
mamba env create                            # For production
mamba env create -f environment.dev.yml     # For development
mamba activate azure
```

</details>

## Install Javascript dependencies

- Install [nvm](docs/node.md) if needed

### Manually config nvm and node

```bash
nvm install
nvm use

npm install
```

## Webpack

```bash
npm run webpack                 # In production mode or
npm run webpack:watch           # In debug mode
```

## Ruff

```bash
ruff check .                # Check mode
ruff check . --watch        # Watch mode
```

## Run the app

```bash
python webapp.py            # In production mode or
python webapp.py --flask    # In flask mode or
python webapp.py --debug    # In debug mode
```

```text
    -h, --help                      Show this help message and exit
    -f, --flask                     Run under flask (default: False)
    -d, --debug                     Debug under flask (default: False)
    -t, --test                      Create app only (default: False)
    -s, --host HOST                 Server host (default: None)
    -p, --port PORT                 Server port (default: None)
```

### Log files

The log file is located at [handler.log]

## Create dotenv files for Secret and Tokens (if needed)

```dosini
# .env for production
# .env.dev for development 

AZURE_ENDPOINT=''
AZURE_API_KEY=''
```
