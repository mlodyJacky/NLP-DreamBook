import re

def analyze_sleep_issues(user_message):
    user_message = user_message.lower()

    issues = []

    if re.search(r"\bwake(?:s|d|ing)?\b|\bfrequent waking\b|\brestless nights?\b|\binterrupt(?:ed|ing)? sleep\b|\bbroken sleep\b|\bkeep waking\b|\bwaking frequently\b|\bmy sleep was interrupted\b|\bwake up repeatedly\b|\bconstant waking\b|\bmultiple awakenings\b|\bawaken(?:ed|ing)? frequently\b|\bwake(?:s|d|ing)? in the night\b|\binterrupted my rest\b|\bnocturnal waking\b|\bawake repeatedly\b|\bstruggling to stay asleep\b|\bkept waking\b|\bfrequent awakenings\b|\bhaving trouble staying asleep\b|\bwide awake in the middle of the night\b", user_message):
        issues.append("częste budzenie się")

    if re.search(r"\bnightmare(?:s)?\b|\bscary dream(?:s)?\b|\btraumatic dream(?:s)?\b|\bterrifying dream(?:s)?\b|\bbad dream(?:s)?\b|\bhorrific dream(?:s)?\b|\bviolent dream(?:s)?\b|\bfrightening dream(?:s)?\b|\bdreadful dream(?:s)?\b|\bnight terror(?:s)?\b|\bdisturbing dream(?:s)?\b|\bshocking dream(?:s)?\b|\bnightmare(?:s)?\b|\bunsettling dream(?:s)?\b|\bdeeply disturbing dream(?:s)?\b|\bfearful dream(?:s)?\b|\bparalyzing nightmare(?:s)?\b|\bvivid nightmare(?:s)?\b|\bunpleasant dream(?:s)?\b|\bgruesome dream(?:s)?\b|\bcreepy dream(?:s)?\b|\bchilling dream(?:s)?\b", user_message):
        issues.append("koszmary")

    if re.search(r"\btired(?:ness)?\b|\bfatigued?\b|\bno energy\b|\blow energy\b|\bexhaust(?:ed|ion)?\b|\bsleepy in the morning\b|\bdrowsy\b|\bweary\b|\bdrained\b|\black of energy\b|\bfeeling sluggish\b|\bfeeling run down\b|\bfatigue in the morning\b|\bfeeling heavy\b|\bfeeling weak\b|\bno stamina\b|\bcan't get out of bed\b|\bfeeling sluggish in the morning\b|\bfeeling like I didn't sleep\b|\bfeeling drained\b|\bslow to wake up\b|\blethargic\b|\bnot refreshed\b|\bstill tired after waking up\b|\bexhausted after sleep\b|\bfeeling groggy\b|\bfeeling sleepy all day\b|\bnot enough rest\b|\bcan't shake off sleep\b", user_message):
        issues.append("zmęczenie po przebudzeniu")

    if re.search(r"\binsomnia\b|\bhard to (fall|get) asleep\b|\bunable to sleep\b|\bcan't sleep\b|\bcannot sleep\b|\bsleepless(?:ness)?\b|\bdifficulty falling asleep\b|\bdifficult to fall asleep\b|\bcan't get to sleep\b|\bstruggling to sleep\b|\btrouble sleeping\b|\bcan't fall asleep\b|\bcan't stay asleep\b|\bdifficulty staying asleep\b|\binsomniac\b|\bawake for hours\b|\brestless at night\b|\blying awake\b|\bcan't drift off\b|\blying in bed awake\b|\bkeep tossing and turning\b|\binsomniac tendencies\b|\bsleeping problems\b|\bsleep deprivation\b|\bwide awake at night\b|\bnights without sleep\b|\bcan't sleep at night\b|\bnever get enough sleep\b|\binsomnia symptoms\b", user_message):
        issues.append("bezsenność")

    if re.search(r"\brestless(?: sleep|ness)?\b|\btossing and turning\b|\bshallow sleep\b|\buncomfortable sleep\b|\buneasy sleep\b|\bshallow\b|\bagitated sleep\b|\bdisrupted sleep\b|\bunsettled sleep\b|\bpoor sleep\b|\buncomfortable rest\b|\bcan't settle\b|\bfrequent awakening\b|\bcan't relax\b|\bconstantly moving in bed\b|\brolling over in bed\b|\bjerky movements\b|\bnon-restorative sleep\b|\binterrupted sleep\b|\bfragmented sleep\b|\bno deep sleep\b|\bnon-restful sleep\b", user_message):
        issues.append("niespokojny sen")

    if re.search(r"\bconcentration issues\b|\btrouble focusing\b|\bdifficulty concentrating\b|\bcan't focus\b|\bscattered thoughts\b|\bcan't concentrate\b|\bshort attention span\b|\black of focus\b|\bmentally distracted\b|\black of concentration\b|\btrouble staying focused\b|\binability to focus\b|\bbrain fog\b|\bmental fatigue\b|\bcan't stay on task\b|\bdistracted mind\b|\btrouble concentrating\b|\bmind wandering\b|\bunable to focus\b|\bfocus problems\b|\black of mental clarity\b|\bfeeling foggy\b|\bspacey\b|\bdaydreaming\b|\bnot being able to focus\b|\blosing track of thoughts\b", user_message):
        issues.append("problemy z koncentracją")

    if re.search(r"\bmood swings?\b|\birritabilit(?:y|ies)\b|\bshort temper\b|\bbad mood\b|\bfeeling down\b|\bfeeling sad\b|\bfeeling blue\b|\bdepressed\b|\bdepression\b|\bdowntrodden\b|\bmood changes?\b|\bfeeling low\b|\boutbursts of anger\b|\bfrustration\b|\bfeeling upset\b|\bbad attitude\b|\bsensitive\b|\bnasty mood\b|\bangry\b|\bannoyed\b|\bfrustrated\b|\bupset\b|\bdiscouraged\b|\bdisappointed\b|\bhopeless\b|\btearful\b|\bmelancholy\b|\banxiety\b|\bfeeling hopeless\b|\bmoody\b|\bstressed\b|\bhighly emotional\b|\bfeeling overwhelmed\b|\bcranky\b|\bbad temper\b|\bcrying\b|\bfeeling irritable\b|\bdismal mood\b|\bdespondent\b", user_message):
        issues.append("problemy z nastrojem")

    if re.search(r"\bno energy\b|\blow energy\b|\bfatigue\b|\bdrowsiness during the day\b|\black of energy\b|\btired all day\b|\bfatigued\b|\bsleepy during the day\b|\bexhausted\b|\bdrained\b|\bmentally exhausted\b|\bphysically drained\b|\bno motivation\b|\bweakness\b|\bfeeling sluggish\b|\bfeeling drained\b|\bcan't keep my eyes open\b|\bfeeling lazy\b|\bfeeling worn out\b|\bzero energy\b|\bfeeling like a zombie\b|\boverwhelmed by tiredness\b|\bdrowsy\b|\bfatigued all day\b|\black of vitality\b|\bcan't stay awake\b|\bfeeling fatigued\b", user_message):
        issues.append("brak energii w ciągu dnia")

    if re.search(r"\bsleep(?:ing)? too much\b|\bover(?:sleeping|slept)\b|\bexcessive sleep\b|\bsleep all day\b|\bsleeping more than usual\b|\btoo much sleep\b|\boversleep\b|\bspending too much time sleeping\b|\blong hours of sleep\b|\boverextended sleep\b|\bexcessive napping\b|\btoo many hours of sleep\b|\bconstantly sleeping\b|\bsleeping excessively\b|\bsleeping for hours\b|\bfeeling like I sleep too much\b|\bresting too much\b|\bspending excessive time in bed\b|\bsleeping all the time\b|\btoo much time sleeping\b", user_message):
        issues.append("problemy z nadmiernym snem")

    if re.search(r"\bsnore(?:s|d|ing)?\b|\bapnea\b|\bbreathing stops?\b|\bcan't breathe\b|\bgasp(?:ing)?\b|\bchoking during sleep\b|\bdifficulty breathing\b|\bshortness of breath\b|\bsleep apnea\b|\bnoisy breathing\b|\bbreathing heavily\b|\bsnoring\b|\bbreathing irregularities\b|\bobstructed breathing\b|\bdifficulty getting air\b|\bcan't catch my breath\b|\bsnoring loudly\b|\binterrupted breathing\b|\bstruggling to breathe\b|\bfeeling smothered\b|\bblocked airway\b|\bbreathing problems\b", user_message):
        issues.append("problemy z oddychaniem")

    if re.search(r"\bsleepwalk(?:ing|er)?\b|\bsomnambulism\b|\bwalking during sleep\b|\bgetting out of bed while asleep\b|\bsleep walking\b|\bwalking in sleep\b|\bnight walking\b|\bnight-time walking\b|\bdoing things while asleep\b|\bwandering while asleep\b|\bacting out dreams\b|\bperforming activities in sleep\b|\bsleepwalker\b|\bgetting up from bed at night\b|\bmoving around while asleep\b|\bwalking around while asleep\b|\bbizarre behavior during sleep\b|\bsleep-related walking\b|\bautomatic behavior while asleep\b", user_message):
        issues.append("lunatykowanie")

    if re.search(r"\bsleeptalk(?:ing|er)?\b|\bsomniloquy\b|\btalking in sleep\b|\bconversations while asleep\b|\bspeaking while asleep\b|\btalking during sleep\b|\btalking at night\b|\bvoices while sleeping\b|\bchatting in sleep\b|\bsleep talking\b|\buttering words while asleep\b|\bshouting in sleep\b|\barguing in sleep\b|\btalking out loud during sleep\b|\bsleep chatter\b|\bverbalizing during sleep\b|\bnocturnal speech\b|\bwhispering in sleep\b|\breciting while asleep\b|\bmuttering in sleep\b|\bmonologues during sleep\b|\bdebating in sleep\b|\bexclaiming in sleep\b|\bdiscussing in sleep\b|\binterrupting sleep with speech\b|\bexpressing thoughts aloud in sleep\b|\bnocturnal verbalization\b|\btalking in your sleep\b|\bspeaking out loud while asleep\b|\breciting dreams aloud\b|\buttering sleep phrases\b", user_message):
        issues.append("mówienie przez sen")

    if re.search(r"\bgrind(?:ing|ed|s|ing)? teeth\b|\bbruxism\b|\bteeth grinding\b|\bclenching teeth\b|\bgrinding teeth\b|\bteeth clenching\b|\bjaw clenching\b|\bjaw grinding\b|\btooth grinding\b|\btooth clenching\b|\bgrinding in sleep\b|\bclenching in sleep\b|\bteeth gnashing\b|\bgrinding of teeth\b|\bgrinding sounds\b|\bteeth wear\b|\btooth wear\b|\btooth damage\b|\bjaw pain\b|\btooth pain\b|\bjaw tension\b|\btooth sensitivity\b|\bteeth sensitivity\b|\bchipped teeth\b|\bcracked teeth\b|\bteeth aches\b|\bmuscle tightness in jaw\b|\bbruxing\b|\bgrinding teeth at night\b|\bgrinding teeth while sleeping\b|\bbruxing teeth\b", user_message):
        issues.append("zgrzytanie zębami")

    if re.search(r"\bvivid dreaming\b|\bexcessive dreaming\b|\blong dreams?\b|\bintense dreams?\b|\bvivid\b|\bfrequent dreams\b|\bdreams every night\b|\bnonstop dreaming\b|\bconstant dreams\b|\bdreaming too much\b|\bdream recall\b|\bmemorable dreams\b|\bunusual dreams\b|\bunreal dreams\b|\bstrange dreams\b|\bodd dreams\b|\bconfusing dreams\b|\bclear dreams\b|\bhyper-realistic dreams\b|\bcomplicated dreams\b|\bfrightening dreams\b|\brecurring dreams\b|\bnightly dreams\b|\bdreaming all night\b|\bexperiencing vivid dreams\b|\bexcessively vivid dreams\b|\bdeep dreams\b|\bprofound dreams\b|\bstrong dreams\b|\bpowerful dreams\b|\bdramatic dreams\b|\bdreaming vividly\b|\bbright dreams\b|\bremarkable dreams\b|\bextreme dreaming\b|\bintricate dreams\b|\bcontinuous dreams\b|\bintense night dreams\b|\bdreaming intensely\b|\bintensified dreaming\b", user_message):
        issues.append("nadmierne marzenia senne")

    if re.search(r"\bnight sweats?\b|\bnocturnal sweating\b|\bexcessive sweating at night\b|\bwaking up drenched\b|\bprofuse sweating\b|\bheavy sweating\b|\bdripping sweat\b|\bsweating in sleep\b|\bsweating during sleep\b|\bsoaked with sweat\b|\bsweating excessively\b|\bhot sweats\b|\bnighttime perspiration\b|\bwet bed\b|\bsweat through sheets\b|\bmoisture in bed\b|\bfeeling drenched\b|\bdripping in sweat\b|\bcovered in sweat\b|\bbath of sweat\b|\bnightly sweats\b|\bexcessive perspiration\b|\boverheating during sleep\b|\bsweat during sleep\b|\bprofuse perspiration\b|\bbreaking into a sweat at night\b|\bnighttime sweating\b|\was sweating\b|\bad sweating\b|\bcovered by sweat\b", user_message):
        issues.append("nadmierne pocenie się")

    if re.search(r"\brestless legs?\b|\buncontrollable leg movement\b|\brestless leg syndrome\b|\btwitching legs\b|\blegs moving uncontrollably\b|\burge to move legs\b|\blegs feel uneasy\b|\bneed to move legs\b|\bitchy legs\b|\blegs discomfort\b|\blegs crawling\b|\blegs tingling\b|\bcramps in legs\b|\bleg cramps\b|\bstrange sensation in legs\b|\blegs feel jittery\b|\blegs shaking\b|\blegs cannot stay still\b|\blegs want to move\b|\binvoluntary leg movement\b|\brestless leg movement\b|\bconstant movement of legs\b|\bleg restlessness\b|\blegs twitch\b|\blegs feeling restless\b|\bconstant urge to move legs\b|\bsensory disturbance in legs\b|\bdiscomfort in legs\b", user_message):
        issues.append("syndrom niespokojnych nóg")

    if re.search(r"\bdaytime sleepiness\b|\bdrowsiness during the day\b|\bcan't stay awake\b|\bfalling asleep during the day\b|\bconstant fatigue\b|\bfeeling sleepy during the day\b|\bexcessive daytime sleepiness\b|\bfeeling drowsy\b|\bneed to nap\b|\bcan't keep eyes open\b|\bfalling asleep at work\b|\bfalling asleep in class\b|\bfalling asleep while driving\b|\bdifficulty staying awake\b|\bconstant tiredness during the day\b|\black of alertness during the day\b|\bfeeling exhausted during the day\b|\bdaytime fatigue\b|\bfeeling drained\b|\black of energy during the day\b|\bafternoon slump\b|\blow energy during the day\b|\bfeeling foggy\b|\bdifficulty staying awake in the afternoon\b|\bconstant need to rest\b|\bfeeling lethargic\b|\btoo tired to focus\b|\bstruggling to stay awake\b|\bfeeling mentally sluggish\b|\bcannot stay alert\b|\bneed to sleep during the day\b|\black of focus during the day\b|\bdaytime exhaustion\b", user_message):
        issues.append("przewlekła senność dzienna")

    if re.search(r"\bsnore(?:s|d|ing)?\b|\bloud breathing\b|\bnasal issues\b|\bnasal blockages\b|\bchronic snoring\b|\bsnoring loudly\b|\bsnore at night\b|\bnoisy breathing\b|\bbreathing issues\b|\bbreathing heavily\b|\bblocked nose\b|\bcongested nose\b|\bobstructed airway\b|\bdifficulty breathing\b|\bdifficulty inhaling\b|\bdifficulty exhaling\b|\bnasal congestion\b|\bstruggling to breathe\b|\bhaving trouble breathing\b|\bheavy snoring\b|\bsnoring sound\b|\binterrupted breathing\b|\bpauses in breathing\b|\bmouth breathing\b|\bsnoring during sleep\b|\bsnoring in my sleep\b|\bsnoring every night\b|\bnasal obstruction\b|\bchoking during sleep\b|\bbreathing stops\b|\bapnea\b|\bsleep apnea\b|\bbreathing difficulties\b", user_message):
        issues.append("chrapanie")

    if re.search(r"\bhard to (fall|get) asleep\b|\bcan't fall asleep\b|\bdifficulty falling asleep\b|\bdifficulty initiating sleep\b|\bstruggle to fall asleep\b|\bcan't get to sleep\b|\bdifficulty getting to sleep\b|\btakes too long to fall asleep\b|\bit takes hours to fall asleep\b|\bfalling asleep is hard\b|\btrouble falling asleep\b|\btrouble getting to sleep\b|\bhours to fall asleep\b|\bcannot sleep\b|\bcannot get to sleep\b|\bsleep onset difficulties\b|\bhaving trouble sleeping\b|\bwaiting to fall asleep\b|\bcan't seem to fall asleep\b|\blying awake\b|\blying in bed for hours\b|\bunable to sleep\b|\bbattle to fall asleep\b", user_message):
        issues.append("trudność z zaśnięciem")

    if re.search(r"\bwake(?:s|d|ing|n)? up too early\b|\bcan't sleep past\b|\bearly waking\b|\bwake before dawn\b|\bwake up too soon\b|\bawake too early\b|\bcan't stay asleep\b|\bnot able to sleep longer\b|\bearly morning wake\b|\bawake in the early hours\b|\bawoke too early\b|\bshort night\b|\bnot enough sleep\b|\bawaking too soon\b|\bfeeling unrested in the morning\b|\btoo early to wake\b|\bbefore sunrise wake\b|\bwake in the middle of the night\b|\bhours before normal wake\b|\bgetting up at unreasonable hour\b|\bfeeling awake at an unnatural time\b", user_message):
        issues.append("budzenie się za wcześnie")

    if re.search(r"\bwake(?:s|d|ing)? up too late\b|\bsleeping past\b|\bover-sleeping\b|\bsleeping until noon\b|\bsleeping too long\b|\bbefore noon waking\b|\bcan't wake up on time\b|\bover sleeping\b|\bsleeping late into the day\b|\bwake late\b|\bsleeping past expected hour\b|\bmissed wake time\b|\bexcessive sleep duration\b|\bcan't seem to wake up\b|\bwake up after late hour\b|\bawoke very late\b|\bstay in bed too long\b|\bdifficult waking after long sleep\b|\blate riser\b|\bsleeping till afternoon\b|\bbreaking sleep patterns\b", user_message):
        issues.append("budzenie się za późno")

    if re.search(r"\bsleep paralysis\b|\bcan't move during sleep\b|\bfrozen in sleep\b|\bunable to move upon waking\b|\bparalysis during sleep\b|\bcannot move at night\b|\bfeeling frozen\b|\bbody won't move while asleep\b|\bimmobility during sleep\b|\btemporary paralysis while sleeping\b|\bfeeling stuck in bed\b|\bcannot move limbs during sleep\b|\bimmobile during the night\b|\bparalysis on waking up\b|\bawakened with immobility\b|\bfrozen body while asleep\b|\bmind awake but body asleep\b|\bsleep paralysis episode\b|\bparalyzed upon waking\b|\bcannot control body while sleeping\b", user_message):
        issues.append("paraliż senny")

    if re.search(r"\bheart palpitations\b|\brapid heartbeat\b|\bracing heart\b|\bpounding chest\b|\bfluttering in chest\b|\bfast heartbeat\b|\bpounding heart\b|\bfeeling heart beat\b|\bthumping in chest\b|\bthrobbing heart\b|\bheart racing\b|\bunusual heart rate\b|\bfluttering heart beat\b|\bfast pulse\b|\bpalpitating chest\b|\bstrong heartbeat\b|\bheart pounding at night\b|\bheart skipping beats\b|\bpounding feeling in chest\b|\bthumping in the chest\b|\bhypersensitive heart\b|\bheart acceleration\b|\bpulse irregularity\b", user_message):
        issues.append("kołatanie serca")

    if re.search(r"\bstomach ache\b|\babdominal pain\b|\bgut pain\b|\bbelly pain\b|\bdigestive discomfort\b|\bpain in the stomach\b|\bcramps\b|\bdiscomfort in abdomen\b|\bupset stomach\b|\bnausea and stomach pain\b|\bgastrointestinal pain\b|\bintestinal cramps\b|\babdominal cramps\b|\bbloating and stomach ache\b|\bpainful digestion\b|\bcrampy belly\b|\bpain in the gut\b|\bbelly cramps\b|\bbowel pain\b|\bsharp abdominal pain\b|\bdigestive upset\b|\bdigestive tract discomfort\b|\bstomach bloating\b", user_message):
        issues.append("ból brzucha")

    if re.search(r"\bgag reflex\b|\bnausea\b|\bfeel like vomiting\b|\babout to vomit\b|\bvomi.*\b|\bvomiting feeling\b|\bgagging\b|\bnauseous\b|\bqueasy\b|\bretching\b|\bcan't keep food down\b|\bfeeling sick\b|\bmight throw up\b|\bupset stomach with nausea\b|\bretching sensation\b|\bfeeling on the verge of vomiting\b|\bnausea with dizziness\b|\bbile taste in mouth\b|\bchurning stomach\b|\bfeeling queasy\b|\bnauseous stomach\b|\bstomach turning\b|\bvomit reflex\b|\bneed to vomit\b|\bretching feeling\b|\bgagging feeling\b|\bnausea all day\b", user_message):
        issues.append("odruch wymiotny")

    if re.search(r"\bheadache\b|\bmigraine\b|\bsharp pain in head\b|\bpressure in head\b|\bhead pain\b|\bthrobbing head\b|\bpounding head\b|\bskull pain\b|\bchronic headache\b|\bhead pressure\b|\bsevere headache\b|\bhead pain that won't go away\b|\bsharp pulsating head pain\b|\bhead hurting\b|\bmigraines\b|\bintense head pain\b|\bpain in the head\b|\bconstant headache\b|\bsharp headache\b|\bpainful skull\b|\bthrobbing in the skull\b|\bmigraine episode\b|\bpounding sensation in head\b|\bneck and head pain\b|\bsevere throbbing head\b|\bheadache every day\b", user_message):
        issues.append("ból głowy")

    if re.search(r"\bscreen time\b|\busing devices before sleep\b|\bblue light\b|\bphone before bed\b|\bwatching tv in bed\b|\busing phone in bed\b|\blooking at screens before sleep\b|\belectronic device use before bed\b|\bchecking phone before bed\b|\belectronic distractions\b|\bbright screens before bed\b|\bblue light exposure\b|\busing laptop at night\b|\busing tablet before bed\b|\bstaring at screen too long\b|\bchecking social media at night\b|\bscreen use before sleep\b|\bwatching phone before sleep\b|\bchecking emails before bed\b|\bwatching video on screen before sleep\b|\busing smartphone before bed\b|\busing technology too much before sleep\b|\boveruse of electronics at night\b|\bphone\b", user_message):
        issues.append("zaburzenia snu z powodu korzystania z urządzeń elektronicznych")

    if not issues:
        return "ok"

    return issues

