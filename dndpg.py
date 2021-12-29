import sys
import random
import time
random.seed(time.time())

#print animato
def p(line):
    for x in line:
        print(x, end = "")
        sys.stdout.flush()
        time.sleep(0.01)
    print("")

#sceglie un valore casuale appartenente all'array    
def r(array):
    size = len(array)
    r_value = random.randrange(0, size)
    return array[r_value]

#prende un valore dall'array (casualmente), cancellandolo
def pick(array):
    size = len(array)
    value = "null"
    while(value == "null"):
        index = random.randrange(0, size)
        value = array[index]
    array[index] = "null"
    return value

#trova il modificatore, dato un numero
def fmod(x):
    if (x <= 3):
        mod = "-3"
    elif (x <= 5):
        mod = "-2"
    elif (x <= 8):
        mod = "-1"
    elif (x <= 12):
        mod = "+0"
    elif (x <= 15):
        mod = "+1"        
    elif (x <= 17):
        mod = "+2"
    else:
        mod = "+3"
    mod = "(" + mod + ")"
    return mod

#crea un animale casuale per il ranger
def ranger_animale():
    specie = ["Lupo","Puma","Orso","Aquila","Cane","Falco","Gatto","Gufo","Piccione","Ratto","Mulo"]
    ferocia = ["veloce","robusto","enorme","calmo","adattabile","riflessi pronti","instancabile","mimetico","feroce","minaccioso","sensi acuti","furtivo"]
    astuzia = ["cacciare","cercare","esplorare","fare da guardia","combattere","dare spettacolo","lavori pesanti","viaggiare"]
    istinto = ["codardo","selvaggio","lento","deperito","spaventoso","smemorato","ostinato","zoppo"]
    sex = ["Maschio","Femmina"]
    p("")
    p("+-----[Compagno]-----------")
    p("| Nome: \t???")
    p("| Specie: \t"+r(specie))
    p("| Sesso: \t"+r(sex))
    p("| Armatura: \t3")
    p("| Tratto 1: \t"+r(ferocia))
    p("| Tratto 2: \t"+r(astuzia))
    p("| Tratto 3: \t"+r(istinto))
    p("+--------------------------")
    
def crea_zaino(classe):
    p("")
    p("+-----[Equipaggiamento]----")
    if (classe == "Ranger"):
        armi = ["Lancia","Spada"]
        p("| Armatura di cuoio rigido")
        p("| Freccia x3")
        p("| Arco da caccia")
        p("| "+r(armi))
    elif (classe == "Guerriero"):
        if (armatura == 1):
            p("| Armatura buona")
        else:
            p("| Armatura pesante")
        p("| Arma fidata")
        p("| Pozioni curative x2")
        p("| Antidoto")
        p("| Erbe unguenti")
        p("| Monete x22")
    elif (classe == "Druido"):  
        armi = ["Shillelagh","Bastone a 2 mani","Lancia"]
        misc = ["Erbe e unguenti","Erba pipa","Antidoto x3"]
        defe = ["Scudo di legno","Armatura di cuoio"] 
        p("| Ricordo della tua terra")
        p("| "+r(defe))
        p("| "+r(armi))
        p("| "+r(misc))
    elif (classe == "Paladino"):
        armi = ["Alabarda","Spada lunga"]
        p("| Armatura buona")
        p("| "+r(armi))
    elif (classe == "Mago"):
        armi = ["Pugnale","Bastone"]
        p("| Libro degli incantesimi")
        if (armatura == 1):
            p("| Armatura di cuoio rigido")
        else:
            p("| Borsa di libri")
            p("| Pozioni curative x3")
        p("| Antidoto x3")
    elif (classe == "Ladro"):
        armi = ["Pugnale","Spada"]
        armi2 = ["Pugnali da lancio x3","Arco logoro e 3 frecce"]
        p("| Armatura di cuoio rigido")
        p("| "+r(armi))
        p("| "+r(armi2))
        p("| Veleno (3 usi)")
        p("| Monete x10")
        p("| Pozione curativa")
    elif (classe == "Barbaro"):
        armi = ["Ascia","Spada lunga"]
        if (armatura == 1):
            p("| Armatura buona")
        p("| Pugnale")
        p("| "+r(armi))
        p("| Ricordo della tua casa")      
    elif (classe == "Chierico"):
        arm = ["Armatura buona","Scudo"]
        armi = ["Martello da guerra","Mazza","bastone"]
        p("| "+r(arm))
        p("| "+r(armi))
        p("| Simbolo della divinità")
        p("| Pozione curativa")
    elif (classe == "Bardo"):
        strumento = ["Mandolino","Liuto","Cornamusa","Corno","Viiolino","Canzoniere"]
        armi = ["Spada","Arco e pugnale"]
        misc = ["Bende","Erba pipa","Monete x3"]
        if (armatura == 1):
            p("| Armatura buona")
        else:
            p("| Abiti appariscenti")
        p("| "+r(strumento))
        p("| "+r(armi))
        p("| "+r(misc))
    else:
        p("| ???")
    p("+--------------------------")

