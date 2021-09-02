/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejerciciosejemplos1;
import java.util.Scanner;
import java.util.Arrays;
import java.lang.Iterable;

/**
 *
 * @author dmcew
 */
public class EjerciciosEjemplos1 {
    /**
     * @param args the command line arguments
     * @param A
     * @return 
     */
    public static double suma_arreglo_reales(double[] A){
        double s = 0;
        for( int i=0; i<A.length; i++){
            s += A[i];
        }
        return s;
    }
    public static int[] lee_arreglo_enteros(Scanner sc, int n){
        int[] x = new int[n];
        for( int i=0; i<n; i++ ){
            System.out.println("Componente "+i+"n-ésima?");
            x[i] = sc.nextInt();
        }
        return x;
    }
    
    public static double[] pos_maximo(double[] A){ //RETORNA
        int m = 0;
        for(int i=0; i<A.length; i++){
            if ( A[i] > A[m] )
                m = i;
        }
        return new double[] {m,A[m]};
    }
    public static void escribe_arreglo_reales(double[] x){ //Calcula la POSICIÓN mayor del arreglo
        int n = x.length;
        for( int i=0; i<n; i++ ){
            System.out.println("x["+i+"]="+x[i]);
        }
    }   
    public static int[][] cuadrados_matriz(int[][] X){
        //permite construir una nueva matriz que contiene
        //el cuadrado de cada componente de una matriz
        int[][] Y = new int[X.length][X[0].length];
        for(int i=0; i<X.length; i++){
            for(int j=0; j<X[i].length; j++){
                Y[i][j] = X[i][j]*X[i][j];
            }
        }
        return Y;
    }
    /*public static double diagonal_matriz(double[][] X){
        double[] Y = new double[X.length];
        for( int i=0; i<X.length; i++){
            Y[i] = X[i][i];
        }
        return Y;
    }*/
    
    public static boolean matriz_simetrica(char[][] X){
        boolean bandera = true;
        for( int i=0; i<X.length-1; i++){
            for( int j=i+1; j<X.length; j++){
                bandera &= (X[i][j] == X[j][i]); //Equivalent: a = a & b;
                //There is no &&= operator.
            }
        }   
        return bandera;
    }
    
    public static double volumen_cono_esfera(double r1,double r2,double h) {
        double vcono = (1/3*Math.PI)*(r2*r2)*h;
        double vesfera = (4/3)*(Math.PI)*(r1*r1*r1);
        return vesfera + vcono;
    }
    public static double area_lateral_carro(double ra1,double ra2, double al1,double ba1, double al2, double ba2) {
        //COMPOSICIÓN DE FUNCIONES EN JAVA
        return suma_llantas(ra1,ra2) + suma_chasis(al1,ba1,al2,ba2);  
    }
    public static double suma_llantas(double r1,double r2) {
        return Math.pow(r1,2)*Math.PI + Math.pow(r2,2)*Math.PI;
        
    }
    public static double suma_chasis(double a1, double b1, double a2, double b2) {
        return a1*b1 + a2*b2;
        
    }
    /*En 2022 el país A tendrá una poblacion de 25 millones de habitantes
    y el paıs B de 18.9 millones. Las tasas de crecimiento anual de la
    poblacion seran de 2% y 3% respectivamente. Desarrollar un
    algoritmo para informar en que año la poblacion del paıs B superara a
    la de A.*/
    public static void poblacion() {
        int contador = 0;
        for (double A=25e6,B=18.9e6; B<A; A+=0.02*A,B+=0.03*B) {
            contador++;
        }
        System.out.println(contador);
    }
    
    public static int factorial(int n) {
        //Imprimir los números de 1 hasta un número natural n dado, cada uno
        //con su respectivo factorial.
        int acum = 1;
        while(n>1){
            acum *= n; 
            n--;
        }
        return acum;
    }
    //Calcular el valor de 2 elevado a la potencia n.
    public static double potencia(int n) {
        double acum = 1;
        int contador = 0;
        if (n>=0) {
            switch (n) {
                case 0:
                    acum = 1;
                    break;
                case 1:
                    acum = 2;
                    break;
                default:
                    while (contador<n) {
                    acum *=2;
                    contador++;    
                }
            }
        } else {
            for (int i=0; i>n;i--) {
                acum *=2;
            }
            acum = 1/acum;  
        }
        return acum;
    }
    //Leer un número natural n, leer otro dato de tipo real x y calcular x a la n
    public static double potenciaAlaN(double x, int n ) {
        double acum = 1;
        int contador = 0;
        if (n>=0) {
            switch (n) {
                case 0:
                    acum = 1;
                    break;
                case 1:
                    acum = x;
                    break;
                default:
                    while (contador<n) {
                        acum *=x;
                        contador++;
                    }
            }
        } else {
            for (int i=0; i>n; i--) {
                acum *=x;
            }
            acum = 1/acum;  
        } 
        return acum;
    }
    
