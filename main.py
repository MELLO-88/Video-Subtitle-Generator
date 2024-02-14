from Engine.convert_video_to_wave import convert_video_to_wave
from Engine.convert_video_to_wave_segments import convert_video_to_wave_segments
from Engine.get_amplitude import get_amplitude
from Engine.get_file_location import get_file_location
from Engine.get_folder_location import get_folder_location
from Engine.make_positive import make_positive
from Engine.reshpe_and_average_of_the_array import reshpe_and_average_of_the_array,average_array
import tempfile
from Engine.find_speech import find_speech
from Engine.convert_speech_to_text import convert_speech_to_text
from Engine.seconds_to_hms import seconds_to_hms
from Engine.write_vtt_file import write_vtt_file

Video_file = get_file_location()
Output_folder = get_folder_location()

with tempfile.TemporaryDirectory() as tmpdirname:

    print('created temporary directory', tmpdirname)

    Wave_file = convert_video_to_wave(Video_file,tmpdirname)

    Speech_amplitude = get_amplitude(Wave_file)

    Positive_speech_amplitude = make_positive(Speech_amplitude)

    Length_of_speech_amplitude = len(Speech_amplitude)

    Column_of_the_array = int(Length_of_speech_amplitude / 441)

    Reshaped_and_average_of_the_array = reshpe_and_average_of_the_array(Positive_speech_amplitude,441,Column_of_the_array)

    Start_threshold = average_array(Positive_speech_amplitude) * 0.5

    End_threshold = average_array(Positive_speech_amplitude) * 0.5

    Speech_time_array = find_speech(Reshaped_and_average_of_the_array,Start_threshold,End_threshold)

    print(Speech_time_array)


    with tempfile.TemporaryDirectory() as tmpdirname:

        print('created temporary directory', tmpdirname)

        Speech_wave_files = convert_video_to_wave_segments(Video_file,Speech_time_array,tmpdirname)

        Wave_file_to_text = convert_speech_to_text(tmpdirname)

        Time_array = seconds_to_hms(Speech_time_array)

        Write_vtt_file = write_vtt_file(Time_array,Wave_file_to_text,Output_folder)

















