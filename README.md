# time-slices
Code to take part of a movie, identify the moving parts, and simulate a multiple exposure image. Useful for teaching kinematics and having students calculate the motion of things from a static image.

# Getting started

You need
* opencv (for the image manipulation)
* ffmpeg (for now, to pull individual frames out of the movie. maybe there's something more general we can use?)

Install [opencv and the python module](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html) on your system.

This can be...challenging. 

## Test your system

Read in and display two images using the opencv python library. 

```
  python test_your_opencv_installation.py
```

"Add" two images.

```
python add_two_images.py
```

## Mock-up a multiple-exposure image!

To try this out, download the [running.mp4](https://www.google.com) (THIS WILL SOON BE A REAL LINK) example that I ripped from 
YouTube. 

Run the following shell script which uses ffmpeg to pull out some images from the movie. 

```
sh dump_frames_from_movie.sh
```

Then run this shell script which calls a python script, ```add_multiple_files.sh```. 

```
sh run_add_multiple_files.sh
```

This should produce something that looks like a multiple exposure image, though a bit pixelated. 
