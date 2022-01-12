import time
from datetime import datetime, timedelta
import ccxt
import requests
import pandas as pd
import numpy as np


def bitmex_getPrice(f, t):
 done = False
 while not done:
  try:
   url = "https://www.bitmex.com/api/udf/history?symbol=XBTUSD&resolution=5&from={start}&to={end}".format(start=f,
                                                                                                          end=t)
   res = requests.get(url).json()
   chart = []
   for i in range(0, len(res['c']) - 1):
    chart.append([res['t'][i], res['o'][i], res['h'][i], res['l'][i], res['c'][i], res['v'][i]])
   columns = ['time', 'open', 'high', 'low', 'close', 'vol']
   df = pd.DataFrame.from_records(chart, columns=columns)
   done = True
  except Exception as e:
   print(e)
   pass
 return df

data = {
 "name": "KHream",
 "type": "public_channel",
 "id": 10083966286,
 "messages": [
  {
   "id": 4984,
   "type": "message",
   "date": "2021-01-31T21:02:29",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33467.0/1"
  },
  {
   "id": 4985,
   "type": "message",
   "date": "2021-01-31T21:16:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33389.0/2"
  },
  {
   "id": 4986,
   "type": "message",
   "date": "2021-01-31T21:27:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33579.5/5.16"
  },
  {
   "id": 4987,
   "type": "message",
   "date": "2021-01-31T21:29:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33875.5/1"
  },
  {
   "id": 4988,
   "type": "message",
   "date": "2021-01-31T22:18:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33772.5/5.42"
  },
  {
   "id": 4989,
   "type": "message",
   "date": "2021-01-31T23:43:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33400.0/1"
  },
  {
   "id": 4990,
   "type": "message",
   "date": "2021-01-31T23:48:34",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33670.0/6.05"
  },
  {
   "id": 4991,
   "type": "message",
   "date": "2021-02-01T00:15:03",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33145.5/1"
  },
  {
   "id": 4992,
   "type": "message",
   "date": "2021-02-01T00:36:51",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 32616.0/2"
  },
  {
   "id": 4993,
   "type": "message",
   "date": "2021-02-01T01:27:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33014.0/6.75"
  },
  {
   "id": 4994,
   "type": "message",
   "date": "2021-02-01T02:46:20",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 32648.0/1"
  },
  {
   "id": 4995,
   "type": "message",
   "date": "2021-02-01T02:53:07",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 32510.0/2"
  },
  {
   "id": 4996,
   "type": "message",
   "date": "2021-02-01T03:40:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 32637.0/7.1"
  },
  {
   "id": 4997,
   "type": "message",
   "date": "2021-02-01T07:41:38",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33058.0/1"
  },
  {
   "id": 4998,
   "type": "message",
   "date": "2021-02-01T09:01:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33069.0/7.11"
  },
  {
   "id": 4999,
   "type": "message",
   "date": "2021-02-01T09:16:58",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 32520.5/1"
  },
  {
   "id": 5000,
   "type": "message",
   "date": "2021-02-01T10:21:44",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 32648.0/7.45"
  },
  {
   "id": 5001,
   "type": "message",
   "date": "2021-02-01T10:36:51",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33178.5/1"
  },
  {
   "id": 5002,
   "type": "message",
   "date": "2021-02-01T10:42:30",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33456.0/2"
  },
  {
   "id": 5003,
   "type": "message",
   "date": "2021-02-01T12:24:02",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33546.0/6.51"
  },
  {
   "id": 5004,
   "type": "message",
   "date": "2021-02-01T13:24:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33910.0/1"
  },
  {
   "id": 5005,
   "type": "message",
   "date": "2021-02-01T13:36:31",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33658.5/7.1"
  },
  {
   "id": 5006,
   "type": "message",
   "date": "2021-02-01T15:41:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34399.5/1"
  },
  {
   "id": 5007,
   "type": "message",
   "date": "2021-02-01T15:45:17",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33784.0/8.47"
  },
  {
   "id": 5008,
   "type": "message",
   "date": "2021-02-01T17:46:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34071.5/1"
  },
  {
   "id": 5009,
   "type": "message",
   "date": "2021-02-01T17:55:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34246.5/2"
  },
  {
   "id": 5010,
   "type": "message",
   "date": "2021-02-01T19:04:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 34317.0/7.86"
  },
  {
   "id": 5011,
   "type": "message",
   "date": "2021-02-01T21:42:34",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33956.0/1"
  },
  {
   "id": 5012,
   "type": "message",
   "date": "2021-02-01T21:52:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33681.5/2"
  },
  {
   "id": 5013,
   "type": "message",
   "date": "2021-02-01T22:45:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33967.5/8.61"
  },
  {
   "id": 5014,
   "type": "message",
   "date": "2021-02-01T23:13:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33467.0/1"
  },
  {
   "id": 5015,
   "type": "message",
   "date": "2021-02-01T23:30:29",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33784.0/9.37"
  },
  {
   "id": 5016,
   "type": "message",
   "date": "2021-02-02T02:52:31",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33784.0/1"
  },
  {
   "id": 5017,
   "type": "message",
   "date": "2021-02-02T03:56:21",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33784.0/9.4"
  },
  {
   "id": 5020,
   "type": "message",
   "date": "2021-02-02T06:32:01",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33692.5/1"
  },
  {
   "id": 5021,
   "type": "message",
   "date": "2021-02-02T07:17:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33772.5/9.97"
  },
  {
   "id": 5022,
   "type": "message",
   "date": "2021-02-02T09:14:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33875.5/1"
  },
  {
   "id": 5023,
   "type": "message",
   "date": "2021-02-02T10:00:50",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33749.5/10.29"
  },
  {
   "id": 5024,
   "type": "message",
   "date": "2021-02-02T11:49:10",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 33864.0/1"
  },
  {
   "id": 5025,
   "type": "message",
   "date": "2021-02-02T11:51:29",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 33681.5/10.75"
  },
  {
   "id": 5026,
   "type": "message",
   "date": "2021-02-02T13:01:17",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 33534.5/1"
  },
  {
   "id": 5027,
   "type": "message",
   "date": "2021-02-02T13:16:42",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 33647.5/11.05"
  },
  {
   "id": 5028,
   "type": "message",
   "date": "2021-02-02T15:53:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34340.5/1"
  },
  {
   "id": 5029,
   "type": "message",
   "date": "2021-02-02T16:03:37",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34423.5/2"
  },
  {
   "id": 5030,
   "type": "message",
   "date": "2021-02-02T17:29:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 34317.0/11.41"
  },
  {
   "id": 5031,
   "type": "message",
   "date": "2021-02-02T17:59:17",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34698.0/1"
  },
  {
   "id": 5032,
   "type": "message",
   "date": "2021-02-02T18:01:45",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 34940.5/2"
  },
  {
   "id": 5033,
   "type": "message",
   "date": "2021-02-02T18:05:28",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35236.0/3"
  },
  {
   "id": 5034,
   "type": "message",
   "date": "2021-02-02T18:17:27",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35549.5/4"
  },
  {
   "id": 5035,
   "type": "message",
   "date": "2021-02-02T19:15:43",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 35174.0/10.95"
  },
  {
   "id": 5036,
   "type": "message",
   "date": "2021-02-02T20:29:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 35014.0/1"
  },
  {
   "id": 5037,
   "type": "message",
   "date": "2021-02-02T20:53:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 34855.5/2"
  },
  {
   "id": 5038,
   "type": "message",
   "date": "2021-02-02T21:01:02",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 34638.0/3"
  },
  {
   "id": 5039,
   "type": "message",
   "date": "2021-02-02T22:05:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 34928.5/11.71"
  },
  {
   "id": 5040,
   "type": "message",
   "date": "2021-02-02T22:16:37",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35137.0/1"
  },
  {
   "id": 5041,
   "type": "message",
   "date": "2021-02-02T22:30:42",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 34965.0/12.14"
  },
  {
   "id": 5042,
   "type": "message",
   "date": "2021-02-02T23:30:34",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 34459.0/1"
  },
  {
   "id": 5043,
   "type": "message",
   "date": "2021-02-02T23:57:05",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 34867.5/13.11"
  },
  {
   "id": 5044,
   "type": "message",
   "date": "2021-02-03T03:32:23",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35051.0/1"
  },
  {
   "id": 5045,
   "type": "message",
   "date": "2021-02-03T03:47:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35087.5/2"
  },
  {
   "id": 5046,
   "type": "message",
   "date": "2021-02-03T03:51:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35286.0/3"
  },
  {
   "id": 5047,
   "type": "message",
   "date": "2021-02-03T04:03:28",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35335.5/4"
  },
  {
   "id": 5048,
   "type": "message",
   "date": "2021-02-03T04:54:51",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 35804.0/5"
  },
  {
   "id": 5049,
   "type": "message",
   "date": "2021-02-03T05:00:31",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36010.0/6"
  },
  {
   "id": 5050,
   "type": "message",
   "date": "2021-02-03T06:12:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 35727.0/9.53"
  },
  {
   "id": 5051,
   "type": "message",
   "date": "2021-02-03T09:26:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36049.0/1"
  },
  {
   "id": 5052,
   "type": "message",
   "date": "2021-02-03T10:30:16",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 36023.0/9.63"
  },
  {
   "id": 5053,
   "type": "message",
   "date": "2021-02-03T12:21:51",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36179.5/1"
  },
  {
   "id": 5054,
   "type": "message",
   "date": "2021-02-03T12:53:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36390.0/2"
  },
  {
   "id": 5055,
   "type": "message",
   "date": "2021-02-03T13:00:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36616.5/3"
  },
  {
   "id": 5056,
   "type": "message",
   "date": "2021-02-03T14:15:27",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 36643.5/8.23"
  },
  {
   "id": 5057,
   "type": "message",
   "date": "2021-02-03T15:38:10",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36792.0/1"
  },
  {
   "id": 5058,
   "type": "message",
   "date": "2021-02-03T15:59:32",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 36643.5/8.57"
  },
  {
   "id": 5059,
   "type": "message",
   "date": "2021-02-03T16:48:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 36443.0/1"
  },
  {
   "id": 5060,
   "type": "message",
   "date": "2021-02-03T17:00:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 36284.5/2"
  },
  {
   "id": 5061,
   "type": "message",
   "date": "2021-02-03T17:32:09",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 35816.5/3"
  },
  {
   "id": 5062,
   "type": "message",
   "date": "2021-02-03T18:55:30",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 35958.5/7.27"
  },
  {
   "id": 5063,
   "type": "message",
   "date": "2021-02-03T19:57:43",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36088.0/1"
  },
  {
   "id": 5064,
   "type": "message",
   "date": "2021-02-03T20:52:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 36062.0/7.36"
  },
  {
   "id": 5065,
   "type": "message",
   "date": "2021-02-04T00:23:14",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36805.5/1"
  },
  {
   "id": 5066,
   "type": "message",
   "date": "2021-02-04T00:32:24",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 36982.5/2"
  },
  {
   "id": 5067,
   "type": "message",
   "date": "2021-02-04T01:20:45",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 36805.5/7.79"
  },
  {
   "id": 5068,
   "type": "message",
   "date": "2021-02-04T01:54:53",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37244.0/1"
  },
  {
   "id": 5069,
   "type": "message",
   "date": "2021-02-04T02:31:49",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37023.5/8.27"
  },
  {
   "id": 5070,
   "type": "message",
   "date": "2021-02-04T03:16:02",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 36900.5/1"
  },
  {
   "id": 5071,
   "type": "message",
   "date": "2021-02-04T03:27:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37092.0/8.7"
  },
  {
   "id": 5072,
   "type": "message",
   "date": "2021-02-04T05:03:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 36710.5/1"
  },
  {
   "id": 5073,
   "type": "message",
   "date": "2021-02-04T05:22:59",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 36941.5/9.22"
  },
  {
   "id": 5074,
   "type": "message",
   "date": "2021-02-04T05:42:44",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37064.5/1"
  },
  {
   "id": 5075,
   "type": "message",
   "date": "2021-02-04T06:00:53",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37188.5/2"
  },
  {
   "id": 5076,
   "type": "message",
   "date": "2021-02-04T06:34:13",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37397.0/3"
  },
  {
   "id": 5077,
   "type": "message",
   "date": "2021-02-04T07:52:50",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37369.0/8.4"
  },
  {
   "id": 5078,
   "type": "message",
   "date": "2021-02-04T09:13:57",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38052.0/1"
  },
  {
   "id": 5079,
   "type": "message",
   "date": "2021-02-04T10:21:38",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 38008.5/8.52"
  },
  {
   "id": 5080,
   "type": "message",
   "date": "2021-02-04T14:18:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37994.0/1"
  },
  {
   "id": 5081,
   "type": "message",
   "date": "2021-02-04T14:39:31",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37778.5/8.99"
  },
  {
   "id": 5082,
   "type": "message",
   "date": "2021-02-04T15:30:10",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38168.0/1"
  },
  {
   "id": 5083,
   "type": "message",
   "date": "2021-02-04T16:31:30",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 38023.0/9.09"
  },
  {
   "id": 5084,
   "type": "message",
   "date": "2021-02-04T17:14:43",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38565.5/1"
  },
  {
   "id": 5085,
   "type": "message",
   "date": "2021-02-04T17:23:41",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38759.5/2"
  },
  {
   "id": 5086,
   "type": "message",
   "date": "2021-02-04T17:46:28",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 38255.5/10.76"
  },
  {
   "id": 5087,
   "type": "message",
   "date": "2021-02-04T17:59:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37369.0/1"
  },
  {
   "id": 5088,
   "type": "message",
   "date": "2021-02-04T19:18:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37551.5/11.19"
  },
  {
   "id": 5089,
   "type": "message",
   "date": "2021-02-04T21:00:13",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37341.5/1"
  },
  {
   "id": 5090,
   "type": "message",
   "date": "2021-02-04T21:37:24",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37650.5/11.87"
  },
  {
   "id": 5091,
   "type": "message",
   "date": "2021-02-04T23:38:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37174.5/1"
  },
  {
   "id": 5092,
   "type": "message",
   "date": "2021-02-04T23:47:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37051.0/2"
  },
  {
   "id": 5093,
   "type": "message",
   "date": "2021-02-05T01:19:42",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 36697.5/10.15"
  },
  {
   "id": 5094,
   "type": "message",
   "date": "2021-02-05T03:17:23",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37161.0/1"
  },
  {
   "id": 5095,
   "type": "message",
   "date": "2021-02-05T03:46:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37051.0/10.42"
  },
  {
   "id": 5096,
   "type": "message",
   "date": "2021-02-05T05:04:49",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37750.0/1"
  },
  {
   "id": 5097,
   "type": "message",
   "date": "2021-02-05T06:19:12",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37580.0/10.8"
  },
  {
   "id": 5098,
   "type": "message",
   "date": "2021-02-05T08:47:36",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 36955.0/1"
  },
  {
   "id": 5099,
   "type": "message",
   "date": "2021-02-05T09:25:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37202.5/11.36"
  },
  {
   "id": 5100,
   "type": "message",
   "date": "2021-02-05T10:58:27",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 36846.0/1"
  },
  {
   "id": 5101,
   "type": "message",
   "date": "2021-02-05T11:58:05",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 36914.0/11.54"
  },
  {
   "id": 5102,
   "type": "message",
   "date": "2021-02-05T12:14:16",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37313.5/1"
  },
  {
   "id": 5103,
   "type": "message",
   "date": "2021-02-05T13:38:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37327.5/11.56"
  },
  {
   "id": 5104,
   "type": "message",
   "date": "2021-02-05T15:24:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37566.0/1"
  },
  {
   "id": 5105,
   "type": "message",
   "date": "2021-02-05T17:19:17",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37636.5/11.46"
  },
  {
   "id": 5106,
   "type": "message",
   "date": "2021-02-05T18:58:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37425.0/1"
  },
  {
   "id": 5107,
   "type": "message",
   "date": "2021-02-05T19:16:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37665.0/11.99"
  },
  {
   "id": 5108,
   "type": "message",
   "date": "2021-02-05T21:24:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37979.5/1"
  },
  {
   "id": 5109,
   "type": "message",
   "date": "2021-02-05T21:32:16",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38153.5/2"
  },
  {
   "id": 5110,
   "type": "message",
   "date": "2021-02-05T22:30:57",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37965.0/12.48"
  },
  {
   "id": 5111,
   "type": "message",
   "date": "2021-02-06T01:01:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37836.0/1"
  },
  {
   "id": 5112,
   "type": "message",
   "date": "2021-02-06T01:07:56",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 38182.5/13.24"
  },
  {
   "id": 5113,
   "type": "message",
   "date": "2021-02-06T03:16:49",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37793.0/1"
  },
  {
   "id": 5114,
   "type": "message",
   "date": "2021-02-06T03:59:29",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37397.0/2"
  },
  {
   "id": 5115,
   "type": "message",
   "date": "2021-02-06T04:12:50",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37299.5/3"
  },
  {
   "id": 5116,
   "type": "message",
   "date": "2021-02-06T04:46:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37622.5/14.18"
  },
  {
   "id": 5117,
   "type": "message",
   "date": "2021-02-06T06:13:03",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 37936.5/1"
  },
  {
   "id": 5118,
   "type": "message",
   "date": "2021-02-06T07:11:53",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 37807.0/14.49"
  },
  {
   "id": 5119,
   "type": "message",
   "date": "2021-02-06T08:53:30",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38153.5/1"
  },
  {
   "id": 5120,
   "type": "message",
   "date": "2021-02-06T08:58:46",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38373.0/2"
  },
  {
   "id": 5121,
   "type": "message",
   "date": "2021-02-06T09:00:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38476.5/3"
  },
  {
   "id": 5122,
   "type": "message",
   "date": "2021-02-06T10:50:13",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 38910.5/11.09"
  },
  {
   "id": 5123,
   "type": "message",
   "date": "2021-02-06T13:16:05",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 39047.5/1"
  },
  {
   "id": 5124,
   "type": "message",
   "date": "2021-02-06T14:12:37",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 39017.0/2"
  },
  {
   "id": 5125,
   "type": "message",
   "date": "2021-02-06T15:03:14",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 39169.5/11.72"
  },
  {
   "id": 5126,
   "type": "message",
   "date": "2021-02-06T17:02:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39619.5/1"
  },
  {
   "id": 5127,
   "type": "message",
   "date": "2021-02-06T17:37:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 39494.5/12.0"
  },
  {
   "id": 5128,
   "type": "message",
   "date": "2021-02-06T18:09:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39872.5/1"
  },
  {
   "id": 5129,
   "type": "message",
   "date": "2021-02-06T18:17:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 39588.5/12.6"
  },
  {
   "id": 5130,
   "type": "message",
   "date": "2021-02-06T20:02:10",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 40274.0/1"
  },
  {
   "id": 5131,
   "type": "message",
   "date": "2021-02-06T21:11:47",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 40241.5/12.73"
  },
  {
   "id": 5132,
   "type": "message",
   "date": "2021-02-07T05:16:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 39984.0/1"
  },
  {
   "id": 5133,
   "type": "message",
   "date": "2021-02-07T05:57:07",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 40096.5/13.0"
  },
  {
   "id": 5134,
   "type": "message",
   "date": "2021-02-07T07:55:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 40080.0/1"
  },
  {
   "id": 5135,
   "type": "message",
   "date": "2021-02-07T08:01:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 39856.5/2"
  },
  {
   "id": 5136,
   "type": "message",
   "date": "2021-02-07T08:10:21",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 39730.0/3"
  },
  {
   "id": 5137,
   "type": "message",
   "date": "2021-02-07T09:00:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 38684.5/4"
  },
  {
   "id": 5138,
   "type": "message",
   "date": "2021-02-07T09:31:26",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 39463.5/12.2"
  },
  {
   "id": 5139,
   "type": "message",
   "date": "2021-02-07T10:51:48",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 38971.0/1"
  },
  {
   "id": 5140,
   "type": "message",
   "date": "2021-02-07T12:06:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 38850.0/12.0"
  },
  {
   "id": 5141,
   "type": "message",
   "date": "2021-02-07T13:33:23",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 38402.5/1"
  },
  {
   "id": 5142,
   "type": "message",
   "date": "2021-02-07T13:46:11",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 38110.0/2"
  },
  {
   "id": 5143,
   "type": "message",
   "date": "2021-02-07T14:39:05",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 38476.5/12.99"
  },
  {
   "id": 5144,
   "type": "message",
   "date": "2021-02-07T16:17:02",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39001.5/1"
  },
  {
   "id": 5145,
   "type": "message",
   "date": "2021-02-07T18:36:05",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 39448.0/12.15"
  },
  {
   "id": 5146,
   "type": "message",
   "date": "2021-02-07T18:47:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39761.5/1"
  },
  {
   "id": 5147,
   "type": "message",
   "date": "2021-02-07T18:58:45",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 39494.5/12.71"
  },
  {
   "id": 5148,
   "type": "message",
   "date": "2021-02-07T21:19:56",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 38790.0/1"
  },
  {
   "id": 5149,
   "type": "message",
   "date": "2021-02-07T22:10:26",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 38956.0/13.09"
  },
  {
   "id": 5150,
   "type": "message",
   "date": "2021-02-08T00:18:17",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37879.0/1"
  },
  {
   "id": 5151,
   "type": "message",
   "date": "2021-02-08T01:44:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 37936.5/13.26"
  },
  {
   "id": 5152,
   "type": "message",
   "date": "2021-02-08T05:01:32",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 37750.0/1"
  },
  {
   "id": 5153,
   "type": "message",
   "date": "2021-02-08T05:36:58",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 38241.0/14.32"
  },
  {
   "id": 5154,
   "type": "message",
   "date": "2021-02-08T08:02:11",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38941.0/1"
  },
  {
   "id": 5155,
   "type": "message",
   "date": "2021-02-08T08:12:32",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39032.0/2"
  },
  {
   "id": 5156,
   "type": "message",
   "date": "2021-02-08T09:00:37",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 38850.0/14.95"
  },
  {
   "id": 5157,
   "type": "message",
   "date": "2021-02-08T11:53:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 38285.0/1"
  },
  {
   "id": 5158,
   "type": "message",
   "date": "2021-02-08T12:19:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 38506.0/15.46"
  },
  {
   "id": 5159,
   "type": "message",
   "date": "2021-02-08T14:42:46",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 38910.5/1"
  },
  {
   "id": 5160,
   "type": "message",
   "date": "2021-02-08T15:14:32",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39032.0/2"
  },
  {
   "id": 5161,
   "type": "message",
   "date": "2021-02-08T15:22:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39231.0/3"
  },
  {
   "id": 5162,
   "type": "message",
   "date": "2021-02-08T16:12:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 39001.5/15.92"
  },
  {
   "id": 5163,
   "type": "message",
   "date": "2021-02-08T21:31:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 39231.0/1"
  },
  {
   "id": 5164,
   "type": "message",
   "date": "2021-02-08T21:43:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 39448.0/16.4"
  },
  {
   "id": 5165,
   "type": "message",
   "date": "2021-02-08T21:43:36",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 39714.0/1"
  },
  {
   "id": 5166,
   "type": "message",
   "date": "2021-02-08T21:51:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 41858.5/2"
  },
  {
   "id": 5167,
   "type": "message",
   "date": "2021-02-08T21:59:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 43821.0/3"
  },
  {
   "id": 5168,
   "type": "message",
   "date": "2021-02-08T23:32:49",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 43649.0/6.34"
  },
  {
   "id": 5169,
   "type": "message",
   "date": "2021-02-09T00:56:59",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 44346.0/1"
  },
  {
   "id": 5170,
   "type": "message",
   "date": "2021-02-09T01:21:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 43879.0/7.16"
  },
  {
   "id": 5171,
   "type": "message",
   "date": "2021-02-09T03:52:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 42717.0/1"
  },
  {
   "id": 5172,
   "type": "message",
   "date": "2021-02-09T04:06:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 43103.5/7.88"
  },
  {
   "id": 5173,
   "type": "message",
   "date": "2021-02-09T05:30:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 43403.0/1"
  },
  {
   "id": 5174,
   "type": "message",
   "date": "2021-02-09T05:48:28",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 43821.0/2"
  },
  {
   "id": 5175,
   "type": "message",
   "date": "2021-02-09T08:24:41",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46061.5/3"
  },
  {
   "id": 5176,
   "type": "message",
   "date": "2021-02-09T08:26:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46490.0/4"
  },
  {
   "id": 5177,
   "type": "message",
   "date": "2021-02-09T09:55:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46642.0/-2.43"
  },
  {
   "id": 5178,
   "type": "message",
   "date": "2021-02-09T10:29:12",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46040.5/1"
  },
  {
   "id": 5179,
   "type": "message",
   "date": "2021-02-09T11:36:37",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 46210.5/-2.14"
  },
  {
   "id": 5180,
   "type": "message",
   "date": "2021-02-09T13:58:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46926.5/1"
  },
  {
   "id": 5181,
   "type": "message",
   "date": "2021-02-09T14:37:42",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46707.0/-1.79"
  },
  {
   "id": 5182,
   "type": "message",
   "date": "2021-02-09T15:37:14",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47732.5/1"
  },
  {
   "id": 5183,
   "type": "message",
   "date": "2021-02-09T16:49:18",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47642.0/-1.63"
  },
  {
   "id": 5184,
   "type": "message",
   "date": "2021-02-09T17:17:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47192.0/1"
  },
  {
   "id": 5185,
   "type": "message",
   "date": "2021-02-09T17:34:59",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46860.5/2"
  },
  {
   "id": 5186,
   "type": "message",
   "date": "2021-02-09T19:33:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 46620.0/-2.77"
  },
  {
   "id": 5187,
   "type": "message",
   "date": "2021-02-10T00:23:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46970.5/1"
  },
  {
   "id": 5188,
   "type": "message",
   "date": "2021-02-10T01:02:23",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46663.5/-2.29"
  },
  {
   "id": 5189,
   "type": "message",
   "date": "2021-02-10T03:32:59",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47371.0/1"
  },
  {
   "id": 5190,
   "type": "message",
   "date": "2021-02-10T04:22:56",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46926.5/-1.62"
  },
  {
   "id": 5191,
   "type": "message",
   "date": "2021-02-10T07:02:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46860.5/1"
  },
  {
   "id": 5192,
   "type": "message",
   "date": "2021-02-10T09:15:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 46598.5/-1.97"
  },
  {
   "id": 5193,
   "type": "message",
   "date": "2021-02-10T10:22:53",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46104.0/1"
  },
  {
   "id": 5194,
   "type": "message",
   "date": "2021-02-10T11:03:23",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 46468.5/-1.39"
  },
  {
   "id": 5195,
   "type": "message",
   "date": "2021-02-10T16:20:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46970.5/1"
  },
  {
   "id": 5196,
   "type": "message",
   "date": "2021-02-10T16:43:07",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46904.5/2"
  },
  {
   "id": 5197,
   "type": "message",
   "date": "2021-02-10T16:59:42",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46707.0/-0.65"
  },
  {
   "id": 5198,
   "type": "message",
   "date": "2021-02-10T19:15:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47416.0/1"
  },
  {
   "id": 5199,
   "type": "message",
   "date": "2021-02-10T19:32:57",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46970.5/0.03"
  },
  {
   "id": 5200,
   "type": "message",
   "date": "2021-02-10T21:02:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46318.0/1"
  },
  {
   "id": 5201,
   "type": "message",
   "date": "2021-02-10T21:27:04",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46168.0/2"
  },
  {
   "id": 5202,
   "type": "message",
   "date": "2021-02-10T21:32:48",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 45850.5/3"
  },
  {
   "id": 5203,
   "type": "message",
   "date": "2021-02-10T21:40:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44944.0/4"
  },
  {
   "id": 5204,
   "type": "message",
   "date": "2021-02-10T22:37:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 45850.5/0.41"
  },
  {
   "id": 5205,
   "type": "message",
   "date": "2021-02-11T04:14:50",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44663.0/1"
  },
  {
   "id": 5206,
   "type": "message",
   "date": "2021-02-11T04:15:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 45045.0/1.05"
  },
  {
   "id": 5207,
   "type": "message",
   "date": "2021-02-11T08:50:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44903.5/1"
  },
  {
   "id": 5208,
   "type": "message",
   "date": "2021-02-11T09:02:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44743.0/2"
  },
  {
   "id": 5209,
   "type": "message",
   "date": "2021-02-11T09:14:41",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44523.5/3"
  },
  {
   "id": 5210,
   "type": "message",
   "date": "2021-02-11T09:33:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 45004.5/2.5"
  },
  {
   "id": 5211,
   "type": "message",
   "date": "2021-02-11T09:48:55",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44111.0/1"
  },
  {
   "id": 5212,
   "type": "message",
   "date": "2021-02-11T10:32:38",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 44543.5/3.24"
  },
  {
   "id": 5213,
   "type": "message",
   "date": "2021-02-11T12:10:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 45025.0/1"
  },
  {
   "id": 5214,
   "type": "message",
   "date": "2021-02-11T12:54:16",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 45147.0/2"
  },
  {
   "id": 5215,
   "type": "message",
   "date": "2021-02-11T13:15:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 44984.5/3.68"
  },
  {
   "id": 5216,
   "type": "message",
   "date": "2021-02-11T15:38:53",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 44543.5/1"
  },
  {
   "id": 5217,
   "type": "message",
   "date": "2021-02-11T16:07:22",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 44763.0/4.08"
  },
  {
   "id": 5218,
   "type": "message",
   "date": "2021-02-11T19:44:58",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46040.5/1"
  },
  {
   "id": 5219,
   "type": "message",
   "date": "2021-02-11T20:58:44",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46125.5/3.98"
  },
  {
   "id": 5220,
   "type": "message",
   "date": "2021-02-11T22:05:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 46882.5/1"
  },
  {
   "id": 5221,
   "type": "message",
   "date": "2021-02-11T22:13:11",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47371.0/2"
  },
  {
   "id": 5222,
   "type": "message",
   "date": "2021-02-11T22:19:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47892.5/3"
  },
  {
   "id": 5223,
   "type": "message",
   "date": "2021-02-11T22:21:07",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48356.0/4"
  },
  {
   "id": 5224,
   "type": "message",
   "date": "2021-02-12T00:09:15",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47892.5/2.51"
  },
  {
   "id": 5225,
   "type": "message",
   "date": "2021-02-12T01:01:11",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48402.5/1"
  },
  {
   "id": 5226,
   "type": "message",
   "date": "2021-02-12T08:12:05",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47892.5/3.51"
  },
  {
   "id": 5227,
   "type": "message",
   "date": "2021-02-12T09:10:13",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48733.0/1"
  },
  {
   "id": 5228,
   "type": "message",
   "date": "2021-02-12T09:11:31",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48971.5/2"
  },
  {
   "id": 5229,
   "type": "message",
   "date": "2021-02-12T09:53:11",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 48286.0/5.35"
  },
  {
   "id": 5230,
   "type": "message",
   "date": "2021-02-12T19:21:42",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47710.0/1"
  },
  {
   "id": 5231,
   "type": "message",
   "date": "2021-02-12T19:58:24",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47416.0/5.83"
  },
  {
   "id": 5232,
   "type": "message",
   "date": "2021-02-12T23:29:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47506.0/1"
  },
  {
   "id": 5233,
   "type": "message",
   "date": "2021-02-12T23:31:17",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47236.5/2"
  },
  {
   "id": 5234,
   "type": "message",
   "date": "2021-02-12T23:37:45",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47103.0/3"
  },
  {
   "id": 5235,
   "type": "message",
   "date": "2021-02-12T23:47:30",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46318.0/4"
  },
  {
   "id": 5236,
   "type": "message",
   "date": "2021-02-13T00:40:51",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 47103.0/6.41"
  },
  {
   "id": 5237,
   "type": "message",
   "date": "2021-02-13T01:27:41",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47915.5/1"
  },
  {
   "id": 5238,
   "type": "message",
   "date": "2021-02-13T02:34:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47596.5/6.93"
  },
  {
   "id": 5239,
   "type": "message",
   "date": "2021-02-13T03:25:20",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47393.5/1"
  },
  {
   "id": 5240,
   "type": "message",
   "date": "2021-02-13T03:36:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47303.5/2"
  },
  {
   "id": 5241,
   "type": "message",
   "date": "2021-02-13T03:50:07",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47147.5/3"
  },
  {
   "id": 5242,
   "type": "message",
   "date": "2021-02-13T04:34:28",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 47483.5/8.01"
  },
  {
   "id": 5243,
   "type": "message",
   "date": "2021-02-13T05:35:10",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47619.0/1"
  },
  {
   "id": 5244,
   "type": "message",
   "date": "2021-02-13T06:06:52",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47915.5/2"
  },
  {
   "id": 5245,
   "type": "message",
   "date": "2021-02-13T06:30:49",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48007.5/3"
  },
  {
   "id": 5246,
   "type": "message",
   "date": "2021-02-13T06:42:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48309.0/4"
  },
  {
   "id": 5247,
   "type": "message",
   "date": "2021-02-13T07:35:00",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47892.5/8.59"
  },
  {
   "id": 5248,
   "type": "message",
   "date": "2021-02-13T08:23:43",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47687.0/1"
  },
  {
   "id": 5249,
   "type": "message",
   "date": "2021-02-13T08:31:30",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47416.0/2"
  },
  {
   "id": 5250,
   "type": "message",
   "date": "2021-02-13T09:43:33",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 47596.5/8.81"
  },
  {
   "id": 5251,
   "type": "message",
   "date": "2021-02-13T10:18:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47870.0/1"
  },
  {
   "id": 5252,
   "type": "message",
   "date": "2021-02-13T11:19:11",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47755.5/9.03"
  },
  {
   "id": 5253,
   "type": "message",
   "date": "2021-02-13T11:47:19",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48007.5/1"
  },
  {
   "id": 5254,
   "type": "message",
   "date": "2021-02-13T12:07:03",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48193.0/2"
  },
  {
   "id": 5255,
   "type": "message",
   "date": "2021-02-13T12:32:18",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47938.5/9.62"
  },
  {
   "id": 5256,
   "type": "message",
   "date": "2021-02-13T14:28:18",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47710.0/1"
  },
  {
   "id": 5257,
   "type": "message",
   "date": "2021-02-13T14:44:59",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 47915.5/9.98"
  },
  {
   "id": 5258,
   "type": "message",
   "date": "2021-02-13T16:37:34",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47393.5/1"
  },
  {
   "id": 5259,
   "type": "message",
   "date": "2021-02-13T16:53:43",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47303.5/2"
  },
  {
   "id": 5260,
   "type": "message",
   "date": "2021-02-13T17:00:10",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47059.0/3"
  },
  {
   "id": 5261,
   "type": "message",
   "date": "2021-02-13T17:33:27",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 47483.5/11.24"
  },
  {
   "id": 5262,
   "type": "message",
   "date": "2021-02-13T20:10:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 46490.0/1"
  },
  {
   "id": 5263,
   "type": "message",
   "date": "2021-02-13T21:06:39",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 46794.5/11.73"
  },
  {
   "id": 5264,
   "type": "message",
   "date": "2021-02-14T06:10:40",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47081.0/1"
  },
  {
   "id": 5265,
   "type": "message",
   "date": "2021-02-14T06:28:51",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 46882.5/12.1"
  },
  {
   "id": 5266,
   "type": "message",
   "date": "2021-02-14T06:46:47",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47214.5/1"
  },
  {
   "id": 5267,
   "type": "message",
   "date": "2021-02-14T07:30:07",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47036.5/12.43"
  },
  {
   "id": 5268,
   "type": "message",
   "date": "2021-02-14T09:14:53",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47596.5/1"
  },
  {
   "id": 5269,
   "type": "message",
   "date": "2021-02-14T10:44:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 47596.5/12.47"
  },
  {
   "id": 5270,
   "type": "message",
   "date": "2021-02-14T12:58:25",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 47416.0/1"
  },
  {
   "id": 5271,
   "type": "message",
   "date": "2021-02-14T13:09:54",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 47574.0/12.77"
  },
  {
   "id": 5272,
   "type": "message",
   "date": "2021-02-14T14:24:21",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 47984.5/1"
  },
  {
   "id": 5273,
   "type": "message",
   "date": "2021-02-14T14:47:35",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 48426.0/2"
  },
  {
   "id": 5274,
   "type": "message",
   "date": "2021-02-14T15:00:08",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 49092.0/3"
  },
  {
   "id": 5275,
   "type": "message",
   "date": "2021-02-14T15:00:26",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 49358.5/4"
  },
  {
   "id": 5276,
   "type": "message",
   "date": "2021-02-14T16:05:06",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out long : 48828.0/12.17"
  },
  {
   "id": 5277,
   "type": "message",
   "date": "2021-02-14T17:53:29",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in long : 48709.0/1"
  },
  {
   "id": 5278,
   "type": "message",
   "date": "2021-02-14T18:10:21",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position out short : 48900.0/12.52"
  },
  {
   "id": 5279,
   "type": "message",
   "date": "2021-02-14T21:12:49",
   "from": "KHream",
   "from_id": 10083966286,
   "text": "Position in short : 49480.5/1"
  }
 ]
}
bitmex = ccxt.bitmex({
 'apiKey': 'ebiUGrerxc_KOeqVUp9-j5m6',
 'secret': '0e2iAseYA8bl-ETcgDKpy0wjZ4sxj_u-IcMqG9SXYhrUyjDh',
 'enableRateLimit': True,
 'options' : {
  'api-expires' : 86400
 }
})

