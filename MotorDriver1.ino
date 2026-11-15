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

int i=0;
while(i<255){
Serial.print("The PWM is: ");
Serial.println(i);
digitalWrite(ENA, HIGH);
analogWrite(PWMA, i); 
delay(2000);
i+=5;
}
