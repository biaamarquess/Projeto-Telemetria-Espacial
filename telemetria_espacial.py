import random
from datetime import datetime

# CLASSE TELEMETRIA
class Telemetria:
    """
    Classe para organizar os dados de telemetria
    """
    
    def __init__(self, dados):
        self.temp_interna = dados.get('temp_interna', 0.0)
        self.temp_externa = dados.get('temp_externa', 0.0)
        self.integridade = dados.get('integridade', 0)
        self.energia_percent = dados.get('energia_percent', 0.0)
        self.pressao_tanques = dados.get('pressao_tanques', 0.0)
        self.modulos = dados.get('modulos', [0, 0, 0, 0])
        self.timestamp = dados.get('timestamp', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    def exibir_dados(self):
        """Exibe todos os dados de telemetria"""
        print("\n" + "="*50)
        print(f"TELEMETRIA - {self.timestamp}")
        print("="*50)
        print(f"Temperatura interna: {self.temp_interna:.1f} °C")
        print(f"Temperatura externa: {self.temp_externa:.1f} °C")
        print(f"Integridade estrutural: {self.integridade} {self.integridade}")
        print(f"Energia: {self.energia_percent:.1f}%")
        print(f"Pressão dos tanques: {self.pressao_tanques:.2f} bar")
        modulos_ok = sum(self.modulos)
        print(f"Módulos críticos: {modulos_ok}/4 OK")
        print("="*50)
    
    def verificar_telemetria(self):
        """
        Verifica se todos os parâmetros estão dentro das faixas seguras
        
        Retorna:
            (pronto_para_decolar, lista_de_falhas)
        """
        falhas = []
        
        LIMITES = {
            'temp_interna': (15, 35),      # 15°C a 35°C
            'temp_externa': (-50, 50),     # -50°C a 50°C
            'pressao_tanques': (1.8, 3.2), # 1.8 a 3.2 bar
            'energia_minima': 85.0,        # mínimo 85%
            'integridade_ok': 1
        }
        
        # Verificações
        if not (LIMITES['temp_interna'][0] <= self.temp_interna <= LIMITES['temp_interna'][1]):
            falhas.append(f"Temperatura interna fora da faixa ({self.temp_interna:.1f}°C). Faixa: {LIMITES['temp_interna'][0]}-{LIMITES['temp_interna'][1]}°C")
        
        if not (LIMITES['temp_externa'][0] <= self.temp_externa <= LIMITES['temp_externa'][1]):
            falhas.append(f"Temperatura externa fora da faixa ({self.temp_externa:.1f}°C). Faixa: {LIMITES['temp_externa'][0]}-{LIMITES['temp_externa'][1]}°C")
        
        if self.integridade != LIMITES['integridade_ok']:
            falhas.append(f"Falha na integridade estrutural (status: {self.integridade})")
        
        if self.energia_percent < LIMITES['energia_minima']:
            falhas.append(f"Energia insuficiente ({self.energia_percent:.1f}%). Mínimo: {LIMITES['energia_minima']}%")
        
        if not (LIMITES['pressao_tanques'][0] <= self.pressao_tanques <= LIMITES['pressao_tanques'][1]):
            falhas.append(f"Pressão dos tanques fora da faixa ({self.pressao_tanques:.2f} bar). Faixa: {LIMITES['pressao_tanques'][0]}-{LIMITES['pressao_tanques'][1]} bar")
        
        # Verificar módulos
        modulos_falhos = [i+1 for i, status in enumerate(self.modulos) if status != 1]
        if modulos_falhos:
            falhas.append(f"Módulos com falha: {modulos_falhos}")
        
        pronto = len(falhas) == 0
        return pronto, falhas
    
    def executar_verificacao(self):
        """Executa e exibe o resultado da verificação"""
        self.exibir_dados()
        
        pronto, falhas = self.verificar_telemetria()
        
        print("\nVERIFICAÇÃO PRÉ-LANÇAMENTO")
        print("-" * 30)
        
        if pronto:
            print("RESULTADO: PRONTO PARA DECOLAR")
            print("Todos os sistemas estão OK!")
        else:
            print("RESULTADO: DECOLAGEM ABORTADA")
            print("Falhas identificadas:")
            for falha in falhas:
                print(f"   • {falha}")
        
        return pronto
    
    def analise_energetica(self):
        """Calcula e exibe a análise de autonomia energética"""
        
        capacidade_total = 150.0  # 150 kWh
        consumo_decolagem = 350.0  # 350 kW
        perdas = 8.5  # 8.5%
        
        energia_disponivel = capacidade_total * (self.energia_percent / 100)
        energia_util = energia_disponivel * (1 - perdas / 100)
        consumo_decolagem_total = consumo_decolagem * (5/60)  # 5 minutos em horas
        
        print("\n" + "="*50)
        print("ANÁLISE ENERGÉTICA")
        print("="*50)
        print(f"Capacidade total: {capacidade_total} kWh")
        print(f"Carga atual: {self.energia_percent:.1f}%")
        print(f"Energia disponível: {energia_disponivel:.2f} kWh")
        print(f"Perdas: {perdas}%")
        print(f"Energia útil: {energia_util:.2f} kWh")
        print(f"Consumo na decolagem: {consumo_decolagem} kW")
        print(f"Consumo para 5min: {consumo_decolagem_total:.2f} kWh")
        print("-" * 50)
        
        if energia_util >= consumo_decolagem_total * 1.1:
            print("Energia suficiente para decolagem com margem de segurança")
        else:
            print("ALERTA: Energia insuficiente para decolagem")
    
    def analise_ia(self):
        """Análise por IA (simulada)"""
        
        print("\n" + "="*50)
        print("ANÁLISE POR IA")
        print("="*50)
        
        # Classificação
        print("\nCLASSIFICAÇÃO DOS DADOS:")
        
        if self.temp_interna < 20:
            print("   • Temperatura interna: BAIXA")
        elif self.temp_interna > 30:
            print("   • Temperatura interna: ALTA")
        else:
            print("   • Temperatura interna: NORMAL")
        
        if self.energia_percent >= 95:
            print("   • Energia: ÓTIMA")
        elif self.energia_percent >= 85:
            print("   • Energia: ADEQUADA")
        else:
            print("   • Energia: CRÍTICA")
        
        # Anomalias
        print("\nANOMALIAS IDENTIFICADAS:")
        anomalias = False
        
        if self.temp_interna > 30 and self.temp_externa < -30:
            print("   • Grande diferencial de temperatura")
            anomalias = True
        
        if self.pressao_tanques < 2.0:
            print("   • Pressão baixa - Possível vazamento")
            anomalias = True
        elif self.pressao_tanques > 3.0:
            print("   • Pressão alta - Risco de sobrepressão")
            anomalias = True
        
        if any(m == 0 for m in self.modulos):
            print("   • Falha em módulo crítico")
            anomalias = True
        
        if not anomalias:
            print("   • Nenhuma anomalia detectada")
        
        # Riscos
        print("\nSUGESTÕES DE RISCO:")
        riscos = False
        
        if self.energia_percent < 85:
            print("   • Risco: Autonomia insuficiente")
            riscos = True
        
        if self.integridade == 0:
            print("   • Risco: Falha estrutural crítica")
            riscos = True
        
        if not riscos:
            print("   • Nenhum risco iminente")


# FUNÇÕES AUXILIARES
def ler_dados_manualmente():
    """Permite ao usuário digitar os dados manualmente"""
    print("\nDIGITE OS DADOS DE TELEMETRIA:")
    print("-" * 40)
    
    dados = {}
    
    dados['temp_interna'] = float(input("Temperatura interna (°C): "))
    dados['temp_externa'] = float(input("Temperatura externa (°C): "))
    dados['integridade'] = int(input("Integridade estrutural (1=OK, 0=Falha): "))
    dados['energia_percent'] = float(input("Nível de energia (%): "))
    dados['pressao_tanques'] = float(input("Pressão dos tanques (bar): "))
    
    print("Status dos 4 módulos críticos (1=OK, 0=Falha):")
    modulos = []
    for i in range(4):
        status = int(input(f"  Módulo {i+1}: "))
        modulos.append(status)
    dados['modulos'] = modulos
    
    dados['timestamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    return dados

def gerar_dados_simulados(pronto=True):
    """Gera dados simulados automaticamente"""
    if pronto:
        # Dados dentro das faixas seguras
        dados = {
            'temp_interna': random.uniform(18, 28),
            'temp_externa': random.uniform(-30, 30),
            'integridade': 1,
            'energia_percent': random.uniform(88, 98),
            'pressao_tanques': random.uniform(2.0, 2.8),
            'modulos': [1, 1, 1, 1],
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
    else:
        # Dados com falhas aleatórias
        dados = {
            'temp_interna': random.choice([random.uniform(10, 14), random.uniform(36, 45)]),
            'temp_externa': random.choice([random.uniform(-60, -51), random.uniform(51, 70)]),
            'integridade': random.choice([0, 1]),
            'energia_percent': random.uniform(50, 84),
            'pressao_tanques': random.choice([random.uniform(1.0, 1.7), random.uniform(3.3, 4.0)]),
            'modulos': [random.choice([0, 1]) for _ in range(4)],
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
    
    return dados

def exibir_reflexao():
    """Exibe reflexão sobre ética e sustentabilidade"""
    
    print("\n" + "="*60)
    print("REFLEXÃO CRÍTICA")
    print("="*60)
    
    print("""
1. ÉTICA E RESPONSABILIDADE:
   A decisão de lançamento envolve vidas humanas e altos investimentos.
   Priorizar a segurança sobre prazos é fundamental.

2. IMPACTO SOCIAL:
   - Positivo: Avanços tecnológicos, satélites, monitoramento climático
   - Negativo: Desigualdade de acesso, custos elevados

3. SUSTENTABILIDADE:
   - Desafio: Lixo espacial (>34.000 detritos)
   - Soluções: Foguetes reutilizáveis, combustíveis verdes
    """)
    
    print("="*60)

def menu():
    """Exibe o menu principal"""
    print("\n" + "="*60)
    print("SISTEMA DE VERIFICAÇÃO DE TELEMETRIA")
    print("="*60)
    print("1 - Teste com dados simulados (Tudo OK)")
    print("2 - Teste com dados simulados (Com falhas)")
    print("3 - Inserir dados manualmente")
    print("4 - Sair")
    print("-"*60)
    
    return input("Escolha uma opção (1-4): ")

# FUNÇÃO PRINCIPAL
def main():
    """Função principal do programa"""
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            print("\nSIMULANDO DADOS - CENÁRIO NOMINAL (TUDO OK)")
            dados = gerar_dados_simulados(pronto=True)
            telemetria = Telemetria(dados)
            telemetria.executar_verificacao()
            telemetria.analise_energetica()
            telemetria.analise_ia()
            exibir_reflexao()
            
            input("\nPressione ENTER para continuar...")
        
        elif opcao == "2":
            print("\nSIMULANDO DADOS - CENÁRIO COM FALHAS")
            dados = gerar_dados_simulados(pronto=False)
            telemetria = Telemetria(dados)
            telemetria.executar_verificacao()
            telemetria.analise_energetica()
            telemetria.analise_ia()
            exibir_reflexao()
            
            input("\nPressione ENTER para continuar...")
        
        elif opcao == "3":
            dados = ler_dados_manualmente()
            telemetria = Telemetria(dados)
            telemetria.executar_verificacao()
            telemetria.analise_energetica()
            telemetria.analise_ia()
            exibir_reflexao()
            
            input("\nPressione ENTER para continuar...")
        
        elif opcao == "4":
            print("\nEncerrando o programa...")
            break
        
        else:
            print("\nOpção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()