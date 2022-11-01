package com.collections;

import com.collections.aggregation.AggregationService;
import com.collections.model.CandyConsumption;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        AggregationService api = new AggregationService();
        CandyConsumption candy = api.getCandyConsumptionObject("19-02-2001", "Bucuria", 52);
        List<CandyConsumption> candies = new ArrayList<>();
        candies.add(candy);
        api.aggregate(candies);
    }
}
