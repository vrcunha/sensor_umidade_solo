# define pinSensor1 A0
# define pinSensor2 A1
# define pinSensor3 A2
# define pinSensor4 A3
# define pinSensor5 A4

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int pythonSignal = Serial.read();
      if (pythonSignal == 49) {
        digitalWrite(LED_BUILTIN, HIGH);
      } else if (pythonSignal == 48) {
        digitalWrite(LED_BUILTIN, LOW);
        }
    }
  
  int sensor1Value = analogRead(pinSensor1);
  int sensor2Value = analogRead(pinSensor2);
  int sensor3Value = analogRead(pinSensor3);
  int sensor4Value = analogRead(pinSensor4);
  int sensor5Value = analogRead(pinSensor5);
  
  Serial.print(sensor1Value);
  Serial.print(",");
  Serial.print(sensor2Value);
  Serial.print(",");
  Serial.print(sensor3Value);
  Serial.print(",");
  Serial.print(sensor4Value);
  Serial.print(",");
  Serial.println(sensor5Value);
  delay(100);

}
