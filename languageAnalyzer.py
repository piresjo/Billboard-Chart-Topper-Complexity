from readability import Readability

sampleText = "Men make their own history, but they do not make it as they please; they do not make it under self-selected circumstances, but under circumstances existing already, given and transmitted from the past. The tradition of all dead generations weighs like a nightmare on the brains of the living. And just as they seem to be occupied with revolutionizing themselves and things, creating something that did not exist before, precisely in such epochs of revolutionary crisis they anxiously conjure up the spirits of the past to their service, borrowing from them names, battle slogans, and costumes in order to present this new scene in world history in time-honored disguise and borrowed language. Thus Luther put on the mask of the Apostle Paul, the Revolution of 1789-1814 draped itself alternately in the guise of the Roman Republic and the Roman Empire, and the Revolution of 1848 knew nothing better to do than to parody, now 1789, now the revolutionary tradition of 1793-95. In like manner, the beginner who has learned a new language always translates it back into his mother tongue, but he assimilates the spirit of the new language and expresses himself freely in it only when he moves in it without recalling the old and when he forgets his native tongue."

r = Readability(sampleText)
fk = r.flesch_kincaid()

print(fk.score)
print(fk.grade_level)