tpnl = 0
ptpnl = 0
pnl = 0
wnl = 'win'
f = open("./result.txt", "a")
for i in data['messages']:
 if('out' in i['text']):
  tpnl = float(i['text'].split('/')[1])
  pnl = (100*tpnl - 100*ptpnl)/(100+ptpnl)
  if(pnl > 0):wnl='win'
  else:wnl='lose'
  text = i['date'].split('T')[0]+'/'+i['text'].split('/')[1]+'/'+str(pnl)+'/'+wnl+'\n'
  f.write(text)
  ptpnl = float(i['text'].split('/')[1])
f.close()
#
i = 1
while(datetime.date(datetime(2021, 1, 31)+timedelta(days=i)) <= datetime.date(datetime(2021, 2, 14))):
 f = int(str_to_timestamp('2018-{f}-01 00:00:00'.format(f=k)))
 t = int(str_to_timestamp('2018-{t}-01 00:00:00'.format(t=k+1)))
 df = bitmex_getPrice(f,t)
 bitmex.fetch_ohlcv()

i = 1
while(datetime.date(datetime(2021, 1, 31)+timedelta(days=i)) <= datetime.date(datetime(2021, 2, 14))):
 print(str(datetime.date(datetime(2021, 1, 31)+timedelta(days=i))))
 i = i + 1