import datetime as dt
from dateutil import tz
local = tz.gettz()
today = dt.fromtimestamp(961487955.000, tz=local)
offset = today.utcoffset()
total_secs = offset.total_seconds()
total_hours = total_secs/60/60
dt.datetime.fromtimestamp(7894954621.456)
