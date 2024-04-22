package com.mycompany.metodoc;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);

		byte code = input.nextByte();
		System.out.println(switch (code) {
			case 1 -> new Motocicleta().hashCode();
			case 2 -> new Motocicleta(input.nextInt(),input.next()).hashCode();
			case 3 -> new Motocicleta(input.next(),input.next()).hashCode();
			default -> throw new IllegalArgumentException("Error");
		});

		input.close();
	}
}
