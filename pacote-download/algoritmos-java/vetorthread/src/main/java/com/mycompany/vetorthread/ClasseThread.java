/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.vetorthread;

/**
 *
 * @author elisa
 */
public class ClasseThread extends Thread {
    public void run(){
        
        int[] vet = new int[100];
        
        int cont = 0, soma = 0;
        
        for(int i = 0;i<vet.length;i++){
            cont++;
            vet[i] = cont;
        }
        for(int num:vet){
            soma+=num;
        }
        System.out.println(soma);
        
    }
}
