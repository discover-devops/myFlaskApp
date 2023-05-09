#!/bin/bash

echo '#### Create Python3 Virtual Environment ####'
source scl_source enable rh-python36
VIRTUAL_ENV='venvironment'
python -m venv $VIRTUAL_ENV


echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV/bin/activate


echo '#### Install requirements ####'
pip install -r ./requirements.txt

############Jump to that Path####################
#cd /var/lib/jenkins/workspace/$JOB_NAME/

echo '#### Run tests ####'
pytest utests --junitxml=./xmlReport/output.xml

 
echo '### deactivate virtual environment and exit SCL ###'
deactivate
exit