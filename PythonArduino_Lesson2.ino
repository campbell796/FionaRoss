int cnt=0;
void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.write("I am countin to: ");
Serial.print(cnt);
Serial.print(cnt);
Serial.println(" Mississippi. ");

cnt = cnt+1;
delay(1000);
}
