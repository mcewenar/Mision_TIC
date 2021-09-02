/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ascensocolina;

/**
 *
 * @author dmcew
 * <p> Un programa ejemplo de como implementar un Ascenso a la colina genérico. Ascenso a la </p> 
 * <p> colina es un método de optimización de un solo punto que va verificando si una variación de un punto mejora o no al que se tiene </p>
 */
public class AscensoColina {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        AscensoALaColina<String> opt = new AscensoALaColina<>(); 
        Funcion<String> f = new SoloA();
        Mutacion<String> m = new MutacionCadena();
        opt.aplicar(f, "A ver que pasa", m, 1000);
        
  
        AscensoALaColina<Double> opt1 = new AscensoALaColina<>();
        Funcion<Double> f1 = new Cuarta();
        // Funcion<Double> f = new Tercera();
        Mutacion<Double> m1 = new MutacionReal();
        opt1.aplicar(f1, 1.0, m1, 1000);
    }
}
