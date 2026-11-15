const int PWMA = 10;
const int PWMB = 11;
const int ENA = 12;
const int ENB = 13;


void setup() {
  // put your setup code here, to run once:
pinMode(ENA, OUTPUT);
pinMode(ENB, OUTPUT);
pinMode(PWMA, OUTPUT);
pinMode(PWMB, OUTPUT);

Serial.begin(9600);

}

void loop() {
int left;
int right;
 Serial.println("enter left speed:");
while (Serial.available()==0){
}
while (Serial.available()>0){
   left = Serial.parseInt();
   Serial.read();
   Serial.print("Left motor speed is ");
   Serial.println(left);
}

Serial.println("enter right speed:");
while (Serial.available()==0){
}
while (Serial.available()>0){
   right = Serial.parseInt();
   Serial.read();
   Serial.print("right motor speed is ");
   Serial.println(right);
}

driveRobot(left, right);
}

void driveRobot(int speedLeft, int speedRight){
digitalWrite(ENA, HIGH);
analogWrite(PWMA, speedLeft);
digitalWrite(ENB, HIGH);
analogWrite(PWMB, speedRight); 
delay(5000);
}
