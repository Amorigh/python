print("Už je to více jak dvě hodiny co tu jen tak sedíš a přemýšlíš jak se dostat ven.")
print("Neustále ti totiž vrtá hlavou, proč by někdo stavěl zrovna čtvery dveře vedle sebe.")
print("Ze stropu odkud jsi sem propadl prosvítá kousek světla, díky kterému zjišťuješ, že každé dveře jsou jiné.")
print("Ty první jsou ze ztrouchnivělého dřeva, ty druhé jsou poměrně nové z leštěného dřeva,")
print("třetí jsou z větší části kamenné a porostlé mechem a čtvrté jsou z mosazi.")
print("Na strop nedosáhneš, a proto ti nezbývá nic jiného, než vyzkoušet jedny z těch dveří...") 
print(" 1 - ztrouchnivělé dveře \n 2 - nové dřevěné dveře \n 3 - kamené, mechové dveře \n 4 - mosazné dveře ")
a = int(input())


if (a == 1):
    print("Jakmile zatáhneš za kliku, něco za dveřmi spadne a ty uskočíš, po chvíli je opatrně otevřeš a zjišťuješ, že mistnost je starý sklad. To co spadlo bylo koště, které nyní leží na zemi. Když se porozhlédneš, možná najdeš něco zajímavého.\n 1 - Podívat se do prava \n 2 - Podívat se do leva \n 3 - Podívat se před sebe")
    a1 = int(input())
    
    if (a1 == 1):
        print("Potom co jsi dal na stranu starou bednu se na tebe převrátila skříň. Odtud se už asi nedostaneš...")
    
    elif (a1 == 2):
        print("Potmě nahmatáš něco připomínající páčidlo, ovšem když vyjdeš do předešlé místnosti, tak ti to páčidlo již zdaleka nepřipomíná, nýbrž hodně zdeformovanou trubku. Jdeš se proto podívat zpět do skladu a stále hledáš něco užitečného. Po pár minutách hledání stále nic nenacházíš a slyšíš jak se dveře zabouchly. Nyní již v kompletní tmě se snažíš trubkou rozbít ony dveře, ale marně. Nic nevidíc se uchyluješ ke spánku v domění, že tě někdo snad přijde zachránit, ze spánku se ale neprobudíš...")
    
    elif (a1 == 3):
        print("Před tebou se nachází dveře zaskládané starými věcmi, proto harampádí odklidíš a otevřeš dveře do další místnosti, která je chabě osvětlena jedinou svící stojící na stole uprostřed místnosti. Chopíš se svíce a svítíš si na cestu. Z místnosti vedou dvoje dveře, oboje stejné, zašlé, plísní prorostlé, dřevěné dveře. Které si vybereš? \n 1 - Ty nalevo \n 2 - Ty napravo")
        a2 = int(input())
        
        if (a2 == 1):
            print("Otvíráš ty nalevo. Potom co je otevřeš, tak na tebe spadnou. Zhasnou ti svíci a ty jsi zase beze světla. Každopádně dveře odstrčíš a zajímá tě, co se skrývá v místnosti před tebou. Jelikož nic nevidíš, je pro tebe těžké rozpoznat co tato místnost skrývá. Slyšíš kroky a znepokojuje tě to. Proto se nahlas zeptáš zda-li tam nikdo není. Nikdo ti ovšem neodpoví a místo toho se kroky zrychlily na běh. Otočíš se a vidíš stínovou postavu jak proti tobě vybíhá ze dveří, které jsi před chvílí otevřel, vrhá se přímo na tebe, povaluje tě na zem a začíná te škrtit. \n 1 - Praštit do místa žeber \n 2 - Kopnout do místa rozkroku")
            a3 = int(input())
            
            if (a3 == 1):
                print("Postava nepolevuje a ty již nemáš dost kyslíku...")
            
            elif (a3 == 2):
                print("Postava se svalila na stranu a ty se od ní suneš co nejdál lapajíc po dechu. Vidíš jak postava vstává a blíží se k tobě a zase se na tebe vrhá a cítíš bodavou bolest v oblasti břicha. Postava se od tebe vzdaluje a mizí. Ty se ovšem nedokážeš hýbat, protože ta bolest je stále horší a horší. Začínáš mít halucinace a pomalu zavíráš oči...")
        
        elif (a2 == 2):
            print("Otvíráš ty napravo. V chabém světle vidíš v rohu místnosti pohozené, vezmeš si ho s sebou. Naproti jsou další dveře. Vstupuješ do nich a nestačíš se divit. Místnost je čádně osvětlena a po své pravici vidíš pranýř... CELÝ OD KRVE! Vyděšeně se rozhlížíš po místnosti dále a vidíš oprátku s mrtvolu po své levici. Dveře se zabouchly?! Světlo začalo blikat a celá struktura místnosti se začala otřásat. Ve stropě se utvořila díra a vylezlo z ní něco, co svou stavbou těla připomínalo spíše vlka než člověka. Pomalu se to k tobě blíží. Nacházíš se v bezvýchodné situaci, jakmile se to do tebe zakousne, protože žádné údery ani kopy nepomáhají. Pokoušíš se uniknout, ale marně...")