#crea l'arma caratteristica del guerriero
def crea_arma_guerriero():
    arma = ["Spada","Ascia","Martello","Lancia","Mazzafrusta","Nocche"]
    tipo = ["corta","media","lunga"]
    dettagli = ["uncinata","affilata","seghettata","lucente","enorme","ben costruita","versatile","bilanciata"]
    aspetto = ["antica","senza difetti","ornata","sinistra","insanguinata"]
    p("")
    p("+-----[Arma fidata]--------")
    p("| Arma: \t" + r(arma) + " " + r(aspetto))
    p("| Tipo: \t" + r(tipo) + ", " + r(dettagli))
    p("+--------------------------")
    
#Dati principali
races = ["Elfo","Halfling","Nano","Gnomo","Mezzelfo","Mezzorco","Orco","Umano","Dragonide","Tiefling"]# classi classiche
#races = ["Elfo bianco","Nano","Gnomo","Elfo nero","Orco","Goblin","Umano","Kenku","Tiefling"]# classi Sussurri dall'Abisso
sex = ["Maschio","Femmina"]
classes = ["Barbaro","Bardo","Chierico","Druido","Guerriero","Paladino","Ranger","Ladro","Mago"]
level = 1
allineamento1 = ["Buono","Neutrale","Malvagio"]
allineamento2 = ["Legale","Neutrale","Caotico"]
STR = 0
DEX = 0
CON = 0
INT = 0
WIS = 0
CHA = 0
#stat_type = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
stat_values = [16,15,13,12,9,8]# valori generici

