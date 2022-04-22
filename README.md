# Mine Mod DB

Projeto feito em conjunto com [@julianocts98](https://github.com/julianocts98) com objetivo de explorar conceitos básicos de banco de dados na prática.

A ideia inicial é utilizar [Python](https://www.python.org/) e [PostgreSQL](https://www.postgresql.org/) para construir um programa de comando de linha para explorar relações entre mods e modpacks de [Minecraft](https://www.minecraft.net/pt-pt) e com suporte para inserção, modificação e deleção dos mods e modpacks que serão armazenados num banco de dados.

O projeto também visa explorar o trabalho em conjunto num mesmo código usando controle de versões através do [Git](https://git-scm.com/) no ambiente do [GitHub](https://github.com/).

## Instalação e Uso

É recomendado ter o [Pipenv](https://pipenv.pypa.io/en/latest/) instalado para rodar este projeto.

Clone o projeto e entre na pasta criada:

```shell
git clone https://github.com/MrTaiko314/mine-mod-db.git
cd mine-mod-db
```

Crie o ambiente virtual e instale as dependências:

```shell
python -m pipenv install
```

Entre na shell do ambiente virtual:

```shell
python -m pipenv shell
```

Rode o programa:

```shell
pipenv run main
```
