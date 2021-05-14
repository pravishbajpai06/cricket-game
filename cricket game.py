# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:06:01 2021

@author: Pravish Bajpai
"""

import random
import time
from random import choice
first_total=[]
second_total=[]
balls=["YORKER","FULL TOSS","GOOGLY","LENGTH BALL","CARROM BALL","SLOWER BALL","INSWINGER","OUTSWINGER","LEG CUTTER","OFF CUTTER","DOOSRA","FLIPPER","BOUNCER","BEAMER","KNUCKLE BALL"]
out=["RUN OUT!!!","CATCH OUT!!!"]

print("Choose teams!")
teams={"IND":["Rohit Sharma","Shikhar Dhawan","Virat Kohli","KL Rahul","MS Dhoni","Ravindra Jadeja","Hardik Pandya","Ravindrachandran Ashwin","Bhuvneshwar Kumar","M.Shami","Jasprit Bumrah"],
       "AUS":["David Warner","Aaron Finch","Steve Smith","M.Labuschagne","Glenn Maxwell","M.Stoinis","M.Starc","J.Hazlewood","P.Cummins","N.Lyonn","A.Zampa"],
       "NZ":["M.Guptill","Colin Munro","K.Williamson","Ross Taylor","C.Grandehome","M.Santner","K.Jamieson","L.Ferguson","T.Latham","Tim Southee","Trent Boult"],
       "ENG":["J.Roy","J.Bairstow","D.Malan","J.Root","E.Morgan","J.Butler","B.Stokes","M.Ali","S.Curran","S.Broad","J.Anderson"],
       "SA":["Faf du Plesis","Quinton de Cock","AB deVilliers","R.Dussein","A.Markram","D.Miller","C.Morris","L.Ngidi","I.tahir","K.Rabada","T.Samsi"],
       "PAK":["Imam-ul-Haq","Fakhar Zaman","Babar Azam","M.Hafeez","S.Ahmed","A.Ali","S.Malik","W.Riaz","M.Asif","H.Ali","S.Khan"],
       "WI":["S.Hope","C.Gayle","E.Lewis","D.Bravo","J.Mohammed","K.Pollard","A.Russel","F.Allen","A.Joseph","A.Hosein","S.Cotrell"],
       "SL":["D.Karunaratne","P.Nissanka","O.Fernando","R.Mendis","A.Mathews","T.Perera","D.Chandimal","A.Dhananjaya","K.Mendis","S.Lakmal","D.Chameera"],
       "BAN":["T.Iqbal","S.Sarkar","M.Naim","M.Haque","M.Rahim","M.Mithun","L.Das","M.Mortaza","M.Hasan","R.Hussain","T.Ahmed"],
       "AFG":["U.Ghani","I.Zadran","H.Shahidi","M.Nabi","R.Gurbaz","R.Khan","F.Farooqi","Naveen-ul-Haq","S.Ashraf","A.Afghan","A.Zazai"]}
for keys in teams.keys():
    print(keys)
def select_teams(team):
    if team in teams:
        selected_team=team
        return selected_team
    else:
        selected_team=input("Select your team from above choices only!").upper()
        return selected_team
        
firstteam=input("select1st team").upper()
First=select_teams(firstteam)
secondteam=input("select 2nd team").upper()
Sec=select_teams(secondteam)
if First==Sec:
    print("Thuis team is already chosen!!!Please choose a different team")
    secondteam=input("select 2nd team").upper()
    select_teams(secondteam)
else:
    pass
players=[First,Sec]
for i in range(5,0,-1):
    print(".........",i,".......",end="")
    time.sleep(0.5)
print("\n         ############  LETS PLAY CRICKET!! ############") 

print("\n\n######TOSS TIME! ######")
print("\n")
print(First,"Whats your call? \n Heads or tails")
toss_call=["HEADS","TAILS"]
bat_ball=["BAT","BALL"]
toss=input().upper()

while toss:
    if toss in toss_call:
        print(f"{toss} is the call")
        random.shuffle(toss_call)
        print("It is",toss_call[0])
        break
    else:
        print("type properly")
        toss=input().upper()
        continue

def toss_time(team1,team2):
    print(f"{team1} What would you like to do- BAT OR BOWL")    
    call=input().upper()
    try:
        if call not in bat_ball:
            print("Please type correctly")
            call=input().upper()
    finally:
        print(f"{team1}chose to",call,"first")
        if call=="BAT":
            batting_team,bowling_team=teams[team1],teams[team2]
            return batting_team,bowling_team
        elif call=="BOWL":
            batting_team,bowling_team=teams[team2],teams[team1]
            return batting_team,bowling_team
def innings(batting_team,bowling_team,first_score):
    batting_team_list=teams[batting_team]
    batting_options=iter(batting_team_list)
    on_strike=next(batting_options)
    on_strike_scores=[]
    player_scores=[]
    wickets=10
    total=[]
    team_total=0
    bowling_options=teams[bowling_team][4:]
    
    for over in range(0,5):
        bowler=choice(bowling_options)
        print(on_strike,"is on strike",bowler,"is bowling")
        print("press any key to respond")
        for ball in range(1,7):
            ball_delivered=choice(balls)
            played_for=choice(balls)
            if wickets==0 or team_total>first_score:
                 break
            elif ball_delivered==played_for:
                print(f"\n{over}.{ball}")
                print(f"\n LBW!!! {bowler} has taken the wicket of {on_strike}")
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                out_player_scores={on_strike:player_scores}
                print(f"{batting_team} is at {team_total}")
                print(out_player_scores)
                on_strike=next(batting_options)
                print(f"{on_strike} is on strike\n")
                wickets-=1
                on_strike_scores=[0]
                time.sleep(2)
            else:
                print(f"{over}.{ball}",end="")
                start=time.time()
                input("")
                end=time.time()
                time_taken=end-start
                if time_taken<1:
                    print("A SIXERRR!!")
                    total.append(6)
                    on_strike_scores.append(6)
                    player_scores=sum(on_strike_scores)
                    team_total=sum(total)
                    if team_total> first_score:
                        break
                elif time_taken>1 and time_taken<1.5:
                    print("BOUNDARYY!!")
                    total.append(4)
                    on_strike_scores.append(4)
                    player_scores=sum(on_strike_scores)
                    team_total=sum(total)
                    if team_total>first_score:
                        break
                elif time_taken>2 and time_taken<2.5:
                    print("Two runs")
                    total.append(2)
                    on_strike_scores.append(2)
                    player_scores=sum(on_strike_scores)
                    team_total=sum(total)
                    if team_total>first_score:
                        break
                elif time_taken>2.5 and time_taken<3:
                    print(f"{on_strike} duck the ball")
                    total.append(0)
                    on_strike_scores.append(0)
                    player_scores=sum(on_strike_scores)
                    team_total=sum(total)
                    if team_total>first_score:
                        break
                elif time_taken>1.5 and time_taken<2 or time_taken>3:
                    print(f"{choice(out)} {bowler} has taken the wicket of {on_strike}")
                    player_scores=sum(on_strike_scores)
                    team_total=sum(total)
                    out_player_scores={on_strike:player_scores}
                    print(f"{batting_team} is at {team_total}")
                    print(out_player_scores)
                    on_strike=next(batting_options)
                    wickets-=1
                    on_strike_scores=[0]
                    player_scores=[0]
            print(f"{batting_team} is at {team_total}")
            print(f"{on_strike} is at {player_scores} \n")
    return team_total
if toss==toss_call[0]:
    toss_time(firstteam,secondteam)
    first_innings_total=innings(firstteam,secondteam,1000)
    print(f"{secondteam} needs {first_innings_total} scores to win the match")
    second_innings_total=innings(secondteam,firstteam,first_innings_total)
    if first_innings_total>second_innings_total:
        print(f"{firstteam} has won the match")
    elif second_innings_total > first_innings_total:
        print(f"{secondteam} has won the match")
    elif first_innings_total==second_innings_total:
        print("ITS A TIEE!!!!!!")
if toss==toss_call[1]:
    toss_time(secondteam,firstteam)
    first_innings_total=innings(secondteam,firstteam,1000)
    print(f"{firstteam} needs {first_innings_total} scores to win the match")
    second_innings_total=innings(firstteam,secondteam,first_innings_total)
    if first_innings_total>second_innings_total:
        print(f"{firstteam} has won the match")
    elif second_innings_total>first_innings_total:
        print(f"{secondteam} has won the match")
    elif first_innings_total ==second_innings_total:
        print("DRAW!!!!!!")
            
                        
                    
                
            
        
      