#include <Servo.h>

Servo myServo;  // Cipta objek servo
const int ledPin = 8;
const int servoPin = 9; // Pin PWM untuk servo

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
}

void loop() {
  // Semak jika ada data masuk dari Python melalui Serial
  if (Serial.available() > 0) {
    int angle = Serial.parseInt(); // Baca nombor yang dihantar oleh Python
    
    // Pastikan nilai dalam lingkungan 0 - 180
    if (angle >= 0 && angle <= 180) {
      myServo.write(angle); // Gerakkan servo ke sudut tersebut
    }
  }
}
