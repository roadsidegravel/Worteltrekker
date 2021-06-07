//Servomotor not strong enough, use stepper

#include <Servo.h>
Servo grabberServo;
int grabberServoPin = 9;
int grabberEndstopPin = 8;
int grabberAngleMin = 0;
int grabberAngleMax = 180;
int grabberAngleCurrent = 0;
bool grabberGrabbing = false;

void setup() {
  grabberServo.attach(grabberServoPin);
  //grabber endstop is different from the other endstops, held closed is it's default state, wired to 3 instead of 2 on endstop
  pinMode(grabberEndstopPin, INPUT_PULLUP);
  moveGrabberTo(grabberAngleMin);
  delay(2000);
  moveGrabberTo(100);
  

}

void moveGrabberTo(int newAngle){
  if (newAngle > grabberAngleMax){
      newAngle = grabberAngleMax;
    }
  if (newAngle < grabberAngleMin){
      newAngle = grabberAngleMin;
    }
  //grabberEndstop checken
  grabberAngleCurrent = newAngle;
  int actualAngle = 180-grabberAngleCurrent;
  grabberServo.write(actualAngle);
}

void moveGrabberBy(int deltaAngle){
  int targetAngle = grabberAngleCurrent+deltaAngle;
  moveGrabberTo(deltaAngle);
  }

void loop() {
  // put your main code here, to run repeatedly:
}
