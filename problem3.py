def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    capacity = songs[0][2]
    if capacity > max_size:
        return []
    result = [songs[0][0]]
    sorted_songs = sorted(songs[1:], key=lambda x: x[2])
    for song in sorted_songs:
        if song[2] + capacity <= max_size:
            result.append(song[0])
            capacity += song[2]
    return result
