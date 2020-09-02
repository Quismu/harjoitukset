package com.kuisma;

public class Main {

    public static void main(String[] args) {
        String day = "friday";
        switch(day) {
            case "monday":
                System.out.println("It's monday");
                break;
            case "tuesday":
                System.out.println("It's tuesday");
                break;
            case "wednesday":
                System.out.println("It's wednesday");
                break;
            case "thursday":
                System.out.println("It's thursday");
                break;
            case "friday":
                System.out.println("It's friday");
                break;
            case "saturday":
                System.out.println("It's saturday");
                break;
            case "sunday":
                System.out.println("It's sunday");
                break;
            default:
                System.out.println("What!?");


        }
    }
}
