from readability import Readability
import lyricsCleaner

sample_text = "Men make their own history, but they do not make it as they please; they do not " \
    "make it under self-selected circumstances, but under circumstances existing already, given " \
    "and transmitted from the past. The tradition of all dead generations weighs like a nightmare " \
    "on the brains of the living. And just as they seem to be occupied with revolutionizing " \
    "themselves and things, creating something that did not exist before, precisely in such epochs " \
    "of revolutionary crisis they anxiously conjure up the spirits of the past to their service, " \
    "borrowing from them names, battle slogans, and costumes in order to present this new scene in " \
    "world history in time-honored disguise and borrowed language. Thus Luther put on the mask of " \
    "the Apostle Paul, the Revolution of 1789-1814 draped itself alternately in the guise of the " \
    "Roman Republic and the Roman Empire, and the Revolution of 1848 knew nothing better to do " \
    "than to parody, now 1789, now the revolutionary tradition of 1793-95. In like manner, " \
    "the beginner who has learned a new language always translates it back into his mother " \
    "tongue, but he assimilates the spirit of the new language and expresses himself freely in " \
    "it only when he moves in it without recalling the old and when he forgets his native tongue."

tame_impala_sample_text = "I was raging, it was late In the world my demons cultivate I felt the " \
    "strangest emotion But it wasn't hate for once Yes I'm changing, yes I'm gone Yes I'm older, " \
    "yes I'm moving on And if you don't think it's a crime You can come along with me Life is " \
    "moving, can't you see There's no future left for you and me I was hoping and I was " \
    "searching endlessly But baby, now there's nothing left that I can do So don't be blue " \
    "There is another future Waiting there for you I saw it different, I must admit I caught " \
    "a glimpse, I'm going after it They say people never change But that's bullshit, they do " \
    "Yes I'm changing, can't stop it now And even if I wanted I wouldn't know how Another " \
    "version of myself I think I've found at last And I can't always hide away Curse indulgence " \
    "and despise the fame There is a world out there And it's calling my name And it's calling " \
    "yours, girl It's calling yours, too It's calling yours, too It's calling yours, too It's " \
    "calling yours, too It's calling out for you Arise and walk on through A world beyond that " \
    "door is calling out for you Arise and walk on through It's calling out for you Arise " \
    "and walk, come through A world beyond that door Is calling out for you"

cleaned_madonna = lyricsCleaner.unescape(lyricsCleaner.madonna_text_from_genius)
cleaned_lady_gaga = lyricsCleaner.unescape(lyricsCleaner.lady_gaga_text_from_genius)
cleaned_ariana = lyricsCleaner.unescape(lyricsCleaner.ariana_text_from_genius)

marx_readability = Readability(sample_text)
marx_fk = marx_readability.flesch_kincaid()

# FK Score is 88, which seems way too high
# Might need to process the lyrics more
tame_readability = Readability(tame_impala_sample_text)
tame_fk = tame_readability.flesch_kincaid()

madonna_readability = Readability(cleaned_madonna)
madonna_fk = madonna_readability.flesch_kincaid()

lady_gaga_readability = Readability(cleaned_lady_gaga)
lady_gaga_fk = lady_gaga_readability.flesch_kincaid()

ariana_readability = Readability(cleaned_ariana)
ariana_fk = ariana_readability.flesch_kincaid()

print(marx_fk.score)
print(marx_fk.grade_level)
print("")
print(tame_fk.score)
print(tame_fk.grade_level)
print("")
print(madonna_fk.score)
print(madonna_fk.grade_level)
print("")
print(lady_gaga_fk.score)
print(lady_gaga_fk.grade_level)
print("")
print(ariana_fk.score)
print(ariana_fk.grade_level)