void loop() {
  // put your main code here, to run repeatedly:
  curMillis = millis(); //!!rolls back to zero after +-50 days continuous on time
  //incoming communication
  incomingCommunication();
  //interpretation
  interpretation();
  //movement
  performMovement();
  //outgoing communication
  outgoingCommunication();
}
