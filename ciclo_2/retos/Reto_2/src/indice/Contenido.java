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
public class Contenido extends Pagina {
    public String seccion;
    
    public Contenido(String numero, String encabezado, String imagenes, String seccion) {
        super(numero,encabezado,imagenes);
        this.seccion = seccion;
    }  
    @Override
    public String toString(){
        String lista = "\tPágina del Contenido - Número: " + this.numero + "\n";
        lista += "\tEncabezado: " + this.encabezado + "\n";
        lista += "\tImágenes: " + this.imagenes + "\n";
        lista += "\tSección: " + this.seccion;
        return lista;
    }
}
