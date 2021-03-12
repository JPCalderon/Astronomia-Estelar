## Instalación en GNU/LINUX


1- Instalar (como administradorx), los siguientes paquetes:

```apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6```

Son nesecarios para que funcione el entorno visual del anaconda.

Los siguientes comandos (2- a 4-) se ejecutan por unica vez:

  2- Ejecutar el instalador: ```bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh```

  3- Refrescar las variables de entorno: ```source ~/.bashrc```

  4- Configurar conda para que no inicie cada vez que se abre una terminal: ```conda init && conda config --set auto_activate_base False```


5- Abrir una terminal nueva y ejecutar: ```conda activate && anaconda-navigator```
