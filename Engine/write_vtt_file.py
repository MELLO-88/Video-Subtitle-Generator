import os

def write_vtt_file(time_array, text_array, folder, filename="captions.vtt"):

    # Ensure the time and text arrays have the same length
    if len(time_array) != len(text_array):
        raise ValueError("Time array and text array must have the same number of elements.")

    # Ensure the folder exists, if not, create it
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Define the full path for the VTT file
    file_path = os.path.join(folder, filename)

    # Open the file for writing
    with open(file_path, 'w', encoding='utf-8') as vtt_file:
        # Write the VTT file header
        vtt_file.write("WEBVTT\n\n")

        # Iterate over the time and text arrays, writing each caption
        for i, (time_range, text) in enumerate(zip(time_array, text_array), start=1):
            start_time, end_time = time_range
            # Write the caption number, time range, and text
            vtt_file.write(f"{i}\n")
            vtt_file.write(f"{start_time} --> {end_time}\n")
            vtt_file.write(f"{text}\n\n")

    print(f"VTT file '{filename}' has been saved to '{folder}'.")


