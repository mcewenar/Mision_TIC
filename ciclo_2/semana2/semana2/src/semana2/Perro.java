/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;

/**
 *
 * @author dmcew
 */
public class Perro implements Animal { //Hereda una plantilla. Una clase puede heredar múltiples interfaces, pero no múltiples clases
    // Atributos
    public String nombre;
    private final int edad;
    protected String colorOjos;
    // Constructor
    public Perro(String nombre, int edad, String colorOjos) { //Se tiene que llamar igual que la clase
        this.nombre = nombre;
        this.edad = edad;
        this.colorOjos = colorOjos;
    }
    @Override
    public void sonidoAnimal() { // Cuerpo de sonidoAnimal()
        System.out.println("El perro hace: wow wow");
    }
    @Override
    public void dormir() { // Cuerpo de dormir()
        System.out.println("Zzz");
        
    }
        //La palabra reservada this, hace referencia al objeto que esta en
        //construccion (en otros metodos sera el objeto que esta ejecutando la
        //accion).
        /*El constructor de una clase es una función especial de cada clase que
        permite inicializar los atributos con algun valor en específico al momento
        de crear el objeto. Nos permite definir qué valores tomarán los atributos
        inicialmente al crear nuestro objeto.
        Posee el mismo nombre que la clase, y recibe como entrada los valores que
        inicializarán el objeto.*/
        
        /*Las palabras reservadas public, protected y private hacen referencia
        al nivel de acceso a los métodos y atributos de un objeto (quien puede
        comunicarse con el objeto por medio del atributo o método). En este caso,
        public indica que cualquier otro objeto puede acceder al (comunicarse
        por medio del) atributo o método etiquetado público.*/
    // Metodos
    public void ladrar() {
        System.out.println("Guau guau");
    }
    private void saludar() {
        System.out.println("Hola, mi nombre es " + nombre);
    }
    
    //Objeto instanciado interactuando con otro objeto en el parámetro
    /*Se pretende crear un método que compare las edades de dos perros. Dicho
    método comparará la edad de un perro en específico que invoca, contra la
    edad de otro perro cualquiera.*/
    public void quienEsMayor(Perro otroPerro) {
        if (this.edad > otroPerro.edad) {
            System.out.println("Soy mayor que "+otroPerro.nombre);
        } else if (this.edad == otroPerro.edad) {
            System.out.println("Tenemos la misma edad");
        } else {
            System.out.println(otroPerro.nombre+" es mayor que yo, "+this.nombre);
        }        
    }
    public void saludarOtroPerro(Perro otroPerro) {
        System.out.println("Hola " + otroPerro.nombre + ", yo soy " +this.nombre);
    }
}


/*Es importante mencionar que una Clase y un Objeto no se refieren a lo
mismo. Una clase es la plantilla (o estructura) que se define para todos;
mientras que un objeto es usar dicha plantilla para instanciar un ente en
particular (que tendr ́a caracter ́ısticas particulares para ese objeto).*/