#Dati delle abilità
ranger = (
        "SEGUIRE LE TRACCE\n"
        "Quando segui una traccia lasciata da qualche creatura, tira +Sag.\n"
        "✴Con un 7+, riesci a seguire le tracce della creatura fino al prossimo significativo cambio di direzione o di mezzo di spostamento.\n"
        "✴Con un 10+, puoi scegliere un'opzione:\n"
        " • Ottieni un'informazione utile sulla tua preda, il GM ti dirà che cosa\n"
        " • Determini cosa ha causato l'interrompersi della traccia\n\n"

        "COLPO MIRATO\n"
        "Quando attacchi un nemico sorpreso o indifeso a distanza, puoi scegliere di infliggere i tuoi "
        "danni o nominare una parte specifica del suo corpo e tirare+Des.\n"
        " • Testa – ✴10+: Come 7–9, e infliggi i tuoi danni; ✴7-9: Per qualche momento il bersaglio è stordito.\n"
        " • Braccia – ✴10+: Come 7–9, e infliggi i tuoi danni; ✴7-9: Il bersaglio fa cadere qualunque cosa abbia in mano.\n"
        " • Gambe – ✴10+: Come 7–9, più i tuoi danni; ✴7-9: Il bersaglio zoppica e si muove lentamente.\n\n"

        "COMPAGNO ANIMALE\n"
        "Hai un animale. Non puoi parlargli, ma segue i tuoi ordini.\n"
)
guerriero = (
        "PIEGARE SBARRE, SOLLEVARE CANCELLI\n"
        "Quando usi la forza bruta per distruggere qualcosa, tira +For.\n\n"

        "CORAZZATO\n"
        "Te ne fotti che l'armatura che indossi è ingombrante\n\n"

        "ARMA CARATTERISTICA\n"
        "La tua arma fidata, la conosci meglio di mammita.\n"
)
druido = (
        "NATO DALLA TERRA\n"
        "Puoi prendere la forma di qualsiasi animale che vive dentro la"
        "terra con cui sei in armonia.\n\n"

        "STUDIARE L'ESSENZA\n"
        "Se passi del tempo a contemplare un animale puoi assumerne la forma usando mutaforma.\n\n"

        "PRESERVATO DALLA NATURA\n"
        "Non hai bisogno di bere o mangiare.\n\n"

        "LINGUA DEGLI SPIRITI\n"
        "Riesci a capire la lingua degli animali della tua terra.\n\n"

        "MUTAFORMA\n"
        "Puoi prendere la forma di qualunque animale la cui essenza hai studiato "
        "o che vive nella tua Terra: assieme agli oggetti che porti con te, ti "
        "trasformi in una perfetta copia dell'animale scelto. Acquisici qualunque "
        "capacità o debolezza innata di questa forma: artigli, ali, branchie,"
        "respirare acqua invece che aria. Usi le tue normali statistiche ma alcune"
        "mosse potrebbero essere difficili da attivare: un gattino potrebbe avere "
        "difficoltà a combattere un ogre. Il GM ti dirà anche una o più mosse "
        "associate con la tua nuova forma animale. Spendi 1 presa per fare una di "
        "quelle mosse. Una volta finita la presa, ritorni alla tua forma normale. "
        "In qualunque momento puoi spendere tutta la presa per tornare alla tua forma normale.\n"
)
paladino = (
        "IMPOSIZIONE DELLE MANI\n"
        "Quando tocchi qualcuno e preghi per la sua salute tira +Car.\n"
        "Con 10+ guarisci 1d8 danni e rimuovi una malattia\n"
        "Con 7-9 guarisci 1d8 danni ma vengono trasferiti a te\n\n"

        "CORAZZATO\n"
        "Te ne fotti delle armature ingombranti\n\n"

        "IO SONO LA LEGGE\n"
        "Quando dai un ordine ad un personaggio basandoti sulla tua autorità"
        "Divina tira un dado +car\n"
        " - con 7+ il png può obbedirti, scappare o attaccarti\n"
        " - con 10+ hai in aggiunta un +1 al prossimo tiro contro di lui\n"
        " - con un fallimento il png se ne fotte di ciò che dici e hai -1 al prossimo tiro.\n\n"

        "MISSIONE\n"
        "Hai un obiettivo divino, un traguardo da raggiungere con la preghiera e la purificazione rituale:\n"
)
mago = (
        "LIBRO DEGLI INCANTESIMI\n"
        "Hai padroneggiato diversi incantesimi e li hai trascritti nel tuo libro "
        "degli incantesimi. Inizi il gioco con tre magie di primo livello e tutti i "
        "trucchetti. Ogni volta che sali di livello, aggiungi un nuovo incantesimo "
        "del tuo livello o inferiore al tuo libro.\n\n"

        "PREPARARE INCANTESIMI\n"
        "Quando trascorri del tempo non interrotto (un'ora o più) in quieta contemplazione del tuo libro degli incantesimi:\n"
        " • Perdi tutti gli incantesimi che avevi preparato\n"
        " • Prepara nuovi incantesimi a tua scelta dal tuo libro degli incantesimi il cui livello totale non superi il tuo livello+1\n"
        " • Prepara tutti i trucchetti, che non contano mai ai fini del limite.\n\n"
    
        "LANCIARE INCANTESIMI\n"
        "Quando lanci un incantesimo che hai preparato, tira+Int. ✴Con un 10+, "
        "l'incantesimo viene lanciato con successo e non lo dimentichi: puoi "
        "lanciarlo nuovamente in futuro. ✴Con un 7–9, l'incantesimo viene lanciato, ma scegli un'opzione:\n"
        " • Attiri attenzioni indesiderate o metti te stesso in difficoltà. Il GM ti dirà come.\n"
        " • L'incantesimo disturba il tessuto della realtà: prendi -1 continuato a lanciare incantesimi fino al prossimo momento in cui prepari incantesimi.\n"
        " • Dopo che l'hai lanciato, dimentichi l'incantesimo. Non puoi più lanciarlo fino a quando non prepari incantesimi di nuovo.\n"
        "Nota che mantenere attivo un incantesimo con effetti continuati potrebbe causare una penalità al tuo tiro di lanciare incantesimi.\n\n"

        "SCUDO MAGICO\n"
        "Quando plasmi un incantesimo continuato in uno scudo di magia arcana per deviare un attacco, l'incantesimo termina e sottrai il suo livello al danno ricevuto.\n\n"

        "RITUALE\n"
        "Quando attingi a un luogo di potere per creare un effetto magico, di' al GM cosa stai cercando di fare. Gli effetti dei rituali sono sempre possibili, ma il GM ti darà da una a quattro delle seguenti condizioni:\n"
        " • Ci vorranno giorni/settimane/mesi\n"
        " • Prima dovrai ____\n"
        " • Avrai bisogno di aiuto da ____\n"
        " • Serviranno molti soldi\n"
        " • Il meglio che puoi fare è una versione minore, inaffidabile e limitata\n"
        " • Tu e i tuoi alleati rischierete di mettervi in pericolo con ____\n"
        " • Dovrai disincantare ____ per farlo\n"
)
ladro = (
        "ESPERTO DI TRAPPOLE\n"
        "Quando spendi un momento per controllare un'area pericolosa, tira+Des. ✴Con un 10+, prendi 3. ✴Con un 7–9, prendi 1. Spendi la tua presa mentre attraversi l'area per fare queste domande:\n"
        " • C'è una trappola qui, e se sì, che cosa la attiva?\n"
        " • Che cosa fa la trappola quando viene attivata?\n"
        " • Che cos'altro c'è qui di nascosto?\n\n"

        "TRUCCHI DEL MESTIERE\n"
        "Quando scassini serrature, borseggi o disattivi trappole, tira+Des. ✴Con un 10+, lo fai senza problemi. ✴Con un 7–9, lo fai comunque, ma il GM ti offrirà due opzioni tra sospetto, pericolo o costo.\n\n"

        "ATTACCO FURTIVO\n"
        "Quando attacchi un nemico indifeso o preso di sorpresa con un'arma da mischia, puoi scegliere di infliggere i tuoi danni o di tirare +Des.\n"
        " ✴Con un 10+ scegli due opzioni.\n"
        " ✴Con un 7–9 scegline una.\n"
        "  • Non entri in corpo a corpo col nemico\n"
        "  • Infliggi i tuoi danni +1d6\n"
        "  • Ti crei un vantaggio, +1 al prossimo tiro tuo o di un alleato contro il nemico\n"
        "  • Riduci la sua armatura di uno finché non la ripara\n\n"

        "MORALITà FLESSIBILE\n"
        "Quando qualcuno prova a individuare il tuo allineamento puoi dirgli l'allineamento che preferisci.\n\n"

        "AVVELENATORE\n"
        "Sei un esperto nella preparazione e nell'uso dei veleni. Scegli un veleno dalla lista sotto; quel"
        "veleno non è più pericoloso per te. Inizi anche con tre utilizzi del veleno che hai scelto. Ogni"
        "volta che hai tempo di raccogliere i materiali e un posto sicuro per distillare puoi creare tre"
        "utilizzi del tuo veleno prescelto gratuitamente. Nota che alcuni veleni sono Applicati, il che"
        "significa che devi applicarlo con cautela al bersaglio o a qualcosa da mangiare o da bere. I veleni"
        "a contatto hanno soltanto bisogno di toccare il bersaglio, puoi anche usarli sulla lama di un'arma.\n"
        " • Olio di Tagete (applicato): Il bersaglio cade in un sonno leggero\n"
        " • Ambrosia rossa (a contatto): Il bersaglio infligge -1d4 danni continuati finché non viene curato.\n"
        " • Rodiola dorata (applicato): Il bersaglio tratta la prossima creatura che vede come un amico a meno che non venga provato altrimenti.\n"
        " • Lacrime di Serpente (a contatto): Chiunque infligga danni al bersaglio tira due volte e prende il miglior risultato.\n"
)
barbaro = (
    "INGOMBRANTE\n"
    "Ignori l'etichetta ingombrante sull'armatura che indossi.\n\n"

    "APPETITI ERCULEI\n"
    "Gli altri si accontenteranno di un semplice sorso di vino o del potere su una manciata di servi,"
    "ma tu vuoi di più. Scegli due appetiti. Se devi tirare per una mossa mentre persegui questi"
    "appetiti, tiri 1d6+1d8 invece di 2d6. Se il d6 è il dado più alto dei due, il GM introdurrà una"
    "complicazione o un pericolo derivante dalle tue azioni avventate.\n\n"

    "DOMINARE LA MORTE\n"
    "Prendi +1 continuato ai tiri di ultimo respiro. Quando esali il tuo ultimo respiro, con un 7–9"
    " sei tu a fare un'offerta alla Morte in cambio della tua vita. Se la Morte accetta ti riporterà in"
    " vita. Se no, morirai.\n\n"

    "UN FASCIO DI MUSCOLI\n"
    "Mentre impugni un'arma, ottiene le etichette devastante e possente.\n\n"

    "COSA STAI ASPETTANDO?\n"
    "Quando lanci una sfida ai tuoi nemici, tira+Cos. ✴Con un 10+ ti trattano come la minaccia"
    "più importante di cui occuparsi e ignorano i tuoi compagni, prendi +2 danni continuati"
    "contro di loro. ✴Con un 7–9 solo alcuni (i più deboli o i più avventati tra lor) cadono preda"
    "della tua provocazione\n"
)
chierico = (
    "DIVINITà\n"
    "Servi e veneri una divinità o una potenza che ti concede incantesimi.\n\n"

    "ASSISTENZA DIVINA\n"
    "Quando supplichi la tua divinità in accordo con il precetto della tua religione, ottieni qualche"
    "informazione utile o una benedizione relativa al dominio della tua divinità. Il GM ti dirà che cosa.\n\n"

    "COMUNIONE\n"
    "Quando trascorri del tempo non interrotto (un'ora o più) in quieta comunione con la tua"
    "divinità:\n"
    " • Perdi tutti gli incantesimi che ti erano stati concessi\n"
    " • La tua divinità ti concede dei nuovi incantesimi a tua scelta il cui livello totale non superi il tuo livello+1.\n"
    " • Prepara tutte le orazioni, che non contano mai ai fini del limite.\n\n"

    "LANCIARE INCANTESIMI\n"
    "Quando lanci un incantesimo concessoti dalla tua divinità, tira+Sag.\n"
    " ✴Con un 10+, l'incantesimo viene lanciato con successo e la tua divinità non lo revoca: puoi lanciarlo nuovamente in futuro.\n"
    " ✴Con un 7–9, l'incantesimo viene lanciato, ma scegli un'opzione:\n"
    " • Attiri attenzioni indesiderate o metti te stesso in difficoltà. Il GM ti dirà come.\n"
    " • Il lancio ti allontana dalla tua divinità: prendi -1 continuato a lanciare incantesimi fino alla tua prossima comunione.\n"
    " • Dopo che l'hai lanciato, la tua divinità revoca l'incantesimo. Non puoi più lanciarlo fino alla tua prossima comunione.\n"
    "Nota che mantenere attivo un incantesimo con effetti continuati potrebbe causare una penalità al tuo tiro di lanciare incantesimi.\n\n"

    "SCACCIARE NON MORTI\n"
    "proteggerti, tira+Sag. ✴Con un 7+, fintanto che continui a pregare "
    "e brandire il tuo simbolo sacro, nessun non morto può avvicinarsi "
    "a te. ✴Con un 10+ i non morti intelligenti sono temporaneamente "
    "storditi dalla luce del tuo dio e quelli non senzienti fuggono. Se "
    "effettui un'azione aggressiva contro un non morto mentre scacci "
    "non morti l'effetto termina, e possono agire come di consueto. I non "
    "morti intelligenti, i vampiri e simili, riusciranno a trovare comunque "
    "modi di farti del male da lontano. Sono abbastanza furbi.\n"
)
bardo = (
    "ARTE ARCANA\n"
    "Quando infondi un semplice incantesimo in un'esibizione della tua arte, scegli un alleato "
    "e un effetto:\n"
    " • Guarisci 1d8 danni\n"
    " • +1d4 al prossimo tiro di danno\n"
    " • La mente del bersaglio viene purificata da un incantesimo\n"
    " • La prossima volta che qualcuno aiuta con successo il bersaglio, questi prende +2 invece che +1\n"
    "Dopodiché tira+Car.\n"
    " ✴Con un 10+, l'alleato subisce l'effetto desiderato.\n"
    " ✴Con un 7-9, il tuo incantesimo funziona, ma attiri attenzioni indesiderate oppure la magia riverbera anche su altri bersagli, a scelta del GM.\n\n"

    "CONOSCENZE BARDICHE\n"
    "Quando ti imbatti per la prima volta in una creatura, un luogo o un oggetto importante (a "
    "tua discrezione) che rientri nelle tue conoscenze bardiche puoi fare al GM una domanda al "
    "riguardo, il GM ti risponderà sinceramente. Il GM potrà chiederti da quale racconto, canzone "
    "o leggenda hai tratto questa informazione.\n\n"

    "AFFASCINANTE E ONESTO\n"
    "Quando parli onestamente con qualcuno, puoi fare al giocatore che lo interpreta (il GM se "
    "è un personaggio del GM) una domanda tra le seguenti. Deve rispondere onestamente, e può "
    "farti a sua volta una domanda dalla lista (a cui devi rispondere onestamente).\n"
    "• Di chi sei al servizio?\n"
    "• Cosa vorresti che io facessi?\n"
    "• Come posso fare in modo che tu ______?\n"
    "• Cosa provi realmente in questo momento?\n"
    "• Qual è il tuo desiderio più grande?\n\n"

    "UN PORTO NELLA TEMPESTA\n"
    "Quando torni in un luogo civilizzato che hai visitato in precedenza, di' al GM quando ci sei "
    "stato l'ultima volta. Lui ti dirà che cosa è cambiato da allora.\n"
)
#Dati anagrafici----------------------------------------------------------------------
p("+-----[Identità]-----------")
p("| Nome: \t???")
p("| Sesso: \t" + r(sex))
p("| Razza: \t" + r(races))
CLASS = r(classes)
p("| Classe: \t" + CLASS)
p("| Livello: \t" + str(level))
p("| Carattere: \t" + r(allineamento1) + " - " + r(allineamento2))
p("+--------------------------")

