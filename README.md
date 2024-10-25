# IPL Team Comparison Web Application

This project is a web application built with Flask that allows users to compare IPL teams. The application fetches data from an external API to display teams and perform comparisons.

## Features

- Home page displaying a form to select two IPL teams for comparison.
- Fetches team data from a REST API.
- Compares two selected teams and displays the results on the same page.
- Basic error handling for API requests.

## Project Structure

- `app.py`: Main application file that contains Flask routes and API request logic.
- `templates/index.html`: HTML template that renders the form and displays comparison results.
- `requirements.txt`: Contains the Python dependencies for the project.

## Prerequisites

- Python 3.7 or higher
- Flask and Requests libraries (install from `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ipl-comparison-app.git
   cd ipl-comparison-app


Install dependencies:
 pip install -r requirements.txt


Usage
Start the Flask server:
 python app.py

Open your browser and navigate to:
http://127.0.0.1:7000


Select two teams from the dropdowns and click Find Track Record to view their comparison.

API Endpoints
The app relies on two API endpoints to fetch data. Ensure the following endpoints are available:

GET /api/teams: Fetches the list of IPL teams.
GET /api/teamvteam?team1={team1}&team2={team2}: Fetches the comparison result for the selected teams.
Error Handling
The application includes error handling to manage API failures and displays user-friendly messages on the webpage.

Contributing
Feel free to open issues or submit pull requests if you would like to contribute to this project.

License
This project is licensed under the MIT License. See the LICENSE file for more information.