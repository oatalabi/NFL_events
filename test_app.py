import json
import unittest
from app import app, combine_data

class BasicTestCase(unittest.TestCase):
    def test_api(self):
        # tests if API endpoint returns a response
        tester = app.test_client(self)
        response = tester.get('/events', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_error(self):
        # tests if API returns error when an invalide route is entered
        tester = app.test_client(self)
        response = tester.get('/events-error', content_type='application/json')
        responseJSON = json.loads(response.data)
        self.assertEqual(responseJSON['status'], 500)
        self.assertEqual(responseJSON['message'], 'An unexpected error has occurred.')

    def test_method(self):
        # tests method combine_data which transforms and combines data from the two external API calls
        test_scoreboard_data = {'2020-01-12':
                                {'data': {
                                    '1233827':{
                                        'stadium': 'Arrowhead Stadium', 'event_id': '1233827', 'event_date': '2020-01-12 15:05',
                                        'away_team_id': '42', 'away_primary_color': '#02253A', 'away_secondary_color': '#B31B34',
                                        'away_tertiary_color': '#FFFFFF', 'away_abbreviation': 'HOU', 'away_name': 'Houston Texans',
                                        'away_nick_name': 'Texans', 'away_city': 'Houston', 'away_image_id': '', 'home_team_id': '63',
                                        'home_primary_color': '#E1AC00', 'home_secondary_color': '#BD0100', 'home_tertiary_color': '#FFFFFF',
                                        'home_abbreviation': 'KC', 'home_name': 'Kansas City Chiefs', 'home_nick_name': 'Chiefs',
                                        'home_city': 'Kansas City', 'home_image_id': '', 'status': 'Final', 'away_score': '31', 
                                        'home_score': '51', 'boxscore_available': 'Yes', 'home_short_name': 'KC', 'away_short_name': 'HOU',
                                        'home_display_name': 'Kansas City', 'away_display_name': 'Houston', 'tv_station': 'CBS',
                                        'tv_station_name': 'CBS', 'surface': 'Grass', 'stadium_rotation': '140', 'roof': 'Open',
                                        'away_record': '11-6', 'home_record': '12-4', 'recap_available': 'Yes',
                                        'scoring': {
                                            'data': {
                                                'A': {'quarter1score': '21', 'quarter2score': '3', 'quarter3score': '7', 'quarter4score': '0', 'overtimescore': '0', 'totalscore': '31'}, 
                                                'H': {'quarter1score': '0', 'quarter2score': '28', 'quarter3score': '13', 'quarter4score': '10', 'overtimescore': '0', 'totalscore': '51'}
                                            },
                                            'columns': {'quarter1score': 'Quarter1Score', 'quarter2score': 'Quarter2Score', 'quarter3score': 'Quarter3Score', 'quarter4score': 'Quarter4Score', 'overtimescore': 'OvertimeScore', 'totalscore': 'TotalScore'}
                                        }, 
                                        'home_rotation': '306',
                                        'away_rotation': '305'},
                                    '1233912': {
                                        'stadium': 'Lambeau Field', 'event_id': '1233912', 'event_date': '2020-01-12 18:40',
                                        'home_team_id': '39', 'home_primary_color': '#244729', 'home_secondary_color': '#E0A200',
                                        'home_tertiary_color': '#FFFFFF', 'home_abbreviation': 'GB', 'home_name': 'Green Bay Packers',
                                        'home_nick_name': 'Packers', 'home_city': 'Green Bay', 'home_image_id': '', 'away_team_id': '52',
                                        'away_primary_color': '#0B2343', 'away_secondary_color': '#549F27', 'away_tertiary_color': '#FFFFFF',
                                        'away_abbreviation': 'SEA', 'away_name': 'Seattle Seahawks', 'away_nick_name': 'Seahawks', 
                                        'away_city': 'Seattle', 'away_image_id': '', 'status': 'Final', 'away_score': '23', 'home_score': '28', 
                                        'boxscore_available': 'Yes', 'home_short_name': 'GB', 'away_short_name': 'SEA', 'home_display_name': 'Green Bay', 
                                        'away_display_name': 'Seattle', 'tv_station': 'FOX', 'tv_station_name': 'FOX', 'surface': 'Grass', 
                                        'stadium_rotation': '180', 'roof': 'Open', 'away_record': '12-5', 'home_record': '13-3', 'recap_available': 'Yes', 
                                        'scoring': {
                                            'data': {
                                                'H': {'quarter1score': '7', 'quarter2score': '14', 'quarter3score': '7', 'quarter4score': '0', 'overtimescore': '0', 'totalscore': '28'}, 
                                                'A': {'quarter1score': '3', 'quarter2score': '0', 'quarter3score': '14', 'quarter4score': '6', 'overtimescore': '0', 'totalscore': '23'}
                                            }, 
                                            'columns': {'quarter1score': 'Quarter1Score', 'quarter2score': 'Quarter2Score', 'quarter3score': 'Quarter3Score', 'quarter4score': 'Quarter4Score', 'overtimescore': 'OvertimeScore', 'totalscore': 'TotalScore'}
                                        }, 
                                        'home_rotation': '308', 
                                        'away_rotation': '307'}
                                    },
                                'columns': {'away_record': 'away record', 'home_record': 'home record', 'event_id': 'event id', 'event_date': 'event date', 'away_team_id': 'away team id', 'away_abbreviation': 'away abbreviation', 'away_name': 'away name', 'away_city': 'away city', 'away_nick_name': 'away nick name', 'away_image_id': 'away image id', 'away_primary_color': 'Away Primary Color', 'away_secondary_color': 'Away Secondary Color', 'away_tertiary_color': 'Away Tertiary Color', 'home_team_id': 'home team id', 'home_name': 'home name', 'home_city': 'home city', 'home_nick_name': 'home nick name', 'home_abbreviation': 'home abbreviaiton', 'home_image_id': 'home image id', 'home_primary_color': 'Home Primary Color', 'home_secondary_color': 'Home Secondary Color', 'home_tertiary_color': 'Home Tertiary Color', 'stadium': 'Stadium', 'away_score': 'away score', 'home_score': 'home score', 'away_short_name': 'Away Short Name', 'home_short_name': 'Home Short Name', 'status': 'Status', 'recap_available': 'recap available', 'boxscore_available': 'Boxscore Available', 'scoring': 'scoring', 'home_rotation': 'Home Rotation Number', 'away_rotation': 'Away Rotation Number', 'weather_code': 'Weather Code', 'stadium_rotation': 'Stadium Rotation', 'roof': 'Roof', 'surface': 'surface', 'away_display_name': 'away display name', 'home_display_name': 'home display name'}},
                                '2020-01-13': []
                                }

        test_ranking_data = [
                            {
                                "team_id": "48",
                                "team": "Baltimore",
                                "rank": "1",
                                "last_week": "1",
                                "points": "65.186",
                                "modifier": "0.540",
                                "adjusted_points": "35.200"
                            },
                            {
                                "team_id": "63",
                                "team": "Kansas City",
                                "rank": "2",
                                "last_week": "2",
                                "points": "38.544",
                                "modifier": "0.550",
                                "adjusted_points": "21.199"
                            },
                            {
                                "team_id": "44",
                                "team": "New England",
                                "rank": "6",
                                "last_week": "4",
                                "points": "19.073",
                                "modifier": "0.570",
                                "adjusted_points": "10.872"
                            },
                            {
                                "team_id": "62",
                                "team": "Tennessee",
                                "rank": "7",
                                "last_week": "11",
                                "points": "23.031",
                                "modifier": "0.467",
                                "adjusted_points": "10.748"
                            },
                            {
                                "team_id": "64",
                                "team": "LA Rams",
                                "rank": "9",
                                "last_week": "14",
                                "points": "13.017",
                                "modifier": "0.556",
                                "adjusted_points": "7.232"
                            },
                            {
                                "team_id": "57",
                                "team": "Minnesota",
                                "rank": "10",
                                "last_week": "6",
                                "points": "11.939",
                                "modifier": "0.478",
                                "adjusted_points": "5.704"
                            },
                            {
                                "team_id": "39",
                                "team": "Green Bay",
                                "rank": "12",
                                "last_week": "12",
                                "points": "12.938",
                                "modifier": "0.390",
                                "adjusted_points": "5.046"
                            },
                            {
                                "team_id": "52",
                                "team": "Seattle",
                                "rank": "19",
                                "last_week": "18",
                                "points": "-7.691",
                                "modifier": "0.556",
                                "adjusted_points": "-3.418"
                            },
                            {
                                "team_id": "42",
                                "team": "Houston",
                                "rank": "21",
                                "last_week": "17",
                                "points": "-13.338",
                                "modifier": "0.550",
                                "adjusted_points": "-6.002"
                            },
                            {
                                "team_id": "67",
                                "team": "Indianapolis",
                                "rank": "23",
                                "last_week": "20",
                                "points": "-13.711",
                                "modifier": "0.522",
                                "adjusted_points": "-6.551"
                            },
                            {
                                "team_id": "55",
                                "team": "NY Giants",
                                "rank": "27",
                                "last_week": "26",
                                "points": "-18.001",
                                "modifier": "0.456",
                                "adjusted_points": "-9.800"
                            }
                        ]
        self.assertEqual(combine_data(test_scoreboard_data, test_ranking_data),  
                                    [{'event_id': '1233827', 'event_date': '12-01-2020', 'event_time': '15:05', 'away_team_id': '42',
                                     'away_nick_name': 'Texans', 'away_city': 'Houston', 'away_rank': '21', 'away_rank_points': '-6.00',
                                     'home_team_id': '63', 'home_nick_name': 'Chiefs', 'home_city': 'Kansas City', 'home_rank': '2', 
                                     'home_rank_points': '21.20'},
                                     {'event_id': '1233912', 'event_date': '12-01-2020', 'event_time': '18:40', 'away_team_id': '52',
                                     'away_nick_name': 'Seahawks', 'away_city': 'Seattle', 'away_rank': '19', 'away_rank_points': '-3.42', 
                                     'home_team_id': '39', 'home_nick_name': 'Packers', 'home_city': 'Green Bay', 'home_rank': '12', 
                                     'home_rank_points': '5.05'}
                                    ])

if __name__ == '__main__':
    unittest.main()
