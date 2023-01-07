# Tic Tac Toe

![license](https://img.shields.io/badge/license-mit-green)
![python-version](https://img.shields.io/badge/python-v3.9-success)
![module](https://img.shields.io/badge/pip-pygame-critical)
![size](https://img.shields.io/badge/assets_size-1.55kB-blue)


Ce petit programme lance un tic tac toe basique développé 
en **python** avec la librairie *pygame*

## Architecture du projet

```
├── assets
│   ├── circle.png
│   └── cross.png
├── const.py
├── game.py
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
    WHITE = (231, 242, 0)
```

Les quatre constantes générales sont :
```python
class Game(Enum):
    SCREEN_SIZE = 500
    PLAYERS = ('x', 'o')
    TOKEN_IMAGE = ['./assets/cross.png', './assets/circle.png']
    TOKEN_POSITION = [
        [(50, 50), (200, 50), (350, 50)],
        [(50, 200), (200, 200), (350, 200)],
        [(50, 350), (200, 350), (350, 350)]
    ]
```

Elles représentent :
- ``SCREEN_SIZE`` la taille de la fenêtre *(en pixel)*
- ``PLAYERS`` la liste des joueurs
- `TOKEN_IMAGE` la source des sprites de chaque joueur
- `TOKEN_POSITION` la différente position des sprites sur le plateau
