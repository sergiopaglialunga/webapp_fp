from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_HOST"] = "dbf"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

class DbRoutines():
    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)
        
    def user_credentials(self):
        return "test"

dbRoutines = DbRoutines(app)

goalkeepers = ['Mendy', 'Ederson', 'Alisson', 'Martínez', 'Pope', 'Lloris', 'de Gea', 'Sá', 'Ramsdale', 'Fabianski', 'Patrício', 'Pickford']
defenders = ['Alexander-Arnold', 'Robertson', 'Cancelo', 'van Dijk', 'Dias', 'Rüdiger', 'James', 
            'Azpilicueta', 'Alonso', 'Thiago Silva', 'Chilwell', 'Laporte','Varane', 'Zouma', 'Evans', 
            'Walker', 'Maguire', 'Reguilón', 'Gabriel', 'Castagne', 'Stones']
midfielders = ['Salah', 'De Bruyne', 'Mané', 'Fernandes', 'Sterling', 'Son', 'Rashford', 
            'Sancho', 'Mahrez', 'Jota', 'Foden', 'Pulisic','Havertz', 'Mount', 'Grealish', 
            'Bernardo', 'Pogba', 'Ziyech', 'Gündogan', 'Greenwood', 'Coutinho']
forwards = ['Ronaldo','Kane',	'Lukaku,', 'Vardy', 'Aubameyang', 'Firmino', 'Werner', 'Jesus',
            'Lacazette', 'Cavani', 'Calvert-Lewin', 'Antonio', 'Watkins', 'Bamford', 'Ings',
            'Martial', 'Richarlison', 'Jiménez', 'Wilson', 'Daka', 'Iheanacho']

@app.route('/')
def index():
    return render_template("sign_in.html")

@app.route('/sign_in', methods=['POST','GET'])
def login():
    return render_template("sign_in.html")

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']:
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_dbf;")
            cursor.execute(f"SELECT COUNT(*) FROM `Users` WHERE user_name = '{userName}';")
            user_list = cursor.fetchall()
            

            if user_list[0]['COUNT(*)'] > 0:                  
                cursor.close()
                return render_template("sign_up.html", message="The username is not available")
            else:               
                cursor.execute(f"INSERT INTO `Users` (`user_name`, `user_password`) VALUES ('{userName}','{userPwd}');")
                cursor.execute(f"SELECT user_id FROM `Users` WHERE user_name = '{userName}';")
                user_list = cursor.fetchall()
                user_id = user_list[0]['user_id']
                cursor.execute(f"INSERT INTO `Teams` (`user_id`) VALUES ('{user_id}');")
                dbRoutines.mysql.connection.commit()
                cursor.close()
                return render_template("sign_in.html")
        else:
            return render_template("sign_up.html", message="Invalid input")

    return render_template("sign_up.html")

@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "":
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_dbf;")
            cursor.execute(f"SELECT COUNT(*) FROM `Users` WHERE user_name = '{userName}' AND user_password = '{userPwd}';")
            user_list = cursor.fetchall()                          
                
            if user_list[0]['COUNT(*)'] > 0:
                cursor.execute(f"SELECT user_id FROM `Users` WHERE user_name = '{userName}';")
                user_list = cursor.fetchall()
                user_id = user_list[0]['user_id']
                cursor.execute(f"UPDATE `ID` SET `user_id`='{user_id}',`user_name`='{userName}' WHERE `id`='1';")
                dbRoutines.mysql.connection.commit()
                cursor.execute(f"SELECT * FROM `Teams` WHERE user_id = '{user_id}';")
                user_list = cursor.fetchall()
                cursor.close()
            
                return render_template("my_team.html", template_username=userName, template_team=user_list)

    return render_template("sign_in.html", message="You are not a registered user!")

@app.route('/pick_team',  methods=['POST','GET'])
def pick_team():
    if request.method == 'POST':
        if (request.form['teamName'] != "" and request.form['goalkeeper'] != "" and request.form['defender1'] != "" and 
            request.form['defender2'] != "" and request.form['defender3'] != "" and request.form['midfielder1'] != "" and 
            request.form['midfielder2'] != "" and request.form['midfielder3'] != "" and request.form['midfielder4'] != "" and 
            request.form['forward1'] != "" and request.form['forward2'] != "" and request.form['forward3'] != ""):
           
            teamName = request.form['teamName']
            goalkeeper = request.form['goalkeeper']
            defender1 = request.form['defender1']
            defender2 = request.form['defender2']
            defender3 = request.form['defender3']
            midfielder1 = request.form['midfielder1']
            midfielder2 = request.form['midfielder2']
            midfielder3 = request.form['midfielder3']
            midfielder4 = request.form['midfielder4']
            forward1 = request.form['forward1']
            forward2 = request.form['forward2']
            forward3 = request.form['forward3']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_dbf;")
            cursor.execute(f"SELECT * FROM `ID`;")
            user_list = cursor.fetchall()
            user_id = user_list[0]['user_id']     
            userName = user_list[0]['user_name']  
            cursor.execute(f"UPDATE `Teams` SET `team_name`='{teamName}',`goalkeeper`='{goalkeeper}',`defender1`='{defender1}',`defender2`='{defender2}',`defender3`='{defender3}',`midfielder1`='{midfielder1}',`midfielder2`='{midfielder2}',`midfielder3`='{midfielder3}',`midfielder4`='{midfielder4}',`forward1`='{forward1}',`forward2`='{forward2}',`forward3`='{forward3}' WHERE `user_id`='{user_id}';")
            cursor.execute(f"SELECT * FROM `Teams` WHERE user_id = '{user_id}';")
            dbRoutines.mysql.connection.commit()
            user_list = cursor.fetchall()
            cursor.close()
                
            return render_template("my_team.html", template_username=userName, template_team=user_list)

    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_dbf;")
    cursor.execute(f"SELECT * FROM `ID`;")
    user_list = cursor.fetchall()
    userName = user_list[0]['user_name'] 
    cursor.close()

    return render_template("pick_team.html", message = "Please, select all your players!", template_username=userName, template_goalkeepers=goalkeepers, template_defenders=defenders, 
                            template_midfielders=midfielders, template_forwards=forwards)

@app.route('/my_team')
def my_team():
    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_dbf;")
    cursor.execute(f"SELECT * FROM `ID`;")
    user_list = cursor.fetchall()
    user_id = user_list[0]['user_id']     
    userName = user_list[0]['user_name']  
    cursor.execute(f"SELECT * FROM `Teams` WHERE user_id = '{user_id}';")
    dbRoutines.mysql.connection.commit()
    user_list = cursor.fetchall()
    cursor.close()

    return render_template("my_team.html", template_username=userName, template_team=user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


