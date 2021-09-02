/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ascensocolina;

/**
 *
 * @author dmcew
 */
public class SoloA implements Funcion<String> {
    @Override
    public double evaluar(String x){
        int cuenta=0;
        for( int i=0; i<x.length(); i++ ){
            if(x.charAt(i)=='a' || x.charAt(i)=='A') {
               cuenta++;
            }
        }
        return cuenta;
    }
}