elif (a == 2):
    print("Otevřeš druhé dveře. Jen jakmile je otevřeš, tak na tebe něco vyskočí, tedy lépe řečeno někdo. Člověk, muž, jež má obličej celý špinavý od sazí. V očích mu vidíš chtíč zabíjet, ale i ztrach ze smrti. Každý z opačné strany místnosti se navzájem sledujete. Vše co na něm vidíš je, že není viditelně ozbrojen. Musíš něco udělat, dřív než on!  \n 1 - *Kdo jsi a co tu děláš?*/Promluvit si/ \n 2 - Vrhnout se na něj a pokusit se ho zpacifikovat dříve než on tebe./Útok/")
    b1 = int(input())
    
    if (b1 == 1):
        print("Muž na tebe nechápavě kouká a následně na tebe mluví jiným jazykem. Ty jsi tento jazyk již slyšel, je to ruština, ty ovšem rusky moc dobře neumíš. Stihl jsi zaregistrovat slova \x1B[3mMít, zabít a zbraň\x1B[0m. Nejsi z toho zchopen poskládat normální větu. Muž na tebe stále zírá. \n 1 - Zaútočit \n 2 - Zeptat se ho co tu dělá")
        b2 = int(input())
        if (b2 == 1):
            print("Rozbíš se na něj a vší silou se opřeš do úderu. Muž ti uhne a trefíš zeď za ním. Následně ze zadní kapsy vytáhne malý nožík a dřív než stihneš cokoliv udělat, tak ti zasadí několik bodných ran. Padáš na zem, zatímco do tebe muž bodá...")
    
    elif (b2 == 2):
        print("Muž na tebe zase spustí rusky. Tentokrát rozpoznáváš slova \x1B[3mPohyb, místnost, lano\x1B[0m. S tímto mužem se aasi nedomluvíte, proto mu dávaš posunky najevo, že ho nechceš zranit. Jakmile to muž vidí, tak se k tobě začne přibližovat. Ty ustupuješ dál a dál, až dojdeš úplně ke zdi. Než stačíš cokoliv udělat, tak tě muž udeří a ty ztratíš vědomí... \n 1 - Probudit se")
        b3 = int(input())
        if (b3 == 1):
            print("Jsi na pranýři v nějaké KRVÍ PROSÁKLÉ MÍSTNOSTI! Rozhlížíš se kolem sebe a vidíš muže s kudličkou v ruce. Zase začne něco mluvit rusky. Tentokrát mu nerozumíš ani slovo. Cítíš, jak na tebe něco zezadu sahá. Bodavá bolest následně zaplaví celé tvé tělo a slyšíš už jen slova které dobře rozumíš a nikdy by sis je nespletl s žádnými jinými, ZEMŘI...")


