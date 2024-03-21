from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)

currentId = 11
data = {
    "1": {
        "id": "1",
        "title": "YHLQMDLG",
        "artist": "Bad Bunny",
        "release_year": "2020",
        "genre": ["Reggaeton", "Latin Trap", "Perreo"],
        "tracklist": [
            "Si Veo a Tu Mama", "La Dificil", "Pero Ya No", "La Santa", "Yo Perreo Sola",
            "Bichiyal", "Solia", "La Zona", "Que Malo", "Vete", "Ignorantes", "A Tu Merced",
            "Una Vez", "Safaera", "25/8", "Esta Cabrón Ser Yo", "Puesto Pa' Guerrial",
            "P FKN R",  "Hablamos Mañana", "<3"
        ],
        "cover_art": "https://upload.wikimedia.org/wikipedia/en/3/3f/Bad_Bunny_-_Yhlqmdlg.png",
        "featured_artists": [
            "Daddy Yankee", "Mora", "Sech", "Jowell & Randy", "Anuel AA"
        ],
        "label": "Rimas Entertainment",
        "description": (
            "YHLQMDLG is the second studio album by Puerto Rican rapper Bad Bunny. "
            "It was released on February 29, 2020, through Rimas Entertainment. The "
            "album's music style is heavily influenced by 'old school' reggaeton. "
            "YHLQMDLG was the best selling Latin album in the US of 2020 and "
            "became Spotify's most streamed album globally of 2020. It also won a Grammy for Best "
            "Latin Pop/Urban Album at the 63rd Annual Grammy Awards."
        ),
        "length": "65:48"
    },
    "2": {
        "id": "2",
        "title": "MAÑANA SERA BONITO",
        "artist": "Karol G",
        "release_year": "2023",
        "genre": ["Reggaeton", "Latin Pop"],
        "tracklist": [
            "MIENTRAS ME CURO DEL CORA", "X SI VOLVEMOS", "PERO TU", 
            "BESTIES", "GUCCI LOS PAÑOS", "TQG", "TUS GAFITAS", "OJOS FERRARI",
            "MERCURIO", "GATUBELA", "KARMIKA", "PROVENZA", "CAROLINA", "DAÑAMOS LA AMISTAD",
            "AMARGURA", "CAIRO", "MAÑANA SERA BONITO"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/9b/01/44/9b0144e6-21ae-b53f-2b25-ef6c594b18a3/22UM1IM38716.rgb.jpg/1200x1200bb.jpg",
        "featured_artists": [
            "Romeo Santos", "Shakira", "Quevedo", "Bad Gyal", "Sean Paul"
        ],
        "label": "Universal Music Latino",
        "description": (
            "MAÑANA SERÁ BONITO is the fourth studio album by Colombian singer Karol G, released on February 24, 2023, "
            "via Universal Music Latino. Featuring seventeen tracks blending reggaeton and Latin pop, the album "
            "includes collaborations with artists like Romeo Santos and Shakira. It reached the top spot on the "
            "US Billboard 200, making Karol G the first female artist with an all-Spanish album to achieve this "
            "feat. The album also won the Grammy Award for Best Música Urbana Album and received multiple awards at "
            "the Latin Grammy Awards."
        ),
        "length": "52:52"
    },
    "3": {
        "id": "3",
        "title": "FELIZ CUMPLEAÑOS FERXXO",
        "artist": "Feid",
        "release_year": "2022",
        "genre": ["Reggaeton", "Latin Trap", "Perreo"],
        "tracklist": [
            "Intro", "Castigo", "Feliz Cumpleaños Ferxxo", "Nieve", "Ferxxo 100", "Belixe",
            "XQ Te Pones Asi", "X20X", "Prohibidox", "Lady Mi Amor", "Quemando Calorias", 
            "Aguante", "Si Te La Encuentras Por Ahi", "Normal", "La Buena Fai"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/54/90/df/5490dfaf-d6a4-579c-f6e4-81fd59f6ae3f/22UM1IM04831.rgb.jpg/600x600bf-60.jpg",
        "featured_artists": [
            "Yandel", "Sky Rompiendo"
        ],
        "label": "Universal Music Latino",
        "description": (
            "FELIZ CUMPLEAÑOS FERXXO is the fifth studio album by Colombian singer Feid. "
            "It was released on September 14, 2022, through Universal Music Latino. "
            "Commercially, the album was highly successful, receiving certifications in the United States, "
            "Spain and Argentina. At the Billboard 200 chart, it peaked at number 188, being Feid's first appearance in the chart. " 
        ),
        "length": "38:40"
    },
    "4": {
        "id": "4",
        "title": "FERXXOCALIPSIS",
        "artist": "Feid",
        "release_year": "2023",
        "genre": ["Reggaeton", "Latin Trap"],
        "tracklist": [
            "ALAKRAN", "50 PALOS", "LA VUELTA", "CUAL ES ESA",
            "INTERLUDE", "LUNA", "ESQUIRLA", "DESQUITE", "YO AK",
            "CLASSY 101"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/7c/54/aa/7c54aa94-9ae3-4b80-7b23-8b23955dc3a2/23UM1IM60703.rgb.jpg/1200x1200bf-60.jpg",
        "featured_artists": [
            "Young Miko", "Pirlo"
        ],
        "label": "Universal Music Latino",
        "description": (
            "FERXXOCALIPSIS is the seventh studio album by Colombian singer Feid. "
            "It was released on December 1, 2023, through Universal Music Latino. "
            "Following the release of this album, Feid announced a tour of the same name, "
            "set to take place in 2024. At the end of 2023, Feid was the 6th most-listened to "
            "artist on Spotify."
        ),
        "length": "25:39"
    },
    "5": {
        "id": "5",
        "title": "Un Verano Sin Ti",
        "artist": "Bad Bunny",
        "release_year": "2022",
        "genre": ["Reggaeton", "Latin Trap"],
        "tracklist": [
            "Moscow Mule", "Despues de la Playa", "Me Porto Bonito", "Titi Me Pregunto",
            "Un Ratito", "Yo No Soy Celoso", "Tarot", "Neverita", "La Corriente", "Efecto",
            "Party", "Aguacero", "Enseñame A Bailar", "Ojitos Lindos", "Dos Mil 16", "El Apagon",
            "Otro Atardecer", "Me Fui de Vacaciones", "Un Verano Sin Ti", "Agosto", "Callaita"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/3e/04/eb/3e04ebf6-370f-f59d-ec84-2c2643db92f1/196626945068.jpg/1200x1200bb.jpg",
        "featured_artists": [
            "Rauw Alejandro", "Tainy", "Jhayco", "Chencho Corleone", "Las Marias"
        ],
        "label": "Rimas Entertainment",
        "description": (
            "Un Verano Sin Ti is the fourth studio album of Puerto Rican rapper Bad Bunny. "
            "It was released on May 6, 2022, by Rimas Entertainment. "
            "A critical and commercial success, Un Verano Sin Ti debuted atop the US Billboard 200, "
            "marking Bad Bunny's second number-one album and the second all-Spanish language album to top the chart. "
            "At the 23rd Annual Latin Grammy Awards, Un Verano Sin Ti won Best Urban Music Album. It made history at the "
            "65th Annual Grammy Awards, by becoming the first Spanish-language album to earn a Grammy nomination for "
            "Album of the Year."
        ),
        "length": "81:53"
    },
    "6": {
        "id": "6",
        "title": "Barrio Fino",
        "artist": "Daddy Yankee",
        "release_year": "2004",
        "genre": ["Reggaeton", "Urbano", "Perreo"],
        "tracklist": [
            "Intro", "King Daddy", "Dale Mas Duro", "No Me Dejes Solo", "Gasolina", 
            "Like You", "El Muro", "Lo Que Paso, Paso", "Tu Príncipe", "Cuentame", 
            "Santifica Tus Escapularios", "Sabor a Melao", "El Empuje", "¿Qué Vas a Hacer?", 
            "Salud y Vida", "Intermedio 'Gavilan'", "Corazones", "Golpe de Estado", "2 Mujeres",
            "Saber Su Nombre", "Outro"
        ],
        "cover_art": "https://upload.wikimedia.org/wikipedia/en/d/dd/Barrio_Fino.jpg",
        "featured_artists": [
            "Wisin & Yandel", "Zion & Lennox"
        ],
        "label": "El Cartel Studios",
        "description": (
            "Barrio Fino is the groundbreaking debut studio album by Puerto Rican reggaeton artist "
            "Daddy Yankee. Released on July 13, 2004, under the El Cartel Records label, the album quickly "
            "became a cultural phenomenon. Boasting an electrifying fusion of reggaeton, hip-hop, and Latin "
            "rhythms, Barrio Fino captured the essence of urban life in Puerto Rico. Its chart-topping "
            "success and widespread acclaim solidified Daddy Yankee's status as a pioneer of the genre. "
            "Barrio Fino not only dominated the airwaves but also earned critical acclaim, establishing "
            "itself as a timeless classic in the realm of reggaeton music."
        ),
        "length": "66:24"
    },
    "7": {
        "id": "7",
        "title": "DATA",
        "artist": "Tainy",
        "release_year": "2023",
        "genre": ["Reggaeton", "Latin Trap"],
        "tracklist": [
            "obstaculo", "PASIEMPRE", "Todavia", "FANTASMA | AVC", "MOJABI GHOST", "11 Y ONCE", 
            "desde las 10 (KANY'S INTERLUDE)", "mañana", "BUENOS AIRES", "COLMILLO", "LA BABY", 
            "me jodi...", "VOLVER", "EN VISTO", "Lo Siento BB:/", "si preguntas por mí", "Sci-Fi", 
            "CORLEONE INTERLUDE", "PARANORMAL", "SACRIFICIO"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/ad/da/1f/adda1f4a-f2d3-fe31-c965-e0753d2990ad/196922654572_Cover.jpg/1200x1200bb.jpg",
        "featured_artists": [
            "Rauw Alejandro", "Bad Bunny", "Arcangel", 'Young Miko', "Myke Towers"
        ],
        "label": "Neon16",
        "description": (
            "DATA marks the highly anticipated solo debut of Puerto Rican record producer and songwriter Tainy. "
            "Released on June 29, 2023, under his own record label Neon16, this album represents a fusion of talent "
            "and creativity. Tainy's production prowess shines throughout the album, with a lineup of co-producers "
            "contributing to its rich sound palette. The album spawned six hit singles, including the platinum-certified "
            "'Lo Siento BB:/', and garnered critical acclaim, earning Tainy the Latin Grammy Award for Best Reggaeton Performance."
        ), 
        "length": "66:24"
    },
    "8": {
        "id": "8",
        "title": "VICE VERSA",
        "artist": "Rauw Alejandro",
        "release_year": "2021",
        "genre": ["Reggaeton", "Latin Pop", "Perreo", "Electropop"],
        "tracklist": [
            "Todo De Ti", "Sexo Virtual", "Nubes", "Desesperados", 
            "2/Catorce", "Aquel Nap ZzZz", "Curame", "Cosa Guapa", "Desenfocao'",
            "¿Cuándo Fue?", "La Old Skul", "¿Y Eso?", "Tengo Un Pal", "Brazilera"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/58/13/c3/5813c326-a7fa-f792-77e1-8310d9c80742/886449738724.jpg/1200x1200bf-60.jpg",
        "featured_artists": [
            "Tainy", "Chencho Corleone", "Anitta"
        ],
        "label": "Sony Music Latin",
        "description": (
            "VICE VERSA is Rauw Alejandro's bold second studio album, released on June 25, 2021. "
            "Departing from his signature style, Alejandro explores electropop, reggaeton, Latin pop, "
            "and more. The album's singles, including 'Todo de Ti', 'Sexo Virtual', and 'Desesperados', "
            "achieved chart-topping success. VICE VERSA received critical acclaim, with Rolling Stone "
            "naming it the best Spanish-language album of 2021. Commercially, it debuted at number one " 
            "on US Top Latin Albums and Latin Rhythm Albums charts."
        ), 
        "length": "47:39"
    },
    "9": {
        "id": "9",
        "title": "PLAYA SATURNO",
        "artist": "Rauw Alejandro",
        "release_year": "2023",
        "genre": ["Reggaeton", "Miami Bass", "Latin Pop"],
        "tracklist": [
            "PLAYA SATURNO INTRO", "CUANDO BAJE EL SOL", "AL CALLAO'", "CUKI", "NO ME LA MOLESTE",
            "PICARDIA", "PONTE NASTY", "INQUIETO", "HOY AQUÍ", "CELEBRANDO", "NO ME SORPRENDE",
            "DILUVIO", "SI TE PEGAS", "BABY HELLO"
        ],
        "cover_art": "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/d2/1a/63/d21a6376-80b9-ce89-e4f3-af3f0b70acf9/196871287098.jpg/1200x1200bb.jpg",
        "featured_artists": [
            "Bizzarap", "Ivy Queen"
        ],
        "label": "Sony Music Latin",
        "description": (
            "PLAYA SATURNO emerges as the vibrant fourth studio album from Puerto Rican sensation "
            "Rauw Alejandro, hitting the airwaves on July 7, 2023, under Sony Music Latin. It was "
            "introduced as a spin-off, and was released only 7 months after his third studio album SATURNO. "
            "This 14-track project unveils Alejandro's cosmic journey, cultivated during his Saturno World "
            "Tour. Departing from its predecessor's sonic landscape, PLAYA SATURNO delves into diverse themes, "
            "ranging from love and heartbreak to carefree revelry."
        ), 
        "length": "45:54"
    },
    "10": {
        "id": "10",
        "title": "ESTRELLA",
        "artist": "Mora",
        "release_year": "2023",
        "genre": ["Reggaeton", "Latin Trap"],
        "tracklist": [
            "MEDIA LUNA", "PASAJERO", "POLVORA", "DONDE SE APRENDE A QUERER?", "REINA", 
            "FANTASIAS", "EL CHACAL", "LAGUNA", "LOKITA", "PIDE", "UN DESEO", "DIAMONDS", 
            "CORCEGA", "MAREA", "AYER Y HOY"
        ],
        "cover_art": "https://assets.crownnote.com/s3fs-public/2023-09/nuevo-album-mora-estrella-06.jpg",
        "featured_artists": [
            "Arcangel", "Yandel", "Saiko", "Dei V"
        ],
        "label": "Rimas Entertainment",
        "description": (
            "On August 28, 2023, Puerto Rican singer Mora released his fourth studio album titled ESTRELLA. "
            "In the project, listeners can experience a melancholic side with songs like 'Donde se aprende " 
            "a querer?' and 'Pasajero', as well as romantic tunes like 'Media Luna' and 'Reina'. The Puerto "
            "Rican artist also returns to the roots of Latin trap with 'El Chacal', 'Diamonds' and 'Ayer y "
            "hoy'. According to Mora, ESTRELLA is perhaps the most personal album of his entire career."
        ), 
        "length": "48:10"
    }
}

# ROUTES
@app.route('/', methods=['GET'])
def home():
    global data
    return render_template('home.html', data=data)


@app.route('/search_results/<search_string>', methods=['GET'])
def search_results(search_string):
    global data
    results = []

    for album_data in data.values():
        if search_string.lower() in album_data["title"].lower():
            if album_data not in results:
                results.append(album_data)

    for album_data in data.values():
        if search_string.lower() in album_data["artist"].lower():
            if album_data not in results:
                results.append(album_data)

    for album_data in data.values():
        if search_string.lower() in album_data["release_year"].lower():
            if album_data not in results:
                results.append(album_data)
    
    for album_data in data.values():
        for genre in album_data["genre"]:
            if search_string.lower() in genre.lower():
                if album_data not in results:
                    results.append(album_data)
    

    return render_template('search.html', results=list(results), search_string=search_string)

@app.route('/view/<id>', methods=['GET'])
def view(id):
    global data
    result = data.get(id)

    return render_template('view.html', result=result)

@app.route('/add')
def add():
   return render_template('add.html')  

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global data
    global currentId
    newId = currentId
    json_data = request.get_json() 
    print(json_data)
    newEntry = {
        "id": str(newId),  # Generate a new ID
        "title": json_data['title'],
        "artist":  json_data['artist'],
        "release_year": json_data['release_year'],
        "genre":  json_data['genre'],
        "tracklist":  json_data['tracklist'],
        "cover_art":  json_data['cover_art'],
        "featured_artists":  json_data['featured_artists'],
        "label":  json_data['label'],
        "description":  json_data['description'],
        "length":  json_data['length']
    }
    data[str(newId)] = newEntry        
    currentId += 1

    print(newEntry)

    return jsonify({'id': newId})

@app.route('/edit/<id>', methods=['GET'])
def edit(id):
    global data
    result = data.get(id)
    return render_template('edit.html', result=result)

@app.route('/update', methods=['GET','PUT'])
def update():
    global data
    json_data = request.get_json() 
    data[json_data["id"]] = json_data

    return jsonify({'id': json_data["id"]})

if __name__ == '__main__':
   app.run(debug = True)