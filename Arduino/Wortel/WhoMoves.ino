void WhoMoves(){
  if (Moving == 'X'){
    if (MovingPulse != XPulse){
      MovingPulse = XPulse;
    }
    if (MoveIncreasing){
      digitalWrite(XDir, HIGH);
    } else {
      digitalWrite(XDir, LOW);
    }
    if (MovingMin != 0){
      MovingMin = 0;
    }
    if (MovingMax != 0 ){
      MovingMax = 0;
    }
    if (MovingCount != 0){
      MovingCount = 0;
    }
  } 
  else if (Moving == 'A'){
    if (MovingPulse != APulse){
      MovingPulse = APulse;
    }
    if (MoveIncreasing){
      digitalWrite(ADir, HIGH);
    } else {
      digitalWrite(ADir, LOW);
    }
    if (MovingMin != 1){
      MovingMin = 1;
    }
    if (MovingMax != 1){
      MovingMax = 1;
    }  
    if (MovingCount != 1){
      MovingCount = 1;
    }  
  }
  else if (Moving == 'B'){
    if (MovingPulse != BPulse){
      MovingPulse = BPulse;
    }
    if (MoveIncreasing){
      digitalWrite(BDir, HIGH);
    } else {
      digitalWrite(BDir, LOW);
    }
    if (MovingMin != 2){
      MovingMin = 2;
    }
    if (MovingMax != 2){
      MovingMax = 2;
    }
    if (MovingCount != 2){
      MovingCount = 2;
    }   
  }
  else if (Moving == 'C'){
    if (MovingPulse != CPulse){
      MovingPulse = CPulse;
    }
    if (MoveIncreasing){
      digitalWrite(CDir, HIGH);
    } else {
      digitalWrite(CDir, LOW);
    }
    if (MovingMin != 3){
      MovingMin = 3;
    }
    if (MovingMax != 3){
      MovingMax = 3;
    }
    if (MovingCount != 3){
      MovingCount = 3;
    }    
  }
  else if (Moving == 'D'){
    if (MovingPulse != DPulse){
      MovingPulse = DPulse;
    }
    if (MoveIncreasing){
      digitalWrite(DDir, HIGH);
    } else {
      digitalWrite(DDir, LOW);
    }
    if (MovingMin != 4){
      MovingMin = 4;
    }
    if (MovingMax != 4){
      MovingMax = 4;
    }
    if (MovingCount != 4){
      MovingCount = 4;
    }   
  }
  else if (Moving == 'F'){
    if (MovingPulse != FPulse){
      MovingPulse = FPulse;
    }
    if (MoveIncreasing){
      digitalWrite(FDir, HIGH);
    } else {
      digitalWrite(FDir, LOW);
    }
    if (MovingMin != 5){
      MovingMin = 5;
    }
    if (MovingMax != 5){
      MovingMax = 5;
    }
    if (MovingCount != 5){
      MovingCount = 5;
    }   
  }
  else if (Moving == 'S'){
    stopMoving();
  }
  else {
    Serial.println("Command not understood, unclear who has to move, stopping "+Moving);
    stopMoving();
  }
}
