import pickle as p 

# Create your views here.
from flask import Flask , render_template ,request

app = Flask(__name__)

model = p.load(open('ipl_tree_model.dat' , 'rb'))
f = open('ipl_data.dat' , 'rb')

encoded_data = p.load(f)

decoded_data = {}
for k,v in encoded_data.items():
    decoded_data[v] = k 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict' , methods = ['GET' , "POST"])
def predict():

        team1 = encoded_data[request.args.get('team1')]
        team2 = encoded_data[request.args.get('team2')]
        city = encoded_data[request.args.get('city')]
        venue = encoded_data[request.args.get('venue')]

        neutral_venue = 0

        toss_winner = request.args.get('toss_winner')


        toss_decision = encoded_data[request.args.get('toss_decision')]

        eliminator = encoded_data[request.args.get('eliminator')]

        if team1 == team2:
            return redirect(url_for('home'))

        if toss_winner == 'team1':
            toss_winner = encoded_data[ decoded_data[team1]  ]
        else:
            toss_winner = encoded_data[ decoded_data[team2] ]

        data = [[team1 , team2 ,toss_winner , toss_decision,city, venue ,neutral_venue, eliminator]]

        print(data)

        predict = model.predict(data) 
        print(predict)
       # [[75, 80, 75, 62, 23, 43, 82]]

        if predict[0] == 0:
            winner = decoded_data[team1]
        else:
            winner = decoded_data[team2]
        print(winner)

        return render_template('predict.html' ,data = winner)

if __name__ == '__main__':
    app.run(debug= True)