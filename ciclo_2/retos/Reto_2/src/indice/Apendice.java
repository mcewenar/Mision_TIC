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
public class Apendice extends Pagina {
    public String referencia;
  
    public Apendice(String numero, String encabezado, String imagenes, String referencia) {
        super(numero,encabezado,imagenes);
        this.referencia = referencia;
    }   
    @Override
    public String toString(){
        String lista = "\tPágina del Apéndice - Número: " + this.numero + "\n";
        lista += "\tEncabezado: " + this.encabezado + "\n";
        lista += "\tImágenes: " + this.imagenes + "\n";
        lista += "\tReferencia: " + this.referencia;
        return lista;
    }
}

