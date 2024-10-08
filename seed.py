from models import Music, Artist, db
from app import app

with app.app_context():
    artist1 = Artist(name="artist one", location="artist one pin")
    artist2 = Artist(name="artist two", location="artist two pin")

    music1 = Music(title="music one", album_audio="albumaudioonelink",
                   album_image="albumimageonelink", artist=artist1)
    music2 = Music(title="music two", album_audio="albumaudiotwolink",
                   album_image="albumimagetwolink", artist=artist1)
    music3 = Music(title="music three", album_audio="albumaudiothreelink",
                   album_image="albumimagethreelink", artist=artist2)

    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(music1)
    db.session.add(music2)
    db.session.add(music3)

    db.session.commit()