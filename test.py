import datetime
import pytz

local_timezone = datetime.datetime.now(pytz.utc).astimezone().tzinfo
print(local_timezone)
