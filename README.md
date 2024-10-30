# Flask Template

A Flask framework template.

Utilizing python, and flask, running on waitress for backend;
typescript, tailwindcss, metroui, htmx and sass bundled by webpack for frontend.

## Using this template

[Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template)

## Git clone repository with gh cli

```bash
gh repo clone user/your-project -- --recursive -j8 --branch main
```

### List of submodule

///

## List of dependencies

<details> <!-- markdownlint-disable-line MD033 -->

[package.json]: package.json
[environment.yml]: environment.yml
[setting.py]: webapp/config/setting.py

### Python dependencies

|Package            |Version        |Channel        |Settings         |Remarks                |
|:------------------|:--------------|:--------------|:----------------|:---------------------:|
|python             |>=3.11.0       |conda-forge    |[environment.yml]|                       |
|flask              |>=3.0          |conda-forge    |[environment.yml]|                       |
|waitress           |>=3.0          |conda-forge    |[environment.yml]|                       |
|apscheduler        |>=3.10.0       |conda-forge    |[environment.yml]|                       |
|cython             |>=3.0.10       |conda-forge    |[environment.yml]|                       |
|python-dotenv      |>=1.0.0        |conda-forge    |[environment.yml]|                       |
|regex              |>=2023.12.25   |conda-forge    |[environment.yml]|                       |

### Javascript dependencies

|Package            |Version        |Channel        |Settings         |Remarks                |
|:------------------|:--------------|:--------------|:----------------|:---------------------:|
|typescript         |>=5.5          |npm            |[package.json]   |                       |
|tailwindcss        |>=3.4          |npm            |[package.json]   |                       |
|sass               |>=1.77         |npm            |[package.json]   |                       |
|webpack            |>=5.93         |npm            |[package.json]   |                       |
|metroui            |==5.0.6        |cdn            |[setting.py]     |                       |
|htmx               |>=2.0.0        |cdn            |[setting.py]     |                       |

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

### For Deployment

```bash
python compile.py           # Compile codes only or
python deploy.py            # Compile and deploy code

unzip deploy.zip -d deploy  # Unzip the zip anywhere you want
cd deploy                   # Change directory into the unzip directory
python webapp.py            # "mamba env create" on remote if needed
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
