from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('http://127.0.0.1:5000/api/teams')
        response.raise_for_status()  # Raises an error if the request fails
        teams = response.json().get('teams', [])
        if not teams:
            return render_template('index.html', teams=[], error="No teams found.")
    except requests.RequestException:
        return render_template('index.html', teams=[], error="Failed to fetch teams.")

    return render_template('index.html', teams=sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    if not team1 or not team2 or team1 == "Select Team 1" or team2 == "Select Team 2":
        return render_template('index.html', result=None, error="Please select two teams.", teams=[])

    try:
        response = requests.get(f'http://127.0.0.1:5000/api/teamvteam?team1={team1}&team2={team2}')
        response.raise_for_status()
        result = response.json()
    except requests.RequestException:
        return render_template('index.html', result=None, error="Failed to fetch team comparison.", teams=[])

    # Fetch teams again to repopulate the dropdown in case of rerender
    try:
        teams_response = requests.get('http://127.0.0.1:5000/api/teams')
        teams_response.raise_for_status()
        teams = teams_response.json().get('teams', [])
    except requests.RequestException:
        teams = []

    return render_template('index.html', result=result, teams=sorted(teams))

if __name__ == '__main__':
    app.run(debug=True, port=7000)