    public static void tablasMultiplicar() {
        //#FPV7-generar las tablas de multiplicar del 1 al 9 
        for (int i = 1; i<=12; i++){  //for externo, i indica cual tabla voy a generar
            System.out.print(i+":");
            for (int j=1; j<=10; j++) {
                //for interno, por cada valor de i, la j toma los valores de 1 a 9
                 int prod = i * j;
                 System.out.print("\t"+ prod); //aqui termina el for interno, despues de esta instruccion ingreso al for i por debajo
            }
            System.out.println(); // aqui termina el for externo, es un cambio de linea   
        }
    }  
}   
    /*public static void serieMcLaurin(int x,int n) {
        //Disenar una funcion que permita calcular una aproximacion de la
        //funcion exponencial alrededor de 0 para cualquier valor x ∈ R,
        //utilizando los primeros n terminos de la serie de Maclaurin
        double su=0.;
        for (int i = 0; i<=n; i++) {
            int num = x**i;
            den=facto(i)
             ter=num/den
            su += ter
            return su 
            def facto(n):
            f=1 #1 es el modulo de la multiplicacion
            for i in range(1, n+1): # lenguaje matematico [1, 10) = [1, 9]
            f *=  i 
            return f
            print(expo(1,10))  #e**1
        }
            
    }*/
    /*public static int ocurrencias(char letter, String chain) {
        //Elabore un programa que, dada una letra, cuente cuántas ocurrencias
        //de esta letra hay.
        int cont = 0;
        int posicion = chain.indexOf(letter); //The indexOf() method returns the position of the first occurrence of specified character(s) in a string.
        //An int value, representing the index of the first occurrence of the character in the string, or -1 if it never occurs
        while (posicion != -1) {
               cont++;
               posicion = chain.indexOf(letter, posicion + 1);
        }  
        return cont;
    }*
    
    public static void main(String[] args) {
        System.out.println(ocurrencias('c',"Érase una vez un carro"));
    } 
}       
        
        //tablasMultiplicar();
        //Otra forma, ingresando datos de x tipo
        /*Scanner sc = new Scanner (System.in);
        System.out.print("Ingresa base (número real): ");
        double x = sc.nextDouble();
        System.out.print("Ingresa exponente: ");
        int n = sc.nextInt();
        System.out.println(potenciaAlaN(x,n));*/
        
        
        /*Scanner sc = new Scanner (System.in);
        System.out.print("Ingresa base (número real): ");
        double x = Double.parseDouble(sc.nextLine());
        System.out.print("Ingresa exponente: ");
        int n = Integer.parseInt(sc.nextLine());
        System.out.println(potenciaAlaN(x,n));*/
        /*Scanner sc = new Scanner (System.in);
        System.out.print("Enter a integer number: ");
        int n = Integer.parseInt(sc.nextLine());
        System.out.println(potencia(n));
        System.out.println(factorial(6));*/
        
        //poblacion();
        /*for (int x = 1;x<=999; x+=2) {
            System.out.println(x);  
        }
        int y = 2;
        while (y<=1000) {
            System.out.println(y);
            y+=2;
        }*/
        
        
        
        
        
        //System.out.println(volumen_cono_esfera(3,4,5));  
        //System.out.println(area_lateral_carro(3.1,4.5,2.4,4.5,6.5,1.4));
        /*int x = 1;
        while (x<=100) {
            System.out.println(x+"="+Math.pow(x, 2));
            x++;*/          
        /*Scanner sc = new Scanner (System.in);
        System.out.print("Escriba la dimensión: ");
        int n = Integer.parseInt(sc.nextLine());
        double[] x = new double[n];
        for (int r = 0;r<x.length; r++) {
            System.out.print("Escriba el real de la posición "+(r+1)+": ");
            double y = Double.parseDouble(sc.nextLine());
            x[r]= y;
        }
        double[] arr = pos_maximo(x);
        System.out.println("La posición con el valor mayor es:"+(arr[0]+1));
        System.out.println("El valor mayor es: "+arr[1]);
        escribe_arreglo_reales(x);
        
        int[][] z = new int[n][3];
        //System.out.print(Arrays.toString(cuadrados_matriz(z))); Muestra el contenido de un array unidimensional
        System.out.println(Arrays.deepToString(cuadrados_matriz(z))); //Muestra
        //el contenido de una matriz, pero de 0 porque no están llenos. Sólo aparece el espacio reservado en la RAM*/      
        
        //lee_arreglo_enteros(3);
        /*Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la lista separada por &:");
        String s = sc.nextLine();
        String[] line = s.split("&");
        String nombre = line[0];
        int edad = Integer.parseInt(line[1]);
        double estatura = Double.parseDouble(line[2]);
        System.out.println("nombre: " + nombre);
        System.out.println("edad: " + edad);
        System.out.println("estatura: " + estatura + "m");*/
        
        
        // TODO code application logic here
        /*String c = "Programar es genial!";
        
        String s = "Juan 30 1.68";
        String[] line = s.split(" ");
        String nombre = line[0];
        int edad = Integer.parseInt(line[1]);
        double estatura = Double.parseDouble(line[2]);
        System.out.println("nombre: " + nombre);
        System.out.println("edad: " + edad);
        System.out.println("estatura: " + estatura + "m");
        
        System.out.println(c.substring(10, c.length())); //Output: Es genial*/
