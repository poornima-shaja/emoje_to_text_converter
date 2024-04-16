from flask import Flask,render_template,request
import demoji
demoji.download_codes()

app = Flask(__name__)
@app.route("/" , methods = ['GET','POST'])
def index():
    if request.method == "POST":
        emoje_list = request.form['emoje_list']
        result = demoji.findall(emoje_list)
        return render_template("index.html",emoje_list=emoje_list,result=result)
    else:
        return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)





