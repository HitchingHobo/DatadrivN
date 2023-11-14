# DatadrivN
Som uppgift i kursen datadriven verksamhetsutveckling skulle vi skapa värde med hjälp av AI och arbetsförmedlingens öppna data,
resultat blev en annonskoll som dels scannar annonser efter maskulint och feminint kodade ord och sedan hittar en liknande annons via cosine simulatiry.

Med utgångspunkt av alla arbetsannonser från platsbanken år 2022 kokade vi ner antalet till 5442 st annonser för att göra denna relativt korta uppgift mer hanterbar, 
vårt scope var svenska annonser inom techbranchsen.

Målgruppen för vår applikation var annonsskrivare i alla former, dessa annonsskrivare får hjälp att bli av med könsbias i sina annonser genom att vår annonskoll.
Scanningen visar de maskulint kodade orden som skrivits in i inputfältet, vår ai gör om annonsen till en vector och jämför med alla andra annonser i databasen för att hitta
den mest liknande annonsen med mindre bias-ord än den man skrev in. 

För ökat värde har vi även en checklista att sin annons igenom för att säkerställa en bias-fria annons samt en "highscore" funktion som visar företag som skriver helt
könsneutrala annonser samt de generellt mest använda maskulint kodade orden i alla annonser från vår data.

Detta projekt sträckte sig över drygt fem veckor varav 1.5 gick till planering och 3.5 till iterativ programmering.
Med mer tid framför oss hade vi velat träna ytterligare en AI så att de könskodade orden i den angivna annonsen får bias-fria ersättnigsförslag.