#Creazione statistiche
STR = pick(stat_values)
DEX = pick(stat_values)
CON = pick(stat_values)
INT = pick(stat_values)
WIS = pick(stat_values)
CHA = pick(stat_values)

#Dati dipendenti dalla classe
global armatura
if (CLASS == "Barbaro"):
    pf = 8
    damage_dice = "1d10"
    atks = []
    abi = []
    armatura = random.randrange(0,1)
elif (CLASS == "Chierico"):
    pf = 8
    damage_dice = "1d6"
    atks = []
    abi = []
    armatura = 1
elif (CLASS == "Ranger"):
    pf = 8
    damage_dice = "1d8"
    atks = []
    abi = []
    armatura = 1
elif (CLASS == "Bardo"):
    pf = 6
    damage_dice = "1d6"
    atks = []
    abi = []
    armatura = random.randrange(0,1)
elif (CLASS == "Druido"):
    pf = 6
    damage_dice = "1d6"
    atks = []
    abi = []
    armatura = 1
elif (CLASS == "Ladro"):
    pf = 6
    damage_dice = "1d8"
    atks = []
    abi = []
    armatura = 1
elif (CLASS == "Guerriero"):
    pf = 10
    damage_dice = "1d10"
    atks = []
    abi = []
    armatura = random.randrange(1,2)
