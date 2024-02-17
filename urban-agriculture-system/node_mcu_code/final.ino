#include  <ESP8266WiFi.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>
LiquidCrystal_I2C lcd(0x3F, 16, 2);
DHT dht(D3, DHT11);
//declaretion
int value;
int soil = A0;
int relay = D0;
double T, P;
#define echo D5
#define triger D4
#define Max_distance 200
long duration;
float distance;

void setup() {
  dht.begin();
  Serial.begin(115200);
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  pinMode (relay, OUTPUT);
  digitalWrite(relay, LOW);
  pinMode(echo, INPUT);
  pinMode(triger, OUTPUT);
  digitalWrite(triger, LOW);
  
  lcd.setCursor(0, 0);
  lcd.print("  Initializing  ");
  for (int a = 5; a <= 10; a++) {
    lcd.setCursor(a, 1);
    lcd.print(".");
    delay(500);
  }
  lcd.clear();
  lcd.setCursor(11, 1);
  lcd.print("W:OFF");
}
void loop() {
  soil_moisture();
  water_level ();
  humidity_temp ();
    if (value > 40 && T>35  )
  {
    Serial.println("moisture of the plant is ");
    Serial.print(value);
    Serial.print("%");
    delay(1000);
    digitalWrite(relay, LOW);
  }
  else if(value<40 && T<35)
    {
    Serial.println("water pumup ON");
    Serial.print(value);
    Serial.print("&");
    delay(1000);
    digitalWrite(relay, HIGH);
  }
  else if(value<40 && T>35)
    {
    Serial.println("water pumup off");
    Serial.print(value);
    Serial.print("&");
    delay(1000);
    digitalWrite(relay, LOW);
  }
  delay(500);
}
//analysise of soil mositutre value
void soil_moisture()
{
  
  value = analogRead(soil);
  value = map(value, 0, 1024, 0, 100);
  value = (100 - value);
   lcd.setCursor(0, 1);
  lcd.print("S:");
  lcd.print(value);
  lcd.print(" ");
}
//water level sensor using ultrasonic sensor
void water_level ()
{
  digitalWrite(triger, LOW);
  delayMicroseconds(2);
  digitalWrite(triger, HIGH);
  delayMicroseconds(10);
  digitalWrite(triger, LOW);
  duration = pulseIn(echo, HIGH);
  distance = (duration * 0.017);
  int dis_p = map( distance, 0, 1023, 0, 100);
  Serial.print("duration: ");
  Serial.println(duration);
  Serial.print("distance: ");
  Serial.println(distance);
  Serial.print("distance in percent: ");
  Serial.println(dis_p);
}
// adentify value of humidity and temperture
void humidity_temp ()
{
  float H = dht.readHumidity();
  float T = dht.readTemperature();
  if (isnan(H) || isnan(T))
  {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  Serial.print("Temp:");
  Serial.println(T);
  Serial.print("Humi:");
  Serial.println(H);
  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(T);
  lcd.setCursor(8, 0);
  lcd.print("H:");
  lcd.print(H);
}
