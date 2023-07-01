<h1 align="center">Pac-Man<br><br>
<img src ="https://github.com/romulodm/Pac-Man/blob/main/Sprites/Readme/pac-man.png" width = 150 heigth = 150>
</h1>

# :newspaper: Descrição do Projeto
<p align="justify ">Esse projeto foi concluído no final do meu primeiro ano da graduação, na disciplina de Algoritmos e Estrutura de Dados I. O objetivo foi colocar em prática o conhececimento
adquirido sobre POO. Tentei fazer com que o jogo ficasse o mais parecido possível com o Pac-Man original, porém, devido às limitações da biblioteca usada e também de conhecimento acerca de programação e boas práticas, o projeto final é, de certa forma, bem simples.</p>
<br>
<p align="center"><img src = "https://github.com/romulodm/Pac-Man/blob/main/Sprites/Readme/initial-window.png" width = 600 heigth = 400 ></p>

<br>

# :mag_right: Visão Geral
<p align="justify ">O jogo possui apenas um mapa, com 244 comidas no total (contando com as especiais). Sempre que as comidas se esgotam, o jogo reinicia no mesmo mapa mantendo apenas a pontução do usuário.</p>
<br>
<p align="center"><img src = "https://github.com/romulodm/Pac-Man/blob/main/Sprites/Readme/game.png" width = 600 heigth = 400 ></p>
<br>
<p align="justify ">
Esse mapa é representado através de uma matriz de tamanho 28x31, que é usada para fazer os testes de colisão do Pac-Man com as paredes. Além disso, ela é utilizada para fazer com que os fantasmas consigam traçar o seu caminho através do <b>Algoritmo A*</b>.</p>
<br>
<p align="center"><img src = "https://github.com/romulodm/Pac-Man/blob/main/Sprites/Readme/matriz.png" width = 600 heigth = 400 ></p>
<br>
<p align="justify ">Cada fantasma tem uma forma de se movimentar pelo mapa:</p>
<br>

 # :ghost: Fantasmas
 
- `Blinky (vermelho)`: Traça o seu caminho para ir diretamente até o Pac-Man (seguindo-o);
- `Pinky (rosa)`: Tem movimentos definidos e fica repetindo-os ao longo do jogo;
- `Clyde (laranja)`: Se movimenta de forma aleatória (tentando se manter no meio do mapa);
- `Inky (azul)`: Pega o quadrante e o movimento atual do Pac-Man, para tentar interceptá-lo. Se o Pac-Man estiver no quadrante 1 do mapa (parte superior esquerda) e está se movendo para a direita, o Inky vai até o quadrante 2 (parte superior direita) em um ponto pré-definido;
<br>

<p align="justify ">Vale salientar que os fantasmas que precisam traçar os seus caminhos, precisam usar o A* para definir o trajeto. Esse trajeto não é atualizado a todo momento, para não termos problema com memória. Por isso, os movimentos dos fantasmas ficam armazenados em uma lista. Toda vez que a lista fica vázia, eles traçam uma nova rota.</p>
<br>

<p align="center"><img src = "https://github.com/romulodm/Pac-Man/blob/main/Sprites/Readme/a-star.png" width = 600 heigth = 400 ></p>
<p align="center">Algoritmo A*</p>

# :hammer_and_wrench: Rodar o Projeto
* Ter `python` instalado;
* Baixar a biblioteca <a href="https://pypi.org/project/pathfinding/">pathfinding</a>: `pip install pathfinding`;
* Rodar o arquivo `main.py`;