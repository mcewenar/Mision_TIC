/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package artefacto;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


/**
 *
 * @author dmcew
 */
public class Artefacto {
    /**
     *@return 
     * @param listaArtefactos
     */
    public static ArrayList<String> obtenerArtefactos(List<String> listaArtefactos) {
        ArrayList<String> NuevaLista = new ArrayList<>();
        for(String cadena: listaArtefactos) { 
            if(!NuevaLista.contains(cadena))
                NuevaLista.add(cadena);
        }
        return NuevaLista;
    }
    public static ArrayList<Integer> obtenerArtefactosFaltantes(List<Integer> listaPosiciones, List<String> faltantes, String categoria) {
        ArrayList<Integer> listaFinal = new ArrayList<>();
        for (Integer c : listaPosiciones ) {
            if (faltantes.get(c).equals(categoria))
                listaFinal.add(c);   
        }
        return listaFinal;       
    }
    public static ArrayList<String> obtenerFaltantes(List<String> listaPulgasMagicas, List<String> listaArtefactos) {
        ArrayList<String> listaInteres = new ArrayList<>();
        for (String cadena:listaPulgasMagicas) {
            if(!listaArtefactos.contains(cadena))
                listaInteres.add(cadena);  
        }
        return listaInteres;
    }
    public static String obtenerArtefactosIntercambiables(List<String> listaPulgasMagicas, List<String> listaArtefactos) {
        int cont1=0, cont2 = 0;
        for (String cadena1:listaPulgasMagicas) {
            if(!listaArtefactos.contains(cadena1))
                cont1+=1; 
        }
        for(String cadena2:listaArtefactos) {
            if(!listaPulgasMagicas.contains(cadena2))
                cont2+=1;  
        }
        int numero = cont1 < cont2 ? cont1 : cont2;
        return Integer.toString(numero);
    }
    public static void main(String[] args) {
        //Método 1:
        List<String> listas = Arrays.asList("CARPA MÁGICA", "TENNIS VOLADORES", "LIMPIAGAFAS", "TENNIS VOLADORES", "MAPAS", "BRILLAVARITAS", "LIMPIAGAFAS");
        System.out.println(obtenerArtefactos(listas));
        
        //Método 2:
        List<Integer> listaPosiciones = Arrays.asList(0, 1, 4, 5, 6);
        List<String> faltantes = Arrays.asList("BRILLAVARITAS", "TENNIS VOLADORES", "LIMPIAGAFAS", "BRILLAVARITAS", "MAPAS", "BRILLAVARITAS", "LIMPIAGAFAS");
        String categoria = "BRILLAVARITAS";
        System.out.println(obtenerArtefactosFaltantes(listaPosiciones,faltantes,categoria));
        
        //Método 3:
        List<String> listaPosiciones1 = Arrays.asList("BRILLAVARITAS", "BALINERO EXPRESS", "TENNIS VOLADORES", "LIMPIAGAFAS", "MAPAS", "CRISTALES DE PANELA");
        List<String> faltantes1 = Arrays.asList("GARRA DE CHIGUIRO", "BALINERO EXPRESS", "CRISTALES DE PANELA", "BRILLAVARITAS", "DETECTOR DE PORTALES");
        System.out.println(obtenerFaltantes(listaPosiciones1,faltantes1));
        
        
        //Método 4:
        List<String> listaPulgasMagicas = Arrays.asList("SNITCH EXPLORADORA", "BALINERO EXPRESS", "TENNIS VOLADORES", "LIMPIAGAFAS", "MAPAS", "CRISTALES DE PANELA");
        List<String> listaArtefactos = Arrays.asList("GARRA DE CHIGUIRO", "BALINERO EXPRESS", "CRISTALES DE PANELA", "BRILLAVARITAS", "DETECTOR DE PORTALES");
        System.out.println(obtenerArtefactosIntercambiables(listaPulgasMagicas,listaArtefactos));
        
     }    
}