elif (CLASS == "Paladino"):
    pf = 10
    damage_dice = "1d10"
    atks = []
    abi = []
    armatura = 2
elif (CLASS == "Mago"):
    pf = 4
    damage_dice = "1d4"
    atks = []
    abi = []
    armatura = random.randrange(0,1)

p("")
p("+-----[Combattimento]------")
p("| Max HP: \t"+str(pf))
p("| HP: \t\t"+str(pf))
p("| Armatura: \t"+str(armatura))
p("| Danno: \t"+damage_dice)
p("+--------------------------")

#Stampa statistiche
p("")
p("+-----[Statisticche]--------")
p("| Forza: \t" + str(STR) + "\t" + fmod(STR))
p("| Destrezza: \t" + str(DEX) + "\t" + fmod(DEX))
p("| Costituzione:\t" + str(CON) + "\t" + fmod(CON))
p("| Intelligenza:\t" + str(INT) + "\t" + fmod(INT))
p("| Saggezza: \t" + str(WIS) + "\t" + fmod(WIS))
p("| Carisma: \t" + str(CHA) + "\t" + fmod(CHA))    
p("+--------------------------")

#Attacchi
#p("")
#p("+-----[Attacchi]-----------")
#p("+--------------------------")

#Equipaggiamento
crea_zaino(CLASS)