elif (a == 3):
    print("Otevíráš kamenné, mechem zarostlé dveře. Za nimi se nachází místnost, s kruhovým kobercem a obrovským lustrem přímo uprostřed místnosti. Na koberci je pohozena kniha. Naneštěstí je v ruštině, kterou moc neovládáš. Každopádně v ní jsou prapodivné postupy mučení lidí. Nahání ti to hrůzu, ale i tak pokračuješ do dalších dveří. Po otevření dveří se před tebou rozprostírá několik stovek vystavených mučících nástrojů. Slyšíš těžké kroky. \n 1 - Vzít něco podobného nunčaku \n 2 - Vzít něco podobného chodící holi")
    c1 = int(input())
    
    if (c1 == 1):
        print("Něco přišlo, ale nazývat to člověkem by bylo hloupé. Byl to spíše robot. Jakmile mne viděl, začal postupovat směrem ke mne. \n 1 - Hodit \n 2- Udeřit")
        c2 = int(input())
        
        if (c2 == 1):
            print("S robotem to nic neudělalo a ty jsi nyní bezbranný, NA CO JSI SAKRA MYSLEL? Byl jsi omráčen... \n 1 - Probudit se")
            c3 = int(input())
            
            if (c3 == 1):
                print("Jsi na pranýři v nějaké KRVÍ PROSÁKLÉ MÍSTNOSTI! Rozhlížíš se kolem sebe a vidíš muže s kudličkou v ruce. Začne něco mluvit rusky. Nerozumíš ani slovo. Cítíš, jak na tebe něco zezadu sahá. Bodavá bolest následně zaplaví celé tvé tělo a slyšíš už jen slova které dobře rozumíš a nikdy by sis je nespletl s žádnými jinými, ZEMŘI...")
        
        elif (c2 == 2):
            print("Udeřil jsi do robota, bohužel bez výsledku. Byl jsi umlácen k smrti.")
    
    elif (c1 == 2):
        print("Něco přišlo, ale nazývat to člověkem by bylo hloupé. Byl to spíše robot. Jakmile mne viděl, začal postupovat směrem ke mne. \n 1 - Udeřit \n 2- Píchnout")
        c4 = int(input())
            
        if (c4 == 1):
            print("Robot se zapotácel, začal jsi do něj bušit holí. Robot začal pípat, ale ty jsi nepřestával do něj bušit a neuvědomoval sis co se děje. Výbuch...")
        
        elif (c4 == 2):
            print("Zarazil jsi holi do břišního prostoru robota. Robot upadl a ty jsi rychle vyběhl dveřmi naproti. Běžel jsi jak o závod z místnosti do místnosti. Vždy do náhodných dveří. Vyrazil jsi honosněji vypadající dveře a ocitl ses na denním světle. To tě ale nevyvedlo z míry a běžel jsi stále dál a dál... \n KONEC")


elif (a == 4):
    print("Rozhodl ses pro mosazné dveře. Zjišťuješ, že jsou zamknuté a nelze je tedy normálně otevřít. Někdo vyrazí vedlejší dveře a vrhne se na tebe. Ty jsi v momentu překvapení zapomněl se jakkoli pohnout. Byl jsi omráčen... \n 1 - Probudit se")
    d1 = int(input())
    
    if (d1 == 1):
        print("Jsi na pranýři v nějaké KRVÍ PROSÁKLÉ MÍSTNOSTI! Rozhlížíš se kolem sebe a vidíš muže s kudličkou v ruce. Začne něco mluvit rusky. Nerozumíš ani slovo. Cítíš, jak na tebe něco zezadu sahá. Bodavá bolest následně zaplaví celé tvé tělo a slyšíš už jen slova které dobře rozumíš a nikdy by sis je nespletl s žádnými jinými, ZEMŘI...")