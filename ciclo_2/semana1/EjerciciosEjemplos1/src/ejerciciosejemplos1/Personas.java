/* EJEMPLO DE DESARROLLO MÓVIL
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejerciciosejemplos1;

/**
 *
 * @author dmcew
 */
public class Personas {
    private String nombre;
    private int edad;

    public Personas (String nombre, int edad) {
        this.nombre = nombre;
        this.setEdad(edad);

    }
    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        String nombre = this.nombre;
        return nombre;

    }
    public static void main(String[] args) {
        Personas personas = new Personas("Fernando",12);
        System.out.println(personas.getNombre());
        personas.setNombre("Luis");
        System.out.println(personas.getNombre());
    }
}
