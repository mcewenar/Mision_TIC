/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;

/**
 *
 * @author dmcew
 * @param <T>
 */

public class Caja<T> {
    protected T obj;
    //Constructor:
    public Caja(T obj){ 
        this.obj = obj;
    }
    public T obtener(){ 
        return obj;
    }
    public String decorar() {
        String s = obj.toString();
        String linea = "*";
        for( int i=0; i<s.length(); i++)
            linea += "*";
        linea += "*";
        return linea + "\n*" + s + "*\n" + linea;
    }
}
    
    
    
    
    
    /*public String decorar( int n ) {
        String s = ""+n;
        System.out.println(s.length());
        String linea = "*"; //Va sumando
        for( int i=0; i<s.length(); i++) {
            linea += "*"; //Va sumando la longitud del parámetro
        }
        linea += "*"; //vuelve a sumar
        return linea + "\n*" + s + "*\n" + linea;
        
    }*/
    /*UNA FORMA DE HACER ESTE CÓDIGO GLOBAL PARA TODO TIPO DE DATOSS:
    De nuevo, el codigo es muy similar al anterior de decorar un int o un
    double, es decir, tenemos un patron de programaci ́on.
    Ahora podemos reducir estos tres m ́etodos a un solo m ́etodo
    aprovech ́andonos de las propiedades de herencia y amoldamiento de datos:
    los tipos b ́asicos int y double se amoldan a Integer y Double,
    respectivamente y estos heredan de Object:*/
    
// Eliminamos los otros metodos
//FORMA 1. Permite ingresar todo tipo de dato, pues es un patrón de progrmación:
    
    /*Se quiere que la clase Caja mantenga como atributo el objeto que se
        quiere decorar, por lo tanto, el metodo decorar ya no lo recibe como
        argumento, sino el constructor. Adicionalmente se quiere un metodo
        obtener que retorne el objeto que se decora:*/
    /*protected Object obj;
    public Caja(Object obj){ //Constructor 
        this.obj = obj; 
    }
    public Object obtener(){ 
        return obj;
    }
    public String decorar() { //Object, al ser una superclase de todas las demás clases, tiene todos los tipos de atributos y, por tanto, puede recibir cualquier dato de tipo primitivo o no primitivo
        */
        /*String s = obj.toString(); //Convierte a string
        System.out.println(s.length());
        String linea = "*";
        for( int i=0; i<s.length(); i++) {
            linea += "*";
        }
        linea += "*";
        return linea + "\n*" + s + "*\n" + linea + "\n";*/
        
        //Otra forma de volver genérica una clase usando operador diamante: