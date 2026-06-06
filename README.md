# 📈 Calculadora de Preço Justo de Ações

Ferramenta em Python que automatiza a análise de valor intrínseco de ações da B3, combinando dois métodos clássicos de valuation — **Graham** e **Bazin** — para gerar uma tabela comparativa com preço atual, preço justo e margem de segurança.

---

## 🎯 O que o projeto faz

O usuário parte de uma carteira predefinida de ações e pode adicionar qualquer ticker da B3. O programa:

1. Busca automaticamente o **preço atual** da ação via API
2. Calcula o **Preço Justo pelo Método Graham** — baseado no LPA (Lucro por Ação) e VPA (Valor Patrimonial por Ação)
3. Calcula o **Preço Justo pelo Método Bazin** — baseado no dividendo médio e yield-alvo de 6%
4. Calcula a **Margem de Segurança** (%) em relação a cada método
5. Exibe uma **tabela formatada** com semáforo visual de oportunidade

---

## 🖥️ Exemplo de output

```
Ticker  | Preço Atual | P. Justo Graham | Margem Graham | P. Justo Bazin | Margem Bazin
--------|-------------|-----------------|---------------|----------------|-------------
PETR4   | R$ 38,50    | R$ 52,10        | +35,3% ✅     | R$ 44,20       | +14,8% ✅
VALE3   | R$ 61,20    | R$ 55,80        |  -8,8% ❌     | R$ 48,60       | -20,6% ❌
ITUB4   | R$ 34,10    | R$ 41,30        | +21,1% ✅     | R$ 39,50       | +15,8% ✅
BBAS3   | R$ 27,80    | R$ 30,20        |  +8,6% ⚠️     | R$ 29,10       |  +4,7% ⚠️
```

> ✅ Margem > 15% — compra com segurança  
> ⚠️ Margem entre 0% e 15% — monitorar  
> ❌ Margem negativa — ação acima do preço justo

---

## ⚙️ Como usar

**Pré-requisitos:**
```bash
pip install yfinance pandas tabulate
```

**Executar:**
```bash
python main.py
```

**Adicionar ações personalizadas:**

O programa solicita que o usuário informe tickers adicionais no terminal. Ex:
```
Ações da carteira padrão: PETR4, VALE3, ITUB4, BBAS3
Adicione tickers (ex: MGLU3, WEGE3) ou ENTER para pular: WEGE3 RENT3
```

---

## 🧮 Metodologia

### Método Graham
Benjamin Graham propôs que o preço justo de uma ação é determinado por:

```
Preço Justo = √(22,5 × LPA × VPA)
```

Onde:
- `LPA` = Lucro por Ação dos últimos 12 meses
- `VPA` = Valor Patrimonial por Ação
- `22,5` = constante de Graham (P/L de 15 × P/VP de 1,5)

### Método Bazin
Décio Bazin estabeleceu que uma ação vale o que ela paga em dividendos, com yield mínimo de 6%:

```
Preço Justo = Dividendo Médio (últimos 3 anos) / 0,06
```

### Margem de Segurança
```
Margem de Segurança = ((Preço Justo - Preço Atual) / Preço Atual) × 100
```

---

## 🛠️ Stack

- **Python 3.x**
- **yfinance** — coleta de dados financeiros em tempo real da B3
- **pandas** — estruturação e manipulação dos dados
- **tabulate** — formatação da tabela de output

---

## 📌 Limitações conhecidas

- Os dados de LPA, VPA e dividendos dependem da disponibilidade e atualização do Yahoo Finance
- O modelo de Graham funciona melhor para empresas com histórico consistente de lucros
- O método Bazin não se aplica bem a empresas que não pagam dividendos regularmente (ex: empresas de crescimento)

---

## 🚀 Próximas melhorias planejadas

- [ ] Dashboard visual com Power BI ou matplotlib
- [ ] Exportação automática para Excel/CSV
- [ ] Integração com banco de dados SQL para histórico de análises
- [ ] Análise por setor (bancário, energia, consumo)
- [ ] Alertas automáticos por e-mail quando ação entra na zona de compra

---

## 👤 Autor

**João Henrique Marchesano Cukier**  
Estudante de Ciência da Computação — UFSCar  
[github.com/JHCukier](https://github.com/JHCukier)
