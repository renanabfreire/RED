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
  - Ratinhos em Rodas de Exercício
  - Urânio

### A missão:

Problema: Cada subsistema consome energia de 5 tipos de fontes: Células de Fusão, Núcleos de Hipermatéria, Capacitores Solares, Ratinhos em Rodas de Exercício, Urânio.

Modelo: Criar uma matriz de consumo energético onde cada linha é um subsistema e cada coluna é uma fonte de energia.

Objetivo: Resolver um sistema linear para encontrar quanto cada fonte precisa produzir para atender a demanda total.

## Modelagem Matemática

Assumindo a matriz $A$ que indica qual a quantidade a_{ij} que o subsistema $i$ necessita da fonte $j$. Temos o vetor de fontes de energia x, que possui a quantidade $x_i$ de cada fonte $i$ disponível.

Por fim, temos o vetor resultante b, que indica quanto $b_j$ de cada subsistema $j$ foi projetado para determinada base.

Considerando a equação:

 $A \cdot x = b$

Basta aplicarmos os diferentes métodos para a obtenção do vetor x.

_May the Force be with you_
