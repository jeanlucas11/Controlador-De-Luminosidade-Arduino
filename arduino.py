const int LED_QUARTO = 9;
const int LED_COZINHA = 10;
const int LED_SALA = 11;

bool estadoQuarto = false;
bool estadoCozinha = false;
bool estadoSala = false;

void setup() {
  Serial.begin(9600);

  pinMode(LED_QUARTO, OUTPUT);
  pinMode(LED_COZINHA, OUTPUT);
  pinMode(LED_SALA, OUTPUT);

   
  digitalWrite(LED_QUARTO, LOW);
  digitalWrite(LED_COZINHA, LOW);
  digitalWrite(LED_SALA, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();  

    if (comando == "1") {
      estadoQuarto = !estadoQuarto;
      digitalWrite(LED_QUARTO, estadoQuarto ? HIGH : LOW);
    } 
    else if (comando == "2") {
      estadoCozinha = !estadoCozinha;
      digitalWrite(LED_COZINHA, estadoCozinha ? HIGH : LOW);
    } 
    else if (comando == "3") {
      estadoSala = !estadoSala;
      digitalWrite(LED_SALA, estadoSala ? HIGH : LOW);
    }

    Serial.println("OK");
  }
}
