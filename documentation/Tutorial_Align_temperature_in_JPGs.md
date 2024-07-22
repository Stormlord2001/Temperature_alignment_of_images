# Tutorial - Align temperature in JPG's

An example dataset can be found in Example_data
The example data is two temperature images both containing the same road and field, one of the images has a car on the road the other does not.

The dataset consists of the folowing files:
- Road_and_field.JPG
- Road_and_field_with_car.JPG

Install the **Align_temparature_in_JPGs** by running these commands on the command line.
'''bash
# This is not on github as of now, and this will need to be changed
'''

Export the libraries, by running the following command.
'''bash
export LD_LIBRARY_PATH=<path to the folder containing the program>
'''

Example if the folder is downloaded on the desktop:
'''bash
export LD_LIBRARY_PATH=~/Desktop/Align_temperature_range_in_images
'''

To align the temperatur range of the images, use the following command
'''bash
python3 change_temperatureimage_to_specified_range.py test_data -30 97
DIRP API version number : 0x13
DIRP API magic version  : d4c7dea
R-JPEG file path : Example_data/Road_and_field_with_car.JPG
R-JPEG version information
    R-JPEG version : 0x200
    header version : 0x1
 curve LUT version : 0x1
R-JPEG resolution size
      image  width : 640
      image height : 512
Measurement: get params range:
distance: [1,25]
humidity: [20,100]
emissivity: [0.1,1]
reflection: [-40,500]
Run action 1
Save image file as : Example_data/raw_files/Road_and_field_with_car.raw
Test done with return code 0
DIRP API version number : 0x13
DIRP API magic version  : d4c7dea
R-JPEG file path : Example_data/Road_and_field.JPG
R-JPEG version information
    R-JPEG version : 0x200
    header version : 0x1
 curve LUT version : 0x1
R-JPEG resolution size
      image  width : 640
      image height : 512
Measurement: get params range:
distance: [1,25]
humidity: [20,100]
emissivity: [0.1,1]
reflection: [-40,500]
Run action 1
Save image file as : Example_data/raw_files/Road_and_field.raw
Test done with return code 0
Warning: [minor] Bad MakerNotes directory - Example_data/Road_and_field_with_car.JPG
    1 image files updated
Warning: [minor] Bad MakerNotes directory - Example_data/Road_and_field.JPG
    1 image files updated
'''

In the folder Example_data two new folders will have appeared, new_range_files which contains the images within the new temperatur ranges
![Image](documentation/Example_data/new_range_files/Road_and_field.JGP)
![Image](documentation/Example_data/new_range_files/Road_and_field_with_car.JGP)
