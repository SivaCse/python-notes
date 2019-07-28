'''Timezones'''


# A reminder: it's best to avoid working with timezones. Instead, the best
# practice would be to convert any times/dates to UTC at the start, do all
# your processing in UTC and then convert back to timezones only if you have
# to at the end for the user.

# As it turns out, the web browser knows the user's timezone, and exposes it
# through the standard date and time JavaScript APIs. A good way of utilizing
# this is to let the conversion from UTC to a local timezone happen in the
# web client using JavaScript. There is a small open-source JavaScript library
# called moment.js that handles this very well. Though not demonstrated in this
# file, note that there is a Flask extension called Flask-Moment that makes it
# easy to incorporate moment.js into your Flask app.


# pytz module
# -----------------------------------------------------------------------------
import datetime
import pytz

# FYI pytz pulls timezone information from this database:
# https://www.iana.org/time-zones

# see all timezones:
for x in pytz.all_timezones:
    print(x)

# see all country codes:
for x in sorted(pytz.country_names):
    print(x, ':', pytz.country_names[x])

# see all country names:
for x in sorted(pytz.country_names):
    print(f'{x}: {pytz.country_names[x]}: {pytz.country_timezones.get(x)}')

# see names, zones and their times:
for x in sorted(pytz.country_names):
    print(f'{x}: {pytz.country_names[x]}')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print(f'\t{zone}: {local_time}')
    else:
        print('\tNo timezone defined')


# pytz example
# -----------------------------------------------------------------------------
import datetime
import pytz


country = "Europe/Moscow"
tz = pytz.timezone(country)
world_time = datetime.datetime.now(tz=tz)

print(f'UTC is {datetime.datetime.utcnow()}')
# UTC is 2018-03-28 19:39:09.028962

print(f'The time in {country} is {world_time}')
# The time in Europe/Moscow is 2018-03-28 22:39:09.028943+03:00

print(f'In {country} it is {world_time.strftime("%A %x %X")} - {world_time.tzname()}')
# In Europe/Moscow it is Wednesday 03/28/18 22:39:09 - MSK


# convert a naive datetime to an aware datetime
# -----------------------------------------------------------------------------
import datetime
import pytz


naive_local_time = datetime.datetime.now()
naive_utc_time = datetime.datetime.utcnow()

print(f'Naive local time: {naive_local_time}')
print(f'Naive UTC: {naive_utc_time}')

# Naive local time: 2018-03-28 12:39:09.029068
# Naive UTC: 2018-03-28 19:39:09.0290701

# When these next two print you can tell they are aware because they now
# include an offset at the end. Both will show the same time zone and same
# offset (+00:00, UTC) because the naive datetimes we supplied to it don't
# carry that information. The third example shows how to get the correct local
# offset and time zone:

aware_local_time = pytz.utc.localize(naive_local_time)
aware_utc_time = pytz.utc.localize(naive_utc_time)
aware_local_time_zone = pytz.utc.localize(naive_utc_time).astimezone()

print(f'Aware local time: {aware_local_time} - '
      f'time zone: {aware_local_time.tzinfo}')
# Aware local time: 2018-03-28 12:39:09.029068+00:00 - time zone: UTC

print(f'Aware UTC: {aware_utc_time} - '
      f'time zone: {aware_utc_time.tzinfo}')
# Aware UTC: 2018-03-28 19:39:09.029070+00:00 - time zone: UTC

print(f'Aware local time: {aware_local_time_zone} - '
      f'time zone: {aware_local_time_zone.tzinfo}')
# Aware local time: 2018-03-28 12:39:09.029070-07:00 - time zone: PDT


# date in a timezone from epoch
# -----------------------------------------------------------------------------
# Use time stamps (seconds since the epoch) to convert to actual date.
# For this example we'll be supplying the timezone since an epoch number could
# be from anywhere. This particular timestamp is the hour before DST in the UK
# on October 25, 2015. You will see the difference before and after the DST in
# the offset.

s = 1445733000
t = s + (60 * 60)

tz = pytz.timezone("Canada/Pacific")
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(tz)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(tz)

print(f'{s} seconds since epoch is {dt1}')
print(f'{t} seconds since epoch is {dt2}')

# 1445733000 seconds since epoch is 2015-10-24 17:30:00-07:00
# 1445736600 seconds since epoch is 2015-10-24 18:30:00-07:00
