from flask import Flask, render_template
from stock_price import aapl_info, jpm_info, nflx_info
from correlation import aapl_correlation, jpm_correlation, nflx_correlation
import json

app = Flask(__name__)

# print(len(aapl_info['stock']), len(aapl_info['date_list']), len(aapl_info['sentiment']))
# print(nflx_info)
# print(jpm_info)

@app.route("/", methods=['GET'])
def home():
	nflx = json.dumps(nflx_info)
	aapl = json.dumps(aapl_info)
	jpm = json.dumps(jpm_info)
	return render_template('index.html',
							nflx_info=nflx,
							aapl_info=aapl,
							jpm_info=jpm,
							aapl_corr=aapl_correlation[0][1],
							nflx_corr=nflx_correlation[0][1],
							jpm_corr=jpm_correlation[0][1]
							)


if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)