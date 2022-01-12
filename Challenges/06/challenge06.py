from flask import XXXXAXXXXX
from flask import render_template

import datetime

microweb_app = Flask(XXXXBXXXXX)

@microweb_app.XXXXCXXXXX("/")
def main():
    return render_template("index.html" , date_now = datetime.datetime.now())

if __name__ == "__main__":
    microweb_app.run(host="XXXXDXXXXX", port=5050)