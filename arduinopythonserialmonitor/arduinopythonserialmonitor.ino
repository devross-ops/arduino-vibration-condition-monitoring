int LED_Pin1 = 13;
int vibr_Pin = 3;
int LED_Pin2 = 12;

void setup() {
    pinMode(LED_Pin1, OUTPUT);
    pinMode(LED_Pin2, OUTPUT);
    pinMode(vibr_Pin, INPUT);
    Serial.begin(9600); // Initialize Serial Communication
}

void loop() {
    long measurement = pulseIn(vibr_Pin, HIGH); // Read vibration data
    Serial.println(measurement); // Send data to Serial Monitor
    delay(100); // Small delay to prevent flooding

if (measurement > 500) {
        digitalWrite(LED_Pin1, HIGH); //LED1 high, LED2 stays off, these can be changed dependent on the vibration sensors capabilities
        delay(500);
        digitalWrite(LED_Pin2, LOW);
    } else {
        digitalWrite(LED_Pin1, LOW);
        delay(100);
        digitalWrite(LED_Pin2, HIGH); //LED2 high, LED1 stays off
    }
  }