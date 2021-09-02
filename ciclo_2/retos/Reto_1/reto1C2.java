/*
 La moneda de los Hititas cuatro años antes era el doble de la moneda Pesos 
y la quinta parte de la suma de la moneda de los Hititas y la moneda Pesos es igual 
a la moneda Libra (todas en números enteros). La categoría de la moneda es calculada 
teniendo que cuando el valor de la moneda está entre 0 y 20 unidades la categoría es 'uno' 
cuando está entre 21 y 30 unidades la categoría es 'dos' cuando está entre 31 y 50 unidades la 
categoría es 'tres' y cuando es más de 50 unidades la categoría es 'cuatro'. Calcular las unidades 
de las monedas de los Hititas y la Libra desde un valor de moneda Pesos imprimiéndolas en una línea 
separadas por espacio en orden Pesos Hititas Libra y una nueva línea imprimiendo 
la categoría de la moneda Libra.
 */
package ejerciciosejemplos1;
import java.util.Scanner;

public class reto1C2 {
    public static int[] moneda(int peso) {
        int hilita = 2*peso+4; 
        int libra = (hilita+peso)/5;
        return new int[] {hilita,libra};   
    }
    
    public static void main(String[] args) {
        String categoria;
        Scanner sc = new Scanner (System.in);
        System.out.print("Ingrese un número: ");
        int i = Integer.parseInt(sc.nextLine());
        int[] arr = moneda(i);
        if (arr[1] >= 0 && arr[1] <= 20) {
            categoria = "uno";
        } else if (arr[1] > 20 && arr[1] <= 30) {
            categoria = "dos";  
        } else if (arr[1] > 30 && arr[1] <= 50) {
            categoria = "tres";
        } else {
            categoria = "cuatro";
        }
        System.out.println(i + " " + arr[0] + " " + arr[1]);
        System.out.print(categoria);
    }
    
}
