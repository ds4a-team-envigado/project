# flake8: noqa

# In[]:
# Controls for webapp

#Departamentos
COUNTIES = {
    "001": "Albany",
    "003": "Allegany",
    "005": "Bronx",
    "007": "Broome",
    "009": "Cattaraugus",
    "011": "Cayuga",
    "013": "Chautauqua",
    "015": "Chemung",
    "017": "Chenango",
    "019": "Clinton",
    "021": "Columbia",
    "023": "Cortland",
    "025": "Delaware",
    "027": "Dutchess",
    "029": "Erie",
    "031": "Essex",
    "033": "Franklin",
    "035": "Fulton",
    "037": "Genesee",
    "039": "Greene",
    "041": "Hamilton",
    "043": "Herkimer",
    "045": "Jefferson",
    "047": "Kings",
    "049": "Lewis",
    "051": "Livingston",
    "053": "Madison",
    "055": "Monroe",
    "057": "Montgomery",
    "059": "Nassau",
    "061": "New York",
    "063": "Niagara",
    "065": "Oneida",
    "067": "Onondaga",
    "069": "Ontario",
    "071": "Orange",
    "073": "Orleans",
    "075": "Oswego",
    "077": "Otsego",
    "079": "Putnam",
    "081": "Queens",
    "083": "Rensselaer",
    "085": "Richmond",
    "087": "Rockland",
    "089": "St. Lawrence",
    "091": "Saratoga",
    "093": "Schenectady",
    "095": "Schoharie",
    "097": "Schuyler",
    "099": "Seneca",
    "101": "Steuben",
    "103": "Suffolk",
    "105": "Sullivan",
    "107": "Tioga",
    "109": "Tompkins",
    "111": "Ulster",
    "113": "Warren",
    "115": "Washington",
    "117": "Wayne",
    "119": "Westchester",
    "121": "Wyoming",
    "123": "Yates",
}

#Linea productiva
WELL_STATUSES = {
    'ORDENAMIENTO DE LA PRODUCCIÓN':'ORDENAMIENTO DE LA PRODUCCIÓN',
    "ASISTENCIA TÉCNICA Y EXTENSIÓN":"ASISTENCIA TÉCNICA Y EXTENSIÓN",
    'ADECUACIÓN DE TIERRAS':'ADECUACIÓN DE TIERRAS',
    'AGRICULTURA POR CONTRATO':'AGRICULTURA POR CONTRATO',
    'TRANSVERSAL':'TRANSVERSAL',
}

#tipo de proyecto o cadena productiva
WELL_TYPES = {
    'ANTIOQUIA':'ANTIOQUIA',
    'ARAUCA':'ARAUCA',
    'ATLANTICO':'ATLANTICO',
    'BOLIVAR':'BOLIVAR',
    'BOLÍVAR':'BOLÍVAR',
    'BOYACA':'BOYACA',
    'CALDAS':'CALDAS',
    'CAUCA':'CAUCA',
    'CESAR':'CESAR',
    'CHOCO':'CHOCO',
    'CORDOBA':'CORDOBA',
    'CUNDINAMARCA':'CUNDINAMARCA',
    'GUAINIA':'GUAINIA',
    'HUILA':'HUILA',
    'LA_GUAJIRA':'LA_GUAJIRA',
    'MAGDALENA':'MAGDALENA',
    'META':'META',
    'NARIÃ‘O':'NARIÃ‘O',
    'NORTE DE SANTANDER':'NORTE DE SANTANDER',
    'QUINDIO':'QUINDIO',
    'SANTANDER':'SANTANDER',
    'TOLIMA':'TOLIMA',
    'VALLE DEL CAUCA':'VALLE DEL CAUCA',
    'VAUPES':'VAUPES',
    'VICHADA':'VICHADA'
}

LINEA_PROD_STATUSES = dict(MA='MAIZ', 
PL='PLATANO', 
GA='GANADERIA', 
YU='YUCA', 
AR='ARROZ', 
CA='CACAO',
AC='ACUICULTURA',
NI='NISPERO',
AH='AGRICOLA',
CO='COMERCIALIZACION',
CI='CITRICOS',
AG='AGROPECUARIO',
MN='MANGO',
PA1='PAPAYA',
AP='APICULTURA',
AV='AVICULTURA',
HO='HORTOFRUTICOLA', 
LA='LACTEO', 
CA1='CAFE', 
AC1='ACHIRA',
FR='FRESA',
GR='GRANADILLA', 
TO='TOMATE', 
ARV='ARVEJA',
PA='PAPA', 
AGU='AGUACATE',
COC='COCO',
PEC='PECUARIO', 
FRIJ='FRIJOL', 
CEB='CEBOLLA', 
MOR='MORA',
PLAN='PLANTAS AROMATICAS, MEDICINALES, ESPECIAS Y SEMILLAS',
CEBA='CEBADA',
TRIG='TRIGO', 
TOMAT='TOMATE DE ARBOL',
UCHU='UCHUVA',
GULP='GULUPA', 
FIQU='FIQUE',
LUL='LULO',)


WELL_COLORS = dict(
    GD="#FFEDA0",
    GE="#FA9FB5",
    GW="#A1D99B",
    IG="#67BD65",
    OD="#BFD3E6",
    OE="#B3DE69",
    OW="#FDBF6F",
    ST="#FC9272",
    BR="#D0D1E6",
    MB="#ABD9E9",
    IW="#3690C0",
    LP="#F87A72",
    MS="#CA6BCC",
    Confidential="#DD3497",
    DH="#4EB3D3",
    DS="#FFFF33",
    DW="#FB9A99",
    MM="#A6D853",
    NL="#D4B9DA",
    OB="#AEB0B8",
    SG="#CCCCCC",
    TH="#EAE5D9",
    UN="#C29A84",
)