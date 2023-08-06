import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class ReadCsv {
    public static void main(String[] args) {
        String path = "C:\\Users\\user\\Documents\\06_공부\\06_07_java\\Calculator_piping\\src\\resources";
        String line = "";
        String cvsSplitBy = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            // Read header
            String[] header = br.readLine().split(cvsSplitBy);
            int nameIndex = -1, ageIndex = -1, resultIndex = -1;

            for (int i = 0; i < header.length; i++) {
                if (header[i].equals("name")) nameIndex = i;
                if (header[i].equals("age")) ageIndex = i;
                if (header[i].equals("result")) resultIndex = i;
            }

            if (nameIndex == -1 || ageIndex == -1 || resultIndex == -1) {
                System.out.println("Columns not found");
                return;
            }

            while ((line = br.readLine()) != null) {
                String[] row = line.split(cvsSplitBy);

                if (row[nameIndex].equals("John") && row[ageIndex].equals("25")) {
                    System.out.println("Result: " + row[resultIndex]);
                    break;
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
