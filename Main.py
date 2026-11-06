import Menus
import API_vinofyi
import API_WineAPI
import random
from requests.exceptions import RequestException

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
                try:
                    Menus.show_encycl_menu()
                    choice = Menus.menu_choice()

                    match choice:
                        case 1:
                            #Druiven
                            grape_color = Menus.menu_grapes()

                            if grape_color is not None:
                                selected_grape = Menus.menu_selection_grapes(grape_color)

                                if selected_grape is not None:
                                    Menus.show_grape_details(selected_grape)
                        case 2:
                            #Geuren                        
                            while True:
                                aroma_category = Menus.menu_aromas()

                                if aroma_category is None:
                                    break

                                while True:
                                    selected_aroma = Menus.menu_aroma_results(
                                        aroma_category
                                    )

                                    if selected_aroma is None:
                                        break

                                    Menus.show_flavor_details(selected_aroma)
                        case 3:
                            #Smaken                        
                            while True:
                                flavor_category = Menus.menu_flavor()

                                if flavor_category is None:
                                    break

                                flavor_subcategory = Menus.menu_flavor_subcategories(
                                    flavor_category
                                )

                                if flavor_subcategory is None:
                                    continue

                                while True:
                                    selected_flavor = Menus.menu_flavor_results(
                                        flavor_category,
                                        flavor_subcategory
                                    )

                                    if selected_flavor is None:
                                        break

                                    Menus.show_flavor_details(selected_flavor)
                except RequestException:
                    continue  

            case 2:
                #Wijnhuizen zoeken
                try:
                    choice = Menus.menu_wineries()
                
                    match choice:
                        case 1:
                        #Zoeken op naam
                            search_term = Menus.menu_search_winery()

                            wineries = API_vinofyi.search_wineries(search_term)
                        
                            selected_winery = Menus.menu_winery_results(wineries)

                            if selected_winery is None:
                                continue

                            winery_details = API_vinofyi.get_winery_details(selected_winery)

                            selected_wine = Menus.show_winery_details(winery_details)

                            if selected_wine is None:
                                continue

                            wine_details = API_vinofyi.get_wine_details(selected_wine["slug"])

                            Menus.show_wine_details(wine_details)

                        case 2:
                            #Zoeken op land en regio
                            country = Menus.menu_countries()

                            if country is not None:
                                #Regio's ophalen uit de API
                                regions = API_vinofyi.list_regions(country)

                                if regions:
                                    #Regio laten selecteren
                                    selected_region = Menus.menu_regions(regions)

                                    if selected_region is not None:
                                        wineries = API_vinofyi.search_wineries(
                                            selected_region["name"]
                                        )

                                        matching_wineries = []

                                        for winery in wineries:
                                            winery_details = API_vinofyi.get_winery_details(
                                                winery
                                            )

                                            if (
                                                winery_details
                                                and winery_details["country"].lower() == country.lower()
                                                and winery_details["region"].lower()
                                                == selected_region["name"].lower()
                                            ):
                                                matching_wineries.append(winery)

                                        if matching_wineries:
                                            selected_winery = Menus.menu_winery_results(
                                                matching_wineries
                                            )

                                            if selected_winery is not None:
                                                winery_details = API_vinofyi.get_winery_details(
                                                    selected_winery
                                                )
                                                Menus.show_winery_details(winery_details)
                                        else:
                                            Menus.console.print(
                                                "[yellow]Geen wijnhuizen gevonden.[/yellow]"
                                            )
                                else:
                                    Menus.console.print(
                                        "[yellow]Geen regio's gevonden.[/yellow]"
                                    )
                                            
                        case 3:
                            #Willekeurig wijnhuis
                            wineries = API_vinofyi.list_wineries()

                            if wineries:
                                selected_winery = random.choice(wineries)

                                winery_details = API_vinofyi.get_winery_details(
                                    selected_winery
                                )

                                selected_wine = Menus.show_winery_details(winery_details)

                                if selected_wine is not None:
                                    wine_details = API_vinofyi.get_wine_details(
                                        selected_wine["slug"]
                                    )
                                    print(wine_details)
                                    Menus.show_wine_details(wine_details)
                except RequestException:
                    continue
                        
            case 3:
                #Wijn zoeken
                try:
                    search_term = Menus.menu_search_wine()

                    data = API_WineAPI.search_wine(search_term)
                    wines = data["results"]

                    if not wines:
                        print("Geen wijnen gevonden.")
                        continue

                    selected_wine = Menus.menu_wine_results(wines)

                    if selected_wine is None:
                        continue

                    Menus.show_wine_details(selected_wine)
                except RequestException:
                    continue
            
            case 4:
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