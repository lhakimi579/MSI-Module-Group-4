const int ledPin = 8;       // Connect LED + 220 ohm resistor to digital pin 8
const int potPin = A0;      // Potentiometer connected to analog pin A0

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // 1. Read and send potentiometer value to Python
  int potValue = analogRead(potPin);
  Serial.println(potValue);

  // 2. Check if Python sent a command back
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'H') {
      digitalWrite(ledPin, HIGH); // Turn LED ON
    } else if (command == 'L') {
      digitalWrite(ledPin, LOW);  // Turn LED OFF
    }
  }
  
  delay(100); // Small delay for stability
}