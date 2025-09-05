SELECT  sum(precio_total) as ingreso_total
FROM tickets;

SELECT strftime('%Y-%m',fecha) as Mes, SUM(precio_total) as ingreso_total_mes
FROM tickets
GROUP BY Mes
ORDER by Mes;

SELECT id_departamento, sum(precio_total) as ventas_dep
FROM tickets
GROUP by id_departamento
ORDER by ventas_dep DESC;

SELECT id_seccion, sum(precio_total) as ventas_seccion
FROM tickets
GROUP by id_seccion
ORDER by ventas_seccion DESC;

SELECT nombre_producto, sum(cantidad) as cantidad_prod_vndido
FROM tickets
GROUP by nombre_producto
ORDER by cantidad_prod_vndido DESC
LIMIT 10;

SELECT nombre_producto, sum(precio_total) as ventas_productos 
FROM tickets 
GROUP by  nombre_producto
ORDER by ventas_productos DESC
LIMIT 10;

SELECT id_cliente, sum(precio_total) as ventas_cliente
FROM tickets
GROUP by id_cliente
ORDER by ventas_cliente DESC
LIMIT 20;

SELECT avg(venta_tot_cliente) as venta_media_cliente
FROM (
SELECT id_cliente, sum(precio_total) as venta_tot_cliente
FROM tickets
GROUP by id_cliente);

SELECT count(distinct id_pedido) as total_pedidos
FROM tickets;

SELECT avg(pedido_tot_promedio) as venta_promedio_pedido
FROM(
SELECT id_pedido, sum(precio_total) as pedido_tot_promedio
FROM tickets
GROUP by id_pedido );
