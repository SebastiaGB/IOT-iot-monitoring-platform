# Raspberry

**Passes a seguir per a configurar la raspberry**

Al URL es poden veure totes les especificacions necessaries de la raspberry:

	https://www.raspberrypi.com/documentation/


## Instalar sistema operatiu 

Depenent del model de la raspberry a usar s'instala un sistema operatiu especific, per a realitzar aquesta instalació es descarrega el Raspberry Pi Imager a l'URL:

	https://www.raspberrypi.com/software/

 S'instala a una MICRO-SD de 32 GB mínim.\
 Agafar el sistema de 32 GB si té 4 o menys GB de RAM.

 Es imporatant conectar el hdmi abans d'encendre la raspberry, en cas contrari aquesta no es visualitzarà.

## Actualitzar la raspberry

La primera passa a realitzar una vegada encessa la raspberry es configurarla seguint les senzilles passes que indica la pantalla, llavors un cop reiniciada accedir a la terminal i actualitzarla, per a ferho es comprova quins paquets s'han d'actualitzar realitzant: 

	sudo apt update && sudo apt full-upgrade 

## Configurar ip estàtica 
Per a poder assiganr una ip estàtica a la raspberry pi s'usa el Network manager:

1. Usa la comanda: i agafa l'opció de modificar.

   		sudo nmtui 
2. Modifica l'eth0 que es l'entarda de ehternet.
3. Es canvia la configuració d'ipv4 d'automàtic a manual.
4. Possar una adreça privada dins del rang de la càmara i un adreça port (opcional),DNS no necessari.
5. Guardar i sortir
6. sudo reboot per a aplicar canvis

ip a , per comrpovar si s'ha assignat sols, mirar interficie de eth0.

> **Es vol que el dispositiu Dragino tranmeti cada 10 minuts, per tant s'usa el crontab per a realitzar aquesta transmissió automàtica.**

> **Els scripts reiniciar contadors també funcionen amb contab amb la funció de reiniciar les dades de la càmara cada dia. S' ha estodiat que a les 2:00h es la millor hora per a realitzar aquest reinici.**

> **El script del milesight s'ha d'estar executant continuament , per tant, crontab no es adient per a fer aquesta funció. S'usa un 'while True' a l'script.**


## Configuració de crontab per **Dragino** i **Reiniciar contadors**
Per a configurar el crontab i afeguir l'arxiu cal seguir aquestes passes:

1.	Accedir a la terminal/finesta de comandes.
2.	Executar comanda:

  		crontab -e
4.	Copiar la ruta de l'archiu anat al escritori clic dret.
3.	Al final de la página escriure:

  		* 2 * * * python3 /rutaalarxiuaexecutar/arxiu.py

Cada asterisc (*) que hi ha a la comanda té un significat i una limitació:

* minuts(0-60) 
	* hores(0-24) 
		* dies de mes(1-31) 
			* mes(1-12) 
				* dies de la semana(1-7)

## Configuració de servei per **Milesight**

Es vol configurar un servei per a executar l'script de la raspberry cada vegada que aquesta s'inicia i per a prevenir errors, ja que si n'apareix algún que aturi el script el servei s'encarregarà de reiniciarlo.\
Les pases a seguir són les següents:

1. Executar aquesta comanda a terminal:

   		sudo nano /etc/systemd/system/milesight_controller.service
2. Copiar i editar el camps corresponents:

		[Unit]
		Description=<Descripció del script>	
 		After=network.target

		[Service]
		ExecStart=python3 </ruta/al/script.py>
		WorkingDirectory=</ruta/al/>
		StandardOutput=inherit
		StandardError=inherit
		Restart=always
		User=pi
	
		[Install]
		WantedBy=multi-user.target

3. Executar comanda:

   		sudo systemctl enable milesight_controller.service
4. Executar comanda:

   		sudo systemctl start milesight_controller.service
5. (Opcional), per a comprovar si està activat:

   		sudo systemctl status milesight_controller.service


## Port Dragino 

Per a saber quin es el port al que es troba el dispositiu Dragino conetcat es realitza la comanda: 

	dmesg | grep tty     

i a la darrera linea apareixerà el ' port : USB ACM device'
                            usaualment es el port 'ttyACM0'

## Port Milesight 

Per a saber quin es el port al que es troba el dispositiu Milesight conetcat es realitza la comanda: 

	dmesg | grep tty     

i a la darrera linea apareixerà el 'FTDI USB Serial'
                            usaualment es el port 'ttyUSB0'


## Usar PC de monitor

Per a realitzar aquesta passa cal:
- Establir una ip estàtica a la raspberry i al ordinador.
- Es conecta el cable ethernet.
- Realitzar una conexió ssh a la raspberry empreant la consola 'cmd':

  		nomd'usuariraspberry@adreçaipestàtica

 



	



