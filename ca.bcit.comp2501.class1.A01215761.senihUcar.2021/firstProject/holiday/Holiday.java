package com2501.firstProject.holiday;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Holiday
{
    // Instance variables
    private String name;
    private int month; // 1 = january; 12 = december
    private int day;
    private boolean statutory;

    /**
     * Constructor: code that is called automatically
     * each time a 'Holiday' object is made
     * @param name = Holiday name
     * @param month = Holiday month
     * @param day = Holiday day
     */
    public Holiday(String name, int month, int day)
    {
        this.name = name;
        this.month = month;
        this.day = day;
    }

    /**
     * @return the name of the holiday
     */
    public String getName()
    {
        return name;
    }
    /**
     * @return the month of the holiday
     */
    public int getMonth()
    {
        return month;
    }
    /**
     * @return the day of the holiday
     */
    public int getDay()
    {
        return day;
    }
    /**
     * @return the statuory of the holiday
     */
    public boolean isStatutory()
    {
        return statutory;
    }
    /**
     * @sets the statuory of the holiday
     */
    public void setStatutory(boolean statutory)
    {
        this.statutory = statutory;
    }
}
