from datetime import timedelta

def seconds_to_hms(array):
    result = []
    for start, end in array:
        # Convert seconds to timedelta
        start_td = timedelta(seconds=start)
        end_td = timedelta(seconds=end)
        # Format as HH:MM:SS
        start_str = str(start_td)
        end_str = str(end_td)
        # Check if hours are missing in the string representation and add "00:" if needed
        if len(start_str.split(':')) < 3:
            start_str = "00:" + start_str
        if len(end_str.split(':')) < 3:
            end_str = "00:" + end_str
        # Append the formatted times to the result list
        result.append((start_str, end_str))
    return result

