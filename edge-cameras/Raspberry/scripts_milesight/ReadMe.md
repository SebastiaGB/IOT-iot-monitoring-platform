##  Aclariment inicial
A part dels dos arxius `.py`, a la Raspberry també hi haurà d'haver un arxiu `.txt` on es guardaran les dades dels objectes de perfil de les càmeres. Aquest fitxer ha de tenir el nom desitjat, però cal assegurar-se que la seva ruta s'indiqui correctament en el codi (`ruta/a/fitxer.txt`).

Un cop creat l'arxiu a la Raspberry, feu clic dret sobre ell, copieu la seva ruta d'accés i enganxeu-la en el codi allà on s'indica `ruta/a/fitxer.txt`.

---

##  Configuració necessària
A continuació es detallen els canvis necessaris per al correcte funcionament dels scripts.

>Al respositori **LabCodi_privat** a la carpeta distribució_camares es troben les claus.

###  Fitxer `milesight_controller.py`
Per configurar aquest fitxer, cal modificar les següents línies:

- **Línia 12:** Port sèrie de Dragino (`port_dragino`).
- **Línia 17:** Contrasenya (`password`).
- **Línia 18:** Adreça IP de la càmera (`direccio_ip`).
- **Línia 27:** Ruta del fitxer `.txt` on es guardaran els contadors (`ruta/a/fitxer.txt`).

### 🛠 Fitxer `reiniciarcontadors.py`
Per configurar aquest fitxer, cal modificar les següents línies:

- **Línia 9:** Contrasenya (`password`).
- **Línia 12:** Adreça IP de la càmera (`direccio_ip`).

---

##  Explicació dels scripts
Es necessita `<CAMERA_USERNAME>`, `<CAMERA_PASSWORD>` i `<CAMERA_HOST_OR_IP>` per comunicar-se amb l'API de Bosch.

### **`milesight_controller.py`**
Aquest script s'encarrega de:

- Configurar el **port sèrie** i el **baudrate**.
- Especificar la **ruta del fitxer `.txt`**.
- **Desactivar advertències SSL** per evitar problemes amb certificats.
- Utilitzar un **sistema de semàfors** per sincronitzar operacions.

#### **Funcions principals**

1. **`get_camera_data()`**
   - Realitza una petició GET HTTPS a la càmera per obtenir la resposta XML de l'API.
   - Utilitza les credencials (`username` i `password`) per autenticar-se.

2. **`decode_xml_response(xml_response)`**
   - Analitza la resposta XML per obtenir els valors dels contadors.
   - Pas a pas:
     1. Extreu la longitud i el valor de la `string` amb les dades dels contadors.
     2. Elimina espais en blanc per obtenir una cadena contínua.
     3. Extreu els dos primers caràcters, que indiquen el nombre de contadors.
     4. Converteix a decimal per verificar si la longitud de la `string` correspon al nombre de contadors (cada contador té 70 caràcters).
     5. Si la resposta és incorrecta, retorna `0`.
     6. Si la resposta és correcta:
        - Processa els contadors i els converteix a decimal.
        - Guarda els valors en una llista `counters`.
     7. Retorna `counters`.

3. **`save_counters_to_txt(counters)`**
   - Guarda els valors dels contadors en un fitxer `.txt`.
   - Escriu la data i hora de cada registre.

4. **`send_data(ser)`**
   - Agafa el semàfor.
   - Envia les dades mitjançant el port sèrie.
   - Obre el port sèrie, obté els valors de la càmera i els envia.
   - Si no hi ha dades, envia `0xFF 0xFF` per indicar error.
   - Guarda els valors al fitxer `.txt`.
   - Allibera el semàfor.

5. **`listen_for_data(ser)`**
   - Escolta el port sèrie de forma continuada si el semàfor no està agafat.
   - Llegeix les dades rebudes i processa les ordres.
   - Si la dada rebuda té 14 caràcters i és numèrica:
     - La interpreta com una data i actualitza l'hora del sistema.
   - Si la dada rebuda té 4 caràcters i és numèrica:
     - La interpreta com una hora i actualitza l'hora del sistema.
   - Si no es rep res, espera 15 segons i surt del bucle.

6. **Bucle principal**
   - Es crea un objecte serial.Serial per establir la connexió amb el dispositiu a través del port SERIAL_PORT i la velocitat BAUDRATE.
   - Mitjançant la llibreria schedule, s'estableix una tasca (send_data) que s'executarà cada 10 minuts per enviar dades al dispositiu connectat al port sèrie.
   - Fil per executar el planificador (scheduler_thread):
        - run_scheduler és una funció que manté schedule.run_pending() en execució contínua per garantir que les tasques programades (com send_data) es compleixin.
        - Es crea un fil daemon per executar run_scheduler de manera independent al codi principal.
   - Fil per escoltar el port sèrie (listen_thread):
        - listen_for_data és una funció que llegeix contínuament les dades rebudes pel port sèrie.
        - Es crea un fil daemon per gestionar l'escolta sense bloquejar el programa principal.
   - El 'while true' manté el programa actiu indefinidament, fent que continuï executant els fils en segon pla.
---

### **`reiniciarcontadors.py`**
Aquest script:
- Realitza una petició d'escriptura HTTPS a la càmera.
- Utilitza l'API de Bosch per reiniciar els valors dels contadors a `0`.

---

##  Conclusió
Aquests scripts permeten obtenir dades de les càmeres Bosch i enviar-les via port sèrie al dispositiu Milesight. També permeten escoltar dades per actualitzar l'hora del sistema i reiniciar els contadors quan sigui necessari.

Aquest sistema està optimitzat per funcionar de manera automàtica i fiable en una Raspberry Pi, garantint un registre adequat de les dades.

