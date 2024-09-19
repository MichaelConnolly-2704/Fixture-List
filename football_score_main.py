from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


API_URL = "http://api.football-data.org/v4/matches"
API_KEY = "f86acedb99f24979b04c499ccd74e05f"  









def get_upcoming_fixtures():
    headers = {
        "X-Auth-Token": API_KEY,
        "X-Unfold-Goals": "true"  
    }
    
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['matches']
    else:
        print(f"Error: {response.status_code}")
        return None







@app.route('/')
def home():
    upcoming_fixtures = get_upcoming_fixtures()
    return render_template('main.html', fixtures=upcoming_fixtures)

@app.route('/match/<int:match_id>')
def match_details(match_id):
    return f"Details for match ID: {match_id}"

if __name__ == '__main__':
    app.run(debug=True)
