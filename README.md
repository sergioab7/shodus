<p align="center">
<img src="https://gyazo.com/221b94ce5b2da615eb7f80b3e1fb5e6d.png"
    alt="HackWeb"
    width="600"
    height="200"
    style="float: left; margin-right:10px;" />
</p>


<h1>Shodus</h1>

Script para la automatización de búsquedas en shodan. Uso fácil e intuitivo.



## :hammer: Requisitos de instalación 

Instalar las siguientes librerías:

**Argparse**
```
pip3 install argparse
```
**Colorama**
```
pip3 install colorama
```
**BeautifulTable**
```
pip3 install beautifultable
``` 

## :pencil2: Autor
xaxxjs

## :white_check_mark: Funcionamiento

Existen 4 argumentos en este script.
<ul>
    <li>-H -> Asignar la IP que queremos y siempre debe ir acompañada de el parametro "-S" o "-A" [Parametro obligatorio]</li>
    <li>-S -> Búsqueda Simple, una vez añadido el parametro "-H" [Parametro obligatorio]</li>
    <li>-A -> Búsqueda Avanzada, una vez añadido el parametro "-H"</li>
</ul>

Ejemplo: 
```
> python3 shodus.py -H 8.8.8.8 -S
```
Además existen otros 2 argumentos.
<ul>
    <li>-s -> Asignas la búsqueda que desees de cualquier servicio</li>
    <li>-show -> Va de la mano con el parámetro "-s", para ver únicamente las IPs [Parametro NO obligatorio]</li>
</ul>

Ejemplo: 
```
> python3 shodus.py -s apache 
> python3 shodus.py -s apache -show
```

## :trophy: Ejemplos

<p align="center">
<img src="https://gyazo.com/09710fe54fd7e46bf808a8f494035b62.png"
    alt="HackWeb"
    width="600"
    height="800"
    style="float: left; margin-right:10px;" />
</p>

<p align="center">
<img src="https://gyazo.com/8935fd6b5cf14bffe1b2b767d3ab6089.png"
    alt="HackWeb"
    width="600"
    height="800"
    style="float: left; margin-right:10px;" />
</p>

Si te ha gustado y aportado agradecería un Like!
¡Muchas gracias!
