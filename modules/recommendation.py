import re

def analyze_sleep_issues(user_message):
    user_message = user_message.lower()

    issues = []

    if re.search(r"\b(wake(s|d|ing)?( up)?|frequent waking|restless night(s)?|interrupted (sleep|rest)|broken sleep|keep waking|waking frequently|my sleep (was|is) interrupted|woke up repeatedly|constant waking|multiple awakenings|awaken(ed|ing)? frequently|waking in the night|interrupted my (rest|sleep)|nocturnal waking|awake repeatedly|struggling to stay asleep|kept waking|frequent awakenings|having trouble staying asleep|wide awake in the (middle of the )?night|trouble sleeping at night|can’t stay asleep|sleep gets interrupted)\b", user_message):
        issues.append("frequent waking")

    if re.search(r"\b(nightmare(?:s)?|scary dream(?:s)?|traumatic dream(?:s)?|terrifying dream(?:s)?|bad dream(?:s)?|horrific dream(?:s)?|violent dream(?:s)?|frightening dream(?:s)?|dreadful dream(?:s)?|night terror(?:s)?|disturbing dream(?:s)?|shocking dream(?:s)?|unsettling dream(?:s)?|deeply disturbing dream(?:s)?|fearful dream(?:s)?|paralyzing nightmare(?:s)?|vivid nightmare(?:s)?|unpleasant dream(?:s)?|gruesome dream(?:s)?|creepy dream(?:s)?|chilling dream(?:s)?)\b", user_message):
        issues.append("nightmare")

    if re.search(r"\b(tired(?:ness)?|fatigued?|no energy|low energy|exhaust(?:ed|ion)?|sleepy in the morning|drowsy|weary|drained|lack of energy|feeling sluggish|feeling run down|feeling heavy|feeling weak|no stamina|can't get out of bed|feeling like I didn't sleep|feeling drained|tired after waking up|exhausted after sleep|feeling sleepy all day|not enough rest)\b", user_message):
        issues.append("tired")

    if re.search(r"\b(insomnia|hard to (fall|get) asleep|unable to sleep|couldn't sleep|can't sleep|cannot sleep|sleepless(?:ness)?|difficulty falling asleep|difficult to fall asleep|can't get to sleep|struggling to sleep|trouble sleeping|can't fall asleep|can't stay asleep|difficulty staying asleep|insomniac|awake for hours|restless at night|lying awake|can't drift off|lying in bed awake|keep tossing and turning|insomniac tendencies|sleeping problems|sleep deprivation|wide awake at night|nights without sleep|can't sleep at night|never get enough sleep|insomnia symptoms)\b", user_message):
        issues.append("insomnia")
    
    if re.search(r"\b(restless(?: sleep|ness)?|tossing and turning|shallow sleep|uncomfortable sleep|uneasy sleep|shallow|agitated sleep|disrupted sleep|unsettled sleep|poor sleep|uncomfortable rest|can't settle|frequent awakening|can't relax|constantly moving in bed|rolling over in bed|jerky movements|non-restorative sleep|interrupted sleep|fragmented sleep|no deep sleep|non-restful sleep)\b", user_message):
        issues.append("restless sleep")

    if re.search(r"\b(concentration issues|trouble focusing|difficulty concentrating|can't focus|can't concentrate|short attention span|lack of focus|distracted|lack of concentration|trouble staying focused|inability to focus|brain fog|mental fatigue|can't stay on task|distracted mind|trouble concentrating|mind wandering|unable to focus|focus problems|lack of mental clarity|feeling foggy|spacey|daydreaming|not being able to focus|losing track of thoughts)\b", user_message):
        issues.append("concentration problems")

    if re.search(r"\b(mood swings?|irritabilit(?:y|ies)|short temper|bad mood|feeling down|feeling sad|feeling blue|depressed|depression|downtrodden|mood changes?|feeling low|outbursts of anger|frustration|feeling upset|bad attitude|sensitive|nasty mood|angry|annoyed|frustrated|upset|discouraged|disappointed|hopeless|tearful|melancholy|anxiety|feeling hopeless|moody|stressed|highly emotional|feeling overwhelmed|cranky|bad temper|crying|feeling irritable)\b", user_message):
        issues.append("mood problems")

    if re.search(r"\b(no energy|low energy|fatigue|drowsiness during the day|lack of energy|tired all day|fatigued|sleepy during the day|exhausted|drained|mentally exhausted|no motivation|weakness|feeling sluggish|can't keep my eyes open|feeling lazy|feeling worn out|zero energy|feeling like a zombie|overwhelmed by tiredness|drowsy|fatigued all day|lack of vitality|can't stay awake|feeling fatigued)\b", user_message):
        issues.append("lack of energy during the day")

    if re.search(r"\b(sleep(?:ing)? too much|over(?:sleeping|slept)|excessive sleep|sleep all day|sleeping more than usual|too much sleep|oversleep|spending too much time sleeping|long hours of sleep|overextended sleep|excessive napping|too many hours of sleep|constantly sleeping|sleeping excessively|sleeping for hours|feeling like I sleep too much|resting too much|spending excessive time in bed|sleeping all the time|too much time sleeping)\b", user_message):
        issues.append("excessive sleep problems")

    if re.search(r"\b(snore(?:s|d|ing)?|apnea|breathing stops?|can't breathe|couldn't breathe|gasp(?:ing)?|choking during sleep|difficulty breathing|shortness of breath|noisy breathing|breathing heavily|snoring|breathing irregularities|difficulty getting air|can't catch my breath|interrupted breathing|struggling to breathe|feeling smothered|blocked airway|breathing problems)\b", user_message):
        issues.append("breathing problems")

    if re.search(r"\b(sleepwalk(?:ing|er)?|walking during sleep|getting out of bed while asleep|sleep walking|walking in sleep|night walking|night-time walking|doing things while asleep|wandering while asleep|acting out dreams|sleepwalker|getting up from bed at night|moving around while asleep|walking around while asleep|bizarre behavior during sleep|sleep-related walking)\b", user_message):
        issues.append("sleepwalking")

    if re.search(r"\b(sleeptalk(?:ing|er)?|talking in sleep|talking during sleep|talking at night|chatting in sleep|sleep talking|shouting in sleep|arguing in sleep|talking out loud during sleep|sleep chatter|whispering in sleep|muttering in sleep|monologues during sleep|debating in sleep|exclaiming in sleep|discussing in sleep|interrupting sleep with speech|talking in your sleep|speaking out loud while asleep)\b", user_message):
        issues.append("sleep talking")

    if re.search(r"\b(grind(?:ing|ed|s)? teeth|bruxism|teeth grinding|clenching teeth|grinding teeth|teeth clenching|jaw clenching|jaw grinding|tooth grinding|tooth clenching|clenching in sleep|teeth gnashing|grinding of teeth|grinding sounds|teeth wear|tooth wear|tooth damage|jaw pain|tooth pain|jaw tension|tooth sensitivity|teeth sensitivity|chipped teeth|cracked teeth|teeth aches|muscle tightness in jaw|bruxing|grinding teeth at night|grinding teeth while sleeping|bruxing teeth)\b", user_message):
        issues.append("teeth grinding")

    if re.search(r"\b(vivid dreaming|excessive dreaming|long dreams?|intense dreams?|vivid|frequent dreams|dreams every night|nonstop dreaming|constant dreams|dreaming too much|dream recall|memorable dreams|unusual dreams|unreal dreams|strange dreams|odd dreams|confusing dreams|clear dreams|realistic dreams|complicated dreams|frightening dreams|recurring dreams|dreaming all night|vivid dreams|deep dreams|profound dreams|strong dreams|powerful dreams|dramatic dreams|dreaming vividly|bright dreams|remarkable dreams|extreme dreaming|continuous dreams|intense night dreams|dreaming intensely|intensified dreaming)\b", user_message):
        issues.append("excessive dreaming")

    if re.search(r"\b(night sweats?|sweating|dripping sweat|soaked with sweat|sweating excessively|hot sweats|wet bed|drenched|dripping in sweat|covered in sweat|bath of sweat|nightly sweats|overheating during sleep|sweat during sleep|sweat)\b", user_message):
        issues.append("excessive sweating")

    if re.search(r"\b(restless legs?|leg movement|restless leg syndrome|twitching legs|legs moving|urge to move legs|legs feel uneasy|need to move legs|itchy legs|legs discomfort|cramps in legs|leg cramps|strange sensation in legs|legs shaking|legs want to move|leg restlessness|legs twitch|discomfort in legs)\b", user_message):
        issues.append("restless legs syndrome")

    if re.search(r"\b(daytime sleepiness|drowsiness|can't stay awake|falling asleep during the day|constant fatigue|feeling sleepy|daytime sleepiness|feeling drowsy|need to nap|can't keep eyes open|falling asleep at work|falling asleep in class|falling asleep while driving|difficulty staying awake|tired|tiredness|lack of alertness|feeling exhausted|fatigue|feeling drained|lack of energy|low energy|feeling foggy|difficulty staying awake|constant need to rest|too tired to focus|struggling to stay awake|need to sleep during the day|lack of focus during the day|exhaustion)\b", user_message):
        issues.append("chronic daytime sleepiness")

    if re.search(r"\b(snore(?:s|d|ing)?|loud breathing|nasal issues|nasal blockages|noisy breathing|breathing issues|breathing heavily|blocked nose|difficulty breathing|difficulty inhaling|difficulty exhaling|struggling to breathe|having trouble breathing|interrupted breathing|pauses in breathing|mouth breathing|choking during sleep|breathing stops|apnea|sleep apnea|breathing difficulties)\b", user_message):
        issues.append("snoring")

    if re.search(r"\b(hard to (fall|get) asleep|can't fall asleep|couldn't fall asleep|difficulty falling asleep|struggle to fall asleep|can't get to sleep|difficulty getting to sleep|takes too long to fall asleep|it takes hours to fall asleep|falling asleep is hard|trouble falling asleep|trouble getting to sleep|hours to fall asleep|can't sleep|cannot sleep|sleep difficulties|trouble sleeping|waiting to fall asleep|can't seem to fall asleep|lying awake|lying in bed for hours|unable to sleep|unable to fall asleep)\b", user_message):
        issues.append("difficulty sleeping")

    if re.search(r"\b(wake(?:s|d|ing|n)? up too early|can't sleep past|early waking|wake before dawn|wake up too soon|awake too early|can't stay asleep|not able to sleep longer|early morning wake|awake in the early hours|awoke too early|short night|not enough sleep|awaking too soon)\b", user_message):
        issues.append("waking up too early")

    if re.search(r"\b(wake(?:s|d|ing)? up too late|sleeping past|over-sleeping|sleeping until noon|sleeping too long|before noon waking|can't wake up on time|over sleeping|sleeping late into the day|wake late|sleeping past expected hour|missed wake time|can't seem to wake up|wake up after late hour|awoke very late|stayed in bed too long|sleeping till afternoon|breaking sleep patterns)\b", user_message):
        issues.append("waking up too late")

    if re.search(r"\b(sleep paralysis|can't move|frozen in sleep|unable to move|paralysis during sleep|cannot move at night|feeling frozen|body won't move|feeling stuck in bed|frozen body|mind awake but body asleep|sleep paralysis episode|paralyzed|cannot control body while sleeping)\b", user_message):
        issues.append("sleep paralysis")

    if re.search(r"\b(heart palpitations|rapid heartbeat|racing heart|pounding|fluttering in chest|fast heartbeat|feeling heart beat|thumping in chest|throbbing heart|heart racing|unusual heart rate|fluttering heart beat|fast pulse|palpitating chest|strong heartbeat|heart pounding at night|heart skipping beats|pounding in chest)\b", user_message):
        issues.append("palpitations")

    if re.search(r"\b(stomach ache|abdominal pain|gut pain|belly pain|digestive discomfort|pain in the stomach|cramps|discomfort in abdomen|upset stomach|nausea and stomach pain|gastrointestinal pain|intestinal cramps|abdominal cramps|bloating and stomach ache|painful digestion|crampy belly|pain in the gut|belly cramps|bowel pain|sharp abdominal pain|digestive upset|digestive tract discomfort|stomach bloating)\b", user_message):
        issues.append("stomachache")

    if re.search(r"\b(gag reflex|nausea|vomi.*|gagging|nauseous|feeling sick|might throw up|upset stomach|bile taste in mouth|feeling queasy|nauseous stomach|stomach turning|reflex|need to vomit|retching feeling|gagging feeling|nausea all day)\b", user_message):
        issues.append("gag reflex")

    if re.search(r"\b(headache|migraine|pain in head|pressure in head|head pain|throbbing head|pounding head|skull pain|chronic headache|head pressure|severe headache|head hurting|migraines|painful skull)\b", user_message):
        issues.append("headache")

    if re.search(r"\b(screen time|phone|blue light|phone before bed|watching tv in bed|looking at screens before sleep|electronic device|texting|electronic|laptop|tablet|staring at screen|social media|screen use|watching movies|checking emails|watching videos|smartphone)\b", user_message):
        issues.append("use of electronic devices")

    if not issues:
        return "ok"

    return issues

