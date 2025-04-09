El modulo "vehiculos" contiene toda la informacion referida al vehiculo, como placa, año, modelo, color, etc. Además de la ultima fecha de pago y el proximo vencimiento (a 30 dias del ultimo pago)
Ademas de contener el nombre del dueño (cliente), y un respartner con la licencia del dueño.
En este modulo tambien vemos heredado el modulo inventario propio de Odoo, para poder obtener los distintos planes de seguro. En la interfaz se puede observar que plan de seguro tiene cada vehiculo.
El modulo siniestros contiene un historial de cada vehiculo, donde se van anotando cada siniestro ocurrido por el vehiculo, con su descripcion, costo total de la reparación, el porcentaje que el seguro cubrió y cuanto debió pagar el seguro.
Ademas de recabar informacion como la fecha del suceso y una descripcion breve de lo sucedido, tambien da opciones a elegir como "tipo" de siniestro (impacto, rotura, etc)
