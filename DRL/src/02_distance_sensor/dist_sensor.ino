int sensorpin = 0;                 // analog pin used to connect the sharp sensor
int val = 0;                 // variable to store the values from sensor(initially zero)

void setup()
{
  Serial.begin(9600);               // starts the serial monitor
}
 
void loop()
{
   while(Serial.available()) {
      char command = Serial.read();
      if (command == 'r') {
        val = analogRead(sensorpin); 
        // min = 88 max = 680 so we take range 100 - 700 
        val = (val - 100) / 6;
        Serial.println(val);
      }
  }
}
