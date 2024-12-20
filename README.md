# Experiments with whisper


## Setup
- Install poetry
  `brew install poetry`
- Create poetry env
  `poetry shell`
- Install deps
  `poetry install`


## Troubleshooting

- if you find you can't install librosa with poetry - error due to incompatble version of llvm. I solved this before by (inside poetry venev) using `pip install librosa`. Then had to downgrade numpy version and it worked. Not ideal but I couldn't fix any other way. On my other mac this worked fine, presumably because llvm version was different.

- This project was set up with python version 3.10.9. Other versions may not place nicely with the dependencies etc
