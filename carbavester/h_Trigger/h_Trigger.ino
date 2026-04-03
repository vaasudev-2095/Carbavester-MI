// HumanLed.ino
// Turns LED on pin 13 ON when 'H' received via Serial, OFF when 'L'

const int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == 'H') {
      digitalWrite(LED_PIN, HIGH);
    } else if (c == 'L') {
      digitalWrite(LED_PIN, LOW);
    }
  }
}