recommendations = {
    "częste budzenie się": "Try to establish a regular sleep schedule, reduce caffeine and alcohol before bed, and ensure a comfortable sleeping environment, e.g., a quiet and dark room.",
    "koszmary": "Practice relaxation techniques before bed, such as meditation, reading books, avoiding stress, and consulting a psychotherapist in case of chronic nightmares.",
    "zmęczenie po przebudzeniu": "Ensure regular sleep, aim for 7-9 hours of sleep each night, and maintain healthy habits before bed, such as avoiding electronic screens.",
    "bezsenność": "Try relaxation techniques like breathing exercises, regular physical activity (but not right before bed), and avoid caffeine in the afternoon.",
    "niespokojny sen": "Ensure the right room temperature, a comfortable mattress, and reduce stress during the day.",
    "problemy z koncentracją": "Physical exercise, a healthy diet, and regular sleep can help improve concentration. Take mental breaks during work.",
    "problemy z nastrojem": "Try stress management techniques, such as meditation, and maintain regular sleep. If symptoms are severe, consult a psychotherapist.",
    "brak energii w ciągu dnia": "Regular sleep, a diet rich in protein and carbohydrates, and regular breaks for rest can help increase energy. Try to maintain physical activity as well.",
    "problemy z nadmiernym snem": "Try to establish a regular sleep time and reduce naps during the day. A balanced lifestyle can help regulate sleep cycles.",
    "problemy z oddychaniem": "It is advisable to consult a doctor to check for sleep apnea issues. Maintaining a healthy weight and sleeping on your side can help improve breathing.",
    "lunatykowanie": "Ensure regular sleep, reduce stress, and use relaxation techniques before bed. If symptoms are severe, consult a doctor.",
    "mówienie przez sen": "Talking in your sleep is often caused by stress or fatigue. Try relaxation techniques and ensure a peaceful sleep.",
    "zgrzytanie zębami": "Avoid stress before bed, try relaxation exercises, and if the problem persists, consult a dentist to check if you need special mouth guards.",
    "nadmierne marzenia senne": "Try to reduce stress and tension during the day, and ensure proper sleep. Regular physical exercise can help improve sleep quality.",
    "nadmierne pocenie się": "Ensure the right temperature in the bedroom, comfortable sleepwear, and avoid alcohol and caffeine before bed. If the problem persists, consult a doctor.",
    "syndrom niespokojnych nóg": "Regular physical exercise, avoiding caffeine, and massaging your legs before bed can help alleviate symptoms. Consult a doctor if the problem is severe.",
    "przewlekła senność dzienna": "Ensure regular sleep, a healthy diet, and avoid excessive stress during the day. If the problem persists, consult a doctor.",
    "chrapanie": "Ensure the right sleeping position (e.g., sleeping on your side), avoid alcohol before bed, and consult a doctor to rule out sleep apnea.",
    "trudność z zaśnięciem": "Use relaxation techniques such as meditation, and ensure the right atmosphere in the bedroom – a dark, quiet, and cool place promotes sleep.",
    "budzenie się za wcześnie": "Try to establish a regular sleep time and use relaxation techniques before bed. Avoid looking at screens right before bed.",
    "budzenie się za późno": "Ensure a regular daily rhythm, consistent sleep times, and avoid naps during the day. Try to go to bed at the same time each night.",
    "paraliż senny": "Regular sleep, avoiding stress, and using relaxation techniques can help reduce sleep paralysis. If the problem persists, consult a doctor.",
    "kołatanie serca": "If the problem occurs at night, consult a doctor. Avoid stress, alcohol, and caffeine before bed.",
    "ból brzucha": "Eat small meals regularly, avoid heavy meals before bed, and consult a doctor if the problem persists to alleviate the pain.",
    "odruch wymiotny": "Avoid large meals and fatty foods before bed. Try to eat light meals in the evening and use relaxation techniques before going to bed.",
    "zaburzenia snu z powodu korzystania z urządzeń elektronicznych": "Avoid using electronic devices right before bed."
}
def generate_recommendation(user_message):
    issues = analyze_sleep_issues(user_message)
    if issues == "ok":
        return """I couldn't spot any clear concerns about your sleep habits at the moment. 
                  However, DreamMate still recommends keeping a consistent bedtime routine and limiting screen time before bed.
                  If anything else comes to mind, feel free to share more details!"""
     
    advice = []
    for issue in issues:
        if issue in recommendations:
            advice.append(f"•{recommendations[issue]}")
    
    return "Here is what you can do to improve your sleep:\n\n" + "\n".join(advice)


# test_message = "I keep waking up frequently at night, and my sleep feels very shallow. I also experience vivid dreams and night sweats."
# print(analyze_sleep_issues(test_message))

# print(generate_recommendation(test_message))
