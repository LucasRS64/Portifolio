using System;
using System.Globalization;

namespace ExercicioStatic {
    class Program {
        static void Main(string[] args) {

            Console.Write("Qual e a cotacao do dolar? ");
            double cot = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Quantos dolares voce vai comprar? ");
            double dol = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            double convS = ConversorDeMoeda.Conversao(cot, dol);

            Console.WriteLine("Valor total sem impostos: " + convS.ToString("F2", CultureInfo.InvariantCulture));

            double convR = ConversorDeMoeda.ConversaoReal(convS);

            Console.WriteLine("Valor a ser pago em reais = " + convR.ToString("F2", CultureInfo.InvariantCulture));
        
        }
    
    }
}