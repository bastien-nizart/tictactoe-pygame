# Tic Tac Toe

![License](https://img.shields.io/badge/License-MIT-green)
![python-version](https://img.shields.io/badge/Language-Python_v3.9-success)
![module](https://img.shields.io/badge/Librairies-PyGame-critical)
![size](https://img.shields.io/badge/Assets_Size-1.55kB-blue)


Ce petit programme lance un tic tac toe basique développé 
en **python** avec la librairie *pygame*

![demo](https://bastien.nizart.me/projects/tictactoe-pygame/demo.gif)


## Architecture du projet

```
├── assets
│   ├── circle.png
│   └── cross.png
├── app
│   ├── const.py
│   ├── player.py
│   └── game.py
├── main.py
└── requirements.txt
```

- `const.py` contient l'ensemble des constantes du projet
- `game.py` contient les méthodes permettant de faire fonctionner le jeu
- `main.py` contient le lancement global du programme
- `assets` contient les différents sprites du jeu

## Constantes

Le fichier `const.py` contient deux types de constantes :
- Les couleurs
- Les constantes générales

Quatre couleurs sont nécessaires au lancement, *(blanc, noir, rouge, bleu)*

Pour en rajouter d'autre il suffit de rajouter un paramètre dans l'enum `Color`
le code couleur est un tuple au format rgb. Exemple :

```python
class Color(Enum):
    COLOR = (231, 242, 0)
```

Les quatre constantes générales sont :
```python
class Game(Enum):
    SCREEN_SIZE = 500
    TOKEN_POSITION = [
        [(50, 50), (200, 50), (350, 50)],
        [(50, 200), (200, 200), (350, 200)],
        [(50, 350), (200, 350), (350, 350)]
    ]
```

Elles représentent :
- ``SCREEN_SIZE`` la taille de la fenêtre *(en pixel)*
- `TOKEN_POSITION` la différente position des sprites sur le plateau
