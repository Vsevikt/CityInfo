from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html', {'active_page': 'home'})

def news(request, slug=None):
    articles = [
        {
            'category': 'City life',
            'date': 'November 8, 2026',
            'title': 'Warsaw expands its network of cycling routes',
            'text': 'New connections are making it easier to travel between neighbourhoods, parks and the city centre by bike.',
            'icon': '↗',
        },
        {
            'category': 'Culture',
            'date': 'November 5, 2026',
            'title': 'A new season of exhibitions opens by the river',
            'text': 'Local museums and galleries invite residents to discover contemporary art, history and creative workshops.',
            'icon': '✳',
        },
        {
            'category': 'Public spaces',
            'date': 'November 2, 2026',
            'title': 'More greenery is coming to the city centre',
            'text': 'The next round of neighbourhood improvements will add shade, seating and accessible walking routes.',
            'icon': '⌂',
        },
    ]
    return render(request, 'main/news.html', {
        'active_page': 'news',
        'articles': articles,
    })


def management(request, slug=None):
    officials = [
        {
            'role': 'Mayor of Warsaw',
            'name': 'Rafał Trzaskowski',
            'initials': 'RT',
            'photo': 'https://commons.wikimedia.org/wiki/Special:FilePath/Rafa%C5%82_Trzaskowski_HQ.jpg',
            'photo_credit': 'https://commons.wikimedia.org/wiki/File:Rafa%C5%82_Trzaskowski_HQ.jpg',
            'photo_author': 'European Union',
            'description': 'Leads the city administration and represents Warsaw residents.',
        },
        {
            'role': 'Deputy Mayor',
            'name': 'Renata Kaznowska',
            'initials': 'RK',
            'photo': 'https://commons.wikimedia.org/wiki/Special:FilePath/Renata_Kaznowska_2023.jpg',
            'photo_credit': 'https://commons.wikimedia.org/wiki/File:Renata_Kaznowska_2023.jpg',
            'photo_author': 'Adrian Grycuk',
            'description': 'Oversees key areas of public services and city development.',
        },
        {
            'role': 'Deputy Mayor',
            'name': 'Aldona Machnowska-Góra',
            'initials': 'AM',
            'photo': 'https://commons.wikimedia.org/wiki/Special:FilePath/Aldona_Machnowska-G%C3%B3ra.jpg',
            'photo_credit': 'https://commons.wikimedia.org/wiki/File:Aldona_Machnowska-G%C3%B3ra.jpg',
            'photo_author': 'Smogo21',
            'description': 'Works with city departments to deliver Warsaw’s local priorities.',
        },
    ]
    return render(request, 'main/management.html', {
        'active_page': 'management',
        'officials': officials,
    })


def facts(request, slug=None):
    facts_list = [
        {
            'number': '1.86M',
            'title': 'People call Warsaw home',
            'text': 'The capital is Poland’s largest city and one of Central Europe’s lively urban hubs.',
            'icon': '♙',
        },
        {
            'number': '191 km²',
            'title': 'A city along the Vistula',
            'text': 'The river runs through Warsaw, connecting green banks, neighbourhoods and landmarks.',
            'icon': '⌁',
        },
        {
            'number': 'UNESCO',
            'title': 'A remarkable Old Town',
            'text': 'Warsaw’s carefully rebuilt historic centre is recognised as a World Heritage Site.',
            'icon': '✳',
        },
    ]
    return render(request, 'main/facts.html', {
        'active_page': 'facts',
        'facts_list': facts_list,
    })


def contacts(request, slug=None):
    services = [
        {
            'name': 'Warsaw City Contact Centre',
            'number': '19 115',
            'description': 'City information, requests and local services',
            'icon': '⌕',
        },
        {
            'name': 'Emergency number',
            'number': '112',
            'description': 'Police, fire or medical emergency',
            'icon': '✚',
        },
        {
            'name': 'Police',
            'number': '997',
            'description': 'Police assistance in Poland',
            'icon': '◉',
        },
        {
            'name': 'Fire and rescue service',
            'number': '998',
            'description': 'Fire or rescue emergency',
            'icon': '↗',
        },
        {
            'name': 'Ambulance',
            'number': '999',
            'description': 'Urgent medical assistance',
            'icon': '✚',
        },
        {
            'name': 'Municipal Guard',
            'number': '986',
            'description': 'Local public order and city assistance',
            'icon': '⌂',
        },
    ]
    return render(request, 'main/contacts.html', {
        'active_page': 'contacts',
        'services': services,
    })


def history(request, slug=None):
    milestones = [
        {
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Warszawa%20-%20Rynek%20Starego%20Miasta.jpg?width=640',
            'image_alt': 'Warsaw Old Town market square',
            'period': '13th century',
            'title': 'Early settlement',
            'text': 'Warsaw grew on the Vistula river, at a crossroads linking communities and trade routes.',
        },
        {
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/RoyalCastleWarsaw.jpg?width=640',
            'image_alt': 'Royal Castle in Warsaw',
            'period': '1596',
            'title': 'A royal capital',
            'text': 'King Sigismund III Vasa moved his court to Warsaw, helping establish its role as Poland’s political centre.',
        },
        {
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Warsaw%20Old%20Town%201945.jpg?width=640',
            'image_alt': 'Warsaw Old Town after the war, 1945',
            'period': '1944–1945',
            'title': 'Rebuilding the city',
            'text': 'After wartime destruction, residents rebuilt Warsaw, including its historic Old Town.',
        },
    ]
    return render(request, 'main/history.html', {
        'active_page': 'history',
        'milestones': milestones,
        'page': {
            'title': 'History of Warsaw',
            'eyebrow': 'THE CITY THROUGH TIME',
            'heading_first': 'Warsaw',
            'heading_second': 'history.',
            'intro': 'Discover the story of a city shaped by resilience, change and the people who call it home.',
            'section_kicker': 'A CITY WITH MANY LAYERS',
            'section_heading': 'From its beginnings to today',
            'section_count': 'Warsaw, Poland',
            'welcome_title': 'Explore Warsaw’s past.',
            'welcome_text': 'Meet its people and see historical photographs.',
            'people_link': 'Famous residents',
            'photos_link': 'Historical photos',
        },
    })


