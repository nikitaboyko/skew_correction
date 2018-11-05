# skew_correction
De-skewing images with slanted content by finding the deviation using Canny Edge Detection.

To Run:
-  In python 3.6,

from deskew import Deskew

deskew = Deskew(input_file_path='path-to-input-image',
                display_image=True,
                output_file_path='path-to-output-image',
                rot_angle = 0)
deskew.run()

- config.json
  
  toggle debug key between 1/0 to print the following details:
    
    Image File
    
    Average Deviation from pi/4
    
    Estimated Angle
    
    Angle bins
