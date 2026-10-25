#include <Wire.h>
#include <MPU6050.h>
#include <Servo.h>

MPU6050 mpu;
Servo servo;

int servoPosition = 90;
unsigned long lastSendTime = 0;
const int sendInterval = 100; // Send sensor data every 100ms

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed!");
    while (1);
  }

  servo.attach(9);       // Servo signal on D9[cite: 4]
  servo.write(servoPosition);
  
  pinMode(4, OUTPUT);    // Green LED on D4[cite: 4]
  pinMode(3, OUTPUT);    // Red LED on D3[cite: 4]
}

void loop() {
  // 1. Stream MPU6050 data periodically (every 100ms)
  if (millis() - lastSendTime >= sendInterval) {
    lastSendTime = millis();
    
    int ax, ay, az, gx, gy, gz;
    mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    
    // Print in the exact comma-separated format Python expects
    Serial.print(ax); 
    Serial.print(","); 
    Serial.print(ay); 
    Serial.print(","); 
    Serial.println(az);
  }

  // 2. Check if Python sent an access command ('A' or 'D')
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'A') {
      servo.write(180);       // Unlock servo[cite: 4]
      digitalWrite(4, HIGH);  // Green LED ON[cite: 4]
      digitalWrite(3, LOW);   // Red LED OFF[cite: 4]
    } 
    else if (command == 'D') {
      servo.write(90);        // Lock servo[cite: 4]
      digitalWrite(4, LOW);   // Green LED OFF[cite: 4]
      digitalWrite(3, HIGH);  // Red LED ON[cite: 4]
    }
  }
}
