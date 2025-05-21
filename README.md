Integrantes: Jean Lucas De Cesare / Fabrício Vecchi Panisson

💡 Projeto: Controle de Iluminação via Serial com Arduino + Raspberry Pi
Esse projeto permite controlar três LEDs (representando os cômodos quarto, cozinha e sala) através da comunicação serial entre uma Raspberry Pi e um Arduino.

Cada LED é tratado como um interruptor independente. Tu envia os comandos pela serial (via socket, script Python ou terminal) e o Arduino liga ou desliga o LED correspondente:

1 → Liga/Desliga o LED do quarto

2 → Liga/Desliga o LED da cozinha

3 → Liga/Desliga o LED da sala

A lógica garante que cada número só altera o estado do seu próprio LED, sem afetar os outros.

🚀 Tecnologias Usadas
▪ Arduino Uno
▪ Raspberry Pi
▪ Comunicação Serial (USB)
▪ Código em C++ (Arduino IDE)
▪ Python + socket para envio dos dados (cliente/servidor)
