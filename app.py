import sqlite3
from flask import Flask , render_template, g
import Log, time
#import datetime

app = Flask(__name__)

@app.route("/forside")
def forside():
    data = get_db()
    print(data)
    return render_template("forside.html", all_data = data)

if Log.getMotiondata is True:
    @app.route("/db")
    def tilbud():
        return render_template("test.html")
if Log.getMotiondata and Log.getButtondata is True:
    @app.route("/blank")
    def blank():
        return render_template("index.html")


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
if __name__ == '__main__':
    app.run()

def loop():
    print("hej")
    time.sleep(1)
    Log.getButtondata()
    Log.getMotiondata()
    Log.logData()
    #app.run()
    if(Log.data.motion == 1):
        forside()
        for i in range (240):
            Log.getButtondata()
            Log.getMotiondata()
            Log.logData()
            if(Log.data.button == 1):
                tilbud()
                time.sleep(120)
                break
            time.sleep(0.25)


