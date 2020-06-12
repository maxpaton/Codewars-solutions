def song_decoder(song):
    
    stripped = song.replace("WUB", " ")
    return ' '.join(stripped.split())

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")