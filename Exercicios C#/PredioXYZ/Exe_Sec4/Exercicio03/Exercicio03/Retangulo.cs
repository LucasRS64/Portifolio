using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicio03 {
    public class Retangulo {
        public double Largura;
        public double Altura;

        public double Area(double largura, double altura) {

            return largura * altura;

        }

        public double Perimetro(double largura, double altura) {

            return (2 * largura) + (2 * altura);
        }

        public double Diagonal(double largura, double altura) {

            return Math.Sqrt(Math.Pow(largura,2) + Math.Pow(altura,2));
        }

    }
}



    

