# pip install emoji
>>> import emoji
>>> emoji.emojize(":snake:")
'🐍'
>>> emoji.demojize('👍')
':thumbs_up:'

>>> [emo for name, emo in emoji.EMOJI_UNICODE.items() if 'Spain' in name]
['🇪🇸']

>>> from pprint import pprint as pp
>>> pp([(name, emo) for name, emo in emoji.EMOJI_ALIAS_UNICODE.items()
        if 'flag_for' in name])
[(':flag_for_Afghanistan:', '🇦🇫'),
 (':flag_for_Albania:', '🇦🇱'),
...
...
 (':flag_for_Zimbabwe:', '🇿🇼'),
 (':flag_for_Åland_Islands:', '🇦🇽')]