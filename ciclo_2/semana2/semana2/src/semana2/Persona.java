/*
Crear la clase Persona que tenga como atributos Nombre, Edad,
Genero (H hombre, M mujer), peso y altura. El constructor debe
recibir todos los parametros para su inicializacion.
La clase debe tener los siguientes metodos:
calcularIMC(): Calcular ́a y retornar ́a el Indice de Masa Corporal del
objeto.
esMayorDeEdad(): Devolver ́a true si es mayor de edad, false en
caso contrario.
toString(): Devolverá toda la informacion del objeto en un String.
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;

/**
 *
 * @author dmcew
 */
public class Persona {
    //Atributos
    String nombre,genero;
    int edad;
    double peso,altura;
    //Constructor:
    public Persona(String nombre,String genero, int edad, double peso, double altura) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.peso = peso;
        this.altura = altura;
    }
    //Métodos:
    public double calcularIMC() {
        double imc = (this.peso)/(this.altura*this.altura);
        return imc;
    }
    public boolean esMayorDeEdad() {
       boolean mayor = this.edad >=18;
       return mayor;
    }
    @Override
    
    
    
    
    public String toString() {
        String inf = ("Nombre: "+ this.nombre+"\n"+
                "Género: "+this.genero+"\n"+
                "Edad: "+this.edad+"\n"+
                "Peso: "+this.peso+"\n"+
                "Altura: "+this.altura);
        return inf;
    }
}
