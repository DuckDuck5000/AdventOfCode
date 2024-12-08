using System;

class Program {
  public static void Main (string[] args) {
    
    string[] input = System.IO.File.ReadAllLines(@"input.txt");

    long ans1 = part1(input);
    long ans2 = part2(input);

    Console.WriteLine("Ans1 {0}", ans1);
    Console.WriteLine("Ans2 {0}", ans2);

    long part1(string[] lines){
      long horz = 0;
      long vert = 0;
      for (int i = 0; i < lines.Length; i++){

        string[] line = lines[i].Split(' ');
        string direction = line[0];
        long delta = long.Parse(line[1]);

        if (direction == "forward"){
          horz += delta;
        } else if (direction == "up"){
          vert -= delta;
        } else {
          vert += delta;
        }
      
      }
      long ans = horz*vert;
      return ans;
    }
    

    long part2(string[] lines){
      long horz = 0;
      long vert = 0;
      long aim = 0;
      for (int i = 0; i < lines.Length; i++){

        string[] line = lines[i].Split(' ');
        string direction = line[0];
        long delta = long.Parse(line[1]);

        if (direction == "forward"){
          horz += delta;
          vert += (delta*aim);
        } else if (direction == "up"){
          aim -= delta;
        } else {
          aim += delta;
        }
      
      }
      long ans = horz*vert;
      return ans;
    } 
  }
}
