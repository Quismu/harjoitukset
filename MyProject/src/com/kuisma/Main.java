package com.kuisma;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("--------------");
        System.out.println("  Calculator ");
        System.out.println("--------------");
        System.out.print("Input first number: ");
        int number1 = Integer.parseInt(scanner.nextLine());
        System.out.print("Input second number: ");
        int number2 = Integer.parseInt(scanner.nextLine());
        int addition = number1 + number2;
        int subtraction = number1 - number2;
        int multiplication = number1 * number2;
        int division = number1 / number2;
        System.out.println("Addition: " + addition + ".");
        System.out.println("Subtraction: " + subtraction + ".");
        System.out.println("Multiplication: " + multiplication + ".");
        System.out.println("Division: " + division + ".");
    }
}