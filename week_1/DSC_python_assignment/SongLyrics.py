import time
song="Kabhi kaali ratiyaa kabhi din suhaane, Kismat ki baate toh kismat hi jaane, O beta ji, O beta ji, Are! o baabu ji, Kismat ki hawa kabhi naram, kabhi garam, Kabhi naram-naram kabhi garam-garam, Kabhi naram-garam naram-garam, O beta ji, Kismat ki hawa kabhi naram, kabhi garam Kabhi naram-naram kabhi garam-garam,  Kabhi naram-garam naram-garam, O beta ji"
s=song.split(", ")
for i in range(len(s)):
    print(s[i])
    time.sleep(1)