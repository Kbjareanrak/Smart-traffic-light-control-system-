#include <ESP8266WiFi.h>

WiFiServer server(88);
int led1 = D1; // กำหนดขาใช้งาน
int led2 = D2; // กำหนดขาใช้งาน
int led3 = D3; // กำหนดขาใช้งาน

void setup()
{
  //server
  Serial.begin(115200); // เปิดใช้การ Debug ผ่าน Serial
  WiFi.mode(WIFI_AP); // ใช้งาน WiFi ในโหมด AP
  WiFi.softAP("BOW"); // ตั้งให้ชื่อ WiFi เป็น ESP_IOXhop

  server.begin(); // เริ่มต้นใช้ TCP Server
  
  //LED  
  pinMode(led1, OUTPUT); // กำหนดขาทำหน้าที่ให้ขา D1 เป็น OUTPUT
  pinMode(led2, OUTPUT); // กำหนดขาทำหน้าที่ให้ขา D2 เป็น OUTPUT
  pinMode(led3, OUTPUT); // กำหนดขาทำหน้าที่ให้ขา D3 เป็น OUTPUT
  digitalWrite(led1, LOW); // LED 1 ติด
  digitalWrite(led2, LOW);// LED 2 ดับ
  digitalWrite(led3, LOW);// LED 3 ดับ
}

void loop()
{
  WiFiClient client = server.available();
  if (!client) // ถ้าไม่มีการเชื่อมต่อมาใหม่
    return; // ส่งลับค่าว่าง ทำให้ลูปนี้ถูกยกเลิก

  Serial.println("New client");
  while (client.connected()) { // วนรอบไปเรื่อย ๆ หากยังมีการเชื่อมต่ออยู่
    if (client.available()) { // ถ้ามีการส่งข้อมูลเข้ามา
      char key = client.read(); // อ่านข้อมูลออกมา 1 ไบต์
      Serial.println(key);
      
      if (key == '0') { //สัญญาณไฟแดง
        digitalWrite(led1, HIGH); // LED 1 9ติด
        digitalWrite(led2, LOW);// LED 2 ดับ
        digitalWrite(led3, LOW);// LED 3 ดับ
        Serial.println("RED ON");
        break;
     }
     if (key == '1') { //สัญญาณไฟทั่วไป
        Serial.println("RED ON");
        digitalWrite(led1, HIGH);
        delay(10000);
        digitalWrite(led1, LOW);
        digitalWrite(led3, HIGH);
        Serial.println("GReen ON");
        delay(10000);
        digitalWrite(led3, LOW);
        digitalWrite(led2, HIGH);
        Serial.println("Yellow ON");
        delay(3000);
        digitalWrite(led2, LOW);
        digitalWrite(led1, HIGH);
        Serial.println("RED ON");
        break;
    }
    }
  }
 
  delay(1);
  client.stop(); // ปิดการเชื่อมต่อกับ Client
  Serial.println("Client disconnect"); // ส่งข้อความว่า Client disconnect ไปที่ Serial Monitor
}
