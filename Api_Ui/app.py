from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('home.html',teams = sorted(teams))


@app.route('/team')
def teams():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('teams.html', teams=sorted(teams))

@app.route('/team-record')
def team_record():
    team1 = request.args.get('team1')


    response = requests.get('http://127.0.0.1:5000/api/team-record?team={}'.format(team1))
    response = response.json()
    print("API Response Data:", response)

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template('team-record.html',result = response,teams = sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
    response = response.json()

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template('teamvteam.html',result = response,teams = sorted(teams))


@app.route('/batsman-record')
def batsman_record():
    batsman = request.args.get('batsman')

    if batsman:
        response = requests.get('http://127.0.0.1:5000/api/batting-record?batsman={}'.format(batsman))
        result = response.json()
    else:
        result = {}

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json().get('teams', [])

    return render_template('batsman-record.html', result=result, teams=sorted(teams))

@app.route('/bowler-record')
def bowling_record():
    bowler = request.args.get('bowler')

    if bowler:
        response = requests.get('http://127.0.0.1:5000/api/bowling-record?bowler={}'.format(bowler))
        result = response.json()
    else:
        result = {}

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json().get('teams', [])

    return render_template('bowler-record.html', result=result, teams=sorted(teams))


app.run(debug=True,port=7000)
