import numpy as np
from tweets.jpm import sentiment_jpm
from tweets.aapl import sentiment_aapl
from tweets.nflx import sentiment_nflx
from stock_price import aapl_info, jpm_info, nflx_info

aapl_sentiment = [float(x) for x in sentiment_aapl.final[1:]]
aapl_array = np.asarray(aapl_sentiment)


jpm_sentiment = [float(x) for x in sentiment_jpm.final[1:]]
jpm_array = np.asarray(jpm_sentiment)

nflx_sentiment = [float(x) for x in sentiment_nflx.final[1:]]
nflx_array = np.asarray(nflx_sentiment)

aapl = np.asarray(aapl_info['stock'][1:8])
jpm = np.asarray(jpm_info['stock'][1:8])
nflx = np.asarray(nflx_info['stock'][1:8])

aapl_correlation = np.corrcoef(aapl_array, aapl)
jpm_correlation = np.corrcoef(jpm_array, jpm)
nflx_correlation = np.corrcoef(nflx_array, nflx)
print(aapl_correlation, nflx_correlation, jpm_correlation)

