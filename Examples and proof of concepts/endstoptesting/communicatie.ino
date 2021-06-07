void outgoingCommunication(){
String OutgoingString = "";
if (digitalRead(endstop) == HIGH){
    OutgoingString = "high";
  } else if (digitalRead(endstop) == LOW){
    OutgoingString = "low";
    }else {
      OutgoingString = "que?";
    }
  Serial.println(OutgoingString);
}  
