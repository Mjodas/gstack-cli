
# Take user input, return an event.
# Uses custom parse_date function.
# Todo: assert input

def create_cal_event():

    data = input("summary/location/description/YY-MM-DD-hh-mm \n")
    data = data.split("/")

    summary = data[0]
    location = data[1]
    description = data[2]
    date = data[3]

    start, end = parse_date(date)

    event = {
        'summary': data[0],
        'location': data[1],
        'description': data[2],
        'start': {
            'dateTime': start,
            'timeZone': 'Europe/Stockholm',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Europe/Stockholm',
        },
        'reminders': {
            'useDefault': True,
            'overrides': [
            ],
        },
    }

    return event


# Function parses the input date, return parsed start date and end date. end date = start + 1h.
# One day events only. All events are one hour (bad but quick solution)
# todo: fix so that day, month and year shifts if needed. Error check??


def parse_date(not_parsed_date):

    data = not_parsed_date.split('-')
    YY = data[0]
    MM = data[1]
    DD = data[2]
    hh = data[3]
    mm = data[4]

    end_hh = str(((int(hh) + 1) % 24))

    start = "20%s-%s-%sT%s:%s:00+01:00" % (YY, MM, DD, hh, mm)
    end = "20%s-%s-%sT%s:%s:00+01:00" % (YY, MM, DD, end_hh, mm)

    return start, end
