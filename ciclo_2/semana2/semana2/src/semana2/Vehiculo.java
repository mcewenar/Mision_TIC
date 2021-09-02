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
public abstract class Vehiculo {
    
    protected double velocidad;
    protected int pasajeros;
    public Vehiculo(int pasajeros, double velocidad) {
        this.velocidad = velocidad;
        this.pasajeros = pasajeros;
    }
    public int posicion( int tiempo ) {
        return (int)(tiempo*velocidad);
    }
    public void espacios(int espacios) {
        for( int i=0;i<espacios;i++)
            System.out.print(" ");
    }
    public abstract void pintar(int posicion);
  
}
