using Classes;

public class Program
{
    static void Main(String[] args)
    {
        Person me = new Person("Will", "Rochelle", 26);
        Person dylan = new Person("Dylan", "Pogue", 20);
        Person dolly = new Person(lastName: "Parton", age: 70, firstName: "Dolly");
        Person madonna = new Person(firstName: "Madonna", age: 50);
        Person shade = new Person();

        Console.WriteLine(me.GetInitials());

        Console.WriteLine(dylan.FirstName);

        shade.FirstName = "Napolean";
        shade.LastName = "Shade";
        shade.FavoriteColor = "Grey";

        Console.WriteLine($"{shade.Name}'s favorite color is {shade.FavoriteColor}");

        int numWeeks = me.CalculateWeeks(26);

        Console.WriteLine(numWeeks);



        // copying objects
        Person copyCat = new Person(dolly);
        Console.WriteLine($"{dolly.Name}");
        Console.WriteLine($"{copyCat.Name}");


        // Subtype polymorphism means I can reference a subtype with a reference variable of the
        // parent type (e.g., a Person can reference a Baby, but a Baby can't reference a Person)
        Person grogu = new Baby(firstName: "Grogu", age: 54);
        Console.WriteLine(grogu.FirstName);
        grogu.FavoriteColor = "Green";

        Console.WriteLine();
        Console.WriteLine(grogu);
    }

    static void SayGoodbye()
    {
        Console.WriteLine($"Bye loser. Today is a {Weekday.Tuesday}.");
    }
}
