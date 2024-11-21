# Simple Web HAM Logger
by Janek, operatorit.pl

# Project idea

Simple Web HAM Logger is a Python project aimed to develop web application for logging amateur radio (HAM) calls (QSOs). It's an educational project startted to improve my coding skills. 

Project is based on Django framework. Core functionalities are based on tutorial "Project 3: Web Applications" in "Python Crash Course 2nd Edition" by Eric Matthes (No Starch Press).

# License

Simple Web HAM Logger is distributted on __BSD 3-Clause License__ shared in ```license.md``` file in project's folder.

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
It's a very long-term plan (or dream rather), but I would like to extend this application with:
- test coverage,
- inputs validation for report fields,
- removing QSOs,
- removing activities,
- captcha for user's registration,
- radioshack/antenna/power selection,
- visualisations of QSOs,
- ADIF export.

# Amateur (HAM) radio

It's an application supporting HAM radio operators with logging QSOs with other amateurs. HAM (or amateur) radio operators are a hobbysts that use radio devices to connect with... other operators (or "stations"). Basic setup is a radio (tranceiver) connected to antenna(s) and power supply. It may be portable (handheld), mobile (mounted in a car/boat/plane) or stationary. Dependent on the hardware, radio amateurs connect (make QSOs) using CW (morse telegraphy), phone, or data transmission modes. There are also specific "projects", like QSOs via moon (EME), aurora, satelites, terrain activities (SOTA/POTA - the one where I'm active in), contests... If you are interested in this topic, you can find more in the web, starting from [Wikipedia](https://en.wikipedia.org/wiki/Amateur_radio).

# Application logic

In this application, each user has it's own account and cannot view other's QSOs. In the application, user is a __person or club__, and may use different callsigns in its account (however can also establish different accoutns for different callsigns).

QSOs are groupped in activations. Thus, you need to create an activation first, than add QSO there. Each QSO needs to be assigned to an activation. It's the logic I've learned through the activations and use when logging QSOs (yeah, one of my activations is just "HOME").

User can edit and delete QSOs and activations.

# Deployment

To run the application on your end:
1. Download/clone the repository.
```
git clone https://github.com/operatorit/simple_web_HAM_logger/tree/main
```
2. In project's folder, create and activate  virtual environment. Here I present venv as an example, but you can use Conda (or any other manager) as well:
```
python -m venv your_environment_name
source ./your_environment_name/bin/your_activation_script
```
As your_activation_script please use:
- ```activate``` for Linux and MacOS,
- ```activate.ps1``` for Windows.

As your_activation_script please use:
- ```activate``` for Linux and MacOS,
- ```activate.ps1``` for Windows.

4. Install requirements within the virtual environment (again, I present for PIP, but use the manager you like):
```
pip install -r requirements.txt
```

5. If you run the application for the first time, create the database:
```
python manage.py migrate
```

6. Run the server:
```
python manage.py runserver
```

7. Enter ```127.0.0.1:8000``` in your web browser.

Have fun!

# Contact
Feel free to contact me if you have any questions, doubts, or want to contribute to the project. Your feedback is really welcome!
