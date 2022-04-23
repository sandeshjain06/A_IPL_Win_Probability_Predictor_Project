# Ipl_score_predict_Project

- Objective of this Project :

Ipl Score predict will tell the win and loss probablity of two teams playing at any particular point , give details such as batting team , bowling team , target , venue , total runs scored , total overs completed , wickets details 


- Click here to check the dataset - https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set

- Click here to check the website hosted on Heruko - https://ipl-score--predictor.herokuapp.com/


Screenshot of the project 

![image](https://user-images.githubusercontent.com/91243691/164946113-e3d975e7-235f-47c4-b74c-8e8d97632f42.png)

1. Explanation about the dataset Details  - 2 dataset are used - teams.csv and delivery.csv

Team.csv - (756, 18)

It consists of (756, 18) values , here each row tells about single match data .

So total 756 matches was played in total 12 Seasons.

Below are the columns of team.csv

'id', 'Season', 'city', 'date', 'team1', 'team2', 'toss_winner', 'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs', 'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2', 'umpire3'


Deliveries.csv - (179078, 21) 

- This dataset tells the complete match details ball by ball , every ball how much runs was scored .

- Below are the columns 

'match_id', 'inning', 'batting_team', 'bowling_team', 'over', 'ball','batsman', 'non_striker', 'bowler', 'is_super_over', 'wide_runs','bye_runs', 'legbye_runs', 'noball_runs', 'penalty_runs', 'batsman_runs', 'extra_runs', 'total_runs', 'player_dismissed','dismissal_kind', 'fielder'


2. Performing EDA and Feature Engineering 

- Output that we require from the datset is  Batting team , Bowling team , city , runs_left , balls_left, wickets_left, total_runs , current RunRate , 
required RunRate , Result





























































