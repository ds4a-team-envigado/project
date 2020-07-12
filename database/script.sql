DROP DATABASE adr_db;
DROP USER adr_user;

'CREATE DATABASE adr_db
   TEMPLATE = template0
   ENCODING = 'UTF8'
   TABLESPACE = pg_default
   LC_COLLATE = 'Spanish_Colombia.1252'
   LC_CTYPE = 'Spanish_Colombia.1252';
'

CREATE DATABASE adr_db
   ENCODING = 'UTF8';
CREATE USER adr_user with login encrypted password '';
grant all privileges on database adr_db to adr_user;

DROP TABLE ap_sabanageneral;
DROP TABLE ap_predios;
DROP TABLE ap_activos;
DROP TABLE ds_asistencia_tecnica;
DROP TABLE eva_cultivos;
DROP TABLE adt_adecuaciontierras;
DROP TABLE pidar;

SET datestyle = 'ISO,DMY';

CREATE TABLE AP_SABANAGENERAL (
AP_Numero_BP   SMALLINT  PRIMARY KEY,
AP_Porcentaje_Avance   FLOAT,
AP_Beneficiarios_Definitivos   SMALLINT,
AP_Cant_Afrocolombiano   SMALLINT,
AP_Cant_Campesinos   SMALLINT,
AP_Cant_Mujeres   SMALLINT,
AP_Cant_Indigenas   SMALLINT,
AP_Cant_Hombre   SMALLINT,
AP_Cant_MujerRural   SMALLINT,
AP_Raizal   SMALLINT,
AP_Cant_Victimas   SMALLINT,
AP_Sector_Productivo   VARCHAR(255),
AP_ID_ADR   VARCHAR(6),
AP_CADENA_PRODUCTIVA_ADR   VARCHAR(60),
AP_Nombre_Proyecto   VARCHAR(600),
AP_Fecha_Resolucion   DATE,
AP_Departamento   VARCHAR(60)
);

CREATE TABLE ap_predios (
AP_Numero_BP   SMALLINT,
AP_ID_ADR   VARCHAR(6),
AP_CADENA_PRODUCTIVA_ADR   VARCHAR(60),
AP_Id_Predio   SMALLINT,
AP_Departamento   VARCHAR(60),
AP_Municipio   VARCHAR(60),
AP_Longitud_Predio_12   DECIMAL(18,15),
AP_Latitud_Predio_13   DECIMAL(18,15),
AP_Longitud_Predio_13   DECIMAL(18,15),
AP_Latitud_Predio_14   DECIMAL(18,15),
AP_Longitud_Predio_14   DECIMAL(18,15),
AP_Latitud_Predio_15   DECIMAL(18,15),
AP_Latitud_Predio_16   DECIMAL(18,15),
AP_Latitud_Predio_17   DECIMAL(18,15),
AP_Latitud_Predio_18   DECIMAL(18,15),
AP_Latitud_Predio_19   DECIMAL(18,15),
AP_Latitud_Predio_20   DECIMAL(18,15),
AP_Latitud_Predio_21   DECIMAL(18,15),
AP_Latitud_Predio_22   DECIMAL(18,15),
AP_Latitud_Predio_23   DECIMAL(18,15),
AP_Latitud_Predio_24   DECIMAL(18,15),
AP_Latitud_Predio_25   DECIMAL(18,15)
);

CREATE TABLE ap_activos (
AP_Numero_BP   SMALLINT,
AP_ID_ADR   VARCHAR(6),
AP_CADENA_PRODUCTIVA_ADR   VARCHAR(60),
AP_Horizonte   FLOAT,
AP_Activo_Productivo   VARCHAR(255),
AP_cantidad   FLOAT,
AP_Departamento   VARCHAR(60)
);

CREATE TABLE ds_asistencia_tecnica (
Id_Usuario   SMALLINT,
Sexo   VARCHAR(1),
Tipo_Poblacional   VARCHAR(60),
Discapacidad   VARCHAR(2),
Departamento   VARCHAR(60),
Municipio   VARCHAR(10),
Vereda   VARCHAR(255),
Predio   VARCHAR(255),
Cadena_Productiva   VARCHAR(255),
C1A1   SMALLINT,
C2A1   SMALLINT,
C3A1   SMALLINT,
C4A1   SMALLINT,
C5A1   SMALLINT,
C6A1   SMALLINT,
C7A1   SMALLINT,
C8A1   SMALLINT,
C9A1   SMALLINT,
C10A1   SMALLINT,
NA1   SMALLINT,
C1A2   SMALLINT,
C2A2   SMALLINT,
C3A2   SMALLINT,
C4A2   SMALLINT,
C5A2   SMALLINT,
C6A2   SMALLINT,
C7A2   SMALLINT,
NA2   SMALLINT,
C1A3   SMALLINT,
C2A3   SMALLINT,
C3A3   SMALLINT,
C4A3   SMALLINT,
C5A3   SMALLINT,
NA3   SMALLINT,
C1A4   SMALLINT,
C2A4   SMALLINT,
C3A4   SMALLINT,
C4A4   SMALLINT,
NA4   SMALLINT,
C1A5   SMALLINT,
C2A5   SMALLINT,
C3A5   SMALLINT,
C4A5   SMALLINT,
NA5   SMALLINT,
CLAS_GRAL   SMALLINT,
CADENA_PRODUCTIVA_ADR   VARCHAR(60),
ID_ADR   VARCHAR(6),
Tipo_proyecto   VARCHAR(60)
);   
   
