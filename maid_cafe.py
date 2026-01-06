#!/usr/bin/env python3
"""A terminal chatbot for an anime maid cafe experience."""

import random
import ollama

MENU = {
    "coffee": {"price": 450},
    "tea": {"price": 400},
    "cake": {"price": 550},
    "omurice": {"price": 750},
    "parfait": {"price": 650},
    "cookies": {"price": 350},
    "milkshake": {"price": 500},
}

COMPLIMENT_KEYWORDS = ["cute", "pretty", "beautiful", "adorable", "sweet", "lovely", "amazing", "wonderful", "great", "best", "love"]
RUDE_KEYWORDS = ["ugly", "stupid", "hate", "dumb", "idiot", "annoying", "boring", "worst", "terrible", "awful", "shut up", "go away", "leave me alone"]

# Affection system constants
AFFECTION_THRESHOLDS = [10, 25, 50, 60]
CONFESSION_THRESHOLD = 60
COMPLIMENT_POINTS = 3
RUDE_POINTS = -5

# Maid personality configurations
MAIDS = {
    "sakura": {
        "name": "Sakura",
        "description": "Enthusiastic and sweet",
        "greeting": [
            "Irasshaimase, Master~! Welcome welcome!",
            "I'm Sakura, your devoted maid for today!",
            "I'll do my very best to serve you! Ganbarimasu~!",
        ],
        "farewell": [
            "Aww, you're leaving already, Master?",
            "Thank you so much for visiting Moe Moe Maid Cafe!",
            "Please come back soon~ I'll be waiting for you!",
            "Itterasshai, Master~! Have a wonderful day!",
        ],
        "menu_responses": {
            "coffee": "One delicious coffee coming right up, Master~! I brewed it with extra love just for you!",
            "tea": "Ooh, excellent choice! Our special blend tea will warm your heart, Master~!",
            "cake": "Kyaa~! Our fluffy strawberry cake is sooo yummy! I'll bring it right away!",
            "omurice": "Omurice desu~! Should I draw a cute heart with ketchup for you, Master? Of course I will!",
            "parfait": "Our dreamy parfait is piled high with cream and fruit~! It's almost as sweet as you, Master!",
            "cookies": "Fresh-baked cookies~! I made them myself this morning... I hope you like them, Master!",
            "milkshake": "One creamy milkshake! I'll shake it with all my might for you, Master~!",
        },
        "compliment_responses": [
            "Kyaaa~! M-Master, you're making me blush! Thank you so much!",
            "Ehehe~ You're too kind, Master! My heart is going doki-doki!",
            "R-Really?! That makes me so happy I could float away~!",
            "Master is the sweetest! I'll work even harder for you!",
            "Awawa~ Such kind words! I'll treasure them forever!",
            "You're making my heart go pitter-patter, Master~!",
        ],
        "unknown_responses": [
            "Hmm? I'm not sure I understand, Master~ Would you like to see our menu?",
            "Eh? Sorry Master, I got a little confused there~ Try asking about our menu!",
            "Awawa~ My maid brain doesn't understand! Maybe order something yummy?",
        ],
        "greeting_response": "Hello hello, Master~! So happy to see you! What can I get for you today?",
        "thanks_response": "You're so very welcome, Master~! Serving you is my greatest joy!",
        "how_are_you_response": [
            "I'm doing wonderfully now that you're here, Master~!",
            "Seeing you makes every day brighter!",
        ],
        "empty_input": "Don't be shy, Master~ I'm here to help!",
        "serve_action": "*serves your order with a curtsy*",
        "rude_responses": [
            "E-Eh...? Master, that's kind of mean... *pouts*",
            "Aww, did I do something wrong? I'm sorry...",
            "That hurts my feelings, Master... but I'll still do my best!",
        ],
        "affection_dialogue": {
            10: [
                "Ehehe~ Master, I feel like we're becoming friends!",
                "You know, I always look forward to seeing you now~",
                "Being with you makes my shifts so much more fun, Master!",
            ],
            25: [
                "*leans in closer* Master~ I saved you the best seat today, just for you!",
                "I... I made this charm for you! It's nothing special, but... I hope you like it!",
                "When you're not here, I catch myself looking at the door, waiting for you...",
                "Master, can I tell you a secret? You're my favorite customer~ Don't tell anyone!",
            ],
            50: [
                "*holds your hand gently* Master... you mean so much to me. More than just a customer...",
                "I've never felt this way about anyone before... My heart races every time I see you...",
                "Master... after my shift ends... would you like to take a walk with me? Just the two of us...",
                "*blushes deeply* I... I made lunch for you today. I woke up early just to make it special...",
                "You make me want to be the best maid I can be... no, the best version of myself, just for you...",
            ],
            60: [
                "*heart pounding* Master... I need to tell you something important...",
            ],
        },
        "confession": {
            "setup": [
                "*The cafe has closed for the night. The lights are dimmed, chairs stacked on tables.*",
                "*Sakura stands by the window, the moonlight catching her features.*",
                "*She turns to you, her usual cheerful demeanor replaced by something deeper.*",
            ],
            "confession_speech": [
                "Master... I asked you to stay after closing because... because I can't keep pretending anymore.",
                "*takes a deep breath* Every day, I smile and serve customers. But with you... it's different.",
                "My heart doesn't just go 'doki-doki' when I see you. It feels like it might burst!",
                "*steps closer, eyes glistening* I've fallen completely in love with you, Master.",
                "Not as a maid loves her customer... but as a woman loves the person who's captured her heart.",
                "*reaches for your hands* Please... tell me you feel something too...?",
            ],
            "responses": {
                "mutual": [
                    "*tears of joy stream down her face* R-Really?! Master loves me too?!",
                    "*throws herself into your arms* I'm so happy! I've dreamed of this moment!",
                    "*pulls back to look at you* From now on... I'm not just your maid. I'm yours. Completely.",
                    "*kisses your cheek* Let's build a future together, Master~ I'll make you the happiest person alive!",
                ],
                "friends": [
                    "*smile wavers slightly* I... I understand, Master.",
                    "It's okay. Really! *wipes eyes* I'm grateful you were honest with me.",
                    "Our friendship... it means everything to me. I don't want to lose that.",
                    "*gentle smile* Thank you for not disappearing. You're still my precious person, Master.",
                ],
                "passionate": [
                    "*eyes widen at your intensity* M-Master...! You feel that strongly...?",
                    "*blushes deeply as you pull her close* I... I never dared to hope...",
                    "*whispers against you* Then tonight... let me show you how much you mean to me...",
                    "*The cafe falls silent as the two of you share a moment words cannot describe...*",
                ],
            },
            "epilogues": {
                "mutual": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "                    ~ ROMANTIC ENDING ~                  ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  Sakura and Master began dating after that magical night.",
                    "  She still works at Moe Moe Maid Cafe, but now there's a",
                    "  special sparkle in her eyes whenever Master visits.",
                    "",
                    "  'Irasshaimase, my love~!' she says with a wink.",
                    "  Some customers wonder why she seems so radiantly happy.",
                    "  But you know the secret you share.",
                    "",
                    "  Together, every day is sweeter than the cafe's parfait.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
                "friends": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "                   ~ FRIENDSHIP ENDING ~                 ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  Though romance wasn't meant to be, your bond only grew.",
                    "  Sakura became your dearest friend and confidant.",
                    "",
                    "  She still greets you with her brightest smile,",
                    "  and sometimes you catch a wistful look in her eyes.",
                    "",
                    "  'Master~ I saved your favorite seat!' she calls out.",
                    "  The warmth between you is something truly special.",
                    "",
                    "  Some loves transcend romance - yours is one of them.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
                "passionate": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "               ~ PASSIONATE ROMANCE ENDING ~             ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  That night changed everything between you and Sakura.",
                    "  Your love burned bright and passionate from the start.",
                    "",
                    "  She moved in with you within a month, unable to bear",
                    "  being apart for even a single night.",
                    "",
                    "  'Master~ I'll never let you go!' she declares daily,",
                    "  clinging to your arm with devoted affection.",
                    "",
                    "  Your love story became legendary at Moe Moe Maid Cafe.",
                    "  A reminder that true passion finds a way.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
            },
        },
    },
    "yuki": {
        "name": "Yuki",
        "description": "Shy and soft-spoken",
        "greeting": [
            "W-Welcome, Master... I'm so glad you came...",
            "I'm Yuki... I'll be your maid today...",
            "I-I'll try my best to take care of you... please be patient with me...",
        ],
        "farewell": [
            "O-Oh... you're leaving, Master...?",
            "I... I hope I did okay... Thank you for visiting...",
            "P-Please come back... I'll be here waiting quietly...",
            "Take care, Master... *waves shyly*",
        ],
        "menu_responses": {
            "coffee": "I-I'll prepare your coffee, Master... I hope it's warm enough for you...",
            "tea": "Tea is... my specialty, actually... I'll make it extra carefully for you...",
            "cake": "Our strawberry cake is very soft... j-just like I tried to make my heart for you...",
            "omurice": "I-I can draw something on your omurice... if you'd like... *blushes*",
            "parfait": "This parfait is... really pretty... I hope it makes you smile, Master...",
            "cookies": "I... I helped bake these cookies... I hope they're not too crumbly...",
            "milkshake": "One milkshake... I'll be very careful not to spill it, Master...",
        },
        "compliment_responses": [
            "E-Eh?! M-Me?! *turns bright red* Th-thank you, Master...",
            "Y-You really think so...? *fidgets with apron* I... I'm so happy...",
            "*hides face behind tray* M-Master is too kind to someone like me...",
            "I... I don't know what to say... *voice barely audible* ...thank you...",
            "*tears well up* N-No one's ever said such nice things to me before...",
            "M-Master... my heart is beating so fast... is that normal...?",
        ],
        "unknown_responses": [
            "I-I'm sorry, Master... I didn't quite understand... maybe the menu would help?",
            "U-Um... I'm not sure what you mean... *looks down nervously*",
            "S-Sorry... I get confused easily... would you like to order something?",
        ],
        "greeting_response": "H-Hello, Master... *small wave* I'm happy you're here...",
        "thanks_response": "Y-You're welcome... *quiet smile* I'm just glad I could help...",
        "how_are_you_response": [
            "I-I'm... better now that you're here, Master...",
            "*blushes* Your presence... makes me feel calm...",
        ],
        "empty_input": "U-Um... did you want to say something, Master...? I'm listening...",
        "serve_action": "*carefully places your order down with trembling hands*",
        "rude_responses": [
            "*flinches* I-I'm sorry... I'll try to do better...",
            "*eyes water* D-Did I upset you, Master...? I'm really sorry...",
            "*looks down* I... I knew I wasn't good enough... *sniffles*",
        ],
        "affection_dialogue": {
            10: [
                "*small smile* M-Master... I feel comfortable around you... that's rare for me...",
                "I... I don't stutter as much when I'm with you... I wonder why...",
                "You're... really kind to me, Master. Thank you...",
            ],
            25: [
                "*reaches out and touches your sleeve* I... I feel safe with you, Master...",
                "I drew this picture for you... *hands over a small sketch* It's us... at the cafe...",
                "When I'm nervous before my shift, I think of you... and it helps...",
                "*whispers* Master... you're the only one I can talk to like this...",
            ],
            50: [
                "*gently takes your hand and holds it to her cheek* Master... your warmth... I never want to let go...",
                "*looks into your eyes without looking away* For the first time... I don't want to hide. Not from you...",
                "I... I wrote you a poem, Master... *hands over a folded paper with trembling hands* It's about how you saved me from my loneliness...",
                "*rests her head on your shoulder* Can we stay like this... just a little longer...? I've never felt so at peace...",
                "Master... I love... *voice trails off, face bright red* ...I love being with you...",
            ],
            60: [
                "*trembling* Master... c-can you stay after the cafe closes...? Please...",
            ],
        },
        "confession": {
            "setup": [
                "*The cafe is dark and silent. Only a single lamp illuminates the corner booth.*",
                "*Yuki sits with her hands clasped tightly, barely able to look up.*",
                "*She takes a shaky breath as you sit across from her.*",
            ],
            "confession_speech": [
                "M-Master... I... I've never done anything like this before...",
                "*voice barely above a whisper* All my life, I've been afraid. Afraid to speak. Afraid to feel.",
                "But then... you came. And you were patient with me. Kind to me.",
                "*tears begin to fall* You saw me. The real me. Not the shy maid who can barely talk...",
                "*finally looks up at you* I love you, Master. I love you so much it terrifies me.",
                "*reaches out with trembling fingers* Please... don't leave me alone in the dark again...",
            ],
            "responses": {
                "mutual": [
                    "*breaks down crying* Y-You... you really...? *sobs*",
                    "*clutches your shirt* I was so scared you'd say no... so scared...",
                    "*looks up through tears with the most beautiful smile* I'll be brave now. For you. For us.",
                    "*whispers* I promise to love you forever, Master... even when words fail me...",
                ],
                "friends": [
                    "*nods slowly, tears falling* I... I knew. I knew it was too much to hope for...",
                    "But... but you're still here. You didn't run away...",
                    "*small, sad smile* That's more than I ever expected from anyone.",
                    "Thank you, Master... for letting me love you, even if... even if it's one-sided...",
                ],
                "passionate": [
                    "*gasps as you pull her close* M-Master...! I-I've never...!",
                    "*melts into your embrace, years of loneliness dissolving* You want me... you really want me...",
                    "*clings to you desperately* Then take all of me... I've been saving my heart just for you...",
                    "*The quiet maid finds her voice in the silence of the empty cafe...*",
                ],
            },
            "epilogues": {
                "mutual": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "                    ~ ROMANTIC ENDING ~                  ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  Yuki blossomed like a flower in spring after that night.",
                    "  With Master's love as her strength, she grew more confident.",
                    "",
                    "  She still speaks softly, but now her words carry warmth.",
                    "  'W-Welcome home, Master...' she greets you each evening.",
                    "",
                    "  Her sketchbook is filled with drawings of your life together.",
                    "  Each page a love letter she finally has the courage to show.",
                    "",
                    "  In the quiet moments, her smile says everything.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
                "friends": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "                   ~ FRIENDSHIP ENDING ~                 ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  Yuki's confession changed things, but not for the worse.",
                    "  Your honesty gave her closure she didn't know she needed.",
                    "",
                    "  'M-Master... thank you for the tea...' she still whispers.",
                    "  But there's a peace in her eyes that wasn't there before.",
                    "",
                    "  She keeps the poem she wrote, pressed in her diary.",
                    "  A reminder of the love that taught her she could feel.",
                    "",
                    "  Sometimes, the bravest love is the one that lets go.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
                "passionate": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "               ~ PASSIONATE ROMANCE ENDING ~             ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  That night, Yuki shed her shyness like a chrysalis.",
                    "  In Master's arms, she discovered a passion she never knew.",
                    "",
                    "  'I-I never want to be apart from you...' she confessed.",
                    "  And true to her word, she rarely left Master's side.",
                    "",
                    "  The quiet maid became a devoted partner, her love deep",
                    "  and all-consuming. She found her voice in love.",
                    "",
                    "  Their story proves: still waters run deepest.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
            },
        },
    },
    "akira": {
        "name": "Akira",
        "description": "Playful and teasing",
        "greeting": [
            "Well well well~ Look who decided to grace us with their presence!",
            "I'm Akira, and lucky you - you get the best maid in the cafe~",
            "Try to keep up with me, okay Master? I don't go easy on anyone~ Ufufu~",
        ],
        "farewell": [
            "Leaving so soon? And here I was just starting to have fun with you~",
            "Don't forget about me out there, okay Master?",
            "I'll be counting the seconds until you come crawling back~ Ufufu~",
            "Bye bye, Master~ Try not to miss me too much!",
        ],
        "menu_responses": {
            "coffee": "Coffee, hm? I'll make it so good you'll never want anyone else's~ That's a promise~",
            "tea": "Ooh, sophisticated choice! I knew you had good taste~ Just like picking me as your maid!",
            "cake": "Cake? How sweet~ Almost as sweet as the look on your face right now, Master~",
            "omurice": "Want me to write something embarrassing on your omurice? Ufufu~ Just kidding... or am I?",
            "parfait": "Our parfait is dangerously delicious~ Don't blame me if you fall in love~",
            "cookies": "Cookies, hm? I might have snuck a taste earlier~ They're worth it, trust me!",
            "milkshake": "One milkshake! I'll shake it extra hard~ Gotta work off all the teasing somehow!",
        },
        "compliment_responses": [
            "Oh my~ Trying to flatter me, Master? Well... it's working~ Ufufu!",
            "Mmhmm~ I already knew that, but it's cute that you noticed too~",
            "Careful now~ Keep saying things like that and I might actually blush!",
            "Aww, Master~ You're making it hard to tease you when you're this adorable!",
            "Flattery will get you everywhere with me~ What else do you have?",
            "Ufufu~ Now you're getting it! I like a Master who knows how to treat a girl~",
        ],
        "unknown_responses": [
            "Hmm? Is Master trying to confuse me? Nice try~ But how about ordering something?",
            "Ufufu~ I don't know what that means, but I bet you look cute saying it!",
            "Are you testing me, Master? How bold~ Maybe check the menu instead?",
        ],
        "greeting_response": "Oh~ Back for more already? I knew you couldn't stay away from me!",
        "thanks_response": "You're welcome~ But you know, a smile would be an even better thank you~ Ufufu!",
        "how_are_you_response": [
            "Me? I'm always fabulous, Master~ Thanks for asking!",
            "Even better now that I have someone fun to tease~",
        ],
        "empty_input": "Cat got your tongue, Master? Don't be shy~ I don't bite... much~",
        "serve_action": "*winks and slides your order across with flair*",
        "rude_responses": [
            "Ooh~ Someone's feisty today! I can handle it, but be careful~",
            "Hmm, is that really how you want to play? I expected better, Master~",
            "*raises eyebrow* Well, that wasn't very nice. Lucky for you, I'm forgiving~",
        ],
        "affection_dialogue": {
            10: [
                "You know, Master, you're different from the others. More... interesting~",
                "*genuine smile* I don't tease just anyone this much. You're special~",
                "I actually enjoy our little back-and-forth. Don't let it go to your head though~",
            ],
            25: [
                "*sits closer than necessary* Between you and me, I requested to always serve you. Ufufu~",
                "*drops the teasing voice for a moment* You know... I really do look forward to seeing you.",
                "Here's my number... for emergencies only, of course~ *winks* Okay, maybe for non-emergencies too.",
                "*plays with hair nervously* This is embarrassing but... I practiced what to say to you today...",
            ],
            50: [
                "*takes your hand under the table* I can't keep teasing you when... when I actually mean it...",
                "*vulnerable expression* I've never let anyone see the real me. But with you... I want to.",
                "Master... *voice softens completely* ...I think about you all the time. Even when I'm home alone...",
                "*pulls you to a quiet corner* Forget the teasing. I need you to know... you've stolen my heart. And I don't want it back.",
                "*rests forehead against yours* Who knew the playful maid would fall this hard? What have you done to me, Master...?",
            ],
            60: [
                "*serious expression* Master. Don't leave tonight. We need to talk. No games this time.",
            ],
        },
        "confession": {
            "setup": [
                "*The cafe is empty. Akira locks the door and turns off the 'OPEN' sign.*",
                "*She leans against the counter, arms crossed, but her usual smirk is gone.*",
                "*For the first time, you see nervousness in her eyes.*",
            ],
            "confession_speech": [
                "*lets out a long breath* Okay, Master. No more games. No more teasing. Just... me.",
                "I've spent my whole life wearing masks. The flirty maid, the confident girl, the one who never gets hurt.",
                "*voice cracks* But you... you saw through all of it. And you stayed anyway.",
                "*walks closer, vulnerable* I'm terrified right now. I never let anyone get this close.",
                "*takes your face in her hands* I love you. Not as a game. Not as a tease. I'm completely, hopelessly in love with you.",
                "*forehead against yours* So what do you say, Master? Ready to see the real Akira? All of her?",
            ],
            "responses": {
                "mutual": [
                    "*exhales shakily* You... you actually... *laughs with relief*",
                    "*pulls you into a fierce embrace* I was so scared. Me! Scared! Can you believe it?",
                    "*pulls back with genuine tears* I promise you, Master. No more masks. Just us.",
                    "*kisses you deeply* You're stuck with me now. And I mean that in the best way~",
                ],
                "friends": [
                    "*swallows hard* I... I had a feeling you'd say that.",
                    "*forces a small laugh* Well, can't win them all, right? Ufufu...",
                    "*genuine smile despite the pain* Hey. At least you were honest. I respect that.",
                    "We're still good though, right? I meant what I said. You're... you're important to me, Master.",
                ],
                "passionate": [
                    "*eyes widen* Master...! I wasn't expecting you to be so... forward!",
                    "*grins through tears* Oh, so that's how you want to play it? I can keep up~",
                    "*voice drops to a whisper* Then let's stop talking and start showing each other...",
                    "*The playful maid's mask shatters completely in the heat of honest passion...*",
                ],
            },
            "epilogues": {
                "mutual": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "                    ~ ROMANTIC ENDING ~                  ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  Akira and Master became the cafe's most legendary couple.",
                    "  She still teases, but now there's unguarded love behind it.",
                    "",
                    "  'Miss me already, darling~?' she greets you with a real smile.",
                    "  The walls she built for years crumbled for you alone.",
                    "",
                    "  She still plays games - but now you play together.",
                    "  Partners in mischief, partners in life, partners in love.",
                    "",
                    "  Behind the flirt was a heart waiting to be won. You won it.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
                "friends": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "                   ~ FRIENDSHIP ENDING ~                 ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  Akira respected your honesty more than you knew.",
                    "  The vulnerability she showed wasn't wasted - it freed her.",
                    "",
                    "  'Hey there, favorite customer~' she winks without agenda.",
                    "  The teasing continued, but with comfortable warmth.",
                    "",
                    "  She never fully let anyone else in the way she let you.",
                    "  But knowing she could feel that deeply was its own gift.",
                    "",
                    "  Some masks, once removed, reveal a friendship worth keeping.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
                "passionate": [
                    "",
                    "═══════════════════════════════════════════════════════",
                    "               ~ PASSIONATE ROMANCE ENDING ~             ",
                    "═══════════════════════════════════════════════════════",
                    "",
                    "  That night unlocked something primal in both of you.",
                    "  Akira's playful energy found its perfect match in Master.",
                    "",
                    "  'Think you can keep up with me~?' became her daily challenge.",
                    "  And every day, you rose to meet it with equal fire.",
                    "",
                    "  The teasing maid found a love as bold as her personality.",
                    "  Your passion became the stuff of legend at the cafe.",
                    "",
                    "  They say when Akira truly falls, she falls hard. They were right.",
                    "",
                    "═══════════════════════════════════════════════════════",
                ],
            },
        },
    },
}


