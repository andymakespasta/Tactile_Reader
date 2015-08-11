#define MAX_PORT 20 //this means valid ports are 0~19

byte port=0;
byte power=0;
int errorCount=0;

void setup() {
    Serial.begin(9600);//2400ch/s =120ch/(s*node)
    //testrun();
    //initpins();
    Serial.println("5x4pp");//sayout and protocol
}

void loop(){
    while(Serial.available()>1){
        
        port = Serial.read(); //returns the first byte of incoming serial data available (or -1 if no data is available) - int
        power = Serial.read();
        Serial.print(port);
        Serial.print(",");
        Serial.println(power);
        
        if (port < MAX_PORT){
            mappedWrite(port, power);
        }
        else{ //either incompatible or dropper character
            if (power < MAX_PORT){
                port = power;
                while(Serial.available()==0){}
                power = Serial.read();
            }
            else{
                Serial.print("Possible incompatible code.");
            }
            errorCount++;
            Serial.print(errorCount);
            Serial.println(" errors");
        }
    }

}

void testrun(){
    mappedWrite(0,128);
    delay(100);
    mappedWrite(0,255);
    mappedWrite(1,128);
    delay(100);
    mappedWrite(0,128);
    mappedWrite(1,255);
    mappedWrite(2,128);
    delay(100);
    
    for (int i=0; i < MAX_PORT-3; i++){
        mappedWrite(i,0);
        mappedWrite(i+1,128);
        mappedWrite(i+2,255);
        mappedWrite(i+3,128);
        delay(100);
    }
    
    mappedWrite(MAX_PORT-3,0);
    mappedWrite(MAX_PORT-2,128);
    mappedWrite(MAX_PORT-1,255);
    delay(100);
    mappedWrite(MAX_PORT-2,0);
    mappedWrite(MAX_PORT-1,128);
    delay(100);
    mappedWrite(MAX_PORT-1,0);
}

void mappedWrite(byte port, byte power){ //handles mapping of ports and power to match characteristic of vibration device.
//should also decide to use digital write in case port does not support pwm
    if (power==0){
        digitalWrite(map(port), LOW); 
    }
    else{
        analogWrite(map(port), power);
    }

}

int map(byte port){
    if (port<5){
        return 24+2*port;
    }
    else if (port<10){
        return 34+2*port;
    }
    else if (port<15){
        return 53-2*port;
    }
    else {
        return 83-2*port;
    }
}

void initpins(){
  for (int i=13;i<50;i++){
    pinMode(i, OUTPUT);
  }
}
// Doing analogWrite() on a non PWM pin will cause the pin to be set to HIGH with no other effect.

//alternatively, this is called whenever serial data is available
//void serialEvent(){
//    
//    incomingByte = Serial.read();
//}
//PWM: 2 to 13 and 44 to 46 (tot 15)
//LED: 13

/*
Serial. It communicates on digital pins 0 (RX) and 1 (TX) as well as with the computer via USB. Thus, if you use these functions, you cannot also use pins 0 and 1 for digital input or output.


analogWrite(pin, value)
the duty cycle: between 0 (always off) and 255 (always on).


pin=9
pinMode(9, OUTPUT); //the pins are numbered
analogWrite(pin, value)
digitalWrite(ledPin, HIGH); 

Serial.write(val) will send data as binary
Serial.print(val) will send numbers as characters

*/



