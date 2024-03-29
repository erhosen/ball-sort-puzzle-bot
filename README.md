# Ball Sort Puzzle Bot

<p align="center">
   <img src="img/logo_bsp_small.png" height="480" />
   &nbsp;&nbsp;&nbsp;&nbsp;
   <img src="img/demo.gif" />
</p>

Telegram bot, that solves Ball Sort Puzzle mobile game. Written in Python, hosted by serverless Yandex.Function.

You can find a profound description about how it works [here](https://habr.com/ru/post/536086/) [Russian].

**Usage**
---

* Add the Telegram Bot [@ballsortpuzzlebot](https://t.me/ballsortpuzzlebot) to list of your contacts.
* Send him a screenshot of the Ball Sort Puzzle game.
* You will receive a solution. That's all!

**How to Contribute**
---

1. Clone the repo and create a new branch:
    + `$ git checkout -b name_for_new_branch`.

1. Install all dependencies with [`Poetry`](https://python-poetry.org/)
    + `$ poetry install`

1. Make sure that project is ready for development by running tests
    + `$ make test`

1. Make changes and test

1. Don't forget to format your code, by running
    + `$ make format`
    + or you can install [`pre-commit`](https://pre-commit.com/), that will do it for you

1. Submit Pull Request with comprehensive description of changes
