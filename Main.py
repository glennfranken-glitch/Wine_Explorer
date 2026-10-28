import Menus

def main():
    #Welcome screen
    Menus.show_welcome_screen()
    input()
        
    while True:
        #Main menu
        Menus.show_main_menu()
        choice = Menus.menu_choice()
        
        match choice:
            case 1:
                #Wijnencyclopedie
                Menus.show_encycl_menu()
                choice = Menus.menu_choice()

                match choice:
                    case 1:
                        #Druiven
                        Menus.menu_grapes()
                        choice = Menus.menu_choice()

                        match choice:
                            case 1:
                                #Rood
                                #Druiven laten zien
                                    #Druif selecteren
                                        #Wijnen met Druif
                                            #Wijninformatie
                                                #Wijnhuis informatie
                                                
                                continue
                            case 2:
                                #Wit
                                #Druiven laten zien
                                    #Druif selecteren
                                        #Wijnen met Druif
                                            #Wijninformatie
                                                #Wijnhuis informatie
                                continue
                            case 3:
                                #Rosé
                                #Druiven laten zien
                                    #Druif selecteren
                                        #Wijnen met Druif
                                            #Wijninformatie
                                                #Wijnhuis informatie
                                continue
                            case 4:
                                #Mouserend
                                #Druiven laten zien
                                    #Druif selecteren
                                        #Wijnen met Druif
                                            #Wijninformatie
                                                #Wijnhuis informatie
                                continue
                            case 0:
                                continue
                        continue
                    case 2:
                        #Geuren
                            # Fruitig: Rode vruchten (kers, aardbei), zwarte vruchten (braam, bes), citrus (citroen, grapefruit), of tropisch fruit (ananas, perzik).
                            # Floraal (Bloemig): Rozen, viooltjes, kamille, bloesem of vlierbloesem.
                            # Plantaardig / Groen: Gemaaid gras, groene paprika, munt, eucalyptus of buxus.
                            # Houtachtig: Cederhout, eikenhout, zaagsel of potloodslijpsel.
                            # Gekruid / Kruidig: Zwarte peper, vanille, kruidnagel, kaneel of zoethout.
                            # Etherisch / Zuivel: Boter, gist, briochebrood, yoghurt of vla (vooral bij Chardonnay).
                            # Dierlijk / Aards: Leder, stalgeur, natte herfstbladeren, paddenstoelen of wild.
                            # Branderig / Geroosterd: Koffie, cacao, toast, karamel of rook.
                            # Chemisch / Mineraal: Natte kalk, leisteen, petroleum (typisch voor Riesling) of vuursteen.
                            # Balsemachtig: Honing, hars of wax
                                #Vind druiven met het gekozen aroma
                        continue
                    case 3:
                        #Smaken
                        categories = Menus.menu_flavor()
                        choice = Menus.menu_choice()
                        selected_category = sorted(categories)[choice - 1]
                        print(selected_category)                
            case 2:
                #Wijnhuizen zoeken
                    #Zoeken op naam
                        #Zoekterm invoeren
                        #Zoekresultaten tonen
                            #Wijnhuis selecteren
                            #Wijnhuisdetails
                                #Wijnen van dit wijnhuis
                                    #Wijn selecteren
                                        #Wijninformatie
                    #Zoeken op land
                        #Land selecteren
                            #Regio selecteren
                                #Appellaties bekijken
                                    #Appellatie selecteren
                                        #Wijnhuizen tonen
                                            #Wijnhuis selecteren
                                                #Wijnhuisdetails
                                                    #Wijnen van dit wijnhuis
                                                        #Wijn selecteren
                                                            #Wijninformatie
                
                                    #Overige wijnen uit deze regio
                                        #Wijnhuizen tonen
                                            #Wijnhuis selecteren
                                                #Wijnhuisdetails
                                                    #Wijnen van dit wijnhuis
                                                        #Wijn selecteren
                                                            #Wijninformatie
                
                    #Zoeken op appellatie
                        #Appellatie zoeken of selecteren
                            #Wijnhuizen tonen
                                #Wijnhuis selecteren
                                    #Wijnhuisdetails
                                        #Wijnen van dit wijnhuis
                                            #Wijn selecteren
                                                #Wijninformatie
                
                    #Random wijnhuis
                        #Willekeurig wijnhuis tonen
                            #Wijnhuisdetails
                                #Wijnen van dit wijnhuis
                                    #Wijn selecteren
                                        #Wijninformatie
                
                # Terug
                # Hoofdmenu
                continue
            case 3:
                #Mijn proefnotities
                    #Mijn gemaakte proefnotities
                        #Overzicht van opgeslagen proefnotities
                        #Proefnotitie selecteren
                            #Proefnotitie bekijken
                            #Aanpassen
                            #Bestaande antwoorden wijzigen
                            #Wijzigingen opslaan
                            #Verwijderen
                            #Verwijderen bevestigen
                                #Ja: Proefnotitie verwijderen
                                #Nee: Terug naar proefnotitie
                            #Wijninformatie bekijken
                            #Terug naar overzicht
                    #Nieuwe proefnotitie
                        #Bestaande wijn zoeken
                            #Zoekterm invoeren
                                #Zoekresultaten tonen
                
                                    #Geschikte wijn gevonden
                                        #Wijn selecteren
                                        #Wijn bevestigen
                
                                    #Geen geschikte wijn gevonden
                                        #Wat wil je doen?
                                        #Opnieuw zoeken
                                            #Nieuwe zoekterm invoeren
                                                #Zoekresultaten tonen
                
                                        #Eigen wijnnaam invoeren
                                            #Wijnnaam invoeren
                                                #Wijnhuis en jaargang (optioneel)
                
                                        #Terug
                
                                        #Proefnotitie invullen
                                            #Vragen beantwoorden
                                                #Antwoorden controleren
                                                #Opslaan
                                                #Bevestiging tonen
                
                #Terug
                #Hoofdmenu
                continue
                
            case 0:
                print("Bedankt voor je bezoek!")
                break


if __name__ == "__main__":
    main()
