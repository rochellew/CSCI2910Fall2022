public class Program
{
    // 'string' is lowercase
    static void Main(string[] args)
    {
        /*
         * Console I/O
         */

        // Console.WriteLine() is analagous
        // to System.out.println()
        Console.WriteLine("Hello!");
        Console.WriteLine("New Line!");

        // Console.ReadLine is how we read a line of text
        Console.Write("\nEnter your name: ");
        // ?? is the null operator -- what do you want
        // 'name' to be if Console.ReadLine() is null?
        string name = Console.ReadLine() ?? "n/a";

        Console.Write("Enter your age: ");
        // need to parse Console.ReadLine() to an integer
        // as the method returns a string 
        int age = Convert.ToInt32(Console.ReadLine());
        // int age = Int32.Parse(Console.ReadLine());


        // String concatenation uses the concat operator (+)
        // to join strings / variable values together 
        Console.WriteLine("Hello, " + name + ". You are " + age + " years old.");

        // String interpolation allows inclusion of variable values
        // inside a string without the need of concat operator
        // DOLLAR SIGN ($) OUTSIDE THE QUOTES
        Console.WriteLine($"Hello, {name}. Your first initial is {name[0]} and you are {age} years old.");

        // notice the camelCase on canOrder (remember coding standards)
        bool canOrder;
        if(age >= 21)
        {
            canOrder = true;
        }
        else
        {
            canOrder = false;
        }

        /**
         * Strings and characters
         */

        string message = "The quick brown fox jumped over the lazy dog";
        // strings are just arrays of char, so we can use array notation to pull out individual characters
        char firstCharacter = message[0];
        // last character is length of message minus 1 because indeces start at 0
        char lastCharacter = message[message.Length-1];

        /**
         * Arrays!!!
         */

        // 2 ways to declare and initialize an array
        int[] numbers = new int[10];
        for(int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = i + 1;
        }

        string[] names = { "Will", "Bob", "Jane", "Jill" };
        int[] grades = { 88, 80, 90, 95 };

        Console.Write("Enter a number you would like to raise: ");
        double x = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter the power you would like to raise it to: ");
        double y = Convert.ToDouble(Console.ReadLine());

        double power = Power(x, y);

        Console.WriteLine($"{x}^{y} = {power}");
    }// end Main


    // Method header works the same as in Java/JS
    public static double Power(double x, double y)
    {
        return Math.Pow(x, y);
    }
}