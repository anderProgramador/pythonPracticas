/*El conjunto de todos los clientes que tienen cuenta en el banco*/
select nombre_cliente
from impositor

/*El conjunto de los clientes que tienen concedido un prestamo por el banco*/
select nombre_cliente
from prestatario

/*Determinar todos los clientes del banco que tienen un prestamo, una cuenta o las dos cosas en el banco*/
select nombre_cliente
from impositor
union
select nombre_cliente
from prestatario

/*Si se desea conservar todos los duplicados*/
select nombre_cliente
from impositor
union all
select nombre_cliente
from prestatario

/*Encontrar todos los clientes que tienen tanto un prestamo como una cuenta en el banco*/
select distinct nombre_cliente
from impositor
intersect
select distinct nombre_cliente
from prestatario

/*Si se desea conservar todos los duplicados*/
select nombre_cliente
from impositor
intersect all
select nombre_cliente
from prestatario

/*Determinar todos los clientes que tienen cuenta en el banco pero no tienen ningún prestamo concedido*/
select distinct nombre_cliente
from impositor
except
select nombre_cliente
from prestatario

/*Si se desea conservar todos los duplicados*/
select distinct nombre_cliente
from impositor
except all
select nombre_cliente
from prestatario

/*Determinar el saldo medio de las cuentas de la sucursal de Navacerrada.*/
select avg (saldo)
from cuenta
where nombre_sucursal = 'Navacerrada'

/*Determinar el saldo medio de las cuentas de cada sucursal*/
select nombre_sucursal, avg (saldo)
from cuenta
group by nombre_sucursal

/*Determinar el saldo medio de todas las cuentas*/
select avg (saldo)
from cuenta

/*Determinar el numero de tuplas de la relación cliente*/
select count (*)
from cliente

/*Determinar el numero de impositores de cada sucursal*/
select nombre_sucursal, count (distinct nombre_cliente)
from impositor, cuenta
where impositor.numero_cuenta = cuenta.numero_cuenta
group by nombre_sucursal

/*Estemos interesados en las sucursales en las que el saldo medio de las cuentas sea superior a 1.200.*/
select nombre_sucursal, avg (saldo)
from cuenta
group by nombre_sucursal
having avg (saldo) > 1200

/*Determinar el saldo medio de cada cliente que vive en Peguerinos y tiene, como mínimo, tres cuentas*/
select impositor.nombre_cliente, avg (saldo)
  from impositor, cuenta, cliente
 where impositor.numero_cuenta = cuenta.numero_cuenta 
   and impositor.nombre_cliente = cliente.nombre_cliente 
   and ciudad_cliente = 'Peguerinos'
group by impositor.nombre_cliente
having count (distinct impositor.numero_cuenta) >= 3

/*Determinar todos los numeros de prestamo que aparecen en la relación prestamo con valores nulos para importe*/
select numero_prestamo
from prestamo
where importe is null

/*calcula el total de los importes de todos los prestamos*/
select sum (importe)
from prestamo

/*Determinar todos los clientes del banco que tienen un prestamo, una cuenta o las dos cosas en el banco*/
select distinct nombre_cliente
from prestatario
where nombre_cliente in (select nombre_cliente
from impositor)

/*Determinar todos los clientes que tienen tanto una cuenta como un prestamo en la sucursal de Navacerrada*/
  select distinct nombre_cliente
    from prestatario, prestamo
   where prestatario.numero_prestamo = prestamo.numero_prestamo 
     and nombre_sucursal = 'Navacerrada' 
	 and (nombre_sucursal, nombre_cliente) in (select nombre_sucursal, nombre_cliente
                                                 from impositor, cuenta
                                                where impositor.numero_cuenta = cuenta.numero_cuenta)

/*Encontrar todos los clientes que tienen concedido un prestamo en el banco pero no tienen abierta cuenta*/
select distinct nombre_cliente
from prestatario
where nombre_cliente not in (select nombre_cliente
from impositor)

/*selecciona los nombres de los clientes que tienen concedido un prestamo en el banco y cuyos nombres no son ni Santos ni Gómez*/
select distinct nombre_cliente
from prestatario
where nombre_cliente not in ('Santos', 'Gómez')