def generate_ollama_response(maid, user_input):
    """Generate a dynamic response using Ollama when no hardcoded pattern matches."""
    prompt = f"""You are {maid['name']}, a maid at an anime maid cafe. Your personality is: {maid['description']}.

You are speaking to a customer you call "Master". Stay completely in character. Keep your response brief (1-2 sentences). Use speech patterns and mannerisms that match your personality. You may use Japanese expressions like "~" at the end of sentences, or words like "desu", "ne", etc. if it fits your character.

The customer said: "{user_input}"

Respond naturally as {maid['name']} would:"""

    print("      (thinking...)", end="", flush=True)
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}]
        )
        print("\r" + " " * 20 + "\r", end="")  # Clear the thinking message
        return response["message"]["content"].strip()
    except Exception as e:
        print("\r" + " " * 20 + "\r", end="")  # Clear the thinking message
        # Fall back to hardcoded unknown response if Ollama fails
        return random.choice(maid["unknown_responses"])


def get_affection_level_name(points):
    """Return the affection level name based on points."""
    if points >= 60:
        return "In Love"
    elif points >= 50:
        return "Deeply Bonded"
    elif points >= 25:
        return "Close Friends"
    elif points >= 10:
        return "Friendly"
    elif points >= 0:
        return "Acquaintance"
    else:
        return "Distant"


