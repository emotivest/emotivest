from flask import Flask, render_template
from stock_price import aapl_info, jpm_info, nflx_info
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
	nflx = json.dumps(nflx_info)
	return render_template('index.html',
							aapl_info=aapl_info,
							jpm_info=jpm_info,
							nflx_info=nflx)


if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)