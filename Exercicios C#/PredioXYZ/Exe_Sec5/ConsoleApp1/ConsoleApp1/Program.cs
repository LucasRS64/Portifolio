using System;
using System.Globalization;
using static System.Net.Mime.MediaTypeNames;

namespace Exercicio {
    class Program {
        static void Main(string[] args) {

            Console.WriteLine("\nEntre o número da conta: ");
            string numConta = Console.ReadLine();
            Console.WriteLine("\nEntre o titular da conta: ");
            string titular = Console.ReadLine();
            Console.WriteLine("\nHaverá depósito inicial (s/n)?");
            char x = char.Parse(Console.ReadLine());

            ContaBancaria b;

            if (x == 's' || x == 'S') {

                Console.WriteLine("\nEntre o valor do depósito inicial: ");
                double depositoInicial = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                b = new ContaBancaria(numConta, titular, depositoInicial);

                Console.WriteLine(b);

                Console.WriteLine("\nEntre um valor para depósito: ");
                double valorDeposito = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                b.Deposito(valorDeposito);

                Console.WriteLine("Dados da conta atualizados após depósito:");
                Console.WriteLine(b);

                Console.WriteLine("\nEntre o valor para saque: ");
                double valorSaque = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                b.Saque(valorSaque);

                Console.WriteLine("Dados da conta atualizados após depósito:");
                Console.WriteLine(b);

            }
            else if (x == 'n' || x == 'N') {

                b = new ContaBancaria(numConta, titular);

                Console.WriteLine(b);

                Console.WriteLine("\nEntre um valor para depósito: ");
                double valorDeposito = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                b.Deposito(valorDeposito);

                Console.WriteLine("Dados da conta atualizados após depósito:");
                Console.WriteLine(b);

                Console.WriteLine("\nEntre o valor para saque: ");
                double valorSaque = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                b.Saque(valorSaque);

                Console.WriteLine("Dados da conta atualizados após depósito:");
                Console.WriteLine(b);

            }

        }

    }
}