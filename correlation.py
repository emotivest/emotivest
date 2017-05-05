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

aapl = np.asarray(aapl_info['stock'][1:])
jpm = np.asarray(jpm_info['stock'][1:])
nflx = np.asarray(nflx_info['stock'][1:])

print(aapl_array)
print(aapl)
aapl_correlation = np.corrcoef(aapl, aapl_array)
jpm_correlation = np.corrcoef(jpm, jpm_array)
nflx_correlation = np.corrcoef(nflx, nflx_array)



