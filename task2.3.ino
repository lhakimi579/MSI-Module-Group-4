#include <Servo.h>
const int potPin = A0;
const int ledPin = 8;  

Servo myServo;  // Cipta objek servo
const int servoPin = 9; // Pin PWM untuk servo

void setup() {
  Serial.begin(9600);
   myServo.attach(servoPin);
}

void loop() {
  // 1. Read and send potentiometer value to Python
  int potValue = analogRead(potPin);
   pinMode(ledPin, OUTPUT);
  Serial.println(potValue);

   if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'H') {
      digitalWrite(ledPin, HIGH); // Turn LED ON
    } else if (command == 'L') {
      digitalWrite(ledPin, LOW);  // Turn LED OFF
    }
    
  }
  
  int angle = map(potValue, 0,1023, 0,180);
  myServo.write(angle);
  
  delay(100); // Small delay for stability
}