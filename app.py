from flask import Flask,render_template,request
from robots import bot_controller
import view
import persistence as p

app = Flask(__name__)


@app.route('/subscribe',methods=['GET','POST'])
def subscribe():
    form_data = request.form
    email = form_data['email']
    selected_shoe = form_data['sn']
    shoe_size = form_data['ss']
    weekly_update = False
    gender = 'Male'
    try:
        gender = form_data['sg']
        if gender == 'on':
            gender = 'Female'
    except:
        pass
    try:
        weekly_update = form_data['su']
        if weekly_update == 'on':
            weekly_update = 'Daily'
    except:
        pass
    global details 

    details = {'email':email, 'shoes':selected_shoe, 'size':shoe_size, 'updates':weekly_update, 'gender':gender}
    
    conn = view.website_connection.config_connect()
    p.db_updates.push_to_shoe_request(conn, details)
    
    return render_template('success.html')

@app.route('/')
def index():
    return render_template('index.html')


#if __name__ == '__main__':
app.run()
