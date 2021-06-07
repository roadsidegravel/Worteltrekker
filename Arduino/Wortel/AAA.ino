//Arduino Mega
//X left right
byte XMin = 50;
byte XMax = 51;
byte XPulse = 52;
byte XDir = 53;

//A tool 1 up and down
byte AMin = 46;
byte AMax = 47;
byte APulse = 48;
byte ADir = 49;

//B tool 2 up and down
byte BMin = 42;
byte BMax = 43;
byte BPulse = 44;
byte BDir = 45;

//leaving 40 and 41 empty so pins can physically fit

//C Tool 1
byte CMin = 36;
byte CMax = 37;
byte CPulse = 38;
byte CDir = 39;

//D tool 2
byte DMin = 32;
byte DMax = 33;
byte DPulse = 34;
byte DDir = 35;

//F floor changer
byte FMin = 28;
byte FMax = 29;
byte FPulse = 30;
byte FDir = 31;

const int AmountOfSteppers = 6;
int StepCount[AmountOfSteppers];
byte EndstopPinMin[AmountOfSteppers] = {XMin,AMin,BMin,CMin,DMin,FMin};
byte EndstopPinMax[AmountOfSteppers] = {XMax,AMax,BMax,CMax,DMax,FMax};
byte EndstopMinResult[AmountOfSteppers];
byte EndstopMaxResult[AmountOfSteppers];

//are we moving a stepper?
char Moving = 'S';
byte MovingPulse;
byte MovingDir;
int MovingMin; //index in the endstopresult array
int MovingMax; //index in the endstopresult array
int MovingCount; //index in the stepCount array
//increasing or decreasing?
bool MoveIncreasing = false;
//pulse related stuff
unsigned long requestedSteps = 0;
unsigned long performedSteps = 0;
unsigned long curMillis = 0;
unsigned long prevStepMillis = 0;
unsigned long betweenStepsMillis = 50; //in milliseconds

void stopMoving(){
  Moving = 'S';
  requestedSteps = 0;
  performedSteps = 0;
}

void endstopHitCheck(){
  //endstop check
  if (MoveIncreasing){
    //high means endstop hit or unplugged or wire broken...
    if (EndstopMaxResult[MovingMax] == HIGH){
      stopMoving();
    }
  }
  if (MoveIncreasing){
    //high means endstop hit or unplugged or wire broken...
    if (EndstopMinResult[MovingMin] == HIGH){
      stopMoving();
    }
  }
}

//incoming communication related
const byte numChars = 32;
char receivedChars[numChars];
boolean newData = false;

//outgoing automatic data communication related
unsigned long prevOutMillis = 0;
unsigned long betweenOutMillis = 200;

//setup runt eenmalig, zie setup file
//loop blijft gaan, zie loop file
