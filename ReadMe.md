# Cricket Match Simulator

A Python-based Cricket Match Simulator that models and predicts outcomes between Pakistan and India based on team statistics, player attributes, and probabilistic modeling.

This project combines statistical logic, randomness, and cricketing insights to simulate both single matches and multiple-match series with realistic probability calculations and contextual analysis.

## Features

Object-Oriented Design (OOP):
Built using class-based architecture for modularity and scalability (Cricket, TeamA, TeamB, Stats, and Match).

Team Statistics Integration:
Each team has defined strengths (batting, bowling, attack, defense) and weaknesses (instability, fielding issues, etc.), influencing outcomes.

Single Match Simulation:
Simulates a full T20 match with toss results, innings summaries, random scores, wickets, and match outcomes.

Multi-Match Statistical Analysis:
Runs large-scale simulations (e.g. 1000 matches) to determine each team’s win probability based on relative team ratings.

Realistic Bias:
India’s win probability is statistically higher, reflecting real-world performance trends (based on historical T20 records).

Optional Silent Mode:
Toggle silent=True to suppress detailed commentary output during single-match simulations.

## How It Works

Statistical Modeling
Each team is assigned quantitative attributes such as:

attack, defense, batting_strength, bowling_strength

unstability_percentage (affects consistency)

Probabilities for fielding and batting errors

Toss and Innings Logic
The toss randomly determines which team bats first, and innings are simulated using realistic random ranges for runs, wickets, and overs.

Win Probability Calculation
Each team’s composite rating is calculated as:

team_rating = (defense + attack + batting_strength + bowling_strength) / 4
adjusted for unstability

The relative ratings define india_win_chance and pakistan_win_chance.

Series Simulation
Thousands of simulated matches (simulate_many_matches(n)) determine long-run probabilities for each team’s victory.

## Example Output

  === TOSS ===
  
  India won the toss and decided to bat first.
  
  ----------- 'FIRST INNINGS' -------------
  
  Team India will bat first and give a target to Pakistan.
  
  India scored 165/6 in 20 overs.
  
  Target for Pakistan: 166
  
  --------------- 'SECOND INNINGS' ---------------------
  
  Pakistan scored 170/4 in 18.3 overs.
  
  Pakistan wins by 6 wickets!
  
  Calculated chances before simulation:
  
  Pakistan: 46.89%
  India: 53.11%
  
  Simulated 1000 T20 Matches between Pakistan and India:
  
  Pakistan Win Probability: 45.80%
  India Win Probability: 54.20%

India is more likely to win overall.

## Code Structure

📁 Cricket Match Simulator/

│

├── main.py

├── README.md


## Classes Overview

Class Description
Cricket Base class for shared attributes (overs, players, balls).
TeamA / TeamB Define team-specific stats, lineups, strengths, and weaknesses.
Stats Initializes all team data and probabilities.
Match Handles single and multi-match simulations, toss logic, and win calculations.

## Usage

### 1️⃣ Run the Script

python cricket_simulator.py

### 2️⃣ Example Function Calls

match = Match(20, 11, 120)
match.simulate_single_match("Pakistan", "India")  # Prints full commentary
match.simulate_many_matches(1000)                 # Runs 1000 simulations

### 3️⃣ Optional Silent Mode

To skip detailed commentary:

match.simulate_single_match("Pakistan", "India", silent=True)

## Future Improvements

Integrate real player statistics using APIs (e.g., CricAPI or ESPNcricinfo).

Add database support (SQLite or PostgreSQL) for player and match data.

Use Flask to deploy the simulator on the web with a visual interface.

Implement machine learning models for more accurate probability predictions.

Expand beyond Pakistan–India to support any two teams.

### Note

I had a lot of ideas for this project but I was not able to execute it as I wanted to
due to my limited skillset. I hope to expand it later on beacuse this project has great potential
and I have the vision to excute it.

## Author

Zainab Irfan
