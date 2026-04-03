//const int LED_PIN    = 13;
const int MOTOR1_IN1 = 8;
const int MOTOR1_IN2 = 9;
const int MOTOR2_IN3 = 12;
const int MOTOR2_IN4 = 13;

void setup() {
//  pinMode(LED_PIN, OUTPUT);

  // Motor A
  pinMode(MOTOR1_IN1, OUTPUT);
  pinMode(MOTOR1_IN2, OUTPUT);

  // Motor B
  pinMode(MOTOR2_IN3, OUTPUT);
  pinMode(MOTOR2_IN4, OUTPUT);
  
  // Stop both motors initially
  digitalWrite(MOTOR1_IN1, LOW);
  digitalWrite(MOTOR1_IN2, LOW);
  digitalWrite(MOTOR2_IN3, LOW);
  digitalWrite(MOTOR2_IN4, LOW);

  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == 'H') {
//      digitalWrite(LED_PIN, HIGH);             

      // Motor A forward
      digitalWrite(MOTOR1_IN1, HIGH);
      digitalWrite(MOTOR1_IN2, HIGH);

      // Motor B forward
      digitalWrite(MOTOR2_IN3, HIGH);
      digitalWrite(MOTOR2_IN4, HIGH);

    } else if (c == 'L') {
//      digitalWrite(LED_PIN, LOW);              

      // Stop both motors
      digitalWrite(MOTOR1_IN1, LOW);
      digitalWrite(MOTOR1_IN2, LOW);
      digitalWrite(MOTOR2_IN3, LOW);
      digitalWrite(MOTOR2_IN4, LOW);
    }
  }
}