def history_people(request):
    people = [
        {
            'initials': 'MC',
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Marie%20Curie%20(c.%201900).jpg?width=600',
            'image_alt': 'Portrait of Maria Skłodowska-Curie',
            'photo_credit': 'https://commons.wikimedia.org/wiki/File:Marie_Curie_(c._1900).jpg',
            'role': 'Physicist and chemist · 1867–1934',
            'name': 'Maria Skłodowska-Curie',
            'description': 'Born in Warsaw, she pursued scientific studies in Paris and became the first woman to receive a Nobel Prize. She remains the only person awarded Nobel Prizes in two different sciences.',
            'connection': 'Her birthplace at 16 Freta Street is now a museum dedicated to her life and work.',
        },
        {
            'initials': 'FC',
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Fryderyk%20Chopin.jpg?width=600',
            'image_alt': 'Portrait of Frédéric Chopin by Ambroży Mieroszewski, 1829',
            'photo_credit': 'https://commons.wikimedia.org/wiki/File:Fryderyk_Chopin.jpg',
            'role': 'Composer and pianist · 1810–1849',
            'name': 'Frédéric Chopin',
            'description': 'Chopin spent his youth in Warsaw, studied at the Warsaw Lyceum and the Conservatory, and gave his first public concerts in the city before leaving Poland in 1830.',
            'connection': 'The city preserves places from his early life and holds an international piano competition in his name.',
        },
        {
            'initials': 'JK',
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Janusz%20Korczak%20(cropped).jpg?width=600',
            'image_alt': 'Portrait of Janusz Korczak',
            'photo_credit': 'https://commons.wikimedia.org/wiki/File:Janusz_Korczak.jpg',
            'role': 'Physician, writer and educator · 1878–1942',
            'name': 'Janusz Korczak',
            'description': 'A Warsaw-born doctor and author, Korczak led an orphanage and developed an approach to education grounded in respect for children and their rights.',
            'connection': 'He worked with children in the city for decades and stayed with them during the Holocaust.',
        },
    ]
    return render(request, 'main/history_people.html', {
        'active_page': 'history',
        'people': people,
        'page': {
            'title': 'Famous Residents — History of Warsaw',
            'eyebrow': 'PEOPLE OF WARSAW',
            'heading_first': 'Famous',
            'heading_second': 'residents.',
            'intro': 'Artists, scientists and leaders whose lives and work are connected with Warsaw.',
            'section_kicker': 'PEOPLE AND THEIR LEGACIES',
            'section_heading': 'Known around the world',
            'section_count': 'Warsaw residents',
            'photo_credit': 'Image source',
            'connection_label': 'Warsaw connection:',
            'welcome_title': 'Discover more of Warsaw’s past.',
            'history_link': 'Back to history',
            'photos_link': 'Historical photos',
        },
    })


def history_photos(request):
    photos = [
        {
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Warsaw%201939%20Krakowskie%20Przedmiescie%20photo.jpg?width=640',
            'image_alt': 'Krakowskie Przedmieście and Castle Square in Warsaw, 1939',
            'date': '1939 · Krakowskie Przedmieście',
            'title': 'A city on the eve of war',
            'text': 'A view of Krakowskie Przedmieście and Castle Square from 1939, before years of occupation and destruction changed the city.',
        },
        {
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Warsaw%201944.jpg?width=640',
            'image_alt': 'Warsaw Old Town during the 1944 uprising',
            'date': '1 August – 2 October 1944 · Warsaw',
            'title': 'The Warsaw Uprising',
            'text': 'For 63 days, Polish resistance fighters and residents fought German occupation. The uprising became one of the defining chapters in the city’s history.',
        },
        {
            'image': 'https://commons.wikimedia.org/wiki/Special:FilePath/Warsaw%20Old%20Town%2C%20photograph%20of%201945.jpeg?width=640',
            'image_alt': 'The damaged Warsaw Old Town in 1945',
            'date': '1945 · Old Town',
            'title': 'A city in ruins',
            'text': 'After the uprising and the 1944–45 destruction, much of Warsaw lay in ruins. This photograph records the scale of the loss in the Old Town.',
        },
    ]
    return render(request, 'main/history_photos.html', {
        'active_page': 'history',
        'photos': photos,
        'page': {
            'title': 'Historical Photos — History of Warsaw',
            'eyebrow': 'THE CITY THROUGH TIME',
            'heading_first': 'Historical',
            'heading_second': 'photos.',
            'intro': 'Follow Warsaw through the years of war, destruction and the first steps toward rebuilding.',
            'section_kicker': 'A CITY WITH MANY LAYERS',
            'section_heading': 'From the eve of war to renewal',
            'section_count': 'Warsaw, 1939–1945',
            'welcome_title': 'Continue exploring Warsaw’s past.',
            'history_link': 'Back to history',
            'people_link': 'Famous residents',
        },
    })