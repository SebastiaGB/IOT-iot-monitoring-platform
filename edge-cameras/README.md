# **Control d'Aforament a la Platja d'Es Trenc**
Aquest projecte consisteix a controlar l'aforament de la Platja d'Es Trenc.\
El control es realitza mitjançant dispositius IoT que usen telemetria per enviar les dades de recompte al servidor Iotib.\
Aquests dispositius són càmeres, col·locades de manera estratègica cobrint les entrades de la platja i el pàrquing, juntament amb uns infrarojos cobrint l'entrada restant.\
Amb les dades de tots aquests dispositius, és possible realitzar una estimació de quantes persones hi ha dins la platja en un instant determinat i quants cotxes hi ha al pàrquing.\
Aquest sistema permet saber quin percentatge d'aforament total està disponible.

Les càmeres s'han instal·lat a la Colònia de Sant Jordi, al costat de l'hotel Marqués, a l'entrada de Na Tirapel per controlar l'aforament de les persones, i al pàrquing de la Salinera per controlar el dels cotxes.\
Els infrarojos s'han instal·lat a l'entrada de Ses Covetes.\
Cal destacar que aquest sistema no identifica ni diferencia persones/cotxes, només els compta de manera invariable.

## **Funcionament** 
S'usa la tecnologia LoRa, que ofereix un llarg abast, baix consum i baix bitrate. És ideal per a la transmissió de dades des de llocs més remots on altres tecnologies són menys aplicables, com en el cas de les platges.\
Cada sistema està format per una càmera, una Raspberry Pi i un transmissor LoRa o LoPy. En aquest repositori NO es parlarà del LoPy.\
La càmera, mitjançant un sistema de IA anomenat Intelligent Video Analytics, és capaç de fer un seguiment d'objectes, ja siguin persones o cotxes.\
Aquesta, mitjançant una línia delimitadora, realitza un recompte de persones cada vegada que es traspassa d'un lloc a un altre.\
La Raspberry Pi, connectada directament a la càmera a través d'Ethernet, conté uns scripts amb una API capaços de recollir aquestes dades i enviar-les al transmissor LoRa per sèrie, concretament RS485.\
Aquest transmissor LoRa s'encarrega d'enviar les dades al servidor cada vegada que les rep per sèrie. 

> **Dins la carpeta Distribució_camares** es troba la distribució de càmares de la platja.

# **Passes a seguir**
1. **Configuració de les càmeres**: Instal·lar el software i configurar.
2. **Configuració dels transmissors**: Instal·lar el software dels transmissors i configurar.
3. **Configuració de la Raspberry**: Instal·lar el sistema operatiu a la Raspberry i configurar.
4. **Connexió a la plataforma**: Afegir transmissors a la plataforma.
5. Configuració IR.
6. Construir i provar el sistema.

## **1. Configuració de les càmeres**
El software necessari per a la configuració de les càmeres són Configuration Manager (software) i Project Manager (Apps & Tools), que es poden instal·lar a través d'aquest URL:

    https://downloadstore.boschsecurity.com 

Per a poder configurar la càmera cal alimentar-la i conèixer la seva IP.  
També cal conèixer la definició d'Application Interface API, un conjunt de regles que permeten interactuar amb la càmera, i que s'usaran per a poder extreure les dades del perfil configurat:

    https://download.aras.nl/Video/Bosch/Firmware/Camera/CPP_ALL%206.32.1621/rcpdoc.htm

### **Configuration Manager**
Per a conèixer la IP, el primer pas consisteix en connectar la càmera per cable Ethernet a un PC. Una vegada connectat amb l'aplicació es podrà veure quina és la direcció IP d'aquesta mitjançant el "network scan" situat a la barra lateral esquerra. Abans de connectar-se serà necessari realitzar la configuració de les IP estàtiques al PC i desactivar el DHCP:
    1. Panell de control
    2. Xarxes i Internet
    3. Centre de xarxes i recursos compartits
    4. Canviar configuració de l'adaptador
    5. Ethernet (no posar la mateixa IP que la càmera)

En accedir a la direcció IP de la càmera, serà necessari un nom d'usuari (`<CAMERA_USERNAME>`) i una contrasenya (`<CAMERA_PASSWORD>`). Els valors reals no s'han de publicar.
Una vegada es coneguin aquets paràmetres caldarà seguir aquets punts:

- Possarli una adreça privada si aquesta es pública. A l'apartat de 'my devices' amb el click dret del ratolí es podrà editar la configuració.
- Actualitzar el firmware de la càmara a la darrera versió. A l'URL de descarregues de Bosch es troba l'apartat del 'firmware' i sols s'ha de saber el model de la càmara per a descarregar-ho.
- El protocol de comunicació ussat ha de ser HTTPS encara que no s'usi certificat, per tant si no està configurat cal fer-ho.
- S'acedeix a l'apartat de 'Date/Time' de la barra superior i es sincronitza l'hora amb el pc.
- Es guarda la configuració amb ctrl+ S i es reinicia la càmara.

És **important** destacar que les 8000i disposen d'accés Wi-Fi i les 7000i no.

