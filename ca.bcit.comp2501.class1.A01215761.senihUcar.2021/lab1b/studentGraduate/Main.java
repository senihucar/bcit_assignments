package com2501.lab1b.studentGraduate;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Main
{

    public static void main(String[] args)
    {
        Student student1 = new Student(new Name("Tiger","Woods"), "A00123456", new Date(1975,12,30),true);
        Student student2 = new Student(new Name("Bill","Gates"), "A00987654", new Date(1955,10,28), false);

        System.out.println(student1.getStudentName().getFullName()+" ("+student1.getStudentName().getInitials()+")"+
                " (st# "+student1.getStudentNumber()+")"+" was born on "+student1.getDateOfBirth().getYyMmDd()+"."+
                " The student has "+student1.isGraduatedText());

        System.out.println(student2.getStudentName().getFullName()+" ("+student2.getStudentName().getInitials()+")"+
                " (st# "+student2.getStudentNumber()+")"+" was born on "+student2.getDateOfBirth().getYyMmDd()+"."+
                " The student has "+student2.isGraduatedText());

    }
}
