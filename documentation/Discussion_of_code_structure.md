# Discussion - code structure
The code consists of three main parts
- Using DJI Thermal sdk to extract raw temperature data
- Applying the new tempreature range
- moving the exif data to the new image

## Using DJI Thermal sdk to extract raw temperature data
The raw temperature is extracted with DJI Thermal SDK 

## Applying the new tempreature range
The extracted temperatures are clipped to the temperature range,
meaning a very large temperature will be capped at the upper temperature range 
and will therefore not be represented as very large.

Per default a heatmap is not applied and the image is grayscaled
It was choosen to give the user the option to use a heatmap
as the slight change in temperature is hardly noticebly in a grayscaled image.

## moving the exif data to the new image
The EXIF Data from the original image is then moved to the new image.
As this created a copy of the image without the EXIF data, it was choosen
to delete these copies internally