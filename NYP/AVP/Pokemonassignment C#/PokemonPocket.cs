using System;

namespace PokemonPocket
{

    public void 

    class PokemonPocket
    {
        static void Main(string[] args)
        {
            while (true){
                Console.WriteLine("*****************************");
                Console.WriteLine("Welcome to Pokemon Pocket App");
                Console.WriteLine("*****************************");
                Console.WriteLine("(1) - Add Pokemon to my Pocket");
                Console.WriteLine("(2) - List pokemon(s) in my Pocket");
                Console.WriteLine("(3) - Check if I can evolve pokemon");
                Console.WriteLine("(4) - Evolve pokemon");
                Console.WriteLine("PLease only enter [1,2,3,4] or Q to quit: ");
                try{
                    string i = Console.ReadLine();
                    if(i == "1"){
                        Console.WriteLine("1");
                    }
                    else if(i == "2"){
                        Console.WriteLine("2");
                    }
                    else if(i == "3"){
                        Console.WriteLine("3");
                    }
                    else if(i == "4"){
                        Console.WriteLine("4");
                    }
                    else if(i.ToUpper() == "Q"){
                        break;
                    }
                    else{
                        Console.WriteLine("invalid input");
                    }
                }
                catch
                {
                    Console.WriteLine("Invalid input");
                }
            }
        }
    }
}
