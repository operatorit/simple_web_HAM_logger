# Simple Web HAM Logger
by Janek, operator-paramedyk.pl

# Project idea

Simple Web HAM Logger is a Python project aimed to develop web application for logging amateur radio (HAM) calls (QSOs). It's an educational project startted to improve my coding skills. 

Project is based on Django framework. Core functionalities are based on tutorial "Project 3: Web Applications" in "Python Crash Course 2nd Edition" by Eric Matthes (No Starch Press).

# Project structure

├── HAM_logger
│   ├── migrations
│   └── templates
│       └── HAM_logger
├── simple_web_HAM_logger
└── users
    ├── migrations
    └── templates
        ├── registration
        └── users

# Release notes

## v1.0 2024-OCT-28
First version deployed with basic logging functionalities.
- separate logs for each user,
- user defines activities to group similar QSOs.

### TODO:
- inputs validation for report,
- ADIF export.

# Application logic

It's an application supporting HAM radio operators with logging QSOs with other amateurs.

Each user has it's own account and cannot view other's QSOs.
QSOs are groupped in activations.
 
