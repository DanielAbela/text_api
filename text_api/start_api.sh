#!/bin/bash

WORKING_DIRECTORY=$(dirname "$(readlink -f "$0")")

export FLASK_APP=app
export SETTINGS_ENVIRONMENT="prod"

cd $WORKING_DIRECTORY

python populate_database
flask run

