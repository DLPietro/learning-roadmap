### HOW TO WRITE COMMIT MESSAGES

<tipo>(<ambito>): <descrizione breve>
<riga vuota>
<descrizione estesa (opzionale)>
<riga vuota>
<informazioni aggiuntive (opzionale, es. issue, breaking change)>


### CONVENTION CODES
feat : NEW FUNCTION
fix : FIXING A BUG
docs : DOC AMMENDED
style : FORMAT CHANGED
refactor : RECSTRUCTURED
perf : OPTIMISED
test : ADD/MOD TESTS
build : BUIND AMENDED
ci : CI/CD AMENDMENTS
chore : ORDINARY MANTEINANCE
revert : REVERSING A PREVIOUS COMMIT


### STRUCTURE DESCRIPTION
feat(api): introduce breaking change nell'endpoint /users

BREAKING CHANGE: L'endpoint /users ora restituisce solo utenti attivi.
Per ottenere tutti gli utenti, usare /users?all=true.

Closes #789
Co-authored-by: Maria Rossi <maria@example.com>
LINK: https://www.conventionalcommits.org/en/v1.0.0/


### HOW TO SEE A SCRIPT ONLINE EXECUTED
LINK: https://nbviewer.org/

### HOW TO WRITE A README FILE PROPERLY
LINKS: https://github.com/othneildrew/Best-README-Template?spm=a2ty_o01.29997173.0.0.6c13c921NaPCYq     # README TEMPLATE
https://github.com/matiassingers/awesome-readme?spm=a2ty_o01.29997173.0.0.6c13c921NaPCYq                # TIPS FOR README
https://shields.io/?spm=a2ty_o01.29997173.0.0.6c13c921NaPCYq                                            # CUSTOMISED BADGE
