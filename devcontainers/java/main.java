import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("I'm going to guess the number you're thinking of.");
        System.out.println("Enter a number: ");

        int num = reader.nextInt();

        System.out.println("You think: " + num);
        reader.close();
    }
}