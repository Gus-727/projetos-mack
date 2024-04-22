/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.threadproject;

/**
 *
 * @author elisa
 */
public class ThreadClass extends Thread {
    public void run(){
        for(int i = 0; i<5;i++){
            System.out.println("Oi " + getName());
        }
        
    }
}
