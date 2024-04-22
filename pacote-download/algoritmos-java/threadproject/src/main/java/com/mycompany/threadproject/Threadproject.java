/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.threadproject;

/**
 *
 * @author elisa
 */
public class Threadproject {

    public static void main(String[] args) {
        
        ThreadClass ta = new ThreadClass();
        ta.start();
        
        ThreadClass tb = new ThreadClass();
        tb.start();
        
        for(int i = 0; i<5; i++){
            System.out.println("Hello World!");
        }
        
    }
}
