package com.collections.aggregation;

import com.collections.model.CandyConsumption;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class AggregationService {

    public AggregationService() {
    }

    public CandyConsumption getCandyConsumptionObject(String date, String name, Integer consumption) {
        //functie declarata pentru viitoarea legare dintre componente
        //are scopul de a crea obiecte relevante agregatorului din datele primite
        //va fi modificat pentru structura de date aferenta
        CandyConsumption candyData = new CandyConsumption(date, name, consumption);
        return candyData;
    }

    public void getConsumptionDatewise(HashMap<String, Integer> consumptionDatewise, String date, Integer consumption) {
        if (!consumptionDatewise.containsKey(date))
            consumptionDatewise.put(date, 0);
        consumptionDatewise.put(date, consumptionDatewise.getOrDefault(date, 0) + consumption);
    }

    public void getDates(ArrayList<String> dates, String date) {
        if (!dates.contains(date))
            dates.add(date);
    }

    public void getConsumptionCandywise(HashMap<String, HashMap<String, Integer>> map,
                                        HashMap<String,
                                        Integer> consumptionCandywise)
    {
        for (String candy : map.keySet()){
            HashMap<String, Integer> candyVal = map.get(candy);
            int total = 0;
            for(String date : candyVal.keySet()){
                total += candyVal.get(date);
            }
            consumptionCandywise.put(candy, total);
        }
    }

    public void printConsumption(ArrayList<String> dates,
                                 HashMap<String, HashMap<String, Integer>> map,
                                 HashMap<String, Integer> consumptionDatewise,
                                 HashMap<String, Integer> consumptionCandywise)
    {
        System.out.print(String.format("%-15s", "Candy/Date"));
        for(String date : dates){
            System.out.print(date + "\t");
        }
        System.out.println("Total");

        for(String candy : map.keySet()){
            System.out.print(String.format("%-15s" , candy));
            HashMap<String, Integer> candyVal = map.get(candy);
            for(int i = 0; i < dates.size(); i++){
                if(!candyVal.containsKey(dates.get(i)))
                    System.out.print("0" + "\t\t");
                else
                    System.out.print(candyVal.get(dates.get(i)) + "\t\t");
            }
            System.out.println(consumptionCandywise.get(candy));
        }
        System.out.print(String.format("%-15s", "Total"));
        int total = 0;
        for(int i = 0; i<dates.size(); i++){
            int candiesOnDate = consumptionDatewise.get(dates.get(i));
            total += candiesOnDate;
            System.out.print(candiesOnDate + "\t\t");
        }
        System.out.println(total);
    }

    public HashMap<String, Integer> aggregate(List<CandyConsumption> data){

        HashMap<String, HashMap<String, Integer>> map = new HashMap<>();

        ArrayList<String> dates = new ArrayList<>();

        HashMap<String, Integer> consumptionDatewise = new HashMap<>();

        HashMap<String, Integer> consumptionCandywise = new HashMap<>();

        // Populare map
        for (CandyConsumption c : data){
            String date = c.getDate();
            String candy = c.getCandy();
            int consumption = c.getConsumption();

            if(!map.containsKey(candy))
                map.put(candy, new HashMap<>());

            map.get(candy).put(date, consumption);

            //populare array de date
            getDates(dates, date);

            //populare map pentru consum per data
            getConsumptionDatewise(consumptionDatewise, date, consumption);
        }

        //populare map pentru consum per bomboana
        getConsumptionCandywise(map, consumptionCandywise);

        //afisare date
        printConsumption(dates, map, consumptionDatewise, consumptionCandywise);

        return consumptionCandywise;
    }
}
