void performMovement(){
  //every x milliseconds
  int halfBetweenSteps = int(betweenStepsMillis)/2;
  if (curMillis - prevStepMillis >= betweenStepsMillis){
    prevStepMillis += betweenStepsMillis;
    //update all endstops
    endstopStates();
    //who has to move, if any?
    WhoMoves();
    //check if we've hit an endstop for the moving stepper
    endstopHitCheck();  
    if (requestedSteps > 0){
      if (performedSteps >= requestedSteps){
        //movement complete
        stopMoving();
      } else {
        //take a step
        digitalWrite(MovingPulse, HIGH);
        performedSteps++;
        if (MoveIncreasing){
          StepCount[MovingCount]++;
        } else {
          if (StepCount > 0){
          StepCount[MovingCount]--;
          }
        }
        //delay is in milliseconds
        //200 kHz, full period 0.005 ms, high part half dat?
        //lower delay? 
        //missing steps, increase ampere?
        delay(halfBetweenSteps);
        //delayMicroseconds(200);
        digitalWrite(MovingPulse, LOW);
      }
    }
  }               
}
