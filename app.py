from watson_developer_cloud import ToneAnalyzerV3 as TA
from flask import Flask, render_template, request

# Add you API here
WATSON = {"password": "P6wnCRlWwNAV","username": "3b660917-905a-4d69-9b26-7bbd30bd951e", "version": "2017-03-21"}  
# ^ API key
app = Flask(__name__)
senti_model = None

def analyse(data):
    try:
        senti_model = TA(**WATSON)
    except:
        print "Watson Not reachable"
    if senti_model is None:
        return {}
    return senti_model.tone(text=data)
    # ^This is the analysis part

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/senti', methods = ['GET', 'POST'])
def senti():
    global data
    result = request.form
    data = result['data']
    #^ gets data from form
    senti_dict = analyse(data)                       
    return render_template('senti.html', list=senti_dict['document_tone']['tone_categories'])   
    #^renders senti.html present in templates

if __name__ == "__main__":
    app.run(port=5000)