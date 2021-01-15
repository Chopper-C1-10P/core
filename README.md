<h1 align = "center">K-2SO</h1>

<p align="center">
    <img src = "K-2SO.png" alt="icon">
</p>

## About
A discord bot inspired by K-2SO from Star Wars. The droid is seen in
Rogue One: A Star Wars Story (2018) and is a reprogrammed imperial enforcer droid.
K-2 was reporgrammed by Captain Cassian Andor of the Rebel Alliance.
The droid is known for it's sarcasm and personality.

### Using the bot on your own machine
```bash
cd your-project-directory
git clone https://github.com/consciousatom/K-2SO.git
cd K-2SO-master
pip3 install --user --requirement requirements.txt
touch config.json
```

Now you have cloned the repository, installed the libraries used and created the file named `config.json`.
Inside this file you will have to put a bot application token, default bot prefix,
your user id, reddit client id, client secret and user agent.

This is what your `config.json` file should look like when you are done.

```json
{
    "k-2so_bot_token": "NxjOXJaoU9BDSADNDi89sa.X3S9ug.iVB1SlkWKXp8q-H8p0ohAC5rnUE",
    "k-2so_bot_prefix": "+",
    "k-2so_owner_id": "514403029898887201",
    "reddit_client_id": "ADSBOdbso2Odbo",
    "reddit_client_secret": "ASisdisd-DN98d-8dS_KDisd98GDQ",
    "reddit_user_agent": "[Reddit user agent] v1.0 u/bot_creator",
    "ipinfo_access_token": "43gv3gvg434g45v"
}
```

After you are done doing these steps, simply run the bot with:

```bash
python3 ID10/main.py
```

### Licence
This discord bot is licenced under the MIT licence, read the `LICENCE` file for more information.