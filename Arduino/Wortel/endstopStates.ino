void endstopStates(){  
  //first half, min, second half max
  for (int i = 0; i < AmountOfSteppers; i++){
    if (digitalRead(EndstopPinMin[i]) == HIGH){
      EndstopMinResult[i] = 1;
    } else {
      EndstopMinResult[i] = 0;
    }
    if (digitalRead(EndstopPinMax[i]) == HIGH){
      EndstopMaxResult[i] = 1;
    } else {
      EndstopMaxResult[i] = 0;
    }
  }
}
