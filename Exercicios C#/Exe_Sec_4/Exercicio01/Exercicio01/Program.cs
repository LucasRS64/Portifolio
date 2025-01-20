using System;

namespace Exercicio01 {
    class Program {
        
        static void Main(string[] args) {

            Maria x;
            Joao y;

            x = new Maria();
            y = new Joao();

            Console.WriteLine("Dados da primeira pessoa: ");
            x.Idade = int.Parse(Console.ReadLine());
            x.Nome = Console.ReadLine();
            Console.WriteLine("Dados da segunda pessoa: ");
            y.Idade = int.Parse(Console.ReadLine());
            y.Nome = Console.ReadLine();

            if (x.Idade > y.Idade) {
                Console.WriteLine(x.Nome + " e mais velho(a)");
            }
            else {
                Console.WriteLine(y.Nome + " e mais velho(a)");
            }
        }
    }
}