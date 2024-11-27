# IC2_Projekt
Projekt ma za ulohu logovat terminal pouzivatelov. Script loguje commandy do csv suboru a pomocou SSH ho posiela na vzdialeny server
## Bash script
Pre spravne fungovanie je nutne pridat script do nastaveni bash.
Na koniec suboru /etc/bash.bashrc pridaj.
```bash
LOGFILE="/var/log/command_log.csv"

log_command() {
    local line
    while IFS= read -r line; do
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        USER=$(whoami)
        echo "$TIMESTAMP,$USER,$line" >> $LOGFILE
    done
}

PROMPT_COMMAND='history -a >(tail -n 1 | log_command)'
```

##How to run 
Script spustime prikazom.
```bash
python3 script.py
```
