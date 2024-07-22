# How to - Apply heatmap
A heatmap can be applied to the output image by using the input parameter --apply_heatmap

by default a heatmap is not applied, but if the parameter is set to true it will be applied,
an example can be seen here:
'''bash
python3 align_temperature_range_in_images.py example_data -30 97 --apply_heatmap true
'''

This will apply the colormap_jet