using System;
using System.Globalization;

namespace Exercicio03 {

    class Program {
        static void Main(string[] args) {

            Retangulo retangulo = new Retangulo();

            Console.WriteLine("Entre a largura e altura do retângulo:");
            double larg = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            double alt = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.WriteLine("AREA = " + retangulo.Area(larg, alt).ToString("F2", CultureInfo.InvariantCulture));
            Console.WriteLine("PERIMETRO = " + retangulo.Perimetro(larg, alt).ToString("F2", CultureInfo.InvariantCulture));
            Console.WriteLine("DIAGONAL = " + retangulo.Diagonal(larg, alt).ToString("F2", CultureInfo.InvariantCulture));
        }
    }
}
