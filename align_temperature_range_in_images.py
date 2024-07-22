"""
Copyright 2024 Rasmus Storm, rasto21@student.sdu.dk, University of Southern Denmark
All rights reserved

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import cv2
import numpy as np
import subprocess
import os
import argparse

from icecream import ic

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

class TemperatureImage_given_range:
    def __init__(self):
        self.input_type = ".JPG"
        self.input_location = "test_data"
        self.temp_range = [-30, 97]
        self.apply_heatmap = False
        self.max = 0
        self.data = 0

    def ensure_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def get_files_of_type(self, input_location, input_type):
        return [x for x in os.listdir(input_location ) if x.endswith(input_type)]    

    def get_raw_files(self):
        self.ensure_dir(self.input_location + "/raw_files")

        input_image_list = self.get_files_of_type(self.input_location, self.input_type)
        self.input_image_list = input_image_list
        for i in range(0, len(input_image_list)):
            subprocess.run("./dji_irp -s " + self.input_location + "/" + input_image_list[i] + " -a measure -o" + self.input_location + "/raw_files/" + input_image_list[i][:-len(self.input_type)] + ".raw", shell=True)

    def process_raw_files(self):
        self.ensure_dir(self.input_location + "/new_range_files")
        raw_image_list = self.get_files_of_type(self.input_location + "/raw_files", ".raw")
        self.raw_image_list = raw_image_list
        for i in range(0, len(raw_image_list)):
            data = self.get_data_from_raw_file(raw_image_list, i)
            self.save_image(raw_image_list, i, data)

    def save_image(self, raw_image_list, i, data):
        if self.apply_heatmap:
            heatmap = cv2.applyColorMap(np.uint8(data), cv2.COLORMAP_JET)

            cv2.imwrite(self.input_location + "/new_range_files/" + raw_image_list[i][:-4] + self.input_type, heatmap)
        else:
            cv2.imwrite(self.input_location + "/new_range_files/" + raw_image_list[i][:-4] + self.input_type, data )

    def get_data_from_raw_file(self, raw_image_list, i):
        f = open(self.input_location + "/raw_files/" + raw_image_list[i], mode="rb")
        data = np.fromfile(f, dtype=np.int16)
        data = data.reshape((512, 640))
        data = data/10.0
        data = np.clip(data, self.temp_range[0], self.temp_range[1])
        data = (data - self.temp_range[0])/(self.temp_range[1] - self.temp_range[0])*255
        return data
        

    def move_exif_data(self):
        assert len(self.input_image_list) == len(self.raw_image_list), "The number of raw files and input images are not the same"
        for i in range(0, len(self.input_image_list)):
            subprocess.run("exiftool -TagsFromFile " + self.input_location + "/" + self.input_image_list[i] + " " + self.input_location + "/new_range_files/" + self.raw_image_list[i][:-4] + self.input_type, shell=True)
        self.remove_files_without_exif_data()
        

    def remove_files_without_exif_data(self):
        temp = self.input_type + "_original"
        self.new_range_files = self.get_files_of_type(self.input_location + "/new_range_files", temp)
        for i in range(0, len(self.new_range_files)):
            os.remove(self.input_location + "/new_range_files/" + self.new_range_files[i])

    def main(self):
        self.get_raw_files()
        self.process_raw_files()
        self.move_exif_data()


parser = argparse.ArgumentParser(description = "This program will change the temperature range of thermal images from DJI.\n "
                                 "\nBefore running the program, make sure that the dji_irp is exportes to the library path. "
                                 "\nThis can be done by running the following command in the terminal: "
                                 "export LD_LIBRARY_PATH=<path to the dji_irp> "
                                 "to be able to run the program exiftool must be installed on the system, it can be installed by running the following command: "
                                 "'sudo apt-get install libimage-exiftool-perl' ")
parser.add_argument('file_location', 
                    help='Path to the folder containing all the thermal images to have their range thanged.')
parser.add_argument('temperature_range',
                    nargs='+',
                    type=int,
                    help='New temperature range for all the images in the folder.')
parser.add_argument('--file_type',
                    default=".JPG",
                    help='The type of files in the input folder, default is .JPG.')
parser.add_argument('--apply_heatmap',
                    default=False,
                    type=bool,
                    help='If this flag is set, the program will apply a heatmap to the images.')
args = parser.parse_args()


Temperature = TemperatureImage_given_range()
Temperature.input_location = args.file_location
Temperature.temp_range = args.temperature_range
Temperature.input_type = args.file_type
Temperature.apply_heatmap = args.apply_heatmap
Temperature.main()