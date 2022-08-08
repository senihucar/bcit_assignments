package com2501.lab1b.studentGraduate;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 */

public class Name
{

    // Instance variables
    private String first;
    private String last;

    /**
     * @param first : firstName e.g. : "Tiger"
     * @param last  : lastName e.g.  : "Woods"
     */
    public Name(String first, String last)
    {
        this.first = first;
        this.last = last;
    }

    // METHODS

    /**
     * @return : fullName e.g. : "Tiger Woods"
     */
    public String getFullName() {
        return first+" "+last;
    }

    /**
     * @return : initials e.g. : "T.W."
     */
    public String getInitials() {
        return first.toUpperCase().charAt(0)+"."+last.toUpperCase().charAt(0)+".";
    }

    // GETS
    public String getFirst() {
        return first;
    }

    public String getLast() {
        return last;
    }

    // SETS
    public void setFirst(String first) {
        this.first = first;
    }

    public void setLast(String last) {
        this.last = last;
    }
}
