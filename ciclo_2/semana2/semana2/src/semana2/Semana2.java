/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;
import java.util.Scanner;

/**
 *
 * @author dmcew
 */
public class Semana2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingresa una cadena: ");
        String text = sc.nextLine();
        StringInverse cadenaInversa = new StringInverse(text);
        System.out.println(cadenaInversa.reverse());
        
        //Ejemplo Do-whiles:
        
        int op;
        do {
            String menu = "Menú 1.\n"
                    + "Menú 2\n"
                    + "Menú 3\n"
                    + "Menú 4";
            System.out.println(menu);
            System.out.println("Ingresa un número: ");
            op = Integer.parseInt(sc.nextLine());
        } while (op != 4);
        //Ejemplo 2:
        int i = 0;
        do {
            System.out.println(i);
            i++;
        } while (i < 5);
        
        
        
        
        
        
        
        Pareja<Integer,String> pareja = new Pareja<>(20,"Pedro Páramo");
        System.out.println(pareja);
        Integer x = pareja.clave() + 10;
        System.out.println(x);
        System.out.println(pareja.valor().charAt(2));
        
        //Patrones 1:
        Caja caja1 = new Caja("Pedro Paramo");
        Caja caja2 = new Caja(3.43);
        Caja caja3 = new Caja(45);
        //String s = caja.decorar(10);
        //System.out.println( caja.decorar(10) );
        //System.out.println( caja.decorar("Pedro Páramo") );
        //System.out.println( caja.decorar(10.34) );
        //System.out.println(s); //No sirve porque el método no recibe argumentos, en cambio, 
        //estos están inicializados en el constructor. 
        
        System.out.println( caja1.decorar() ); //No reciben argumentos, porque el constructor los tiene
        System.out.println( caja1.obtener() );
        System.out.println( caja2.decorar() ); 
        System.out.println( caja2.obtener() );
        System.out.println( caja3.decorar() ); 
        System.out.println( caja3.obtener() );
        
        /*En el ejemplo anterior, aunque se sabe que lo que se guardo es una cadena
        de caracteres, el metodo obtener no puede decirnos que es una cadena
        pues simplemente sabe que es un Object, perdió ese conocimiento, por
        eso es que el siguiente codigo genera un error de compilacion:*/
        Caja caja4 = new Caja("Pedro Páramo");
        caja4.decorar();
        //ERROR:
        //char c = caja4.obtener().charAt(2);
        //Forma de arreglarlo. Amoldarlo al objeto requerido:
        //char c = ((String)caja4.obtener()).charAt(2); //Primero se tipea a String y luego obtiene la posición 2 del string para asignarlo a la variable c
        //System.out.println(c);
        //Genericidad:
        //Para definir una clase o interfaz genérica se utiliza el operador diamante <>.
        
        //Otra forma, con genericidad:
        Caja<String> caja = new Caja<>("Pedro Paramo");
        System.out.println( caja.decorar() );
        char c = caja.obtener().charAt(2);
        System.out.println(c);
        Caja<Double> caja5 = new Caja<>(20.34);
        System.out.println( caja2.decorar() );
        double y = caja5.obtener() + 20.0;
        System.out.println(y);
        
        
        
        
        //2
        /*Automovil Chevrolet = new Automovil(5,4);
        Chevrolet.posicion(10);
        Chevrolet.pintar(10);*/
        
    }
}
        
        // TODO code application logic here
        //PRIMER OBJETO:
       /*Perro Annie = new Perro("Annie",10,"Azul");
        System.out.println(Annie.nombre);
        Annie.ladrar(); //Porque no retorna el método ladrar. No hace falta SOUT
        //Annie.saludar(); NO SIRVE PORQUE EL MÉTODO ES PRIVADO
        
        //Objeto 2:
        Perro Blue = new Perro("Blue",6,"Pardo");
        Blue.ladrar();
        System.out.println(Blue.nombre);
        System.out.println(Blue.colorOjos);*/
        //System.out.println(Blue.edad); NO SE PUEDE ACCEDER PORQUE ES PRIVADO
        
        //Blue.saludar(); PORQUE ES PRIVADO
        /*Los objetos en un programa se comunican entre ellos para resolver un
        problema. La forma de comunicarse con un objeto es usar el nombre que
        tiene el objeto en el programa, seguido de un punto (.) y el mensaje que
        queremos enviarle:*/
        
        /*Recordemos, depende del nivel de acceso del atributo o método:
        
            public: Cualquier otro objeto puede acceder al atributo o método.
            protected: Solo objetos de la misma clase, subclase, o del mismo
            paquete (package) pueden acceder al atributo o metodo.
            private: Solo objetos dentro de la misma clase pueden acceder al atributo o
        |   método.Por fuera, instanciando, genera error*/
        //Interactuar con 2 objetos: IMPORTANTE:
        /*Perro miPerro1 = new Perro("Toby",5, "Azul");
        Perro miPerro2 = new Perro( "Vainilla",7 ,"Negro");
        Perro miPerro3 = new Perro("Bony",15 ,"Amarillo");
        miPerro1.quienEsMayor(miPerro2);
        miPerro1.saludarOtroPerro(miPerro2);
        */
        //Ejercicio 1:
        /*Persona David = new Persona("David","H",16,93,1.80);
        System.out.println(David.calcularIMC());
        System.out.println(David.toString());
        System.out.println(David.esMayorDeEdad());*/
        
        
        
