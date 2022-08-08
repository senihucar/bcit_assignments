package com2501.lab1a.bankAccount;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Main
{
    public static void main(String[] args) {
        BankAccount b1 = new BankAccount(100.00, "abc123", "gates");
        BankAccount b2 = new BankAccount(500.00, "xyz789", "woods");

        System.out.println(b1.getbalanceCdn());
        b1.withdraw(5.00);
        System.out.println(b1.getAccountNumber());
        System.out.println(b1.getbalanceCdn());

        System.out.println("---");

        System.out.println(b2.getbalanceCdn());
        b1.deposit(23.00);
        System.out.println(b2.getMemberLastName());
        System.out.println(b2.getbalanceCdn());

        System.out.println("---");

        b1.transfer(50.00, b2);
        System.out.println(b1.getbalanceCdn());
        System.out.println(b2.getbalanceCdn());
    }
}
