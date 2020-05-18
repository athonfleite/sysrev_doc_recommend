from flask import Flask, url_for, render_template, request
#from markupsafe import escape
from text_analysisV2 import CSVs_to_Excel
app = Flask(__name__)#static_url_path='/static')
@app.route('/')
def index():
    #return render_template('index.html', dir_path00="OK Button")
    return render_template('core.html')
    
    @app.route('/', methods=['POST'])
    def my_form_post():
        input_nopol = request.form['question_01']
        if request.method == 'POST':
           with open('question_01.txt', 'w') as f:
                f.write(str(input_nopol))
        return render_template('core.html', nopol=input_nopol)




# @app.route('/csv',methods=["POST","GET"])
# def start_analysis():
#     print(request.form["dirname"])
#     dirname=request.form["dirname"]
    
#     csv_core=CSVs_to_Excel(csv_dirname= dirname)
#     #### Merges All CSV files into a single xlsx file
#     merged_path=csv_core.merge_csv(output='raw_merged.xlsx')
#     return merged_path

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)
    
# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
    #print(url_for('login'))
    #print(url_for('login', next='/'))
    #print(url_for('profile', username='John Doe'))
