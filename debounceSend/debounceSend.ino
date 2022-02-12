#include <RCSwitch.h>                // rf librarie

const int buttonPin = 2;             // number of the pushbutton pin
const int ledPin = 1;                // define led pin
int buttonState;                     // current reading from the input pin
int lastButtonState = LOW;           // previous reading from the input pin
int ledState = LOW;

unsigned long lastDebounceTime = 0;  // last time the output pin was toggled
unsigned long debounceDelay = 50;    // lebounce time

RCSwitch mySwitch = RCSwitch();

void setup() {
  // GPIO setup
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);

  // radio setup
  mySwitch.enableTransmit(3);        // define DATA pin
  mySwitch.setPulseLength(320);      // define pulselength
  mySwitch.setProtocol(1);           // default is 1
  mySwitch.setRepeatTransmit(15);    // define number tries
}

void loop() {
  // read the state of the switch into a local variable:
  int reading = digitalRead(buttonPin);

  // if the switch changed, due to noise or pressing:
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // if the button state has changed:
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == HIGH) {
        // change LED state
        ledState = !ledState;
        digitalWrite(ledPin, ledState);
      }
      // send radio message acording to protocol
      mySwitch.send("10011101");
    }
  }
  // save the reading as lastButtonState
  lastButtonState = reading;
}
