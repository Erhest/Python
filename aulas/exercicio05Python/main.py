from funcionario import *

uno = Veiculo('Fiat Uno', 'KTW15EA3')

func1 = Funcinario('Porter Valenski', '12/02/1997', uno)
func1.addDepen('Perovic Valenski', '12/05/2017', 'Filho')
func1.addDepen('Salenskia Valenski', '12/05/2017', 'Esposa')

func1.exibirFuncionario()