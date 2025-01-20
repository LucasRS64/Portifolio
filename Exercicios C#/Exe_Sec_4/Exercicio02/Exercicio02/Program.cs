namespace Exercicio02 {
    class Program {
        static void Main(string[] args) {

            Funcionario x, y;

            x = new Funcionario();
            y = new Funcionario();

            Console.WriteLine("Dados do primeiro funcionário: ");
            x.Nome = Console.ReadLine();
            x.Salario = double.Parse(Console.ReadLine());
            Console.WriteLine("Dados do segundo funcionário: ");
            y.Nome = Console.ReadLine();
            y.Salario = double.Parse(Console.ReadLine());

            Console.WriteLine("Salario medio = " + Media(x.Salario, y.Salario));
        }
        static double Media(double a, double b) {
            double m;
            m = (a + b)/2;

            return m;
        
        }
    }
}