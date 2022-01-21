from random import random

players = ['Mendy', 'Ederson', 'Alisson', 'Martínez', 'Pope', 'Lloris', 'de Gea',  
            'Fabianski', 'Patrício', 'Pickford','Sá', 'Ramsdale',
            'Alexander-Arnold', 'Robertson', 'Cancelo', 'van Dijk', 'Dias', 'Rüdiger', 'James', 
            'Azpilicueta', 'Alonso', 'Thiago Silva', 'Chilwell', 'Laporte','Varane', 'Zouma',  
            'Walker', 'Maguire', 'Reguilón', 'Gabriel', 'Castagne', 'Stones''Evans',
            'Salah', 'De Bruyne', 'Mané', 'Fernandes', 'Sterling', 'Son', 'Rashford', 
            'Sancho', 'Mahrez', 'Jota', 'Foden', 'Pulisic','Havertz', 'Mount', 'Grealish', 
            'Bernardo', 'Pogba', 'Ziyech', 'Gündogan', 'Greenwood', 'Coutinho',
            'Ronaldo','Kane',	'Lukaku,', 'Vardy', 'Aubameyang', 'Firmino', 'Werner', 'Jesus',
            'Lacazette', 'Cavani', 'Calvert-Lewin', 'Antonio', 'Watkins', 'Bamford', 'Ings',
            'Martial', 'Richarlison', 'Jiménez', 'Wilson', 'Daka', 'Iheanacho']

teams_names = ["My team", "Someone' favourites", "", ";/$%!-_"]

positions = ['goalkeeper', 'defender1', 'defender2', 'defender3', 'midfielder1', 'midfielder2', 'midfielder3', 'midfielder4', 'forward1', 'forward2', 'forward3']

form = {}

def pick_team():
    if (form['teamName'] != "" and form['goalkeeper'] != "" and form['defender1'] != "" and 
        form['defender2'] != "" and form['defender3'] != "" and form['midfielder1'] != "" and 
        form['midfielder2'] != "" and form['midfielder3'] != "" and form['midfielder4'] != "" and 
        form['forward1'] != "" and form['forward2'] != "" and form['forward3'] != ""):
           
        teamName = form['teamName']
        goalkeeper = form['goalkeeper']
        defender1 = form['defender1']
        defender2 = form['defender2']
        defender3 = form['defender3']
        midfielder1 = form['midfielder1']
        midfielder2 = form['midfielder2']
        midfielder3 = form['midfielder3']
        midfielder4 = form['midfielder4']
        forward1 = form['forward1']
        forward2 = form['forward2']
        forward3 = form['forward3']

        print(form)

def test_values():
    number = 0
    for team in teams_names:
        form['teamName'] = team
        for position in positions:
            index = int(random()*len(players))
            form[position] = players[index]
        number += 1
        print(f"\n Team number: {number}")
        try:
            pick_team()
        except:
            print("An exception was captured.")

test_values()            
      

    
