using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PredioXYZ {
    class Registro_Presenca {

        public List<Class_B1> entrada1 = new List<Class_B1>();
        public List<Class_B2> entrada2 = new List<Class_B2>();
        public List<Class_B1> entradaX1 = new List<Class_B1>();
        public List<Class_B2> entradaX2 = new List<Class_B2>();
        public void RegisterEntryB1(Class_B1 class_B1) {

            entrada1.Add(class_B1);
            entradaX1.Add(class_B1);
        }

        public void RegisterEntryB2(Class_B2 class_b2) {

            entrada2.Add(class_b2);
            entradaX2.Add(class_b2);
        }

        public void RemoveEntryB1(Class_B1 class_B1) {

            entradaX1.Remove(class_B1);

        }

        public void RemoveEntryB2(Class_B2 class_b2) {

            entradaX2.Remove(class_b2);

        }

        public void ConsultarListaPF() {

            foreach(Class_B1 class_B1 in entrada1){

                Console.WriteLine(class_B1.Name);
            }
        }

        public void ConsultarListaEm() {

            foreach (Class_B2 class_B2 in entrada2) {

                Console.WriteLine(class_B2.Name);
            }
        }

        public void ConsultarListaPF_NoPredio() {

            foreach (Class_B1 class_B1 in entradaX1) {

                Console.WriteLine(class_B1.Name);
            }
        }

        public void ConsultarListaEm_NoPredio() {

            foreach (Class_B2 class_B2 in entradaX2) {

                Console.WriteLine(class_B2.Name);
            }
        }


    }
}
