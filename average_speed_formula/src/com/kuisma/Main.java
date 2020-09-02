package com.kuisma;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("*************************************");
        System.out.println("* This is the average speed formula *");
        System.out.println("*************************************");
        System.out.println("");
        System.out.print("Input distance (m): ");
        int distance = scan.nextInt();
        System.out.print("Input time (s): ");
        int time = scan.nextInt();
        System.out.println("");
        System.out.println("The average speed calculated is "+(distance/time)+" m/s");
    }
}