CREATE TABLE eva_cultivos (
COD_DEP   SMALLINT,
DEPARTAMENTO   VARCHAR(60),
COD_MUN   INTEGER,
MUNICIPIO   VARCHAR(60),
GRUP_CULTIVO   VARCHAR(60),
SUBGRUP_CULTIVO   VARCHAR(60),
CULTIVO   VARCHAR(60),
DESAGREGACION_SIST_PRODUCTIVO   VARCHAR(60),
YEAR   VARCHAR(4),
PERIODO   VARCHAR(5),
AREA_SEMBR   FLOAT,
AREA_COSECH   FLOAT,
PRODUCCION   FLOAT,
RENDIMIENTO   FLOAT,
ESTADO_PRODUCCION   VARCHAR(60),
NOMBRE_CIENTI   VARCHAR(60),
CICLO_CULTIVO   VARCHAR(20),
CADENA_PRODUCTIVA_ADR   VARCHAR(60),
NIVEL   SMALLINT,
ID_ADR   VARCHAR(6)
);   
   
CREATE TABLE adt_adecuaciontierras (   
Numero_BP   SMALLINT,
Departamento   VARCHAR(60),
Municipio   VARCHAR(60),
Vereda   VARCHAR(1000),
Predio   VARCHAR(60),
Organizacion   VARCHAR(60),
Id_Distrito   SMALLINT,
Nombre_Distrito   VARCHAR(1000),
Escala_Distrito   VARCHAR(60),
Tipo_Distrito   VARCHAR(60),
Distrito_Operativo   SMALLINT,
Area_Bruta_HA   FLOAT,
Area_Neta_Inicial_HA   FLOAT,
Familias   SMALLINT,
Principales_Cultivos   VARCHAR(1000),
Condición_Juridica   VARCHAR(60),
Propiedad_Distrito   VARCHAR(60),
Estado_Propiedad   VARCHAR(60),
Recursos_Construccion   VARCHAR(60),
Administrador_Distrito   VARCHAR(60),
Nombre_Fuente_Hidrica   VARCHAR(255),
Subzona_Hidrica   VARCHAR(60),
Corporacion_Autonoma_Regional   VARCHAR(60),
Concesión_Aguas   SMALLINT,
Numer_Consecion   VARCHAR(60),
Caudal_Consecion   FLOAT,
Fecha_Consecion   DATE,
Vigencia_Consecion   DATE,
Observaciones   TEXT
);
   
   
CREATE TABLE pidar (   
BP   SMALLINT,
No_VP   SMALLINT,
Nombre_Proyecto   TEXT,
Departamento   VARCHAR(60),
Municipio   VARCHAR(255),
Total_beneficiarios   SMALLINT,
Hombres   SMALLINT,
Mujeres   SMALLINT,
Total_Victimas   SMALLINT,
Valor_cofinanciado_ADR   FLOAT,
Valor_encargo_fiduciario   FLOAT,
Valor_total_cofinanciación_ADR   FLOAT,
Valor_Contrapartida   FLOAT,
Valor_total_proyecto   FLOAT,
Hectareas   FLOAT,
Resolucion   SMALLINT,
Fecha_resolucion   TIMESTAMP,
Vigencia   VARCHAR(4),
Lineamiento_consejo_directivo   VARCHAR(60),
AP_ID_ADR   VARCHAR(6),
AP_CADENA_PRODUCTIVA_ADR   VARCHAR(60)
);


SET datestyle = 'ISO,DMY';
SET CLIENT_ENCODING TO 'UTF8';
\copy ap_sabanageneral FROM '../Datasets/AP_SABANAGENERAL2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')
\copy ap_activos FROM '../Datasets/AP_ACTIVOS2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')
\copy ap_predios FROM '../Datasets/AP_PREDIOS2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')
\copy ds_asistencia_tecnica FROM '../Datasets/DS_Asistencia_Tecnica2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')
\copy eva_cultivos FROM '../Datasets/EVA_cultivos_modificado2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')
\copy adt_adecuaciontierras FROM '../Datasets/ADT_adecuaciontierras2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')
\copy pidar FROM '../Datasets/pidar2.csv' with (format CSV, header true, delimiter ';', encoding 'utf8')


TRUNCATE ap_sabanageneral;
TRUNCATE ap_predios;
TRUNCATE ap_activos;
TRUNCATE ds_asistencia_tecnica;
TRUNCATE eva_cultivos
TRUNCATE adt_adecuaciontierras
TRUNCATE pidar


SELECT COUNT(*) FROM ap_sabanageneral;
SELECT COUNT(*) FROM ap_predios;
SELECT COUNT(*) FROM ap_activos;
SELECT COUNT(*) FROM ds_asistencia_tecnica;
SELECT COUNT(*) FROM eva_cultivos;
SELECT COUNT(*) FROM adt_adecuaciontierras;
SELECT COUNT(*) FROM pidar;

ap_sabanageneral
ap_predios
ap_activos
ds_asistencia_tecnica
eva_cultivos
adt_adecuaciontierras
pidar

SELECT p.departamento, p.bp, p.ap_cadena_productiva_adr cadena, p.nombre_proyecto, total_beneficiarios,
       valor_cofinanciado_adr, ap_beneficiarios_definitivos
FROM   pidar p
JOIN   ap_sabanageneral s ON p.bp = s.ap_numero_bp
LIMIT  2;

EXTRACT( YEAR FROM ap_fecha_resolución)

SELECT s.ap_departamento, s.ap_numero_bp, s.ap_cadena_productiva_adr cadena, p.nombre_proyecto, total_beneficiarios,
       valor_cofinanciado_adr, ap_beneficiarios_definitivos
FROM   pidar p
JOIN   ap_sabanageneral s ON p.bp = s.ap_numero_bp
JOIN   eva_cultivos e ON (s.ap_departamento = e.departamento
       AND s.ap_cadena_productiva_adr = e.id_adr)
LIMIT  2;