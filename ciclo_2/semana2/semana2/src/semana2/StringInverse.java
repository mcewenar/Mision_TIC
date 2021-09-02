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
public class StringInverse {
    public String text;
    public StringInverse(String text) {
        this.text = text;
    }
    public String reverse() {
        
	char[] arr = text.toCharArray();
        String cadena = "";
        //your code goes here
        for(int i = arr.length-1; i>=0;i--) {
            cadena += arr[i];
        }     
        return cadena;
    }
}
