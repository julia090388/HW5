#Реализуйте структуру телефонной книги с помощью HashMap.
#Программа также должна учитывать, что во входной структуре будут повторяющиеся имена с разными телефонами, 
#их необходимо считать, как одного человека с разными телефонами. Вывод должен быть отсортирован по убыванию числа телефонов.

import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class Main {
	public static void main(String[] args) {
  Map<Integer, String> db = new HashMap<>();
        db.put(1232323, "Иванов П.В.");
        db.put(4565656, "Васильев К.М.");
        db.put(7898989, "Петрова Л.Д.");
        db.put(1474747, "Иванов П.В.");
        db.put(2585858, "Петрова Л.Д.");  
        db.put(3696969, "Романов К.О.");

        
        Scanner in = new Scanner(System.in);
        System.out.println("Введите абонента: ");
        String people = in.nextLine();
    
             for (int str : db.keySet()) {

            if (db.get(str).equals(people)) {
            System.out.printf("%s %s \n", str, db.get(str));
            }
        

        }
    }

}