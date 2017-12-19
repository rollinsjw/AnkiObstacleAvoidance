
### Set Up

1. Install Python 2.7 and OpenCV 2.4.9
2. Print `pattern.png` and mount on cardboard
3. Replace the pictures in `calibration_images` with your own pictures of your chessboard. (see `calibration_images` for examples of how to take pictures)
4. Take a picture of the track with obstacles laid out on it. Use Preview to remove all elements of image except for obstacles. Save image as `obstacles.jpg`.
5. Run `setup_driver.py` to calibrate camera and build obstacle histogram. 
```
python setup_driver.py
```

### Run

Run `simulation_driver.py`
```
python simulation_driver.py
```
