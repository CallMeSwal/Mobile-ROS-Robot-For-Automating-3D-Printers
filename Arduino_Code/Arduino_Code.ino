#include <Encoder.h>

#define limitBot 5
#define limitTop 6
#define limitTong 7
#define magnet 8
#define motorA 9  
#define motorB 10

bool limitPressed = false;

int encPinA = 2;
int encPinB = 3;
Encoder enc(encPinA, encPinB);
long oldPos = 0;
long newPos = 0;
long offset = 0;

void setup(){
  Serial.begin(9600);

  pinMode(limitTong, INPUT_PULLUP);
  pinMode(limitTop, INPUT_PULLUP);
  pinMode(limitBot, INPUT_PULLUP);

  //pinMode (encPinA, INPUT_PULLUP);
  //pinMode (encPinB, INPUT_PULLUP);

  pinMode(magnet, OUTPUT);
  pinMode(motorA, OUTPUT);
  pinMode(motorB, OUTPUT);
  digitalWrite(magnet,LOW);
  digitalWrite(motorA,LOW);
  digitalWrite(motorB,LOW);

  offset = enc.read();
}

void loop (){
  if (Serial.available()) {
    char ser = Serial.read();
    if (ser == 'P' and !limitPressed){
      //lower winch
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, HIGH);
      //Serial.println("WINCH DOWN");
      }
    else if (ser == 'I' and !limitPressed){
      //raise winch
      digitalWrite(motorA, HIGH);
      digitalWrite(motorB, LOW);
      //Serial.println("WINCH UP");
     }
    else if (ser == 'O'){
      //stop winch
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW);
      //Serial.println("WINCH STOP");
      }
    else if (ser == 'M'){
      //magnet off
      digitalWrite(magnet, LOW);
      //Serial.println("MAGNET OFF");
      }
    else if (ser == 'N'){
      //magnet on
      digitalWrite(magnet, HIGH);
      //Serial.println("MAGNET ON");
      }
    else if (ser == 'Z'){
      //raise winch until specified height is reached
      digitalWrite(motorA, HIGH);
      digitalWrite(motorB, LOW);
      while (newPos<1000){
        newPos = enc.read() - offset;
        if (newPos != oldPos){
          oldPos = newPos;
          Serial.println(newPos);
          }   
        }
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW);
      }
    else if (ser == 'X'){
      //raise winch until specified height is reached
      digitalWrite(motorA, HIGH);
      digitalWrite(motorB, LOW);
      while (newPos<1000){
        newPos = enc.read() - offset;
        if (newPos != oldPos){
          oldPos = newPos;
          Serial.println(newPos);
          }   
        }
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW);
      }
    else if (ser == 'C'){
      //raise winch until specified height is reached
      digitalWrite(motorA, HIGH);
      digitalWrite(motorB, LOW);
      while (newPos<1000){
        newPos = enc.read() - offset;
        if (newPos != oldPos){
          oldPos = newPos;
          Serial.println(newPos);
          }   
        }
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW);
      }
    else if (ser == 'V'){
      //lower winch until lower limit switch is pressed
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, HIGH);
      while (digitalRead(limitBot) == HIGH) {
        //Do nothing
        }
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW);
      }
    else if (ser == 'B'){
      //lower winch until lower limit switch is pressed
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, HIGH);
      while (digitalRead(limitTong) == HIGH) {
        //Do nothing
        }
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW);
      }
  }
  if (digitalRead(limitTong) == LOW || digitalRead(limitTop) == LOW || digitalRead(limitBot) == LOW ){
      //limit reached, stop winch motor
      //Serial.println("LIMIT PRESSED");
      digitalWrite(motorA, LOW);
      digitalWrite(motorB, LOW); 
      limitPressed=true;
      if (digitalRead(limitBot) == LOW){
          offset = enc.read();
        }
    }
  else {
      limitPressed=false; 
    }
    
  newPos = enc.read() - offset;
  if (newPos != oldPos){
      oldPos = newPos;
      Serial.println(newPos);
    }
  delay(50);
}
