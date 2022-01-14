# Shopify Backend Developer Intern
> The task is build an inventory tracking web application for a logistics company. The detailed task details can be found at [Shopify Backend Developer Intern 
Challenge - Summer 2022](https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit#)

### System Pre-requisits:
Ensure that you have Python3.7+ and Git installed in the system. Refer the following links incase the requirements are not installed.
1. [Python 3.7+](https://www.python.org/)
2. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Install and configure the project.
Clone the repository using
```
git clone https://github.com/meetgandhi123/Shopify_Backend_Developer_Intern_Chalange.git
```


### 1. Linux
```
# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```
### 2. Windows
```
# Create python virtual environment
conda create --name venv python=3.8

# Activate the python virtual environment
conda activate venv

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```

## Run the server in development mode
Run the server
```
python manage.py runserver
```
Local API calls can be made at: http://127.0.0.1:8000/

## API Documentation
Postman API documentation is been attached to the repo, which can be used to test the API locally.

## Testing

Few examples for testing APIs

* To test API endpoints
```
python manage.py test
```

## Database migrations
The migrations file (0001_initial.py) consist of basic samples of record, you can delete the file present in migrations folder. On deleting the file we need to make migrations which can be done by following commands.

For creating migrations, run following commands: 

```
python manage.py makemigrations
```
```
python manage.py db migrate
```




