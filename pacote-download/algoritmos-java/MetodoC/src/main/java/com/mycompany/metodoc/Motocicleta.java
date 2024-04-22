package com.mycompany.metodoc;

import java.util.Objects;

public class Motocicleta {
    // Atributos
	String modelo;
	String marca;
	int nroChassi;
	String nroPlaca;
	String cor;
	int nroCilindradas;

	
	// Início: Seção de definição dos métodos construtores ///////////////////////	
    Motocicleta(int nroChassi, String nroPlaca){
        this.nroChassi = nroChassi;
        this.nroPlaca = nroPlaca;
    }
    Motocicleta(String modelo, String marca){
        this.modelo = modelo;
        this.marca = marca;
    }
    Motocicleta(){
        
    }

	// Fim: Seção de definição dos métodos construtores //////////////////////////

	
	// Método que apresenta na tela o estado do objeto
	public void mostraDados() {
		System.out.println("Modelo : " + modelo);
		System.out.println("Marca : " + marca);
		System.out.println("Número do chassi : " + nroChassi);
		System.out.println("Número da placa : " + nroPlaca);
		System.out.println("Cor : " + cor);
		System.out.println("Número de Cilindradas : " + nroCilindradas);
	}

	// Outros métodos da classe
	public int hashCode() {
		return Objects.hash(cor, marca, modelo, nroChassi, nroCilindradas, nroPlaca);
	}
}
