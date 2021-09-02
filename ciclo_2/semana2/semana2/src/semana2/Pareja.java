/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana2;

/**
 *
 * @author dmcew
 * @param <K>
 * @param <V>
 */
public class Pareja<K,V> {
    //Atributos
    protected K clave;
    protected V valor;
    //Constructor:
    public Pareja(K clave, V valor){
        this.clave = clave;
        this.valor = valor;
    }
    public K clave(){ 
        return clave;
    }
    public V valor() { 
        return valor; 
    }
    //Polimorfismo:
    @Override
    public String toString(){
        return "("+clave+","+valor+")";
    }
}