/*Determinar el nombre de todas las sucursales que poseen activos mayores que, al menos, una sucursal de Arganzuela*/
select distinct T.nombre_sucursal
from sucursal as T, sucursal as S
where T.activos > S.activos and S.ciudad_sucursal = 'Arganzuela'

select nombre_sucursal
  from sucursal
 where activos > some (select activos
                         from sucursal
                        where ciudad_sucursal = 'Arganzuela')

/*Determinar el nombre de todas las sucursales que tienen activos superiores al de todas las sucursales de Arganzuela*/
select nombre_sucursal, activos
from sucursal
where activos > all (select activos
from sucursal
where ciudad_sucursal = 'Arganzuela')

/*Determinar la sucursal que tiene el saldo medio máximo*/
select nombre_sucursal
from cuenta
group by nombre_sucursal
having avg (saldo) >= all (select avg (saldo)
from cuenta
group by nombre_sucursal)

/*Determinar todos los clientes que tienen tanto una cuenta abierta como un prestamo concedido en el banco”*/
select nombre_cliente
from prestatario
where exists (select *
from impositor
where impositor.nombre_cliente = prestatario.nombre_cliente)

/*Determinar todos los clientes que tienen una cuenta en todas las sucursales de Arganzuela*/
select distinct S.nombre_cliente
from impositor as S
where not exists ((select nombre_sucursal
from sucursal
where ciudad_sucursal = 'Arganzuela')
except
(select R.nombre_sucursal
from impositor as T, cuenta as R
where T.numero_cuenta = R.numero_cuenta and
S.nombre_cliente = T.nombre_cliente))

/*Determinar todos los clientes que tienen, a lo sumo, una cuenta en la sucursal de Navacerrada*/
select T.nombre_cliente
  from impositor as T
 where unique (select R.nombre_cliente
                 from cuenta, impositor as R
                where T.nombre_cliente = R.nombre_cliente 
				  and R.numero_cuenta = cuenta.numero_cuenta 
				  and cuenta.nombre_sucursal = 'Navacerrada')

/*Determinar todos los clientes que tienen, al menos, dos cuentas en la sucursal de Navacerrada*/
select distinct T.nombre_cliente
from impositor T
where not unique (select R.nombre_cliente
from cuenta, impositor as R
where T.nombre_cliente = R.nombre_cliente and
R.numero_cuenta = cuenta.numero_cuenta and
cuenta.nombre_sucursal = 'Navacerrada')

/*Determinar el saldo medio de las cuentas de las sucursales en las que el saldo medio de las cuentas sea superior a 1.200 e*/
select nombre_sucursal, saldo_medio
  from (select nombre_sucursal, avg (saldo)
          from cuenta
      group by nombre_sucursal) as media_sucursal (nombre_sucursal, saldo_medio)
 where saldo_medio > 1200

/*Se desea determinar el saldo total máximo de las sucursales*/
select max(saldo_total)
 from (select nombre_sucursal, sum(saldo)
         from cuenta
     group by nombre_sucursal) as total_sucursal (nombre_sucursal, saldo_total)

/*selecciona cuentas con el saldo máximo; si hay muchas cuentas con el mismo saldo máximo, se seleccionan todas*/
with saldo_maximo (valor) as ( select max(saldo)
                                 from cuenta )
select numero_cuenta
from cuenta, saldo_maximo
where cuenta.saldo = saldo_maximo.valor

/*determinar todas las sucursales donde el depósito total de las cuentas es mayor que la media de los depósitos totales de las cuentas de todas las sucursales*/
with total_sucursales (nombre_sucursal, valor) as (select nombre_sucursal, sum(saldo)
                                                     from cuenta
                                                 group by nombre_sucursal )
, media_total_sucursales(valor) as ( select avg(valor)
                                       from total_sucursales )
select nombre_sucursal
  from total_sucursales, media_total_sucursales
 where total_sucursales.valor >= media_total_sucursales.valor

/*********************************************************************************************************
9. VISTAS
*********************************************************************************************************/
/*Considérese una persona que necesita saber el numero de prestamo y el nombre de la sucursal de un cliente, pero no necesita ver el importe de ese prestamo.*/
select nombre_cliente, prestatario.numero_prestamo, nombre_sucursal
from prestatario, prestamo
where prestatario.numero_prestamo = prestamo.numero_prestamo

