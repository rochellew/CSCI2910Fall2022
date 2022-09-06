using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes
{
    public class Person
    {
        // fields

        // firstName and lastName are backing fields -- they have a public facing
        // property for read/write access
        protected string firstName;
        protected string lastName;
        protected string birthDay;

        // static means school belongs to Person, not any Person object(s)
        static string school = "ETSU";
        protected int age = 0;

        ////////////////////////////////////
        // Properties
        ////////////////////////////////////
        public string FirstName 
        {
            get { return firstName; } 
            set { firstName = value; } 
        }

        public string LastName
        {
            get { return lastName; }
            set { lastName = value; }
        }


        // Both Name properties do the same thing -- first is a shorthand

        //public string Name => $"{firstName} {lastName}";
        public string Name 
        {
            get { return $"{firstName} {lastName}"; }
        }

        public string BirthDay
        {
            get { return birthDay; }
            init { birthDay = "10/31/1995"; }
        }

        public string FavoriteColor { get; set; }

        // default constructor (aka 'no-arg constructor')
        public Person() { }

        // parameterized constructor
        public Person(string firstName="n/a", string lastName="n/a", int age=0)
        {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
        }

        // copy constructor
        public Person(Person personToCopy)
        {
            this.firstName = personToCopy.firstName.ToUpper();
            this.lastName = personToCopy.lastName.ToUpper();
            this.age = personToCopy.age;
        }

        public virtual string GetCry()
        {
            return "Wah.";
        }

        public string GetFirstName()
        {
            return firstName;
        }

        public string GetInitials()
        {
            return $"{firstName[0]}.{lastName[0]}.";
        }

        public int CalculateWeeks(int age) => age * 52;

        // overriding the base class (Object class's) ToString method
        public override string ToString()
        {
            return
                $"Name:             {Name}\n" +
                $"Age:              {age}\n"  +
                $"Favorite Color:   {FavoriteColor}";
        }
    }
}
