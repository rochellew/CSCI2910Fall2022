using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes
{
    // : replaces Java's 'extends' keyword
    internal class Baby : Person
    {
        public Baby(string firstName="", string lastName = "", int age = 0)
        {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
        }

        public override string GetCry()
        {
            return "WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH";
        }
    }
}
