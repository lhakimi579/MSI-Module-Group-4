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

digitalWrite(ENA, LOW);
analogWrite(PWMA, 75); 
delay(2000);



}
