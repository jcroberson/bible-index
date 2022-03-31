# Bible Project
import xml.etree.ElementTree as elt
import eel, sys, os
global wd
try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()

eel.init('web')

conversion = {
    1:'Genesis', 2:'Exodus', 3:'Leviticus', 4:'Numbers', 5:'Deuteronomy', 
    6:'Joshua', 7:'Judges', 8:'Ruth', 9:'1 Samuel', 10:'2 Samuel', 11:'1 Kings',
    12:'2 Kings', 13:'1 Chronicles', 14:'2 Chronicles', 15:'Ezra', 
    16:'Nehemiah', 17:'Esther', 18:'Job', 19:'Psalms', 20:'Proverbs', 
    21:'Ecclesiastes', 22:'Song of Solomon', 23:'Isaiah', 24:'Jeremiah',
    25:'Lamentations', 26:'Ezekiel', 27:'Daniel', 28:'Hosea', 29:'Joel',
    30:'Amos', 31:'Obadiah', 32:'Jonah', 33:'Micah', 34:'Nahum', 35:'Habakkuk',
    36:'Zephaniah', 37:'Haggai', 38:'Zechariah', 39:'Malachi', 40:'Matthew',
    41:'Mark', 42:'Luke', 43:'John', 44:'Acts', 45:'Romans', 46:'1 Corinthians',
    47:'2 Corinthians', 48:'Galatians', 49:'Ephesians', 50:'Phillipians', 
    51:'Colossians', 52:'1 Thessalonians', 53:'2 Thessalonians', 54:'1 Timothy',
    55:'2 Timothy', 56:'Titus', 57:'Philemon', 58:'Hebrews', 59:'James',
    60:'1 Peter', 61:'2 Peter', 62:'1 John', 63:'2 John', 64:'3 John', 
    65:'Jude', 66:'Revelation'
}

@eel.expose
def my_func(user_input, version):
    bible = elt.parse(os.path.join(wd,'translations', version +'.xml' )).getroot()
    results = []
    for testament in bible:
        for book in testament:
            for chapter in book:
                for verse in chapter:
                    if user_input in verse.text:
                        results.append([book.attrib['number'], 
                            chapter.attrib['number'], verse.attrib['number'], 
                            verse.text])
    string = ''
    if len(results) > 3500:
        string += '<div class="verse"><b>Your search query resulted in over \
            3500 results. This is near the maximum display limit, consider \
            refining your search, otherwise some later results may be cut off. \
            </b></div>'
    for result in results:
        result[0] = conversion[int(result[0])]
        string += ('<div class="verse"><b>{} {}:{}</b>'.format(result[0], 
            result[1], result[2]) + '<br>' + result[3] + '</div>')
    if string == '':
        return '<div class="verse">No Matches</div>'
    return string

eel.start('index.html', size=(400,400), mode='firefox')
