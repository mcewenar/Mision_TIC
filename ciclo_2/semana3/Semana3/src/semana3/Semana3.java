/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semana3;
import binary.Converter;
import java.util.Scanner;

/**
 *
 * @author dmcew
 */
public class Semana3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    	System.out.print("Enter a number:");
    	Scanner sc = new Scanner(System.in);
    	int x = sc.nextInt();   
    	System.out.print(Converter.toBinary(x));
    }
}
    	
    
