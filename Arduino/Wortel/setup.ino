void setup() {
  // put your setup code here, to run once:
  //X left right
pinMode(XMin, INPUT_PULLUP);
pinMode(XMax, INPUT_PULLUP);
pinMode(XPulse, OUTPUT);
pinMode(XDir, OUTPUT);

//A tool 1 up down
pinMode(AMin, INPUT_PULLUP);
pinMode(AMax, INPUT_PULLUP);
pinMode(APulse, OUTPUT);
pinMode(ADir, OUTPUT);

//B tool 2 up down
pinMode(BMin, INPUT_PULLUP);
pinMode(BMax, INPUT_PULLUP);
pinMode(BPulse, OUTPUT);
pinMode(BDir, OUTPUT);

//C tool 1
pinMode(CMin, INPUT_PULLUP);
pinMode(CMax, INPUT_PULLUP);
pinMode(CPulse, OUTPUT);
pinMode(CDir, OUTPUT);

//D tool 2
pinMode(DMin, INPUT_PULLUP);
pinMode(DMax, INPUT_PULLUP);
pinMode(DPulse, OUTPUT);
pinMode(DDir, OUTPUT);

//F floor changer
pinMode(FMin, INPUT_PULLUP);
pinMode(FMax, INPUT_PULLUP);
pinMode(FPulse, OUTPUT);
pinMode(FDir, OUTPUT);

//USB communicatie
Serial.begin(57600);
Serial.setTimeout(20); //default is 1000 ms
}