recommendations = {
    "frequent waking": "Try to establish a regular sleep schedule, reduce caffeine and alcohol before bed, and ensure a comfortable sleeping environment, e.g., a quiet and dark room.",
    "nightmare": "Practice relaxation techniques before bed, such as meditation, reading books, avoiding stress, and consulting a psychotherapist in case of chronic nightmares.",
    "tired": "Ensure regular sleep, aim for 7-9 hours of sleep each night, and maintain healthy habits before bed, such as avoiding electronic screens.",
    "insomnia": "Try relaxation techniques like breathing exercises, regular physical activity (but not right before bed), and avoid caffeine in the afternoon.",
    "restless sleep": "Ensure the right room temperature, a comfortable mattress, and reduce stress during the day.",
    "concentration problems": "Physical exercise, a healthy diet, and regular sleep can help improve concentration. Take mental breaks during work.",
    "mood problems": "Try stress management techniques, such as meditation, and maintain regular sleep. If symptoms are severe, consult a psychotherapist.",
    "lack of energy during the day": "Regular sleep, a diet rich in protein and carbohydrates, and regular breaks for rest can help increase energy. Try to maintain physical activity as well.",
    "excessive sleep problems": "Try to establish a regular sleep time and reduce naps during the day. A balanced lifestyle can help regulate sleep cycles.",
    "breathing problems": "It is advisable to consult a doctor to check for sleep apnea issues. Maintaining a healthy weight and sleeping on your side can help improve breathing.",
    "sleepwalking": "Ensure regular sleep, reduce stress, and use relaxation techniques before bed. If symptoms are severe, consult a doctor.",
    "sleep talking": "Talking in your sleep is often caused by stress or fatigue. Try relaxation techniques and ensure a peaceful sleep.",
    "teeth grinding": "Avoid stress before bed, try relaxation exercises, and if the problem persists, consult a dentist to check if you need special mouth guards.",
    "excessive dreaming": "Try to reduce stress and tension during the day, and ensure proper sleep. Regular physical exercise can help improve sleep quality.",
    "excessive sweating": "Ensure the right temperature in the bedroom, comfortable sleepwear, and avoid alcohol and caffeine before bed. If the problem persists, consult a doctor.",
    "restless legs syndrome": "Regular physical exercise, avoiding caffeine, and massaging your legs before bed can help alleviate symptoms. Consult a doctor if the problem is severe.",
    "chronic daytime sleepiness": "Ensure regular sleep, a healthy diet, and avoid excessive stress during the day. If the problem persists, consult a doctor.",
    "snoring": "Ensure the right sleeping position (e.g., sleeping on your side), avoid alcohol before bed, and consult a doctor to rule out sleep apnea.",
    "difficulty sleeping": "Use relaxation techniques such as meditation, and ensure the right atmosphere in the bedroom – a dark, quiet, and cool place promotes sleep.",
    "waking up too early": "Try to establish a regular sleep time and use relaxation techniques before bed. Avoid looking at screens right before bed.",
    "waking up too late": "Ensure a regular daily rhythm, consistent sleep times, and avoid naps during the day. Try to go to bed at the same time each night.",
    "sleep paralysis": "Regular sleep, avoiding stress, and using relaxation techniques can help reduce sleep paralysis. If the problem persists, consult a doctor.",
    "palpitations": "If the problem occurs at night, consult a doctor. Avoid stress, alcohol, and caffeine before bed.",
    "stomachache": "Eat small meals regularly, avoid heavy meals before bed, and consult a doctor if the problem persists to alleviate the pain.",
    "gag reflex": "Avoid large meals and fatty foods before bed. Try to eat light meals in the evening and use relaxation techniques before going to bed.",
    "headache": "Avoid stress, maintain a regular sleep schedule, and ensure proper hydration. If the problem persists, consult a doctor.",
    "use of electronic devices": "Avoid using electronic devices right before bed."
}
def generate_recommendation(user_message):
    issues = analyze_sleep_issues(user_message)
    if issues == "ok":
        return """I couldn't spot any clear concerns about your sleep habits at the moment.\nHowever, DreamMate still recommends keeping a consistent bedtime routine and limiting screen time before bed.\nIf anything else comes to mind, feel free to share more details!"""
     
    advice = []
    for issue in issues:
        if issue in recommendations:
            advice.append(f"•{recommendations[issue]}")
    
    return "Here's what you can do to improve your sleep:\n" + "\n".join(advice)


# test_message = "I keep waking up frequently at night, and my sleep feels very shallow. I also experience vivid dreams and night sweats."
# print(analyze_sleep_issues(test_message))

# print(generate_recommendation(test_message))