**No realitzar la configuració si la temperatura de la càmera és elevada.** En aquest cas, cal esperar que es refredi, ja que en cas contrari no es guardarà.

#### Configuració

A la barra superior apareixeran diversos apartats de configuració.\
S'haurà d'accedir als de 'Camera' i 'VCA'.

* Per a les càmeres 7000i és necessari accedir a 'Camera' per a crear una pre-posició amb un nom per a poder usar-la a l'apartat de "VCA" i configurar el seu perfil.
  
VCA es la tecnología que empreen les càmares pera funcionar que es diu Video Analitics, s'encarrega de processar video en temps real per a generar metadades que permet realitzar unes tasques de detecció, conteix i seguiment principalment.
La camara conté 32 perfils editables on es poden crear tasques per a la gestió d'objectes.

* En el cas de les 8000i es pot crear directament el perfil al VCA sense necessitat de crear una posició prèvia, ja que no en necessiten.

Passes a seguir (Es important no editar res del que no es mencioni a continuació): 

1. **Crear una pre-posició**: Aquestes són posición pre fixades per a que la càmara apunti a aquest lloc en concret. S'accedeix a 'Camara' a 'Prepositions and Tour'.
     - Es mou el video a l'apartat de Live video fins que es possi al lloc on es vol apuntar.
     - Es crea una preposició donantli a +, es possa un nom i s'accedeix a 'configure pre-position setings'.
     - Es seleciona la pre-posició i creada es guarda.
       
2. **Fixar una pre-posició**: Acedir a 'PTZ' i canviar el paràmetre de 'inactivitat' al número de la pre-posició creada.
     - El periode d'aquesta pot ser de 10 minuts/5 min/ 2 min.
  
3. **Crear perfil VCA**: Accedir a 'VCA' al perfil calibrat i establir la preposició creada.

4. **Indicar altura**: Accedir a 'General' a l'apartat 'Positioning', assignar el perfil on hi ha la preposició creada i assignarli l'altura de la càmara.
       
5. **Calibrar la càmara**: Accedir a 'General' a l'apartat de Calibració i configurar lel perfil de global que ve per defecte (mirar que estigui apuntant a la preposició assignada).
     - Seguir les passes de configuració i al guardad les dades aquestes es podran guardar en "mode normal", "tracking 3D" i "tracking 3D seguiment de persones".
     - En el cas de voler comptar cotxes, es guarda en el segon mode; per comptar persones, en el tercer; i en altres casos, en el primer.
     - En les 8000i no es demanarà res més, mentre que en les 7000i es requerirà guardar la pre-posició en un perfil concret.
       
6. **Configurar perfil VCA**: Accedir a 'VCA' al perfil calibrat.
   - Accedir a  'Tasks' on es selecciona l'objecte que es vol usar, en auqest cas els contadors i es fan línies manualment sobre la pantalla que delimiten dues bandes amb una direcció específica.
   - Guardar la configuració i sortir
   - S'ha de comprovar a l'apartat de 'Codificació de perfil' si hi ha activat el seguiment 3D en cas que sigui necessari.

#### 7000i
El pas 2 es de vital importància ja que si la càmara es reinicia gràcies a aquest pas al cap de el temps establert al paràmetre de periode de inactivitat la càmara agafarà el perfil on hi hagui la preposició configurada. En cas contrari s'inicia amb el perfil per defecte que es el global i es quedaria amb aquest sempre que no s'interactui amb el software de Configuration Manager.

#### 8000i
L'opció del Wi-Fi de les 8000i es troba a l'apartat de "Network", "WLAN". Des d'allà es pot activar o desactivar. També mostrarà la clau d'accés i el SSID, que **no s'ha de canviar en cap cas**.

### **Project Manager**

El Project Manager té menys opcions de configuració. Aquest permet ajustar la imatge i calibrar la càmera. Si hi ha dificultats amb el Configuration Manager en aquestes passes mencionades, el Project Manager és més senzill. I en cas de no trobar la direcció IP utilitzant el Configuration Manager, aquest ofereix diverses possibilitats, entre les més importants:

* Trobar la IP mitjançant una anàlisi de xarxa.
* Trobar la IP mitjançant el Wi-Fi.
* Trobar la IP mitjançant el codi de barres de la capsa.

Una vegada accedeixes a la càmera, s'haurà de configurar mitjançant `<CAMERA_USERNAME>` i `<CAMERA_PASSWORD>`. 

La imatge s'ajusta manualment amb el PTZ accedint a aquesta configuració, i la càmera es calibra de la mateixa manera que l'anterior.

## **2. Configuració dels transmissors i Raspberry**

### Dragino
Aquest transmissor necessita Arduino per a poder ser configurat. 

> A la carpeta **Dragino** es troben les passes a seguir per a la seva configuració.\
> Dins la carpeta **Raspberry/scripts_dragino** es troben els scripts necessaris per a poder enviar i rebre dades mitjançant aquest transmissor, així com les passes necessàries per a la seva execució i configuració.

### Milesight
Aquest transmissor es configura mitjançant ToolBox. 

