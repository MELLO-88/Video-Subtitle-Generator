import moviepy.editor as mp

def convert_video_to_wave(video_path, output_folder):
    # Extract the audio from the video
    clip = mp.VideoFileClip(video_path)
    audio = clip.audio

    # Construct the output file path
    output_file = f"{output_folder}/{video_path.split('/')[-1].split('.')[0]}.wav"

    try:
        # Write the audio to a WAV file
        audio.write_audiofile(output_file)
        print(f"Video converted to WAV and saved at: {output_file}")
    except Exception as e:
        print(f"Error converting video: {e}")

    return output_file