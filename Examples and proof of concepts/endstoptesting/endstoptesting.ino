byte endstop = 8;

void setup() {
  // put your setup code here, to run once:
  pinMode(endstop,INPUT_PULLUP);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  outgoingCommunication();
}
