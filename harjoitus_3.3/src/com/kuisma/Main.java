package com.kuisma;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Anna ensimmäinen luku: ");
        int number1 = scan.nextInt();
        System.out.print("Anna toinen luku: ");
        int number2 = scan.nextInt();
        int multiplied = number1*number2;
        String multiplied_str = Integer.toString(multiplied);
        System.out.println("Lukujen tulo on " + multiplied_str + ".");
    }
}
