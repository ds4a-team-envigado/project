package com.ampd.pidar.project_profile;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class ProductiveChainProvider {

   private String [] productiveChains = {"AGUACATE", "AHUYAMA", "AJI", "ALGODON", "ARAZA", "ARRACACHA", "ARROZ",
            "ARVEJA", "ASAI", "BADEA", "BANANO", "BOROJO", "BREVO", "BROCOLI",
            "CACAO", "CAFE", "CAUCHO", "CAÑA AZUCARERA", "CAÑA PANELERA",
            "CEBOLLA DE BULBO", "CEBOLLA DE RAMA", "CHONTADURO", "CILANTRO",
            "CIMARRON", "COCO", "COLIFLOR", "CURUBA", "FIQUE", "FRESA", "FRIJOL",
            "GRANADILLA", "GUANABANA", "GUAYABA", "HABA", "HORTALIZAS VARIAS",
            "LECHUGA", "LIMON", "LULO", "MAIZ", "MAIZ FORRAJERO", "MALANGA",
            "MAMEY", "MANDARINA", "MANGO", "MANGOSTINO", "MARACUYA", "MELON",
            "MORA", "NARANJA", "PALMA DE ACEITE", "PAPA", "PAPAYA", "PATILLA",
            "PEPINO COHOMBRO", "PIMENTON", "PITAHAYA", "PIÑA", "PLATANO",
            "REMOLACHA", "REPOLLO", "TANGELO", "TOMATE", "TOMATE DE ARBOL", "TRIGO",
            "UCHUVA", "ULLUCO", "UVA", "YACON", "YUCA", "ZANAHORIA", "ÑAME"};


    public ArrayList<String> getProductiveChains() {
        ArrayList<String> chains = new ArrayList<String>();

        Arrays.sort(productiveChains);

        for (String chain : productiveChains) {
            chains.add(chain);
        }


        return chains;
    }


}
