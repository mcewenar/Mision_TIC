/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package indice;

/**
 *
 * @author dmcew
 */
public abstract class  Pagina {
    public String numero;
    public String encabezado;
    public String imagenes;
    
    public Pagina(String numero, String encabezado, String imagenes) {
        this.numero = numero;
        this.encabezado = encabezado;
        this.imagenes = imagenes;   
    }  
}
