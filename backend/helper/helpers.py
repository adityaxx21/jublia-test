from datetime import datetime, timedelta
from pytz import timezone

def get_utc_plus_8():

    # Create a datetime object representing the current time
    # now = datetime.now()

    # Get the current UTC offset
    # utc_offset = now.astimezone().utcoffset()

    
    # Format the timestamp with the UTC offset
    # formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f ") + \
    #                     '{:+03d}'.format(int(utc_offset.total_seconds() // 3600)) + \
    #                     '{:02d}'.format(int(utc_offset.total_seconds() % 3600 // 60))

    singapore_time = datetime.now(timezone('Asia/Singapore'))

    utc_offset_sg = singapore_time.utcoffset()

    formatted_timestamp_sg = singapore_time.strftime("%Y-%m-%d %H:%M:%S.%f ") + \
                      '{:+03d}'.format(int(utc_offset_sg.total_seconds() // 3600)) + \
                      '{:02d}'.format(int(utc_offset_sg.total_seconds() % 3600 // 60))

    return formatted_timestamp_sg