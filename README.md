# The Great Omniscient Guru

**All-knowing. All-seeing. Under no obligation to be helpful.**

Welcome, seeker of wisdom.

The Great Omniscient Guru is a terminal-based oracle.  
Ask him a question, and he shall provide an answer.

Will it be relevant? Perhaps.

Will it be accurate? The Guru finds your lack of faith disturbing.

Will it be comforting? That was never part of the agreement.

## About This Project

This is first and foremost, a creative writing project masquerading as a Python program. The intention is to create a little character that lives in your terminal, always available for consultation, though not necessarily qualified to provide it.

Comments of the code are part of the narrative. Both the responses and the source code are intended to be enjoyed as creative writing. You are therefore encouraged not only to run the program but also to read its source code.

## Features

- A collection of responces I wrote
- Randomized fortunes, because I have decided destiny is now governed by Python's `random` module. (Maybe it always have)
- An interactive consultation that continues for as long as you dare.
- Occasional unexpected farewell messages.
- Absolutely no guarantee of enlightenment, satisfaction, or continued psychological stability.


## Important Disclaimer

The Guru does not actually interpret your questions. His responses are randomly selected from a collection of prewritten answers.

This is intentional.

The Guru insists it is fate. The developer insists it is a feature.

Neither party accepts liability.

New answers will be periodically added as this project expands, basically when i feel like it.

## Installation — Summon the Guru

**Requirements:** Python 3. No external libraries required. The point of the code is to be as simple as possible

Clone the repository or download `guru.py`. There are no other files this is pretty straightforward.

Run the program from your terminal:

```bash
python3 guru.py
```

But

The Guru was never meant to be confined to a directory. Follow the instructions below to summon him from anywhere in your terminal using a single command:

```bash
guru
```

### Linux

Open your terminal and edit your shell configuration file:

```bash
# Bash
nano ~/.bashrc
```

Add this line at the bottom, replacing the path with the location of your downloaded `guru.py`:

```bash
alias guru='python3 "$HOME/{Path to file}"'
```

Save the file and reload your configuration:

```bash
# Bash
source ~/.bashrc
```

### macOS

Open Terminal and edit your Zsh configuration:

```bash
nano ~/.zshrc
```

Add the following alias, adjusting the path to your script:

```bash
alias guru='python3 "$HOME/{Path to file}"'
```

Save and reload:

```bash
source ~/.zshrc
```

### Windows (PowerShell)

Open PowerShell and create your profile file if it doesn't exist:

```powershell
if (!(Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
```

Open your PowerShell profile:

```powershell
notepad $PROFILE
```

Add this function, replacing the example path with the actual location of `guru.py`:

```powershell
function guru {
    py -3 "C:\\{Path to file}"
}
```

If `py -3` is unavailable but Python is installed, use `python` instead.

Save the file and restart PowerShell.

**Note:** PowerShell must allow your profile script to run for the command to become available.

## Consult the Guru

**Important:** Do not move or rename `guru.py` after configuring your command without updating its path in your shell configuration.

Once configured, open any terminal window and type:

```bash
guru
```

The Guru will request your inquiry. Type whatever question troubles your mortal existence and press Enter.

After receiving his wisdom, you may choose to ask another question or end your consultation.

You may also press `Ctrl+C` to interrupt the Guru, although he will not appreciate it.

---

**The Guru thanks you for your interest.**

**The Creature does not.**
