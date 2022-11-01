package com.collections.model;

import java.util.Objects;

public class CandyConsumption {
    //structura declarata ca exemplu
    //a se modifica ulterior conform datelor ce trebuie primite de agregator
    String date;
    String candy;
    int consumption;

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getCandy() {
        return candy;
    }

    public void setCandy(String candy) {
        this.candy = candy;
    }

    public int getConsumption() {
        return consumption;
    }

    public void setConsumption(int consumption) {
        this.consumption = consumption;
    }

    public CandyConsumption(String date, String candy, int consumption){
        this.date = date;
        this.candy = candy;
        this.consumption = consumption;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof CandyConsumption)) return false;
        CandyConsumption that = (CandyConsumption) o;
        return getConsumption() == that.getConsumption() && getDate().equals(that.getDate()) && getCandy().equals(that.getCandy());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getDate(), getCandy(), getConsumption());
    }

    @Override
    public String toString() {
        return "CandyConsumption{" +
                "date='" + date + '\'' +
                ", candy='" + candy + '\'' +
                ", consumption=" + consumption +
                '}';
    }
}
