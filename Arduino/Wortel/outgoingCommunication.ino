void outgoingCommunication(){
  //check if there is incoming, and pause/dont send whilst there is incoming
  //only send every x millis
   if (curMillis - prevOutMillis >= betweenOutMillis){
    prevOutMillis += betweenOutMillis;
  if (Serial.available() > 0){
  } else{
  //to communicate: Moving, EndstopResult, StepCount
  String MoveString = (String)Moving;
  if (MoveIncreasing){
    MoveString += "I";
  } else{
     MoveString += "D";
    }
    String EndstopMinString = "MIN";
    for (int i = 0; i < AmountOfSteppers ; i++){
      EndstopMinString+=EndstopMinResult[i];
    }
    String EndstopMaxString ="MAX";
    for (int i = 0; i < AmountOfSteppers; i++){
      EndstopMaxString+=EndstopMaxResult[i];
    }
    String MoveCountString = "C";
    for (int i = 0; i < AmountOfSteppers; i++){
      MoveCountString+=StepCount[i];
      MoveCountString+='*';
      } 
    String OutgoingString = 'U'+MoveString+EndstopMinString+EndstopMaxString+MoveCountString;
    Serial.println(OutgoingString);
  }
 } 
} 
