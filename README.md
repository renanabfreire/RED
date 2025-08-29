# Distribuição de Energia Rebelde: Uma abordagem com Cálculo Numérico

A Aliança Rebelde mantém uma base avançada no planeta gelado Hot, um refúgio estratégico onde a frota reabastece e repara naves. Com a perseguição imperial intensificando-se, a base possui apenas uma reserva limitada de fontes de energia — e deve distribuí-las entre vários subsistemas críticos para sobreviver ao próximo ataque.

- Os subsistemas vitais são:

  - Escudos Defletores (Shield) — proteção planetária; sua eficiência melhora de forma não linear com a energia aplicada.
  - Sistemas de Proteção Elétrica e Raios Tratores (Defence) — defesas secundárias e manobras eletromagnéticas.
  - Esquadrões de X-Wings (Fighter) — consumo de energia para ataques/batalhas.
  - Canhões de Íons (IonCannon) — uso intensivo em curtos pulsos.
  - Motores / Propulsão (Engines) — necessária para manobrar ou fugir; estabilidade dependente da mistura de fontes.

- Fontes de energia disponíveis (estoque limitado):
  - Células de Fusão (FusionCells) — alta densidade, boa para picos.
  - Núcleos de Hipermatéria (HyperCores) — altíssima potência, uso arriscado (pode ativar restrições não-lineares de estabilidade).
  - Capacitores Solares (SolarCaps) — recarregam lentamente, bom para sustentar sistemas por longos períodos.

### A missão:

Problema: Cada subsistema consome energia de 6 tipos de fontes: Células de Fusão, Núcleos de Hipermatéria, Capacitores Solares.          (geradores geotérmicos e baterias químicas).

Modelo: Criar uma matriz de consumo energético onde cada linha é um subsistema e cada coluna é uma fonte de energia.

Objetivo: Resolver um sistema linear para encontrar quanto cada fonte precisa produzir para atender a demanda total.


VERSÃO ANTIGA:
Decidir quanto de cada fonte alocar a cada subsystema, de modo que as necessidades mínimas sejam atendidas, restrições não-lineares (eficiência dos escudos, estabilidade dos motores) não sejam violadas, e um objetivo operacional seja otimizado (por exemplo, maximizar o tempo total operacional dos subsistemas críticos ou maximizar um índice de sobrevivência ponderado).

## Modelagem Matemática

#### Variáveis
- $r_i$ = Quantidade disponível da fonte de energia $i$ (FusionCells, HyperCores, SolarCaps). Vetor $r \in ℝ^{3}$
- $c_{ij}$ = Consumo da fonte $i$ por hora do subsistema $j$ (matriz $C \in ℝ^{3×5}$)
- $l_{i}$ = Necessidade percentual daquele subsistema

- $x_j$ = quanto de cada subsistema será levado

#### Conjuntos
- $I$ = Fontes
- $J$ = Subsistemas

#### Restrição Linear
$\sum_{j \in J} c_{ij} x_j \leq r_i , ~ \forall i \in I$

#### Restrição Trivial
$x_j \geq 0$

### Objetivo:

$max \sum_{i \in I}\sum_{j \in J} c_{ij} l_i$
