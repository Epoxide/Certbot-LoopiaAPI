# Certbot-LoopiaAPI
Python script to automate Certbot renewal of a wildcard certificate with LoopiaAPI using [`manual-auth-hook`](https://certbot.eff.org/docs/using.html#pre-and-post-validation-hooks).

## Usage
Create a [LoopiaAPI user](https://www.loopia.se/api/). Then change `global_username` and `global_password` in `certbot_LoopiaAPI.py` to the correct user information. [Install Certbot](https://certbot.eff.org/).

### Install python3 and pip (example on Debian 10):
```bash
sudo apt install python3 python3-pip
```

### Install the required python packages:
```bash
sudo pip3 install -r requirements.txt
```

### Run Certbot using:
```bash
certbot certonly --manual -d *.example.com  --email mail@example.com --agree-tos --no-bootstrap --manual-public-ip-logging-ok --preferred-challenges dns-01 --manual-auth-hook /path/to/certbot_LoopiaAPI.py --server https://acme-v02.api.letsencrypt.org/directory
```

## An example of automating using a cronjob and restarting an nginx server:
```bash
crontab -e
```
```bash
35 4 * */2 * certbot certonly --manual -d *.example.com  --email mail@example.com --agree-tos --no-bootstrap --manual-public-ip-logging-ok --preferred-challenges dns-01 --manual-auth-hook /path/to/certbot_LoopiaAPI.py --server https://acme-v02.api.letsencrypt.org/directory && service nginx restart
```
