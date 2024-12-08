using System;

class Program {
  public static void Main (string[] args) {
    
    string[] input = System.IO.File.ReadAllLines(@"input.txt");
    long[] inputParsed = new long[input.Length];

    for (int i = 0; i < input.Length; i++){
      inputParsed[i] = long.Parse(input[i]);
    }
    long count1 = 0;
    long count2 = 0;
    for (int i = 0; i < input.Length; i++){
      if (i >= 1 && inputParsed[i] > inputParsed[i-1] ){
        count1++;
      }
      if (i >= 3){
        long prevSum = inputParsed[i-1] + inputParsed[i-2] + inputParsed[i-3];
        long currSum = inputParsed[i] + inputParsed[i-1] + inputParsed[i-2];

        if (currSum > prevSum){
          count2++;
        }
      }
    }
    Console.WriteLine("Part 1 {0} ", count1);
    Console.WriteLine("Part 2 {0}", count2);
  }
}
