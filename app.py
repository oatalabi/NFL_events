from flask import Flask, jsonify, request
from flask_api import status
from flask_cors import CORS, cross_origin
import requests, re
import os
from dotenv import load_dotenv
import datetime
from datetime import date

# initialize the Flask application
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = False
app.config['JSON_SORT_KEYS'] = False

load_dotenv()
API_KEY = os.getenv('API_KEY')

@app.errorhandler(Exception) #handle any error exception in external API
def handle_error(error):
    response = {}
    response['message'] = 'An unexpected error has occurred.'
    response['status'] = 500
    return jsonify(response), 500

def combine_data(scoreboard, rankings):
    combined_results = []
    for day, day_obj in scoreboard.items():
        if day_obj:
            for id_ in day_obj['data']:

                # get home and away team ids
                away_team_id = day_obj['data'][id_]['away_team_id']
                home_team_id = day_obj['data'][id_]['home_team_id']
                away_ranking_data = next(filter(lambda rank: rank['team_id'] == away_team_id, rankings))
                home_ranking_data = next(filter(lambda rank: rank['team_id'] == home_team_id, rankings))

                day_id_event = {}

                # get data for each event in a day
                day_id_event['event_id'] = day_obj['data'][id_]['event_id']
                event_datetime = datetime.datetime.strptime(day_obj['data'][id_]['event_date'], '%Y-%m-%d %H:%M')
                event_datetime_new = event_datetime.strftime('%d-%m-%Y %H:%M')
                day_id_event['event_date'] = event_datetime_new.split(' ')[0]
                day_id_event['event_time'] = event_datetime_new.split(' ')[1]
                day_id_event['away_team_id'] = away_team_id
                day_id_event['away_nick_name'] = day_obj['data'][id_]['away_nick_name']
                day_id_event['away_city'] = day_obj['data'][id_]['away_city']
                day_id_event['away_rank'] = away_ranking_data['rank']
                day_id_event['away_rank_points'] = str("{:.2f}".format(round(float(away_ranking_data['adjusted_points']), 2)))
                day_id_event['home_team_id'] = home_team_id
                day_id_event['home_nick_name'] = day_obj['data'][id_]['home_nick_name']
                day_id_event['home_city'] = day_obj['data'][id_]['home_city']
                day_id_event['home_rank'] = home_ranking_data['rank']
                day_id_event['home_rank_points'] = str("{:.2f}".format(round(float(home_ranking_data['adjusted_points']), 2)))

                combined_results.append(day_id_event)

    return combined_results
    
@app.route('/events', methods=["GET"])
@cross_origin()
def getEvents():
    # use today's date as default if user does not enter date
    today = date.today()
    default_date = today.strftime("%Y-%m-%d")
    start_date = request.args.get('start_date', default = default_date, type = str)
    end_date = request.args.get('end_date', default = default_date, type = str)

    scoreboard_api_url = f'https://delivery.chalk247.com/scoreboard/NFL/{start_date}/{end_date}.json?api_key={API_KEY}'
    team_rankings_api_url = f'https://delivery.chalk247.com/team_rankings/NFL.json?api_key={API_KEY}'

    scoreboard_data = requests.get(scoreboard_api_url, headers={"Accept": "application/json"})
    scoreboard_results = scoreboard_data.json()['results']
    
    team_rankings_data = requests.get(team_rankings_api_url, headers={"Accept": "application/json"})
    rankings_results = team_rankings_data.json()['results']['data']

    response_data = combine_data(scoreboard_results, rankings_results)
    
    return jsonify(response_data), 200

# start the server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)