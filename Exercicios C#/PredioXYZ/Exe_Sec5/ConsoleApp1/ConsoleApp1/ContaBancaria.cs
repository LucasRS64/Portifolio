using System.Globalization;

namespace Exercicio {
    class ContaBancaria {

        private string _numero;
        public string Nome_Titular { get; set; }
        public double Saldo { get; private set; }

        public ContaBancaria() {

        }

        public ContaBancaria(string numero, string nome_titular) : this() {
            Numero = numero;
            Nome_Titular = nome_titular;
            Saldo = 0;
        }

        public ContaBancaria(string numero, string nome_titular, double saldo) : this(numero, nome_titular) {
            Saldo = saldo;

        }
        public string Numero {
            get { return _numero; }
            set {
                if (value != null && value.Length > 4) {
                    _numero = value;
                }
            }
        }
        public void Saque(double valorSaque) {
         
         Saldo = (Saldo - valorSaque) - 5.00;
         
          
        }

        public void Deposito(double valorDeposito) {
            if (valorDeposito > 0) {
                Saldo += valorDeposito;
            }
            else {
                Console.WriteLine("Valor de depósito inválido.");
            }

        }

        public override string ToString() {
            return "Conta " + _numero + " Titular: "
                    + Nome_Titular + " Saldo: $" + Saldo.ToString("F2", CultureInfo.InvariantCulture); 
        }

    }
}
