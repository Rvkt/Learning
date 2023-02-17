import datetime
import pathlib

# create a file path
f_name = pathlib.Path(r'.\detail.txt')

# get modification time
m_timestamp = f_name.stat().st_mtime
# convert ti to dd-mm-yyyy hh:mm:ss
m_time = datetime.datetime.fromtimestamp(m_timestamp)
print(m_time)

# get creation time on windows
c_timestamp = f_name.stat().st_ctime
c_time = datetime.datetime.fromtimestamp(c_timestamp)
print(c_time)




