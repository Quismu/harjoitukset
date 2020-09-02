package com.kuisma;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        int target_n = random.nextInt(100)+1; //Generate random number between 1-100
        System.out.println("Try to guess the number I'm thinking of.");
        System.out.print("Guess a number in range 1-100: ");
        int n = scanner.nextInt();
        int tries = 0;
        //Loop
        while(true) {
            if(n < target_n) { // if the user guesses too low
                System.out.println("Your guess was too low!");
                tries += 1;
                System.out.print("Make a new guess: ");
                n = scanner.nextInt();
            }
            if(n > target_n) { // if the user guesses too high
                System.out.println("Your guess was too high!");
                tries += 1;
                System.out.print("Make a new guess: ");
                n = scanner.nextInt();
            }
            if(n == target_n) { // if the user guesses correctly
                System.out.println("You guessed correctly!");
                tries += 1;
                System.out.println("Tries: "+tries);
                break;
            }
        }
    }
}