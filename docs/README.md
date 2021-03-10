# Instrucciones de instalación

Hola! esta página contiene instrucciones para instalar jupyter-notebook en un entorno CONDA, para poder utilizar python directamente en un navegador. 

# ¿Qué vas a necesitar?

- Vas a necesitar una PC/notebook con Windows y al menos 3Gb de espacio libre.
- Un poco de paciencia

# Aquí va la receta
1- Descargar el entorno *Anaconda*, que permite mantener un sistema de archivos dentro de un mismo ambiente sin interferir en el resto del sistema operativo: https://www.anaconda.com/products/individual#windows





Esta página contiene los tutoriales que armamos para introducir al manejo de *python*
mediante *jupyter-notebook*.

¿Por dónde empezar?

* Les dejo una receta de los comandos necesarios para instalar el _software_ que vamos a usar en las prácticas.
Su nombre es **CONDA** y se encuentra dentro de [**ANACONDA**](https://astroconda.readthedocs.io/en/latest/).
Por favor, hagan lo siguiente:

```
    $ mkdir -p ~/materias/Astronomia-Estelar
    $ cd ~/materias/Astronomia-Estelar 
    $ mkdir conda && cd conda
    $ wget http://fcaglp.unlp.edu.ar/~jpcalderon/materias/Astronomia_Estelar/conda/Linux-x86_64/AEpracticas.tar.gz
    $ mkdir -p envs/AEpracticas
    $ tar -xzf AEpracticas.tar.gz -C envs/AEpracticas
```
   
Con esto, logran descargar el paquete que armamos con lo necesario de CONDA en su computadora y descomprimirlo en una
carpeta específica. **Se hace una única vez**. Noten que tienen que decargar el _tar.gz_ correspondiente a su Sistema Operativo 
(Linux o Windows) y arquitectura (32 bits o 64 bits). A medida que surja la necesidad, voy agregando los paquetes [aquí](http://fcaglp.unlp.edu.ar/~jpcalderon/materias/Astronomia_Estelar/conda/).

Una vez hecho lo anterior, y cada vez que quieran trabajar con la prácticas, deberán inicializar CONDA con lo siguiente:

```
    $ source ~/materias/Astronomia-Estelar/conda/envs/AEpracticas/bin/activate
    $ conda-unpack
```
El equivalente al comando anterior en Windows es:

```
    $ conda\envs\AEpracticas\Scripts\activate.bat
```
que se ejecuta en una consola de DOS.
    
El comando ```source```, es nativo de Linux y simplemente ejecuta las variables de entorno que estan dentro del archivo 
```activate```. El _prompt_ de la terminal cambiará a algo de este estilo:
 
```
     (AEpracticas) usuarix@maquina: ̃/materias/Astronomia_Estelar
```

Lo que indica que se puede empezar a utilizar CONDA y _jupyter-notebook_.

* Python es un lenguaje de programación orientado al manejo de datos, que puede utilizarse 
directamente en un nevagador web. El archivo [**Tutorial_notebook.ipynb**](https://github.com/JPCalderon/Astronomia-Estelar/blob/master/docs/Tutorial_notebook.ipynb) es un _notebook_
que contiene las herramientas básicas del lenguaje como para empezar a trabajar.
Al acceder al _notebook_ desde github, ustedes ven un _render_ de lo que verian en el navegador
local (en su computadora cuando esten trabajando). En github no lo pueden ejecutar. A esto
vamos a volver a la primer clase.

  **Les propongo que** descarguen el _notebook_ del tutorial y las tablas de datos:
  
```
    wget https://raw.githubusercontent.com/JPCalderon/Astronomia-Estelar/master/docs/Tutorial_notebook.ipynb
    wget https://raw.githubusercontent.com/JPCalderon/Astronomia-Estelar/master/docs/investigadores-2007.csv
    wget https://raw.githubusercontent.com/JPCalderon/Astronomia-Estelar/master/docs/investigadores-2019.csv
    wget https://github.com/JPCalderon/Astronomia-Estelar/raw/master/docs/es_todo_por_hoy.jpg
```

y abran el _notebook_ en el navegador con el siguiente comando:

```
    (AEpracticas) usuarix@maquina: ̃/materias/Astronomia_Estelar$ jupyter-notebook Tutorial_notebook.ipynb 
```

Si al final de todo ven un gatito ya es un montón. Pueden empezar a jugar, y ejecutar cada celda para experimentar
cómo funciona. Lo retomamos en la primer clase.

---
También pueden usar [Binder](https://mybinder.org/), una herramienta _on-line_ para probar el tutorial. 
Haciendo click en el botón de abajo accederán a un entorno que les permite ejecutar cada celda de código 
y visualizar el resultado. Será muy parecido a lo que vean localmente, cuando ejecuten CONDA en su propia
computadora.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JPCalderon/Astronomia-Estelar/master?filepath=docs%2FTutorial_notebook.ipynb)
(Puede tardar unos minutos en cargar :/)
