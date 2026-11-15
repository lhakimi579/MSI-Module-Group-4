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

digitalWrite(ENA, HIGH);
analogWrite(PWMA, 255); 
Serial.println("3");
delay(1000);
Serial.println("2");
delay(1000);
Serial.println("1");
delay(1000);

Serial.println("motor is stopping");
digitalWrite(ENA, LOW);
analogWrite(PWMA, 0); 
delay(5000);

}
