# EmbeddedSystems-3D-Scanner
3D Scanner Project for Image Modeling


## Plan for Next Release V2.0

In this next wave of releases I want to create an installer script the use of this will be to setup the daemon manually for the user.
I want to update the model
- First thing will be putting the camera mount onto some sort of rail allowing it to move back and forth to get the ideal focus and control. <br>
This will be acheived likely with a stepper motor and a lead screw along with some stabliser rails <br>
Alternativly we could use a linear rails for it to slide on. <br>
We would then have the controls for this setup to a led screen that is playing the camera preview so the user can see how this focus is looking. <br>
- Adding a servo Motor for controlling the camera angle will also be useful this will require tweaking in the design as well as a script for moving it up and down. <br>
This will also require a camera preview on an led screen.
- A more tidy housing for the cables and pcbs.

A script that can handle feeding images straight into some photogrammetry software e.g colsmap
The script can then be run at the end of the capture stage process the images and then spitout a recreation of the mesh to an led screen.

## Plan for Release V1.0

### Equipment
- [x] Need Camera Module Either Raspberry Pi or Arduino (Raspberry Pi) *ordered
- [x] External Power for Stepper Motor
- [x] Need Bigger Stepper Motor (defunct) *using small and light turntable

### Model
- [x] Build Model to house camera
- [X] Build Model to house turntable
- [ ] Optional Led Screen and Joystick 
- [X] print
- [X] Gears (to gear down)

### Program Basic Functionality
- [X] Program ~~Arduino~~ to take photos or Raspberry Pi
- [X] Program Arduino to turn the stepper motor.
- [x] Program Arduino and Raspberry Pi to talk to each other
- [X] Program ~~Led Screen~~ to have a start button
- [ ] Joystick For either navigation or starting (optional).

### Program Advanced
- [X] Program Arduino to turn when the pi says so
- [X] Run Python Script on the button press

### Manual testing
- [ ] Test Adding Photos into Regard3d
- [ ] Tweak Settings

### Image Testing (Defunct going to use Raspberry Pi for Imaging)
- [ ] Work on sending photos to raspberry pi if on Arduino

### Raspberry Pi advanced testing
- [ ] Try To render the model on raspberry pi 
- [ ] if successful in a reasonable time
- [ ] work on getting them to import and render from the led screen

### Alternative Method
otherwise, attempt to use a remote computer and import them and render them there
and send them back.



development notes
raspberry pi USB connection
- acm0
