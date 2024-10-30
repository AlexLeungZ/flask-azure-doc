# Flask Project

To be updated.

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

### A. With YAML configuration

```bash
mamba env create                            # For production
mamba env create -f environment.dev.yml     # For development
mamba activate flask
```

### B. With CLI

<details> <!-- markdownlint-disable-line MD033 -->

```bash
mamba create -n flask
mamba activate flask

mamba install -c conda-forge flask cython waitress python-dotenv -y
mamba install -c conda-forge apscheduler regex -y

# Dev dependencies
mamba install -c conda-forge ipykernel djlint ruff -y
```

</details>

## Install Javascript dependencies

- Install [nvm](docs/node.md) if needed

### Automatically Compile TypeScript and Sass on change

```bash
nvm use
npm install
```

## CLI cheat sheet

### For Development

```bash
npm webpack                 # In production mode or
npm webpack:watch           # In debug mode

python webapp.py            # In production mode or
python webapp.py --flask    # In flask mode or
python webapp.py --debug    # In debug mode
```

## Create dotenv files for Secret and Tokens (if needed)

```dosini
# .env for production
# .env.dev for development 

# Flask app Secret Key
SECRET_KEY=...
# Other Tokens (if any)
TOKEN=...
```
