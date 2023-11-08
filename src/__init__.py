import os
from flask import *
app = Flask(__name__,static_folder='./static') 
  
  
@app.route('/') 
def main(): 
    return render_template("index.html") 
  
  
@app.route('/upload', methods=['POST']) 
def upload(): 
    if request.method == 'POST': 
        files = request.files.getlist("file") 
  
        for file in files: 
            file.save(file.filename) 
        return render_template("engine_load.html")

@app.route('/searchterm', methods=['POST','GET'])
def search_term():
    if request.method == 'POST':
        sterm = request.form["sterm"]
        return redirect(url_for('displaysearch.html',sterm = sterm))
    return render_template("searchterm.html")

@app.route('/displaysearch', methods=['POST','GET'])
def display_search():
    sterm = request.args.get('sterm', None)
    return render_template("displaysearch.html",sterm=sterm)

@app.route('/displaytopn', methods=['POST','GET'])
def display_topn():
    return render_template("displaytopn.html")

@app.route('/topn', methods=['POST'])
def top_n():
    return render_template("entertopn.html")

if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=5091) 