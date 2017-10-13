mkdir -p images
ffmpeg -i running.mp4 -r 1/1 images/images%03d.jpg # Just some

mkdir -p lots_of_images
ffmpeg -i running.mp4 lots_of_images/images%04d.jpg # All frames
