import string
import ImageDraw
from PIL import Image
__author__ = 'karl_leswing'


def make_bracket(winners, outfile):
    places = open('../data/locations.txt').readlines()
    places = map(string.strip, places)
    places = map(lambda x: map(int, x.split(',')), places)
    background = Image.open('../data/images/blank_bracket.png')
    draw = ImageDraw.Draw(background)
    for i in xrange(0, len(winners)):
        place = places[i]
        team = Image.open('../data/images/teams/Duke.gif')
        #background.paste(team, (place[0], place[1]))
        draw.text((place[0], place[1]), winners[i], fill=(255, 0, 0))
    background.save(outfile)

if __name__ == '__main__':
    make_bracket(["Karl"] * 63, '../data/images/full_bracket.png')