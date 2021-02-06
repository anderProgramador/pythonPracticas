/*********************************************************************************************************
SQL AVANZADO
*********************************************************************************************************/

/*********************************************************************************************************
2. TIPOS DEFINIDOS POR LOS USUARIOS
*********************************************************************************************************/
/*Tipos de datos definidos por los usuarios Euros y Libras como números decimales con un total de doce cifras, dos de las cuales se hallan tras la coma decimal.*/
CREATE TYPE [dbo].[Euros] FROM [numeric](12, 2) NULL

CREATE TYPE [dbo].[Libras] FROM [numeric](12, 2) NULL

/*Declarar la tabla cuenta como:*/
create table cuenta_alt
(número_cuenta char(10),
nombre_sucursal char(15),
saldo Euros)

/**/
create domain EEuros from numeric(12,2)


/**/

/**/







