package com2501.lab1b.studentGraduate;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Date
{

    // Instance variables
    private int year;
    private int month; // 1 = january; 12 = december
    private int day;

    /**
     * @param year : year e.g. "2021"
     * @param month : month e.g. "12"
     * @param day : day e.g. "25"
     */
    public Date(int year, int month, int day)
    {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    // METHODS

    /**
     * @return : e.g. "2021-12-25"
     */
    public String getYyMmDd()
    {
        return +year+"-"+month+"-"+day;
    }

    // GETS

    public int getYear() {
        return year;
    }

    public int getMonth() {
        return month;
    }

    public int getDay() {
        return day;
    }

    // SETS

    public void setYear(int year) {
        this.year = year;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public void setDay(int day) {
        this.day = day;
    }
}