/*ver una relación que consista en los clientes que tienen o bien cuenta abierta o bien prestamo concedido en el banco y las sucursales con las que trabajan*/
(select nombre_sucursal, nombre_cliente
from impositor, cuenta
where impositor.numero_cuenta = cuenta.numero_cuenta)
union
(select nombre_sucursal, nombre_cliente
from prestatario, prestamo
where prestatario.numero_prestamo = prestamo.numero_prestamo)

/*considérese la vista consistente en las sucursales y sus clientes. Supóngase que se desea que esta vista se denomine todos_los_clientes*/
create view todos_los_clientes as
(select nombre_sucursal, nombre_cliente
from impositor, cuenta
where impositor.numero_cuenta = cuenta.numero_cuenta)
union
(select nombre_sucursal, nombre_cliente
from prestatario, prestamo
where prestatario.numero_prestamo = prestamo.numero_prestamo)

/*Utilizando la vista todos_los_clientes se puede determinar el nombre de todos los clientes de la sucursal de Navacerrada*/
select nombre_cliente
from todos_los_clientes
where nombre_sucursal = 'Navacerrada'

/*Los nombres de los atributos de las vistas pueden especificarse de manera explícita de la manera siguiente:*/
create view total_prestamos_sucursal(nombre_sucursal, total_prestamos) as
select nombre_sucursal, sum(importe)
from prestamo
group by nombre_sucursal

/*definir la vista cliente_navacerrada de la manera siguiente:*/
create view cliente_navacerrada as
select nombre_cliente
from todos_los_clientes
where nombre_sucursal = 'Navacerrada'

/*Como ilustración de la expansión de vistas considérese la expresión siguiente:*/
select *
from cliente_navacerrada
where nombre_cliente = 'López'

/*El procedimiento de expansión de vistas produce inicialmente*/
select *
  from (select nombre_cliente
          from todos_los_clientes
         where nombre_sucursal = 'Navacerrada') as tb
 where nombre_cliente = 'López'

/*luego produce*/
select *
 from (select tb.nombre_cliente
         from ((select nombre_sucursal, nombre_cliente
                  from impositor, cuenta
                 where impositor.numero_cuenta = cuenta.numero_cuenta)
                 union
               (select nombre_sucursal, nombre_cliente
                  from prestatario, prestamo
                 where prestatario.numero_prestamo = prestamo.numero_prestamo)) as tb
         where tb.nombre_sucursal = 'Navacerrada') as tb1
 where nombre_cliente = 'López'

/*Borrar todas las tuplas de cuentas de la sucursal de Navacerrada.*/
delete from cuenta
where nombre_sucursal = 'Navacerrada'

/*Borrar todos los prestamos con importe comprendido entre 1.300 e y 1.500 e.*/
delete from prestamo
where importe between 1300 and 1500

/*Borrar todas las tuplas de cuenta de todas las sucursales de Arganzuela.*/
delete from cuenta
where nombre_sucursal in (select nombre_sucursal
from sucursal
where ciudad_sucursal = 'Arganzuela')

/*Se desea borrar los registros de todas las cuentas con saldos inferiores a la media del banco*/
delete from cuenta
where saldo < (select avg (saldo)
from cuenta)

/*********************************************************************************************************
10.2. Inserción
*********************************************************************************************************/
/*se desea insertar el hecho de que hay una cuenta C-9732 en la sucursal de Navacerrada y que tiene un saldo de 1.200 e*/
insert into cuenta
values ('C-9732', 'Navacerrada', 1200)

/*Las siguientes instrucciones insert tienen una función idéntica a la anterior:*/
insert into cuenta (numero_cuenta, nombre_sucursal, saldo)
values ('C-9732', 'Navacerrada', 1200)
insert into cuenta (nombre_sucursal, numero_cuenta, saldo)
values ('Navacerrada', 'C-9732', 1200)

/*Supóngase que se les desea ofrecer, como regalo, a todos los clientes titulares de prestamos de la sucursal de Navacerrada una cuenta de ahorro con 200 e por cada prestamo que tengan concedido*/
insert into cuenta
select numero_prestamo, nombre_sucursal, 200
from prestamo
where nombre_sucursal = 'Navacerrada'

