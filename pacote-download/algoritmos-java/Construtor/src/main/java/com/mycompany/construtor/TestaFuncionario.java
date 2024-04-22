package com.mycompany.construtor;

public class TestaFuncionario {
    public static void main(String[] args) {
        Funcionario func1 = new Funcionario("Sérgião", 10000.0);
        System.out.println("Nome = " + func1.nome);
        System.out.println("Salário = " + func1.salario);
        System.out.println("Valor do imposto = " + func1.calculaImposto());
    }
}