if (CLASS == "Ranger"):
    ranger_animale()
elif (CLASS == "Druido"):
    terra = ["Foresta","Pianura","Deserto","Delta del fiume","Profondità della terra","Isole","Mare aperto","Montagne","Circolo artico","Arida steppa"]
    p("")
    p("+-----[Terra d'origine]----")
    p("| "+r(terra))
    p("+--------------------------")
elif (CLASS == "Paladino"):
    scopo = ["Uccidere ???, il flagello delle terre","Difendere ??? dalle iniquità","Scoprire la verità riguardo a ???"]
    benedizioni = ["Senso dell'orientamento verso ???","Invulnerabilità a ???","Segno inequivocabile dell'autorità divina","Visione oltre le menzogne","Voce che trascende da ogni linguaggio","Libertà dalla fame, sete o sonno"]
    voto = ["Onore - Niente trucchi o tattiche da codardo","Temperanza - Non mangiare/bere","Devozione - Fare riti sacri ogni giorno","Valore - non lasciar vivere una creatura malvagia incontrata","Onestà - Non dire menzogne","Ospitalità - Aiutare i bisognosi"]
    p("")
    p("+-----[Missione]----------")
    p("| Obiettivo: \t\t"+r(scopo))
    p("| Benedizione: \t\t"+r(benedizioni))
    p("| Voto da rispettare: \t"+r(voto))
    p("+--------------------------")
