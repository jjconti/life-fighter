El Juego
========

**Life Fighter** consiste una una grilla del `Juego de la Vida`_ de Conway en la cual,
de generación a generación, una población de células va cambiando. Algunas nacen, otras
mueren y otras sobreviven. Una de las células es nuestro heroe. El objetivo del juego
es mover al heroe a una posición segura que le permita pasar a la siguiente generación. 
A medida que se realizan movimientos y se sobrevive, se van sumando puntos.

Las Reglas
----------

En el mundo del Juego de la Vida cada casilla representa a una célula. Esta puede estar
viva (representada con una cículo en ella) o puede estar muerta (representada como la 
casilla vacía). Cada célula tiene 8 vecinas.

1) Si una célula está viva y tiene menos de 2 vecinas vivas (0 o 1), muere de soledad.
2) Si una célula está viva y tiene más de 3 vecinas vivas (4 o más), muere de inanición.

De las dos reglas anteriores se deduce que una célula viva sobrevive a la siguiente 
generación solo si tiene 2 o 3 vecinas vivas.

3) Si una célula está muerta y tiene 3 vecina vivas, nace.

Los Modos de Juego
------------------

.. TODO Finish Me

.. _`Juego de la Vida`: https://es.wikipedia.org/wiki/Juego_de_la_vida
