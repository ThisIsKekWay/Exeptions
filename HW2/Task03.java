package ru.geekbrains.lesson1.example;
import java.io.FileNotFoundException;


public class Task03 {

    public static void main(String[] args) throws Exception {
        try {
            int a = 90;
            int b = 3;
            System.out.println(a / b);
            printSum(23, 234);
            int[] abc = { 1, 2 };
            abc[3] = 9;
        } catch (Throwable ex) {
            System.out.println("Что-то пошло не так..." + ex.getMessage());
            // Exception все равно будет выброшен, каккое конкретно, будет ясно изх мэсседжа. Последущие не нужны
        }
    }
    public static void printSum(Integer a, Integer b) throws FileNotFoundException {
        System.out.println(a + b);
    }

}
