import moviepy.editor as mp

def convert_video_to_wave_segments(video_file, time_segments, output_folder):

   clip = mp.VideoFileClip(video_file)

   for i, (start, end) in enumerate(time_segments):
       segment = clip.subclip(start, end)
       output_file = f"{output_folder}/ {i+1}.wav"  # Ensure filename starts with a number
       segment.audio.write_audiofile(output_file)

   clip.close()

# import moviepy.editor as mp
#
# def convert_video_to_wave_segments(video_file, time_segments, output_folder):
#     clip = mp.VideoFileClip(video_file)
#
#     # Process pairs of values as start and end times
#     for i in range(0, len(time_segments), 2):
#         start = time_segments[i]
#         end = time_segments[i + 1]
#         segment = clip.subclip(start, end)
#         output_file = f"{output_folder}/{i//2 + 1}.wav"  # File numbering starts from 1
#         segment.audio.write_audiofile(output_file)
#
#     clip.close()