package com2501.lab1a.bankAccount;

/**
 @author Senih Ucar / A01215761
 @version 1.0
 This class defines properties and methods for bank accounts.
 */

public class BankAccount
{
    // Instance variables
    private double balanceCdn;
    private String accountNumber;
    private String memberLastName;

    /**
     *
     * @param balanceCdn : Account balance 'double'
     * @param accountNumber : Account number 'string'
     * @param memberLastName : Account owner Last Name 'string'
     */
    public BankAccount(double balanceCdn, String accountNumber, String memberLastName)
    {
        this.balanceCdn = balanceCdn;
        this.accountNumber = accountNumber;
        this.memberLastName = memberLastName;
    }


    /**
     * this funct gets balance
     * @return : balance
     */
    public double getbalanceCdn()
    {
        return balanceCdn;
    }

    /**
     * this funct gets account number
     * @return : account number
     */
    public String getAccountNumber()
    {
        return accountNumber;
    }

    /**
     * this func gets member last name
     * @return : member last name
     */
    public String getMemberLastName()
    {
        return memberLastName;
    }

    /**
     * this func calculates total account balance after withdraw amount.
     * @param amountCdn : Withdraw amount
     */
    public void withdraw(double amountCdn)
    {
        this.balanceCdn -= amountCdn;
    }

    /**
     * this func calculates total account balance after deposit amount.
     * @param amountCdn : Deposit amount
     */
    public void deposit(double amountCdn)
    {
        this.balanceCdn += amountCdn;
    }


    /**
     * this func transfers amount to reciepent account.
     * @param amountCdn : transfer amount
     * @param recipientAccount : reciepent account
     */
    public void transfer(double amountCdn, BankAccount recipientAccount)
    {
        recipientAccount.deposit(amountCdn);
        this.withdraw(amountCdn);
    }
}
