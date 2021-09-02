/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package indice;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author dmcew
 */
public class IndiceTest {
    
    public IndiceTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of procesarComandos method, of class Indice.
     */
    @Test
    public void testProcesarComandos() {
        System.out.println("procesarComandos");
        Indice.procesarComandos();
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of agregarPagina method, of class Indice.
     */
    @Test
    public void testAgregarPagina() {
        System.out.println("agregarPagina");
        Pagina comando = null;
        Indice.agregarPagina(comando);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of imprimirPaginas method, of class Indice.
     */
    @Test
    public void testImprimirPaginas() {
        System.out.println("imprimirPaginas");
        Indice.imprimirPaginas();
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of main method, of class Indice.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        String[] args = null;
        Indice.main(args);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
