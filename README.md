# NFL_events

## This API returns a list of NFL events in JSON format.

Download or `git clone` this repository to run locally.

## Backend Server
The code for the backend server is in the `app.py` file.

### Installation
First, ensure Python 3.7+ is installed. Next, install the required dependencies using a virtual environment to avoid installing Python packages globally which could break other projects:
```
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
```

### Environment Variable
Create a `.env` file and keep your API KEY for `https://delivery.chalk247.com` using `.env.sample` as a guide.

### Run the server:
```
python3 app.py
```
The server launched will be available at `http://localhost:8000/`.
URL format `http://localhost:8000/events?start_date=2020-01-12&end_date=2020-01-19` to get NFL events between 2020-01-12 and 2020-01-19
if no dates are specified in the URL i.e `http://localhost:8000/events` NFL events for the current day will be used.
Please enter dates within 1 week

### Run tests
```
python3 test_app.py
```

# Assumptions and Explanations

### API_KEY 
The key was stored in the `.env` file to ensure it remains private and does not end up in the source code control system, a sample format of what should be in the .env file can be seen in `.env.sample`

### URL format
The API is accessed from the URL format `/events` this is to allow users get current day NFL events if no `start_date` or `end_date` parameters are passed.

### Error Handling
Errors and Exceptions from both external API calls are used so as to maintain the normal flow of the application even when unexpected events occur.