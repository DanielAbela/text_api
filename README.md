#Text API

The following instructions assume that you've got Python 3 installed and that you've activated your virtual environment.


###Install the dependencies


pip install -r prerequirements.txt
pip install -r requirements.txt 

###Running the app
cd to text_api
Make sure the following environment variables are set:
set FLASK_APP=app

Run the following script to initialize the database with values.
python populate_database

Start the app
flask run 