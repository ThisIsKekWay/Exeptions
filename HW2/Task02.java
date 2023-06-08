package ru.geekbrains.lesson1.example;
import  java.util.Random;
/*
 * 2. Если необходимо, исправьте данный код
 * (задание 2 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)
 */

import java.util.Random;
import java.util.random.RandomGenerator;

public class Task02 {
    public static void main(String[] args) {
        correctCode1();
    }

//    Решение №1. Не меняем код и добавляем в обработку новое исключение. Приложение не падает.

    private static void correctCode() {
        try {
            int[] intArray = {2, 3, 4, 5, 6, 7};
            int d = 0;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Catching another exception: " + e.getMessage());
        }
    }


// Рещение №2 меняем код для выполнения именно ArithmeticException

    private static void correctCode1() {
        Random rng = new Random();
        try {
            int[] intArray = {2, 3, 4, 5, 6, 7};
            int d = 0;
            double catchedRes1 = intArray[rng.nextInt(intArray.length)] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e.getMessage());
        }
    }
}