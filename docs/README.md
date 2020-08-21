Esta página contiene los tutoriales que armamos para introducir al manejo de *python*
mediante *jupyter-notebook*.

¿Por dónde empezar?
* Python es un lenguaje de programación orientado al manejo de datos, que puede utilizarse 
directamente en un nevagador web. El archivo [**Tutorial_notebook.ipynb**](https://github.com/JPCalderon/Astronomia-Estelar/blob/master/docs/Tutorial_notebook.ipynb) es un _notebook_
que contiene las herramientas básicas del lenguaje como para empezar a trabajar.
Al acceder al _notebook_ desde github, ustedes ven un _render_ de lo que verian en el navegador
local (en su computadora cuando esten trabajando). En github no lo pueden ejecutar. A esto
vamos a volver a la primera clase.

* Les dejo una receta de los comandos necesarios para instalar el _software_ que vamos a usar en las prácticas.
Su nombre es **CONDA** y se encuentra dentro de **ANACONDA** (https://astroconda.readthedocs.io/en/latest/).
Por favor, hagan lo siguiente:

```
    1. mkdir -p ~/materias/Astronomia-Estelar
    2. cd ~/materias/Astronomia-Estelar 
    3. mkdir conda && cd conda
    4. wget http://fcaglp.unlp.edu.ar/~jpcalderon/materias/Astronomia_Estelar/conda/Linux-x86_64/AEpracticas.tar.gz
    5. mkdir -p envs/AEpracticas
    6. tar -xzf AEpracticas.tar.gz -C envs/AEpracticas
```
   
Con esto, logran descargar el paquete que armamos con lo necesario de CONDA en su computadora y descomprimirlo en una
carpeta específica. **Se hace una única vez**. Noten que tienen que decargar el _tar.gz_ correspondiente a su Sistema Operativo 
(Linux o Windows) y arquitectura (32 bits o 64 bits). A medida que surga la necesidad, voy agregando los paquetes [aquí](http://fcaglp.unlp.edu.ar/~jpcalderon/materias/Astronomia_Estelar/conda/).

Una vez hecho lo anterior, y cada vez que quieran trabajar con la prácticas, deberán inicializar CONDA con lo siguiente:

```
    source ~/materias/Astronomia-Estelar/conda/envs/AEpracticas/bin/activate
```

El comando ```source```, es nativo de Linux y simplemente ejecuta las variables de entorno que estan dentro del archivo 
```activate```. El prompt de la terminal cambiará a algo de este estilo:
 
```
    (AEpracticas) usuarix@maquina: ̃/materias/Astronomia_Estelar
```

Lo que indica que se puede empezar a utilizar CONDA y _jupyter-notebook_.
  
