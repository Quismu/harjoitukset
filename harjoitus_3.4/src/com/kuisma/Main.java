package com.kuisma;

import java.util.*;

public class Main {

    public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
        System.out.print("Päivää! Kerro nimesi: ");
        String name = scan.nextLine();
        System.out.println("Olipa kerran pieni lapsi nimeltään "+name+".");
        System.out.println("Kun "+name+" oli kaksivuotias, hän sai käsiinsä vanhan tietokoneen");
        System.out.println("ja alkoi rämpyttämään näppäimistöä.");
        System.out.println("Yrityksen ja erehdyksen kautta "+name+" oppi koodaamaan");
        System.out.println("ja hakkeroi tiensä kolmivuotiaana NSA:n servereille.");
        System.out.println("Onneksi kävi ilmi, että rikosoikeudellinen vastuu");
        System.out.println("alkaa vasta 15-vuotiaana. Huh huh, sanoi "+name+".");
    }
}
