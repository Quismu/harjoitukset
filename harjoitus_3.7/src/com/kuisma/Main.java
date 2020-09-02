package com.kuisma;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Anna kokonaisluku: ");
        int number1 = scan.nextInt();
        System.out.print("Anna toinen kokonaisluku: ");
        int number2 = scan.nextInt();
        System.out.println("");
        System.out.println("Lukujen summa on "+(number1+number2)+".");
        System.out.println("Lukujen erotus on "+(number1-number2)+".");
        System.out.println("Lukujen tulo on "+(number1*number2)+".");
        System.out.println("Lukujen osamäärä on "+(number1/number2)+".");
    }
}
