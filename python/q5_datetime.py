# Q5.a
from dateutil import parser

date_start = '01-02-2013'
date_stop = '07-28-2015'

# convert dates to datetime
date_start_dt = parser.parse(date_start) 
date_stop_dt = parser.parse(date_stop)

# calculate duration between date_start and date_stop
duration = date_stop_dt - date_start_dt

# print duration
print 'There were %s days between %s and %s.' % (duration.days, date_start, date_stop)
print



# Q5.b
date_start = '12312013'
date_stop = '05282015'

# convert dates to datetime
date_start = date_start[0:2] + '-' + \
             date_start[2:4] + '-' + \
             date_start[4:]

date_stop = date_stop[0:2] + '-' + \
            date_stop[2:4] + '-' + \
            date_stop[4:]

# convert dates to datetime
date_start_dt = parser.parse(date_start) 
date_stop_dt = parser.parse(date_stop)

# calculate duration between date_start and date_stop
duration = date_stop_dt - date_start_dt

# print duration
print 'There were %s days between %s and %s.' % (duration.days, date_start, date_stop)
print



# Q5.c
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

# convert dates to datetime
date_start_dt = parser.parse(date_start) 
date_stop_dt = parser.parse(date_stop)

# calculate duration between date_start and date_stop
duration = date_stop_dt - date_start_dt

# print duration
print 'There were %s days between %s and %s.' % (duration.days, date_start, date_stop)
print

