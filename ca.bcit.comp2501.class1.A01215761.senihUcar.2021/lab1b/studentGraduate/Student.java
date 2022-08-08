package com2501.lab1b.studentGraduate;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Student
{

    // Instance variables
    private String studentNumber;
    private boolean graduated;
    private Name studentName;
    private Date dateOfBirth;

    /**
     * @param studentName   : a object Name.java
     * @param studentNumber : a string
     * @param dateOfBirth   : a object Date.java
     * @param graduated     : a boolean
     */
    public Student(Name studentName, String studentNumber, Date dateOfBirth, boolean graduated) {
        this.studentName = studentName;
        this.studentNumber = studentNumber;
        this.dateOfBirth = dateOfBirth;
        this.graduated = graduated;
    }

    // GETS

    public Name getStudentName() {
        return studentName;
    }

    public String getStudentNumber() {
        return studentNumber;
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }

    public boolean isGraduated() {
        return graduated;
    }

    public String isGraduatedText(){
        if (graduated == true) {
            return "GRADUATED";
        } else {
            return "NOT GRADUATED";
        }
    }

    // SETS
    public void setStudentName(Name studentName) {
        this.studentName = studentName;
    }

    public void setStudentNumber(String studentNumber) {
        this.studentNumber = studentNumber;
    }

    public void setDateOfBirth(Date dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public void setGraduated(boolean graduated) {
        this.graduated = graduated;
    }

}
