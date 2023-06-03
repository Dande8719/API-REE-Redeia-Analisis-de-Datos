# API-REE-Redeia



![image](https://github.com/Dande8719/API-REE-Redeia-/assets/103025222/ab6b3223-41dd-4d2c-8152-0c1da8e30af8)



![image](https://github.com/Dande8719/API-REE-Redeia-/assets/103025222/5c4fc708-f427-47b9-b669-19d224b3cfc4)


Resumen:
Utilizando la API REData API de Red Electrica de España obtendremos la información relativa a la demanda, la generación, el coste y el intercambio de energia electrica con los países vecinos. Crearemos varias funciones para la automatización de la descarga de esos datos para posteriormente crear un Data Frame adecuado para poder trabajar con nuestros datos.

La Red Eléctrica de España (REE) es la empresa encargada de la operación y gestión del sistema eléctrico en España. Su función principal es garantizar el suministro de electricidad a todos los usuarios del país de manera segura, eficiente y sostenible.

La red eléctrica de España está compuesta por una extensa infraestructura de líneas de transmisión, subestaciones y centros de control que permiten la distribución de la electricidad desde las centrales generadoras hasta los consumidores finales. REE se encarga de supervisar y controlar el flujo de electricidad en tiempo real, garantizando la estabilidad del sistema y gestionando los desequilibrios entre la oferta y la demanda de electricidad.

Además, REE es responsable de la planificación y desarrollo de la red eléctrica, asegurando que haya suficiente capacidad de transmisión para satisfacer las necesidades presentes y futuras del sistema. También se encarga de la coordinación con los operadores de otros países para garantizar la interconexión y el intercambio de electricidad a nivel europeo.

Paso 1:
Primero haremos una llamada a la API con los parámetros que nos interesan y nos devolverá una respuesta en formato JSON. La documentación la podemos encontrar aquí: https://earthquake.usgs.gov/fdsnws/event/1/

Paso 2:
Una vez tenemos obtenemos la respuesta, transformaremos los datos y los guardaremos en un DataFrame.

Paso 3:
Partiendo del DataFrame anterior visualizaremos los datos en un mapa 3D con plotly.graph_objects que muestre la localización e intensidad de los terremotos.

Paso 4:
Convertiremos el mapa en formato GIF y lo mostraremos aquí.
