import datetime
from helpers import create_cal_event
from paths import slaitnederc
from connection import connection

def main():

    service = connection()
    event = create_cal_event()
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    main()
