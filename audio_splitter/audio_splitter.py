from pydub import AudioSegment
import os


class Status:
    SUCCESS = 0
    FAIL = 1


class ConfigInfo:
    source_audio_filename = "anand.mp3"
    source_audio_dir = "./"
    tracks_list = list()
    author_name = str()
    audio_title = str()


class TrackInfo:
    start_seconds = int()
    end_seconds = int()
    track_name = str()


class Audio_Splitter:
    original_audio_data = None
    original_file_name = "anand.mp3"
    config_file_name = "sukhmani_sahib_katha.csv"
    config_dir = "./"
    config_file_raw_data = None
    enable_logs = True
    config_info = ConfigInfo()
    export_folder_name = None

    def read_config(self):
        filename = self.config_dir + self.config_file_name

        print("opening", filename)
        fd = open(os.path.abspath(filename), mode='r')
        self.config_file_raw_data = fd.readlines()

        self.parse_config_file()

        return Status.SUCCESS

    def parse_config_file(self):

        for line in self.config_file_raw_data:
            line_processed = line.strip()
            line_processed = line.split(",")
            # print("line - ", line_processed)
            if line.find("source_audio_filename") != -1:
                print("source_audio_filename", line_processed[1])
                self.config_info.source_audio_filename = line_processed[1]
            elif line.find("source_audio_dirpath") != -1:
                #      print("source_audio_dirpath", line_processed[1])
                self.config_info.source_audio_dir = line_processed[1]
            elif line.find("author_name") != -1:
                #       print("author_name", line_processed[1])
                self.config_info.author_name = line_processed[1]
            elif line.find("audio_title") != -1:
                #        print("audio_title", line_processed[1])
                self.config_info.audio_title = line_processed[1]
            elif line.find("track_info") != -1:
                print("source_audio_filename", line_processed[2])
                track_info = TrackInfo()
                track_info.track_name = line_processed[1]
                track_info.start_seconds = float(line_processed[2])
                track_info.end_seconds = float(line_processed[3])

                self.config_info.tracks_list.append(track_info)
            # self.config_info.source_audio_filename = line_processed[1]

        if self.enable_logs:
            print("Title ", self.config_info.audio_title)
            print("Author ", self.config_info.author_name)
            print("Dir ", self.config_info.source_audio_dir)
            print("Filename ", self.config_info.source_audio_filename)

            for track_info in self.config_info.tracks_list:
                print("Name", track_info.track_name)
                print("Start", track_info.start_seconds)
                print("End", track_info.end_seconds)

    def load_source_audio(self):
        file_name = self.config_info.source_audio_dir + "/" + self.config_info.source_audio_filename
        print("loading audio file", file_name)
        self.original_audio_data = AudioSegment.from_mp3(file_name)

    def create_target_folder(self):
        self.export_folder_name = self.config_info.audio_title + self.config_info.author_name
     #   os.mkdir(self.export_folder_name)

    def process_audio(self):

        self.load_source_audio()
        self.create_target_folder()
        for track_info in self.config_info.tracks_list:
            self.extract_track(track_info)
        return Status.SUCCESS

    def extract_track(self, track_info):
        print("Extracking track", track_info.track_name)
        audio_track = self.original_audio_data[track_info.start_seconds*1000:track_info.end_seconds*1000]
        export_track = self.config_info.source_audio_dir
        audio_track.export(self.export_folder_name + "\\" + track_info.track_name + ".mp3")

if __name__ == '__main__':

    status = Status.SUCCESS
    audio_splitter_obj = Audio_Splitter()
    status = audio_splitter_obj.read_config()
    if status != Status.FAIL:
        status = audio_splitter_obj.process_audio()

    if False:
        song = AudioSegment.from_mp3("anand.mp3")
        # pydub does things in milliseconds
        ten_seconds = 35 * 1000

        first_10_seconds = song[:ten_seconds]

        first_10_seconds.export("new_gurnoor.mp3", format="mp3")