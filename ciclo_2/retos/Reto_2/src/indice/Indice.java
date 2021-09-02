/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package indice;
import java.util.Scanner;
import java.util.ArrayList;
/**
 *
 * @author dmcew
 */
public class Indice {
    protected static ArrayList<Pagina> listaPagina = new ArrayList<>();
    protected static String[] x;
    
    public static void procesarComandos() {
        if (x[1].equalsIgnoreCase("Apendice")) {
            Apendice pagina1 = new Apendice(x[2],x[3],x[4],x[5]);
            agregarPagina(pagina1);
         
        } else if(x[1].equalsIgnoreCase("Contenido")) {
            Contenido pagina2 = new Contenido(x[2],x[3],x[4],x[5]);
            agregarPagina(pagina2);
        }
    }
    public static void agregarPagina(Pagina comando) {
        listaPagina.add(comando);
    
    }
    public static void imprimirPaginas() {
        System.out.println("***Indice de Henry Plotter***");
        for (int pagina=0; pagina < listaPagina.size(); pagina++) {
            System.out.println(listaPagina.get(pagina));
        }   
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        boolean bandera = true;
        Scanner sc = new Scanner (System.in);
        while(bandera) {
            x = sc.nextLine().split("&");
            switch (x[0]) {
                case "1":
                    procesarComandos();
                    break;
                case "2":
                    imprimirPaginas();
                    break;
                case "3":
                    bandera = false;
            }
        }   
    }
}
