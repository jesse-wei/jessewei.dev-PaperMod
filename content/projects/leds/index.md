---
title: "Blinking Christmas LED's"
date: 2022-08-22T18:08:42-04:00
draft: false
cover:
    image: img/lights.jpg
    alt: "Blinking Christmas LED's"
    caption: "Blinking Christmas LED's"
    hidden: true
    hiddenInSingle: true
summary: "\"Touching wires and breadboards is good for the CS major.\""
tags: ["Arduino", "Hardware"]
---

Quote from post summary is from [Eric](https://eric-unc.tech).

{{< youtube hia_4dOh098 >}}

## Code

```arduino
// Pin 3: Input for reading button
// Pin 2: Output for controlling LED

int button_value = 0;
int BUTTON = 3;
int LED1 = 2;
int LED2 = 4;
void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  button_value = digitalRead(BUTTON);
  // button not pressed, based on my hardware implementation
  if (button_value == 0){
    digitalWrite(LED1, HIGH);
    digitalWrite(LED2, HIGH);
  } else {
    digitalWrite(LED1, HIGH);
    digitalWrite(LED2, LOW);
    delay(100);
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, HIGH);
    delay(100);
  }
}
```

{{< rawhtml >}}
<p align="center"><code>toggle.ino</code></p>
{{< /rawhtml >}}
