# O for serve para quando queremos executar um bloco de código determinado número de vezes baseado em uma condição

# Existem algumas maneiras de implementar o laço for, sendo a mais comum para iniciantes a que utiliza um intervalo para definir o início do laço, o fim dele e o valor incrementado a cada iteração

# A sintaxe mais básica é a seguinte:
for i in range(5):
    print(i)

# Ao executar o código acima, será printado no terminal os números de 0 a 4

# Nesse trecho de código, "i" vem de iterador e representa nossa variável temporária que guarda o valor de cada iteração. o "range" é uma classe do python que representa um intervalo de valores.
 
# O número 5 dentro do parênteses representa até onde o nosso laço vai percorrer (ponto de parada). 

# Por padrão, passando apenas o 5 como parâmetro, o laço iniciará em 0 (variável i receberá o valor 0 na primeira iteração) e o valor incremental será 1 (a cada iteração a variável i terá seu valor alterado para ele próprio mais um)



# E se eu quiser definir além do ponto de parada, o ponto de partida do meu laço?

# Para isso, a sintaxe é a seguinte:
for i in range(1, 5):
    print(i)

# Ao executar o código acima, será printado no terminal os números de 1 a 4

# Diferente do laço anterior, o primeiro número do parênteses representa o ponto de partida do laço e o segundo número o ponto de parada. No exemplo acima, o laço iniciará em 1 e irá parar em 5



# Tá, mas e se eu também quiser mudar o valor incremental padrão?

# A sintaxe é a seguinte:
for i in range(1, 10, 2):
    print(i)

# Ao executar o código acima, será printado no terminal os números ímpares de 1 a 10

# A única diferença desse laço para o anterior, é que estamos alterando o valor incremental para 2, ou seja, o laço começa em 1 e ao invés de na próxima iteração ir para 2, irá para 3, pois passamos 2 como o valor incremental 



# Agora pratique exercícios até cair os dedos e aprender a como usar corretamente