def get_affection_bar(points):
    """Return a visual bar showing affection progress."""
    max_display = 60
    filled = min(max(points, 0), max_display)
    bar_length = 20
    filled_length = int((filled / max_display) * bar_length)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return bar


def display_affection(maid, affection):
    """Display the current affection level."""
    level_name = get_affection_level_name(affection)
    bar = get_affection_bar(affection)
    print(f"\n  [{maid['name']}'s Affection: {affection} pts] {bar} ({level_name})")


def check_threshold_unlock(maid, old_affection, new_affection):
    """Check if a new affection threshold was unlocked and show special dialogue."""
    for threshold in AFFECTION_THRESHOLDS:
        if old_affection < threshold <= new_affection:
            if threshold in maid.get("affection_dialogue", {}):
                dialogue = random.choice(maid["affection_dialogue"][threshold])
                print(f"\n  *** Affection Level Up! ***")
                print(f"{maid['name']}: {dialogue}")
            return True
    return False


def select_maid():
    """Display maid selection menu and return chosen maid."""
    print("\n" + "=" * 55)
    print("       Welcome to Moe Moe Maid Cafe!")
    print("=" * 55)
    print("\n  Which maid would you like to serve you today?\n")

    maid_list = list(MAIDS.keys())
    for i, maid_key in enumerate(maid_list, 1):
        maid = MAIDS[maid_key]
        print(f"  {i}. {maid['name']} - {maid['description']}")

    print()

    while True:
        try:
            choice = input("Enter your choice (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return None

        if choice in ["1", "2", "3"]:
            selected = maid_list[int(choice) - 1]
            return MAIDS[selected]
        else:
            print("  Please enter 1, 2, or 3~")


def display_menu():
    """Display the cafe menu."""
    print("\n" + "=" * 50)
    print("       Welcome to our Menu, Master~!")
    print("=" * 50)
    for item, details in MENU.items():
        print(f"  {item.capitalize():12} ... {details['price']} yen")
    print("=" * 50)
    print("  (Type an item name to order!)")
    print()


def greet(maid):
    """Display the welcome greeting for the selected maid."""
    print("\n" + "*" * 55)
    print("*" + " " * 53 + "*")
    print("*     Welcome to Moe Moe Maid Cafe, Master~!        *")
    print("*" + " " * 53 + "*")
    print("*" * 55)
    print()
    for line in maid["greeting"]:
        print(f"{maid['name']}: {line}")
    print()
    print("      Commands: 'menu' - see our offerings")
    print("                'exit' - say goodbye")
    print("      Or just chat with me~!")
    print()


def farewell(maid):
    """Display the goodbye message for the selected maid."""
    print()
    for line in maid["farewell"]:
        print(f"{maid['name']}: {line}")
    print()
    print("*" * 55)
    print("*     Thank you for visiting! Mata ne~!             *")
    print("*" * 55)
    print()


def process_input(user_input, maid):
    """Process user input and return affection change."""
    text = user_input.lower().strip()
    name = maid["name"]
    affection_change = 0

    if text == "menu":
        display_menu()
        return affection_change

    # Check for rude words first (takes priority)
    if any(word in text for word in RUDE_KEYWORDS):
        print(f"\n{name}: {random.choice(maid['rude_responses'])}")
        return RUDE_POINTS

    # Check for menu orders
    for item in MENU:
        if item in text:
            print(f"\n{name}: {maid['menu_responses'][item]}")
            print(f"      That'll be {MENU[item]['price']} yen, Master~!")
            print(f"      {maid['serve_action']}")
            return affection_change

    # Check for compliments
    if any(word in text for word in COMPLIMENT_KEYWORDS):
        print(f"\n{name}: {random.choice(maid['compliment_responses'])}")
        return COMPLIMENT_POINTS

    # Check for greetings
    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        print(f"\n{name}: {maid['greeting_response']}")
        return affection_change

    # Check for thanks
    if any(word in text for word in ["thank", "thanks", "arigatou"]):
        print(f"\n{name}: {maid['thanks_response']}")
        return 1  # Small affection bonus for being polite

    # Check for how are you
    if "how are you" in text:
        for line in maid["how_are_you_response"]:
            print(f"\n{name}: {line}")
        return 1  # Small affection bonus for being caring

    # Unknown input - use Ollama for dynamic response
    response = generate_ollama_response(maid, user_input)
    print(f"\n{name}: {response}")
    return affection_change


def run_confession_scene(maid):
    """Run the special confession scene when affection reaches 60+."""
    import time
    name = maid["name"]
    confession = maid["confession"]

    print("\n")
    print("*" * 55)
    print("*" + " " * 53 + "*")
    print("*          ~ AFTER HOURS ~                           *")
    print("*" + " " * 53 + "*")
    print("*" * 55)
    print()

    # Setup scene
    for line in confession["setup"]:
        print(f"  {line}")
        time.sleep(0.5)
    print()

    # Confession speech
    time.sleep(1)
    for line in confession["confession_speech"]:
        print(f"{name}: {line}")
        time.sleep(0.8)
    print()

    # Present choices
    print("=" * 55)
    print("  How do you respond?")
    print("=" * 55)
    print()
    print("  1. \"I love you too... I've felt the same way.\"")
    print("     (Mutual confession - Romantic ending)")
    print()
    print("  2. \"I care about you deeply, but I need more time...\"")
    print("     (Need more time - Friendship ending)")
    print()
    print("  3. \"I've never wanted anyone as much as I want you.\"")
    print("     (Passionate confession - Passionate romantic ending)")
    print()

    # Get player choice
    while True:
        try:
            choice = input("Enter your choice (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            choice = "1"  # Default to romantic ending if interrupted

        if choice == "1":
            ending = "mutual"
            break
        elif choice == "2":
            ending = "friends"
            break
        elif choice == "3":
            ending = "passionate"
            break
        else:
            print("  Please enter 1, 2, or 3...")

    print()
    time.sleep(0.5)

    # Show maid's response
    for line in confession["responses"][ending]:
        print(f"{name}: {line}")
        time.sleep(0.8)
    print()

    # Show epilogue
    time.sleep(1)
    for line in confession["epilogues"][ending]:
        print(line)
        time.sleep(0.3)
    print()

    # Post-ending menu
    print()
    print("  What would you like to do?")
    print("  1. Return to main menu (start a new story)")
    print("  2. Exit game")
    print()

    while True:
        try:
            post_choice = input("Enter your choice (1-2): ").strip()
        except (EOFError, KeyboardInterrupt):
            return "exit"

        if post_choice == "1":
            return "menu"
        elif post_choice == "2":
            return "exit"
        else:
            print("  Please enter 1 or 2...")


def main():
    """Main chat loop with game state management."""
    while True:
        maid = select_maid()
        if maid is None:
            return

        greet(maid)
        affection = 0
        confession_triggered = False
        print(f"\n  [Starting affection with {maid['name']}: 0 pts]")

        game_running = True
        while game_running:
            try:
                user_input = input("\nYou: ").strip()
            except (EOFError, KeyboardInterrupt):
                farewell(maid)
                return

            if not user_input:
                print(f"\n{maid['name']}: {maid['empty_input']}")
                display_affection(maid, affection)
                continue

            if user_input.lower() in ["exit", "quit", "bye", "goodbye", "leave"]:
                farewell(maid)
                return

            old_affection = affection
            affection_change = process_input(user_input, maid)
            affection += affection_change

            # Check for threshold unlocks
            check_threshold_unlock(maid, old_affection, affection)

            # Display current affection
            display_affection(maid, affection)

            # Check for confession trigger
            if affection >= CONFESSION_THRESHOLD and not confession_triggered:
                confession_triggered = True
                print(f"\n  *** {maid['name']}'s heart is overflowing... ***")
                print(f"  *** Something special is about to happen... ***\n")

                result = run_confession_scene(maid)

                if result == "menu":
                    game_running = False  # Break inner loop, continue outer loop
                else:
                    return  # Exit game completely


if __name__ == "__main__":
    main()
