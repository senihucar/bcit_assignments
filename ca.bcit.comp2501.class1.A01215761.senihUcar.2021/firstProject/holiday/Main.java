package com2501.firstProject.holiday;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Main
{
    public static void main(String[] args)
    {
        Holiday christmas = new Holiday("Christmas", 12, 25);

        System.out.println(christmas.getName());
        System.out.println(christmas.getMonth());
        System.out.println(christmas.getDay());

        System.out.println(christmas.isStatutory()); // false (default)
        christmas.setStatutory(true);
        System.out.println(christmas.isStatutory()); // True set
    }
}
