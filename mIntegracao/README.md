# Estrutura da Apresentação

## 1. Introdução

* Contextualizar: a eletrônica de potência depende muito de **retificadores** (circuitos que convertem corrente alternada em corrente contínua).
* Mostrar o retificador de meia onda (desenho simples: fonte senoidal → diodo → resistor de carga).
* Objetivo: calcular a **corrente média** de saída.


## 2. Modelo ideal (motivação)

* No diodo **ideal**:

  $$
  i(t) = \frac{V_m \sin(\omega t)}{R}, \quad 0 < \theta < \pi
  $$
* Corrente média seria:

  $$
  I_{ideal} = \frac{1}{\pi R}\int_0^\pi V_m \sin(\theta)\, d\theta = \frac{V_m}{\pi R} \cdot 2
  $$
* Mas isso não é realista → serve só de comparação.


## 3. Modelo real do diodo

* O diodo apresenta:

  * Queda de tensão direta ($V_d$)
  * Resistência dinâmica não linear ($r_d e^{\alpha \sin(\theta)}$)
* Então, a corrente conduzida é:

  $$
  i(\theta) = \frac{V_m \sin(\theta) - V_d}{R + r_d e^{\alpha \sin(\theta)}}, \quad \theta_c \leq \theta \leq \pi
  $$
* $\theta_c = \arcsin\left(\frac{V_d}{V_m}\right)$: ângulo de condução.


## 4. Integral da corrente média

$$
I_{médio} = \frac{1}{\pi} \int_{\theta_c}^\pi \frac{V_m \sin(\theta) - V_d}{R + r_d e^{\alpha \sin(\theta)}} \, d\theta
$$

* Essa integral **não tem solução analítica** (não dá para aplicar o teorema fundamental do cálculo).
* Só pode ser resolvida por **métodos numéricos de integração**.


## 5. Aplicação da Quadratura Gaussiana

* Método: aproximar a integral como soma ponderada de valores da função.

$$
\int_a^b f(x) dx \approx \sum_{i=1}^n w_i \, f\left(\frac{b-a}{2}x_i + \frac{a+b}{2}\right)\cdot \frac{b-a}{2}
$$

* $x_i$: raízes dos polinômios de Legendre
* $w_i$: pesos associados
* Vantagem: mais eficiente que trapézio/Simpson, alta precisão com menos pontos.


## 6. Exemplo numérico

Escolher parâmetros realistas:

* $V_m = 20 \,V$
* $V_d = 0.7 \,V$
* $R = 100 \,\Omega$
* $r_d = 5 \,\Omega$
* $\alpha = 1$

Passos:

1. Calcular $\theta_c = \arcsin(0.7/20) \approx 0.035 \, rad$.
2. Montar a integral definida.
3. Aplicar quadratura gaussiana de ordem $n=4$ ou $n=8$.
4. Obter aproximação de $I_{médio}$.
5. Comparar com caso ideal.


## 7. Conclusão

* Mostra que:

  * Na prática, a corrente média é **menor** que a prevista no modelo ideal.
  * O cálculo exato só é possível via **integração numérica**.
* Aplicação direta em **projetos de fontes retificadoras, carregadores, eletrônica de potência**.
* Integração numérica → ferramenta essencial em engenharia quando o modelo é **não linear**.


## 8. Estrutura da Apresentação em Slides

1. **Título e objetivo**
2. **Retificador de meia onda** (diagrama + explicação)
3. **Modelo ideal vs real**
4. **Equação da corrente média**
5. **Integral que não pode ser resolvida analiticamente**
6. **Método de quadratura gaussiana explicado**
7. **Exemplo numérico resolvido** (passo a passo)
8. **Resultados e comparação**
9. **Conclusão**
