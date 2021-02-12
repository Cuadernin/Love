# Como enamorar a tu chikistrikis ♥ 😍
Como enamorar a tu pareja usando Python.

## Funcionamiento 🔨
Se hace WebScraping al sitio de poemas [frasess](https://www.frasess.net/poemas-de-amor-cortos-y-romanticos-78.html) y se elige un poema al azar. Además, con un archivo .dat
garantizamos almacenar un valor n que irá aumentando conforme se compile el código, es decir, es un contador de compilado. 
Finalmente enviamos el contenido del poema y como asunto se escribe la leyenda "Poema n de 30", como ejemplo. 

## Input 📄
* **email**: _el correo que vas a usar para mandar el mensaje_
* **passw**: _la contraseña del correo_
* **recibido**: _Correo de tu pareja_

Si tu correo no usa el servicio de google entonces debes cambiar la linea donde se hace uso de la libreria **smtplib** por

```
with smtplib.SMTP_SSL("smtp-mail.outlook.com",587,context=context) as server:
with smtplib.SMTP_SSL("smtp.mail.yahoo.com",465,context=context) as server:
```

## Output 📦
Correo enviado con el formato:

**Asunto:** Poema n de 30    \
**Mensaje:** Poema aleatorio de [frasess](https://www.frasess.net/poemas-de-amor-cortos-y-romanticos-78.html)

## Extra 🔧
Para garantizar el poema cada dia o el tiempo deseado programe una tarea con el _programador de tareas de Windows_. 
También puede cargar el proyecto en una maquina virtual. No obstante, esta última opción depende del servicio de correo electrónico desde el cual se envia el correo. 

## Nota 📝
Puede modificar el sitio al que se hace WebScraping pero debe buscar los atributos y etiquetas HTML que contengan el mensaje de interés (esto muy posiblemente requiera modificar el codigo). Además, para garantizar que el poema NUNCA se repita puede hacer lo mismo que se hizo con el archivo .dat pero con un archivo de texto. Las modificaciones son infinitas 🔥.

**By Cuadernin**

