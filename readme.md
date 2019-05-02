# project version 0.0.1



05-01-2019 | 20:18:10

---

## portfolio project for macOS

```bash


###############################################################################
# project : portfolio project for macOS (version 0.0.1)

# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal

# Usage: project {init|reset|version|help}

#   Parameters:
#       init, -i, --init        -- install and initialize
#       reset, -r, --reset      -- reset initial repo files (with backup)
#       version, -v, --version  -- display version information
#       help, -h, --help        -- display usage and information

#   .pre-commit-template.yaml must be in current directory
#       If not, a generic template will be created
#   .pre-commit-bak.yaml will be created (if possible)
#       from .pre-commit-config.yaml as backup
#   .pre-commit-config.yaml will be *overwritten*
#       and updated to current master sha from GitHub
###############################################################################


# Run this script if changes to the pre-commit or yaml configuration are added.

# Please make changes directly to the 'template' file:
#     <.pre\-commit-template.yaml>
# and run the script 'pc' to update the yaml to current versioning.

# Please do not make changes directly to the 'config' file. The 'config' file:
#     <.pre-commit-config.yaml>
#   is created and updated by the 'pc' script automatically in order to maintain
#   the correct, current versioning from git (master sha) so changes to the
#   commit file will be overwritten when updating.
###############################################################################


```


---

```bash

.
├── Mandelbrot_lines.py
├── Mersenne_sequence.py
├── Pipfile
├── Pipfile.lock
├── SqRoot_Finder.pyw
├── SqRoot_Finder.zip
├── bak
│   └── README.bak.md
├── bin_packing.py
├── codecov.yml
├── collatz_conjecture
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── collatz.py
│   └── tempCodeRunnerFile.py
├── datasets
│   ├── corncob_caps.txt
│   ├── corncob_lowercase.txt
│   └── english-words-master.zip
├── datatime.py
├── flask-realworld-example-app-master
│   ├── LICENSE
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── Procfile
│   ├── README.rst
│   ├── Vagrantfile
│   ├── autoapp.py
│   ├── conduit
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── articles
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   ├── commands.py
│   │   ├── compat.py
│   │   ├── database.py
│   │   ├── exceptions.py
│   │   ├── extensions.py
│   │   ├── profile
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   ├── settings.py
│   │   ├── user
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   └── utils.py
│   ├── image.png
│   ├── requirements
│   │   ├── dev.txt
│   │   └── prod.txt
│   ├── requirements.txt
│   ├── setup.cfg
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       ├── factories.py
│       ├── test_articles.py
│       ├── test_authentication.py
│       ├── test_config.py
│       ├── test_models.py
│       └── test_profile.py
├── map_fil_red
│   └── map_fil_red.py
├── ml_flask
│   ├── README.md
│   ├── credentials.json
│   ├── diabetes-model.pkl
│   ├── diabetes_redsamurai_db.ipynb
│   ├── diabetes_redsamurai_endpoint_db.ipynb
│   ├── diabetes_redsamurai_endpoint_db.py
│   ├── invoice-automation-d1.ipynb
│   ├── invoice-automation-d2.ipynb
│   ├── invoice-risk-model-local.ipynb
│   ├── invoice_data_adjusted.csv
│   ├── invoice_data_prog_processed.csv
│   └── ml_flask.py
├── np_loops.py
├── pima-indians-diabetes.data.csv
├── readme.md
├── requirements.txt
└── temperatures_test.py

12 directories, 76 files
```
