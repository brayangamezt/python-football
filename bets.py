import requests
import time

class Bets_methods:

    def __init__(self, league_id, season, english_teams, mexican_teams, spanish_teams, api_key, api_host):
        self.league_id = league_id
        self.season = season
        self.english_teams = english_teams
        self.mexican_teams = mexican_teams
        self.spanish_teams = spanish_teams
        self.api_key = api_key
        self.api_host = api_host
        self.headers = { 'x-rapidapi-host': api_host, 'x-rapidapi-key': api_key }
        self.fixtures = []
        self.final_result = []

    #Method to get the current round of the season
    def get_current_round(self, id):
        url = f'https://v3.football.api-sports.io/fixtures/rounds?league={id}&season=2024&current=true'
        response = requests.get( url, headers = self.headers )
        if len( response.json()['response'] ) > 0:
            data = response.json()['response'][0]
            return data
        return False
    
    #Method to get the current schedule of the round
    def get_current_schedule(self, id, round):
        url = f"https://v3.football.api-sports.io/fixtures?league={id}&season={self.season}&round={round}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    #Method to get the each fixture of the teams i want
    def get_team_matches(self, data, id):
        if id == 39:
            for match in data['response']:
                if match['teams']['home']['name'].lower() in self.english_teams or match['teams']['away']['name'].lower() in self.english_teams:
                    match_game = ( match['fixture']['id'], match['teams']['home']['id'], match['teams']['away']['id'], id )
                    self.fixtures.append( match_game )
        elif id == 140:
            for match in data['response']:
                if match['teams']['home']['name'].lower() in self.spanish_teams or match['teams']['away']['name'].lower() in self.spanish_teams:
                    match_game = ( match['fixture']['id'], match['teams']['home']['id'], match['teams']['away']['id'], id )
                    self.fixtures.append( match_game )
        elif id == 262:
            for match in data['response']:
                if match['teams']['home']['name'].lower() in self.mexican_teams or match['teams']['away']['name'].lower() in self.mexican_teams:
                    match_game = ( match['fixture']['id'], match['teams']['home']['id'], match['teams']['away']['id'], id )
                    self.fixtures.append( match_game )
        return
    

    #Method to get season wins, dra, loses games information for home team
    def get_home_prediction(self, teams):
        hgf = teams['home']['league']['goals']['for']['minute']
        agf = teams['home']['league']['goals']['against']['minute']     

        local_information = {
            'local_team_name':f'{ teams['home']['name'] }',
            'local_last_5_games_gols': f'GF: { teams['home']['last_5']['goals']['for']['total'] } GC: { teams['home']['last_5']['goals']['against']['total'] }',
            'local_average_last_5_games':f'GF: { teams['home']['last_5']['goals']['for']['average'] } GC: { teams['home']['last_5']['goals']['against']['average'] }',
            'home_team_wins':f'Local: { teams['home']['league']['fixtures']['wins']['home'] } Visitante: { teams['home']['league']['fixtures']['wins']['away'] }',
            'home_team_draws':f'Local: { teams['home']['league']['fixtures']['draws']['home'] } Visitante: { teams['home']['league']['fixtures']['draws']['away'] }',
            'home_team_loses':f'Local: { teams['home']['league']['fixtures']['loses']['home'] } Visitante: { teams['home']['league']['fixtures']['loses']['away'] }',
            'home_team_goals_for':f'{ teams['home']['league']['goals']['for']['total']['home'] }, Promedio { teams['home']['league']['goals']['for']['average']['home'] }',
            'home_team_goals_against':f'{ teams['home']['league']['goals']['for']['total']['away'] }, Promedio { teams['home']['league']['goals']['for']['average']['away'] }',
            'home_team_goals_for_first_half':f' 0-15: {hgf['0-15']['total']}   16-30: { hgf['16-30']['total'] }   31-45: { hgf['31-45']['total'] }',
            'home_team_goals_for_second_half':f' 46-60: {hgf['46-60']['total']}   61-75: { hgf['61-75']['total'] }   76-90: { hgf['76-90']['total'] }',
            'home_team_away_against_goals_FH':f' 0-15: {agf['0-15']['total']}   16-30: { agf['16-30']['total'] }   31-45: { agf['31-45']['total'] }',
            'home_team_away_against_goals_SH':f' 46-60: {agf['46-60']['total']}   61-75: { agf['61-75']['total'] }   76-90: { agf['76-90']['total'] }',
        }
        return local_information


    #Method to get sesson wins, draws, loses games information for away team
    def get_away_prediction(self,teams):

        ahgf = teams['away']['league']['goals']['for']['minute']
        aagf = teams['away']['league']['goals']['against']['minute']

        away_information = {
            'away_team_name':f'{ teams['away']['name'] }',
            'away_team_wins':f'Local: { teams['away']['league']['fixtures']['wins']['home'] } Visitante: { teams['away']['league']['fixtures']['wins']['away'] }',
            'away_team_draws':f'Local: { teams['away']['league']['fixtures']['draws']['home'] } Visitante: { teams['away']['league']['fixtures']['draws']['away'] }',
            'away_team_loses':f'Local: { teams['away']['league']['fixtures']['loses']['home'] } Visitante: { teams['away']['league']['fixtures']['loses']['away'] }',
            'away_team_goals_for':f'GF: { teams['away']['league']['goals']['against']['total']['home'] } Promedio { teams['away']['league']['goals']['against']['average']['home'] }',
            'away_team_goals_against':f'GC: { teams['away']['league']['goals']['against']['total']['away'] } Promedio { teams['away']['league']['goals']['against']['average']['away'] }',
            'away_team_goals_for_FH':f' 0-15:  {ahgf['0-15']['total']}   16-30: { ahgf['16-30']['total'] }  31-45: { ahgf['31-45']['total'] }',
            'away_team_goals_for_SH':f' 46-60: {ahgf['46-60']['total']}   61-75: { ahgf['61-75']['total'] }   76-90: { ahgf['76-90']['total'] }',
            'away_team_goals_against_FH':f' 0-15: {aagf['0-15']['total']}   16-30: { aagf['16-30']['total'] }  31-45: { aagf['31-45']['total'] }',
            'away_team_goals_against_SH':f' 46-60: {aagf['46-60']['total']}   61-75: { aagf['61-75']['total'] }   76-90: { aagf['76-90']['total'] }'
        }
        return away_information

    
    #Method to get the full information
    def get_prediction_team(self, fixture):

        try:
            url = f'https://v3.football.api-sports.io/predictions?fixture={fixture}'
            response = requests.get( url, headers=self.headers )
            data = response.json()     

            # print( json.dumps( data, indent=3 ) )
            time.sleep( 1 )

            if len( data['response'] ) > 0:
                teams = data['response'][0]['teams']
                prediction_advice = data['response'][0]['predictions']['advice']
                prediction_victory = data['response'][0]['predictions']['percent'] 
                prediction = {
                    'advice': prediction_advice,
                    'victory':prediction_victory,
                    'local': self.get_home_prediction( teams ),
                    'away' : self.get_away_prediction( teams )   
                }
                return prediction
            
            return False

        except TypeError as err:
            print( err )
    

    def final_results(self):
        for id in self.league_id:
            c_round = self.get_current_round(id)
            time.sleep( 3 )
            c_schedule = self.get_current_schedule(id, c_round)
            time.sleep( 3 )
            self.get_team_matches(c_schedule, id)
            
        for fix in self.fixtures:
            time.sleep( 3 )
            getting = self.get_prediction_team(fix[0])
            time.sleep( 3 )
            self.final_result.append( getting )
            
        return self.final_result
