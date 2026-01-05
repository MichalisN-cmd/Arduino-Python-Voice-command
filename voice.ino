void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "light on") {
      digitalWrite(13, HIGH);
    }
    else if (cmd == "light off") {
      digitalWrite(13, LOW);
    }
  }
}
