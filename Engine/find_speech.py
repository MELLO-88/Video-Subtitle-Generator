def split_array(arr):
    # Check if the array has fewer than 4 elements
    if len(arr) < 3:
        raise ValueError("Array needs at least 4 elements.")

    result = []
    for i in range(len(arr) - 2):
        # Extract a slice from i to i+10
        current_slice = arr[i:i+3]
        result.append(current_slice)

    return result

def all_items_larger_than_start_threshold(array, start_threshold):
    return all(item > start_threshold for item in array)

def all_items_smaller_than_end_threshold(array, end_threshold):
    return all(item < end_threshold for item in array)

def find_speech(array, start_threshold, end_threshold):
    splitted_array = split_array(array)
    finding = "start"
    start_second = None
    speech_array = []

    for index, item in enumerate(splitted_array):
        if finding == "start":
            if all_items_larger_than_start_threshold(item, start_threshold):
                start_second = index * 0.1  # Correct timing calculation
                finding = "end"
        elif finding == "end":
            if all_items_smaller_than_end_threshold(item, end_threshold):
                end_second = (index + 4) * 0.1  # Adjust for the end of the slice
                speech_array.append((start_second, end_second))
                finding = "start"
                start_second = None  # Resetting for next detection

    # Handle case where speech continues until the end of the array
    if start_second is not None:
        end_second = (len(array) - 1) * 0.1  # Assuming each element represents 0.1 second
        speech_array.append((start_second, end_second))

    return speech_array
