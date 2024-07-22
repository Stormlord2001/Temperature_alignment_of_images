
This will be a short introduction to the prerequisite to the program, and how to run it

A prerequisite to be able to run the program is having exiftools installed, which can be installed with the following command on Ubuntu:
'sudo apt-get install libimage-exiftool-perl'

Before being able to run the program the libraries have to be exported, by running the following command:
'export LD_LIBRARY_PATH=<path to the folder containing the program>'


The program requires two input parameters. 
The first is the folder in which the .JPG images is located.
The other is the new range for the thermal images

An example of this is:
python3 change_temperatureimage_to_specified_range.py test_data -30 97

The program also has to optional inputs.
The first is --file_type, this allows to change the input type from .JPG to fx. .jpg
The second is --apply_heatmap, which will apply the jet colormap if set to true
