void incomingCommunication(){
  //https://forum.arduino.cc/index.php?topic=396450.0%20arduino%20communication
  static boolean recvInProgress = false;
  static byte ndx = 0;
  char startMarker = '<';
  char endMarker = '>';
  char rc;
  while (Serial.available() > 0 && newData == false){
    rc = Serial.read();

    if (recvInProgress == true){
        if (rc != endMarker) {
            receivedChars[ndx]=rc;
            ndx++;
            if (ndx >= numChars){
                ndx = numChars - 1;
              }
          }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void interpretation(){
    String incomingString;
    if (newData == true){
      incomingString = receivedChars;
      Serial.print("received: ");
      Serial.println(incomingString);
    //interpretatie
    //first char, which motor to move X, A, B, C, D or F, or S for stop
    //second char, I increasing, D, decreasing
    //then the requested number of steps
    if (incomingString != ""){
      //interpreteer de string
      incomingString.trim();
      incomingString.toUpperCase();
      Moving = incomingString[0];
      if (Moving != 'S'){
        if (incomingString[1] == 'I'){
          MoveIncreasing = true;
        }
        else if (incomingString[1] == 'D'){
          MoveIncreasing = false;
        }
        else {
          stopMoving();
          Serial.println("Command not understood, invalid direction, stopping "+incomingString); 
        }
        String numberString = incomingString.substring(2);
        //check if they're all numbers
        int maxI = numberString.length();
        bool AllNumbers = true;
        for (int i = 0; i < maxI; i++){
          if (!isDigit(numberString[i])){
            AllNumbers = false;
          }
        }
        if (AllNumbers){
          requestedSteps = (unsigned long)numberString.toInt();
          performedSteps = 0;
        } else {
          stopMoving();
          Serial.println("Command not understood, invalid steps, stopping "+incomingString+" "+numberString+".");  
        }
      }
    }
    newData = false;
  }
}
