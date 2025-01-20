using System;

namespace PredioXYZ {
    class Program {
        static void Main(string[] args) {
            Class_B1 visi1 = new Class_B1("Lucas R");
            Class_B2 visi2 = new Class_B2("Mercado Pago");
            Registro_Presenca register = new Registro_Presenca();

            bool continuar = true;

            while (continuar) {
                Console.WriteLine("Qual das opcoes voce gostaria de selecionar? \n" +
                                  "opcao 1: Registrar Entrada de visitante \n" +
                                  "opcao 2: Registrar saida de visitante \n" +
                                  "opcao 3: Consultar visitantes no predio \n" +
                                  "opcao 4: Consultar visitantes(todos) \n" +
                                  "opcao 5: Sair do sistema");
                int resposta = int.Parse(Console.ReadLine());

                switch (resposta) {
                    case 1:
                        Console.WriteLine("Qual tipo? B1 para pessoa fisica e B2 para empresa");
                        string tipoEntrada = Console.ReadLine();

                        if (tipoEntrada == "B1" || tipoEntrada == "b1") {
                            register.RegisterEntryB1(visi1);
                        }
                        else if (tipoEntrada == "B2" || tipoEntrada == "b2") {
                            register.RegisterEntryB2(visi2);
                        }
                        else {
                            Console.WriteLine("Comando invalido!");
                        }
                        break;

                    case 2:
                        Console.WriteLine("Qual tipo? B1 para pessoa fisica e B2 para empresa");
                        string tipoSaida = Console.ReadLine();

                        if (tipoSaida == "B1" || tipoSaida == "b1") {
                            register.RemoveEntryB1(visi1);
                        }
                        else if (tipoSaida == "B2" || tipoSaida == "b2") {
                            register.RemoveEntryB2(visi2);
                        }
                        else {
                            Console.WriteLine("Comando invalido!");
                        }
                        break;

                    case 3:
                        Console.WriteLine("Pessoas fisicas no predio:");
                        register.ConsultarListaPF_NoPredio();
                        Console.WriteLine("Empresas no predio:");
                        register.ConsultarListaEm_NoPredio();
                        break;

                    case 4:
                        Console.WriteLine("Pessoas fisicas:");
                        register.ConsultarListaPF();
                        Console.WriteLine("Empresas:");
                        register.ConsultarListaEm();
                        break;

                    case 5:
                        continuar = false;
                        Console.WriteLine("Saindo do sistema...");
                        break;

                    default:
                        Console.WriteLine("Opcao invalida! Tente novamente.");
                        break;
                }
            }
        }
    }
}