/*También hay que añadir tuplas a la relación impositor*/
insert into impositor
select nombre_cliente, prestamo.numero_prestamo
from prestatario, prestamo
where prestatario.numero_prestamo = prestamo.numero_prestamo and
nombre_sucursal = 'Navacerrada'

/*********************************************************************************************************
10.3. Actualizaciones
*********************************************************************************************************/
/*Supóngase que se va a realizar el pago anual de intereses y que hay que incrementar todos los saldos en un 5 por ciento*/
update cuenta
set saldo = saldo * 1.05

/*Si sólo se paga el interés a las cuentas con un saldo de 1.000 e o superior*/
update cuenta
set saldo = saldo * 1.05
where saldo >= 1000

/*Pagar un interés del 5 por ciento a las cuentas cuyo saldo sea mayor que la media*/
update cuenta
set saldo = saldo * 1.05
where saldo > (select avg (saldo)
from cuenta)

/*Supóngase que las cuentas con saldos superiores a 10.000 e reciben un 6 por ciento de interés, mientras que las demás reciben un 5 por ciento.*/
update cuenta
set saldo = saldo * 1.06
where saldo > 10000

update cuenta
set saldo = saldo * 1.05
where saldo <= 10000

/*SQL ofrece un constructor case que se puede utilizar para llevar a cabo las dos instrucciones de actualización
anteriores en una única instrucción update, evitando el problema del orden de actualización.*/
update cuenta
set saldo = case
when saldo <= 10000 then saldo * 1.05
else saldo * 1.06
end

/*********************************************************************************************************
10.4. Actualización de Vistas
*********************************************************************************************************/
/*considérese un empleado que necesita ver todos los datos de prestamos de
la relación prestamo, excepto importe_prestamo. Sea sucursal_prestamo la vista ofrecida al empleado. Esta
vista se define como*/
create view sucursal_prestamo as
select numero_prestamo, nombre_sucursal
from prestamo

/*Otro problema con la modificación de la base de datos mediante vistas surge con vistas como*/
create view info_prestamo as
select nombre_cliente, importe
from prestatario, prestamo
where prestatario.numero_prestamo = prestamo.numero_prestamo

/*Supóngase que se define la vista cuenta_centro de la manera siguiente:*/
create view cuenta_centro as
select numero_cuenta, nombre_sucursal, saldo
from cuenta
where nombre_sucursal = 'Centro'

/*********************************************************************************************************
11. REUNIÓN DE RELACIONES
*********************************************************************************************************/
/*ejemplo sencillo de reunión interna*/
select prestamo.*, prestatario.* 
from prestamo inner join prestatario on prestamo.numero_prestamo = prestatario.numero_prestamo

/*La relación resultado de la reunión y sus atributos se renombra usando una cláusula as*/
select pp.* 
from (prestamo inner join prestatario on prestamo.numero_prestamo = prestatario.numero_prestamo) 
as pp(numero_prestamo, sucursal, importe, cliente, numero_prestamo_cliente)

/*A continuación se toma en consideración un ejemplo de la operación reunión externa por la izquierda (left outer-join)*/
select prestamo.*, prestatario.* 
from prestamo left outer join prestatario on prestamo.numero_prestamo = prestatario.numero_prestamo

/*ejemplo de la operación reunión natural (natural join).*/
select * from prestamo natural inner join prestatario

/*ejemplo de combinación de la condición de reunión natural con el tipo de reunión externa por la derecha:*/
select * from  prestamo natural right outer join prestatario

/*Determinar todos los clientes que tienen una cuenta abierta pero no tienen ningún prestamo concedido en el banco*/
select i_NC
from (impositor left outer join prestatario
on impositor.nombre_cliente = prestatario.nombre_cliente)
as db1 (i_NC, numero_cuenta, p_NC, numero_prestamo)
where p_NC is null

/*Determinar todos los clientes que tienen una cuenta abierta o un prestamo concedido en el banco (pero no las dos cosas)*/
select nombre_cliente
from (impositor natural full outer join prestatario)
where numero_cuenta is null or numero_prestamo is null

/**/

/**/

/**/

/**/

/**/







