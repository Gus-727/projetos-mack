/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vetorthread;

/**
 *
 * @author elisa
 */
public class Vetorthread {

    public static void main(String[] args) {
       int[] vet = new int[100];
        
        int cont = 0, soma = 0;
        
        for(int i = 0;i<vet.length;i++){
            cont=cont+4;
            vet[i] = cont;
        }
        for(int num:vet){
            soma+=num;
        }
        System.out.println(soma);
        
        ClasseThread ta = new ClasseThread();
        ta.start();
        
    }
}
