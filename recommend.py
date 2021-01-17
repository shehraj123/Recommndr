from imageData import *
import webbrowser

def mood(image):
    if type(image) is str:
        image = Image.open(image)
    l = Luminosity(image)
    s = Saturation(image)
    avg = (l + s)/2
    if avg > 66 or s > 70:
        return 'hype'
    elif avg > 33:
        return 'calm'
    else:
        return 'angry'

def recommend(image):
    keyword = mood(image)
    moods = {
        'angry' : '0KPEhXA3O9jHFtpd1Ix5OB',
        'calm' : '37i9dQZF1DX1s9knjP51Oa',
        'hype' : '37i9dQZF1DX4eRPd9frC1m' 
    }

    link = ['https://open.spotify.com/playlist', moods[keyword]]
    webbrowser.open('/'.join(link))
