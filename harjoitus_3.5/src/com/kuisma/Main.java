package com.kuisma;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Anna sana/lause: ");
        String word = scan.nextLine();
        System.out.println("Merkkijonossa " + word + " on " + word.length() + " merkkiä.");
    }
}
