int mq135_pin = A0;    // MQ-135 (NH3/NOx) is now on A0
int mq7_pin = A1;      // MQ-7 (CO) is now on A1
int dust_led = 2;      // Sharp sensor LED plugged into Digital 2
int dust_out = A2;     // Sharp sensor Output plugged into Analog 2

void setup() {
  // Opens the USB connection so Python can hear it
  Serial.begin(9600);
  pinMode(dust_led, OUTPUT);
}

void loop() {
  // 1. Read and Convert MQ-7 (Carbon Monoxide)
  int raw_co = analogRead(mq7_pin);
  float co_ppm = raw_co * (100.0 / 1023.0); // Convert raw electrical signal to PPM

  // 2. Read and Convert MQ-135 (Ammonia)
  int raw_nh3 = analogRead(mq135_pin);
  float nh3_ppm = raw_nh3 * (200.0 / 1023.0); // Convert raw electrical signal to PPM

  // 3. Read and Convert Sharp Dust Sensor (PM2.5)
  digitalWrite(dust_led, LOW);
  delayMicroseconds(280);
  int raw_dust = analogRead(dust_out);
  delayMicroseconds(40);
  digitalWrite(dust_led, HIGH);
  delayMicroseconds(9680);

  float calcVoltage = raw_dust * (5.0 / 1024.0);
  float dustDensity = 170.0 * calcVoltage - 0.1;
  if (dustDensity < 0) {
    dustDensity = 0.0; // Prevent negative numbers if the air is super clean
  }

  // 4. Send the cleaned data to Python (Format: PM2.5, CO, NH3)
  Serial.print(dustDensity);
  Serial.print(",");
  Serial.print(co_ppm);
  Serial.print(",");
  Serial.println(nh3_ppm); // println adds an "Enter" key at the end

  delay(2000); // Wait 2 seconds before checking the air again
}
