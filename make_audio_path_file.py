# This is a simple script made to aid creation of submissions for the AI project listed below
# https://15.ai/contribute
# Copy your audio files into the provided directory 'audio_files' by default and call this program from cmd
# with `make_audio_path_file.py`

import os
import warnings


def make_and_save_names(audio_dir='audio_files', output_file_name='report.txt'):
    if os.path.isdir(audio_dir):
        path = audio_dir

        output = open(output_file_name, "w") # Get rid of any output report already present
        output.write('')  # Delete anything in the file
        output.close() # done, but the file will exist and be empty!

        output = open(output_file_name, "a")  # open in append mode and fill it up

        print("Saving files...\n")

        for file in os.listdir(path):
            current = os.path.join(path, file)
            if os.path.isfile(current):
                file_name = current + '|'
                output.write(file_name + "\n")
                print(file_name)

        print("\n...done")
    else:
        warnings.warn(f"Cannot find directory with music files {audio_dir}, please have named directory in same location as script", RuntimeWarning)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_and_save_names()
