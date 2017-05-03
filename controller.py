from flask import Flask, render_template
from stock_price import aapl_info, jpm_info, nflx_info
# from correlation import aapl_correlation, jpm_correlation, nflx_correlation
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
	nflx = json.dumps(nflx_info)
	aapl = json.dumps(aapl_info)
	print(aapl)
	jpm = json.dumps(jpm_info)
	print(jpm)
	return render_template('index.html',
							nflx_info=nflx,
							aapl_info=aapl,
							jpm_info=jpm,
							# aapl_corr=aapl_correlation,
							# nflx_corr=nflx_corr,
							# jpm_corr=jpm_correlation
							)


if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)