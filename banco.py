class cliente:
    def __init__(self,nome,numero_cadastro,saldo):
        self.nome = nome
        self.numero_cadastro = numero_cadastro
        self.saldo = saldo
   
    def conta(self,esc,n):
        if (self.saldo <= 0) or (self.saldo< n):
            print('Voce não possui saldo em conta')
            return
        if (esc == 'Saldo'):
            print(f'Saldo da conta:R${self.saldo}')
            return    
        
        if (esc == 'Sacar'):
            self.saldo -= n
            print(f'{self.nome} sacou R${n}')
            return
        
        if (esc == 'Depositar'):
            self.saldo += n
            print(f'{self.nome} depositou R${n}')
            return
    def emprestimo(self,valor,meses):
        calc = (0.5 * valor)+valor
        juros = calc * meses
        for i in range(meses + 1):
            tot_mes = calc
            tot_mes += calc 
        print(f'Um emprestimo de R${valor} a uma taxa de 5% ao mes, em {meses} meses fica:\nTotal em {meses}:R${juros}\nA uma taxa de 5% ao mes fica:R${tot_mes}')
