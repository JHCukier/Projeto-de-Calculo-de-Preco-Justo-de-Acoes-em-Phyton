import yfinance as yf
import pandas as pd
import logging

# 1. Silenciando os avisos internos da biblioteca yfinance para manter o terminal limpo
logger = logging.getLogger('yfinance')
logger.disabled = True
logger.propagate = False

# 1 - Fiz uma carteira de Ações com base nas principais empresas listadas na Bolsa brasileira
tickers = ["ITUB4.SA", "VALE3.SA", "PETR4.SA", "WEGE3.SA"]

print("--- CALCULADORA DE VALUATION: FÓRMULA DE GRAHAM ---")
print(f"Ações já incluídas na análise: {', '.join([t.replace('.SA', '') for t in tickers])}\n")

# 2 - Um loop para o usuário adicionar novas ações que deseja avaliar
while True:
    nova_acao = input("Digite o ticker de outra ação para analisar (ex: BBAS3) ou digite 'CALCULAR' para calcular: ").strip().upper()
    
    if nova_acao == 'CALCULAR':
        break
    elif nova_acao != "":
        # Adiciono o '.SA' automaticamente se o usuário não tiver digitado para não dar erro na biblioteca yfinance
        if not nova_acao.endswith(".SA"):
            nova_acao += ".SA"
        
        # Evita reportar duas vezes a mesma empresa
        if nova_acao not in tickers:
            tickers.append(nova_acao)
            print(f"--> {nova_acao} adicionada com sucesso!\n")
        else:
            print(f"--> {nova_acao} já está na lista.\n")

print("\nColetando dados do Yahoo Finance e calculando...\n")

resultados = []

# 3 - Processamento das ações 
for ticker in tickers:
    try:
        acao = yf.Ticker(ticker)
        info = acao.info
        
        preco_atual = info.get('currentPrice', 0)
        lpa = info.get('trailingEps', 0)
        vpa = info.get('bookValue', 0)

        if not preco_atual or not lpa or not vpa or preco_atual == 0:
            print(f"Não foram encontrados os dados para {ticker.replace('.SA', '')}.")
            continue
        
        if lpa > 0 and vpa > 0:
            preco_justo = (22.5 * lpa * vpa) ** 0.5
            margem_seguranca = ((preco_justo - preco_atual) / preco_atual) * 100
        else:
            preco_justo = 0
            margem_seguranca = 0
            
        resultados.append({
            "Ticker": ticker.replace('.SA', ''), # Tiro o .SA para ficar mais bonito na tabela
            "Preço Atual (R$)": round(preco_atual, 2),
            "Preço Justo (R$)": round(preco_justo, 2),
            "Margem de Segurança (%)": round(margem_seguranca, 2)
        })
        
    except Exception as e:
        print(f"Erro ao processar {ticker}. Verifique se o ticker existe.")

# 4 - Relatório
df_resultados = pd.DataFrame(resultados)
df_resultados = df_resultados.sort_values(by="Margem de Segurança (%)", ascending=False)

print("\n--- VALUATION REPORT ---")
# Resetar o index para não mostrar números nas linhas e alinhar os dados
print(df_resultados.to_string(index=False))