elif (CLASS == "Barbaro"):
    app1 = ["Distruzione pura","Potere sugli altri","Piaceri mortali"]
    app2 = ["Conquista","Ricchezza e proprietà","Fama e gloria"]
    p("")
    p("+-----[Appetiti erculei]---")
    p("| "+r(app1))
    p("| "+r(app2))
    p("+--------------------------")
elif (CLASS == "Chierico"):
    tipo = ["Guarigione e ricostruzione","Conquista sanguinaria","Civilità","Conoscenza e cose nascoste","Reietti e dimenticati","Ciò che giace sotto"]
    precetto = ["Sanità della sofferenza - aggiungi supplica Sofferenza","Sette isolate - aggiungi supplica Ottenere Segreti","Riti sacrificali - Aggiungi supplica Offerta","Singolartenzone - aggiungi supplica Vittoria personale"]
    p("")
    p("+-----[Divinità venerata]--")
    p("| Nome: \t???")
    p("| Tipo: \t"+r(tipo))
    p("| Precetto: \t"+r(precetto))
    p("+--------------------------")
elif (CLASS == "Bardo"):
    misc = ["Incantesimi e magie","Morti e non morti","Grandi storie del mondo conosciuto","Bestiario di creature inconsuete","Le sfere planari","Leggende degli antichi eroi","Gli dei ed i loro servitori"]
    p("")
    p("+--[Conoscenze bardiche]---")
    p("| "+r(misc))
    p("+--------------------------")
elif (CLASS == "Guerriero"):
    crea_arma_guerriero()

#Privilegi
p("")
p("+-----[Abilità]------------")
if (CLASS == "Barbaro"):
    p(barbaro)
elif (CLASS == "Chierico"):
    p(chierico)
elif (CLASS == "Ranger"):
    p(ranger)
elif (CLASS == "Bardo"):
    p(bardo)
elif (CLASS == "Druido"):
    p(druido)
elif (CLASS == "Ladro"):
    p(ladro)
elif (CLASS == "Guerriero"):
    p(guerriero)
elif (CLASS == "Paladino"):
    p(paladino)
elif (CLASS == "Mago"):
    p(mago)
p("+--------------------------")

#Storia
p("")
p("+-----[Storia]-------------")
p("Scrivi qui la storia di questo epico personaggio!")
p("+--------------------------")
