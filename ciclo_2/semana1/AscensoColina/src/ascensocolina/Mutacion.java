/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ascensocolina;

/**
 *
 * @author dmcew
 * @param <T>
 */
public interface Mutacion<T> {
    T aplicar(T x);
}
