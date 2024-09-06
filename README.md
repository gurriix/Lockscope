# Lockscope

Malware educativo de tipo ransomware, desarrollado en fases desde menor complejidad a mayor.

*Fase 1*  
- Generación de una clave asimétrica RSA de 2048 bits aleatoria. 
- La clave se mantendrá estática en todas las ejecuciónes del ransomware.Cifrado de un único archivo concreto almacenado en una carpeta del sistema, este únicamente poseerá un tipo de extensión de archivo concreta.
- La clave de descifrado se almacenará en un archivo ubicado en el lugar del sistema dónde se encuentre el código del ransomware. Tras una pequeña búsqueda en el sistema podrá obtenerse la clave, llevándose a cabo el correspondiente descifrado del archivo.

*Fase 2*	
- Generación de una clave simétrica AES de 256 bits aleatoria. La clave se mantendrá estática en todas las ejecuciones del ransomware.
- Cifrado de un conjunto de archivos almacenados en una carpeta concreta del sistema. Dicha carpeta estará compuesta por archivos con diferentes tipos de extensión.
- La clave de descifrado se almacenará en un archivo ubicado en el lugar del sistema dónde se encuentre el código del ransomware. Poseerá la particularidad de encontrarse en base64, de modo que sea fácilmente reversible el proceso, pero no siendo posible el descifrado de los archivos haciendo uso de la    clave en el estado en el que se encuentra. Para descifrar, será necesario realizar el proceso de transformación de base64 a texto claro, y entonces será posible realizar el descifrado.

*Fase 3*	
- Generación de una clave simétrica AES de 256 bits aleatoria. La clave será distinta y totalmente aleatoria en cada ejecución del ransomware.
- Cifrado de los archivos ubicados en un conjunto de carpetas del sistema seleccionadas. Estas estarán compuestas con archivos de diferentes tipos de extensión habitualmente utilizados. Tras el cifrado la clave, será envida al servidor mediante una conexión establecida por sockets.
- En el descifrado, será necesario que el atacante envíe la clave desde el servidor, de forma que se descifre todo el contenido inmediatamente cuando se haya recibido en el equipo víctima.

*Fase 4*	
- Generación de una clave simétrica AES de 256 bits, la cual, posteriormente se cifrará mediante una clave asimétrica RSA de 2048 bits. Ambas se generarán de forma aleatoria.
- Cifrado de los archivos ubicados en la principal carpeta del sistema, que es la del usuario, la cual, contiene gran cantidad de carpetas en su interior. Abarcará la mayor cantidad de extensiones posibles, secuestrando así toda la información de importancia del usuario actual. Las claves de cifrado y     descifrado serán enviadas y almacenadas en un servidor que establecerá una conexión con el equipo víctima mediante el uso de sockets, esto será realizado en el momento que se finalice el cifrado de la información.
- En el descifrado, será necesario enviar tanto la clave privada asimétrica como la simétrica cifrada desde el servidor del atacante al dispositivo víctima. Una vez realizado esto, se descifrará la clave simétrica y se comenzará con el descifrado de la información mediante la clave simétrica. 

*Fase 5*	
- Generación de una clave simétrica AES de 256 bits, la cual, posteriormente se cifrará mediante una clave asimétrica RSA de 2048 bits. Ambas se generarán de forma aleatoria.
- Cifrado de los archivos ubicados en la principal carpeta del sistema, que es la del usuario, la cual, contiene gran cantidad de carpetas en su interior. Abarcará la mayor cantidad de extensiones posibles, secuestrando así toda la información de importancia del usuario actual. Además, la clave            simétrica una vez cifrada la información será cifrada por la clave pública RSA. Las claves de cifrado y descifrado serán envidas a una carpeta de almacenamiento de Dropbox tras el cifrado de los archivos, de la cual, el servidor que estará en constante observación del contenido de dicha carpeta, las     descargará y eliminará para almacenarlas internamente.
- Para el descifrado, será necesario enviar tanto la clave privada asimétrica como la simétrica a la carpeta de Dropbox, y de ahí, el dispositivo víctima cuando detecte que se han enviado tomará ambas y las recibirá. Una vez realizado esto, se descifrará la clave simétrica mediante la asimétrica, y se     comenzará con el descifrado de la información mediante la clave simétrica.
