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
public class MutacionReal implements Mutacion<Double> {
    @Override
    public Double aplicar(Double x){
        x += Math.random();
        if( x >= 5.0 ) 
            x = 5.0;
        else if( x<-5.0 ) 
            x=-5.0;
        return x;
    }
}