> A la carpeta **Milesight** es troben les passes a seguir per a la seva configuració.\
> Dins la carpeta **Raspberry/scripts_milesight** es troben els scripts necessaris per a poder enviar i rebre dades mitjançant aquest transmissor, així com les passes necessàries per a la seva execució i configuració.

### Raspberry
Una Raspberry Pi és un ordinador de baix cost i mida reduïda dissenyat per ser accessible i versàtil, òptim per a l'ús de dispositius IoT. La seva funció en aquest projecte és obtenir les dades de la càmera, executar els scripts necessaris i enviar les dades al transmissor. 
> A la carpeta **Raspberry** es troba explicat tot el necessari per a comprendre el funcionament d'aquesta, com està configurada i els scripts que conté en cada cas.

**Els cables utilitzats han de ser d'alimentació i de dades.**

## **3. Connexió a la plataforma**

Una vegada configurats els dispositius, s'han de connectar a la plataforma IoTIB perquè es puguin comunicar amb aquesta emprant dues de les tres claus OTAA que s'han establert prèviament al dispositiu transmissor: la **DevEUI** i la **AppEUI**.

També s'haurà d'identificar amb un nom i un tipus de classe.

> El URL a la plataforma es troba al repositori LabCodi_Privat

## **Uplinks plataforma**

Els transmissors LoRa envien trames a la plataforma que es coneixen com a uplinks. Aquestes arriben en format hexadecimal i s'ha de realitzar la conversió a text.

Les dades útils de la trama, on hi ha la informació, es coneixen com el payload. Aquest representa els valors dels comptadors separats per un valor FF, que en hexadecimal és 4646. Per exemple, si s'agafa l'uplink "303146463234464632" i es separa pels valors en hexadecimal, s'obté aquest resultat: "3031 4646 3234 4646 32".

Sabent que 4646 és un separador, es pot observar que hi ha tres valors útils, tres comptadors de dades. 

Per tant, es consulta l'apartat de la distribució de càmeres i, depenent del nom que contingui, es pot saber quin comptador representa cada valor.

Finalment, cal anul·lar el primer 3 de cada dígit per a obtenir el valor numèric real: 
    3031 = 01, 3234 = 24, 32 = 2.

Per tant, el payload en format de text seria: **01 FF 24 FF 2**.\
Si la càmara esta apagada o el perfil on s'han agafat les dades no es el correcte, enviarà FFFF.


## **Downlinks plataforma**

Anteriorment s'ha mencionat la definició d'uplink, i el downlink és el cas invers. Quan es vol enviar una trama de la plataforma al transmissor, s'envia un downlink. Depenent del lloc on es vulgui enviar el downlink, aquest s'enviarà amb un format o altre.

**Cal destacar que el downlink només té la funció de canviar l'hora del dispositiu.**

A la plataforma hi ha l'opció d'enviar downlinks al transmissor desitjat. 
Només es pot enviar o una hora concreta o una data concreta.

* **Prueba-Cartel:**
  El dispositiu Milesight instal·lat a la Salinera, al ser classe C, en qualsevol moment pot rebre un downlink. **Exepte** quan envia un uplink que es una vegada cada 10 minuts. Si l'hora no es canvia es degut a que ha coincidit amb l'enviament i el semàfor l'ha bloquetjat, sols cal tornar a enviarla. S'ha d'enviar en hexadecimal, pel **port 2**:

    - Si es vol enviar una hora concreta, exemple: 12:30 -> 31323330
    - Si es vol enviar una data concreta, exemple: 2024/06/07 12:30:56 -> 3230323430363037313233303536

* **Cámara-Colonia:**
  El dispositiu Dragino instal·lat a la Colònia de Sant Jordi es troba configurat en classe A, i només podrà rebre un downlink just després d'enviar un uplink, per tant, cada 10 minuts (que és quan s'envia un uplink). En aquest cas es pot enviar l'hora en decimal (tenir en compte que l'hora es configurarà després d'enviar l'uplink, no abans), pel **port 1**:

    - Si es vol enviar una hora concreta, exemple: 12:30 -> 1230
    - Si es vol enviar una data concreta, exemple: 2024/06/07 12:30:56 -> 20240607123056

Al canviaar l'hora al milesight es canviarà directamnet, pero al dragino tenir en compte que sols serà quan envii un uplink per tant **ajustar l'hora al temps d'enviament de l'uplink**.
 
## **5. Configuració Infrarrotjos**

A l'entrada del camí de la platja de ses covetes es possaràn dos parelles de sensors infrarrotjos.\
Aquetes parelles de dispositius està formada per un emissor i un receptor, i dos feixos de llum infrarrotja que formeun dues barreres quan es coloquen un davant l'altre.\
Qualsevol objecte que interacciona amb aquest feix romprà la barrera i depenent de quina hagui romput abans es sabrà si aquest objecte, persona en aquest cas, estava entrant o sortint del recinte.
> A la carpeta **IR** es troba la docuemntació e informació necessaria per a comprendre el seu funcionament, configuració i especificacions.


