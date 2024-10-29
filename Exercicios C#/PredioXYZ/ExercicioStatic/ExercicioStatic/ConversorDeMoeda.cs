namespace ExercicioStatic {
    class ConversorDeMoeda {

        public static double IOF = 0.06;

        public static double ConversaoReal(double valor) { 
            return valor + valor * IOF;
        }
        public static double Conversao(double val, double x) {
            return val * x;
        }
    }
}
