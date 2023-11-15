# Relazione di fisica

Nel momento in cui si inviano i file usare il comando 

```git
git add nome_file
git commit -m "Inserire messaggio per rendere più agevole le modifiche"
git push -u origin main
```
Eventualmente, prima di mandare degli eventuali aggiornamenti è necessario "ripescare" gli aggiornamenti dal repository online, pertanto è necessario utilizzare questi comandi:

```git
git config pull.rebase false
git pull
git push -u origin main
```
