# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:22:37 2020

@author: hreef
"""

import pandas as pd
#structuring the data
df = pd.read_csv("responses-3.csv")
pd.set_option('display.max_rows',230)
pd.set_option('display.max_columns',29)
pd.set_option('display.max_colwidth',1000)

#Extracting the questions and manipulating it
df['Questions']
list(set(df.Questions))
df['Questions'].unique()
df.Questions.str.contains('menopause')
df.Questions.str.contains('weight')
df.Questions.str.contains('training')
df.Questions.str.contains('hot flashes')
df.Questions.str.contains('menstruation')
df.Questions.str.contains('period')
df.Questions.str.replace('period','menstruation')
df.Questions.str.replace('NaN','NA').str.replace('no','NA')


#Conducting word frequency analysis
text =""" 
Weight loss/training/fitness 
How can I prevent the weight gain associated with menopause and perimenopause?
How to reduce significant amount of weight in a short time without stressing the body?
How to maximize strength/performance while minimizing muscle loss.
Counting macros and still not loosing weight what else should I do.
Being on the younger side And unable to take HRT due to blood clots, I would love to be able to understand weight management that is not an extreme diet and lots of supplements, how to manage skin changes (thinning and tearing easier from saddle even with lube and proper short) and rebuilding speed and strength after and injury.
How do you work with changes in your body to get fitness results when you were younger? i.e. I have a six-monthly fitness test and it is getting extremely hard to pass. There is a single fitness standard for both males and females. I don’t want to give up my job because I have turned into to a middle-aged woman. I am the only female to make this team ever.
How do I know what is really going on with my body and if what I’m doing is on the right track?
I need more help in a training plan to work in sync with my cycles as I am starting to learn that I can optimise certain times of the month, but that I can also be damaging myself at other times of the month. Because I train with a high level group in the winter I tend to do whatever their session is despite how I’m feeling, do you think perhaps this been impacting my results and body as those are the times that I can skip periods and have mood swings, low sex drive, and feel drained, yet other times I feel amazing, strong, fit  and want to train all the time.
I am trying to navigate weight loss and am having a hard time. I am finding that even following ROAR guidelines, I am gaining, and not muscle. The lack of muscle is due to no access to a gym right now, so my training is mostly biking and running. Should I change something during the quarantine?
Why am I unable to lose weight, even training (exercise) 9 - 12 hours per week, and not eating processed food.
How do I reduce belly fat?
I hear menopausal women don’t process carbs as well, is this true?  What should we fuel with during super long workouts? During races?
What’s the best way to structure training when there are no (apparent) hormone fluctuations?
Is naturally cycling still better with PCOs or what type of contraception should I consider helping mitigate the health issues and still have that performance advantage of training with the naturally cycling period. How should an Athletic woman, looking at the next Commonwealth games approach training and recovery with PCOs?
2: one a request- to help those of us on the verge of menopause best understand how to apply training strategies when we really have no idea where we are in a cycle- do we just move to post menopause training advice? 2: offer: I am a User Experience/ User Interface designer with 13+ years in highly sensitive information design. I would love to help as you develop this! Happy to do free consultations, heuristic reviews, help organize user testing, etc. I am looking for passion projects. And this is a passion.,
I think one of my biggest symptoms that affects my training is weight gain and how doing all the right things doesn’t help.
I want to know what I can do to build bone density. Also interested in how I should be training now. Weights versus cardio.
I need more help in a training plan to work in sync with my cycles as I am starting to learn that I can optimise certain times of the month, but that I can also be damaging myself at other times of the month. Because I train with a high level group in the winter I tend to do whatever their session is despite how I’m feeling, do you think perhaps this been impacting my results and body as those are the times that I can skip periods and have mood swings, low sex drive, and feel drained, yet other times I feel amazing, strong, fit  and want to train all the time.,
More of a statement: Id really love to be able to have an idea of my cycle so I can plan training to go with it. But having a hysterectomy I fear there is no way to truly track it and I’m just SOL.,
. Suggestions on managing symptoms and being effective in training. 
Can you help me figure out the best way to train while going through this?
How do I really know how hard my training session is, to make sure I eat properly when I am a slow athlete,
Protein recipes suggestions to support training. HRT therapies the pros and cons. How to put weight training with running and cycling,
Would like more info on nutrition during this phase, how different is training. trying to lose some fat.,
Id like to know a bit more about optimising my training, I have some understanding from reading Roar, but would like to know more.,
How can I train to help support menstruation?
Can altered training help mitigate symptoms, and increase weight loss/management,
I’m trying to work out how to measure the right training load. I used to (and still am) working with TSS scores in training peaks but feel they don’t really work for HIIT and strength as well as for classic endurance training.  Is there a better way to assess the right training load?
What should I consider re training as a post menopausal triathlete? Nutrition/ training/ recovery,
How can I support my training with irregular menstruation and, at times, amenorrhea?
I train about 4 times a week (cycling) but don’t think I have the nutrition and recovery quite right or when I should train hard and when to ease off. Some guidance would be greatly appreciated!
How do I train and recover when I am still working a stressful, full-time job?
How can I continue to train for long distance events without overloading my system in terms of cortisol response?
How much does almost non-existent testosterone impact my symptoms. I’ve been trying to find someone to prescribe a woman’s dose of T in Canada for over 2years (to no avail),
Is there anything else I can do to even out my hormone fluctuations? I think my estrogen levels have dropped and Id love to find a natural way of boosting them!
How can I eat to not gain weight and help balance my hormones? I’m always an advocate of getting nutrients out of the right foods and not making your liver crazy w just supplements or a drug. (HRT),
How normal does my cycle sound? I went to the dr and had hormone levels tested, but she said the results were fine and its not peri menopause... I’m not convinced. I’m 48
Will managing my cycle make it easier to manage body weight and composition?  I’ve struggled my whole like with body image and, while I know I’m healthier being heavier, its a challenge mentally.  I feel bloated often and I feel like my hormones have a lot to do with this, I can shift water weight like a man does! I find that if I sleep 8.5+ hours a night my body can do what it needs to do, and my weight stabilizes, but I get hot flashes (I’m not menopausal) and wake up, I wake up for no reason and cant fall back asleep etc. so I guess the real question is, will balancing my hormones really help my quality of life, or are these all normal?,
What can I do to avoid (or at least mitigate) abdominal weight gain during menopause?
I’m not as active as I used to be. I’m more tired and find myself needing more sleep. Where should a perimenopausal athlete focus her attention, HIIT, running/cycling, or keep doing everything knowing this is a phase?
There are many menopausal women who wish to continue to be competitive athletes. I am one of them. I train with a group male friends and want to continue to be able to keep up on hills (I’m fine on the flats). I want help to maintain or improve my muscle and help lose this new belly fat. Both are important to keep up my cycling ability, especially with respect to hill climbing. I know that my hormonal changes have been an influencing factor.
How can we get more research for women athletes, especially for those in perk, post and menopausal?
I live in an extreme climate (Vietnam) and would like information on natural beverage choices that might alleviate symptoms. Also wondering if there are any indicators that would help me know HOW long this may go on.  I had a Mirena IUD from the age of 47 to stop my periods (weeklong crampy affairs). I didn’t have periods for about 5 years before I had it removed, but menopause hit a year later, and its been difficult to deal with. Thanks!
I am 48 and want to do better at cycling but how is menopause going to affect me? I want to do long rides and improve my competitiveness. What do I need to be looking to do, what to eat, how to train? How do I not let one day of the month set me back? :),
Anything I should do differently due to post menopause, what’s normal in perimenopause?
Are there particular ways in which my physical activities (time of day, intensity, type of activity) can be used to mitigate my menopausal symptoms?
As I enter perimenopause, I am trying to assess if a newly irregular cycle is related to training, or aging!
How do I know I’m peri menopause?
Training and nutrition suggestions to increase muscle post menopause,
Once I am in menopause, how do I adapt/modify my training for healthy longevity?
How can I structure my training to get around my menopause symptoms?
How are you looking to help with Menopause symptoms.?
Really starting to research what to expect, so in in the ABC stage of learning about menopause (don’t have questions yet),
How can you help those with irregular cycles, not going through menopause?
How to keep motivated during the perimenopause phase.,
When will sports clothing manufacturers recognise that peri/post menopausal athletes want cute clothes too? When will we be invited to be ambassadors for big brands (e.g. Lululemon) and used as models?!
So many. Please make your App telling me what and when to train, what and when to eat. I am the same athlete as younger women with great goals. I train hard. I want my body to help me and not work against me. Just make your App and program for women in peri-, post- and menopause the same as for younger women. We want to be seen.
How to reduce hot flashes? 
How to stop hot flashes and night sweats during perimenopause?
Is there a way to use hot flashes as heat training/acclimation? Is it possible to use your mind to train your brain that hot flashes are comfortable and not hot?
How to deal with ibis/c. The bloating the hot flashes. Fiber is not an answer sadly,
I want to be able to get faster Running without over heating. How?
How can I become better acclimated to heat and humidity?
How do I mitigate feeling sluggish before my period? How do I mentally make it easier to make changes to my diet? How do I change my body composition?
Id love to beta test your app! I’m very open to learning how in a non-perfect cycle that female athletes can train properly and race effectively. Is there anything that can be done nutrition or exercise wise to be more efficient and, in less pain, /bloating the moment I notice signs of an upcoming possible period?
When you are 46 and some months your period is 2 weeks off, how to know if this is peri menopause or over training?
I have a Mirena, I still get menstrual symptoms but its irregular. I have weeks when I can’t do the same training plan, I’m exhausted, foggy--- what can I do to make this less of an issue
is it normal to be so irregular nobody talks about this stage or how to manage it.?
How to know that your body is healthy while having irregular cycles with an IUD.,
Are there factors other than energy imbalance that could cause irregular periods in athletes?
(I’m still in line for the demo) wondering if you’re able to track diet / food sensitivity with menstrual cycle... this has been biggest issue with trying to use other apps- nothing seems connected (exercise, diet, cycle).,
Assistance for non-menstruating but ovulating
How can you use your menstrual cycle to optimise your training?
If I’m not menstruating because of overtraining/under nutrition Id really like to get my periods back!
How can I better track when I have no visual/physical indication of cycle starting like a period?
How can I get my period regular? 😅😩,
What are recommended ways to get period to return naturally?
How can I get rid of breast pain and swelling? 
What to do for the post menopausal athlete to keep going into the future with recovery and to fight fatigue and joint pain.
Why do I feel more fatigued and sorer in the mornings?
How to manage endometriosis pain 
How to get more energy!
How can I get my energy for running back?
What are the safest and most effective treatments for fatigue?
I find that I suffer extreme fatigue from time to time after exercising, like wanting to lay down and sleep.  I would like to know if that is from lack of nutrition or supplements or the HRT,
Fatigue when I train is a problem.... my endurance suffers
Id love to know more about why I might be waking up feeling like I have the flu with no energy sometimes.  It seems a little extreme.
If all can help with the depression that can accompany menopause that’s be fabulous! Also, the muscle cramping, it was so bad I was scared I had neurological damage and went in for an incredible number of tests. Any help there would be wonderful.
Can you help me sleep?
Why does l get such bad DOMS now? How can l sleep better?
What can I do to improve my sleep? Been like this for 6 years now. Started exercising just before my 50 the birthday when my menopause first started, it gave me a focus and a goal but 6 years on and my motivation is dwindling, and fatigue is so bad.!
Hard to know what is askable - except what can I do to work with/around blood sugar and mood swings, and how can I know early on when to do them (hopefully pre-emptively)?
What is the most effective treatment for mood swing?
What kind of tracking are you planning on? We have no cycle and there’s still no research on us,
What are the best ways to track symptoms vs performance?
I think it would be very helpful to be able to track, with data, if there are times when women going thru menopause can look at symptoms as an indicator of greater risk of injury to joints or as better times to train to offset negative symptoms.,
Id really like to work out a way to track my symptoms and how I’m feeling with performance. I’ve never had a regular cycle, plus I became an athlete later in life, so I’ve never had a clear association with my cycle. I’ve tried to manually do it, but I don’t really know what to look for/record and how to match that to performance
More info on tracking and RED-S please, especially for rec amateur athletes without access to professional advice,
Id like to know more about the wild ai app. I understand its a tracking app, but I don’t really have the finer details.
About the app
When will you offer up more access? I am dying to try this out!  For myself and my female athletes,
Interested in estrus effects of women living in the same household,
Create a back button. I wanted to go back in the questionnaire and couldn’t.,
What kind of help can you offer?
Can the app ID where you are in your cycle?
How long until this app is up and running?!,
How can I best share data?
can I be a beta tester?
I would just like to know more about what you are working on. I feel like there is so much complicated stuff with perimenopause and it doesn’t get talked about nearly enough. Having a community to share with is also important.
We need more sources of good information for menopausal athletes. There is a little bit here and there but usually its single sport (e.g. cycling website or ultra running website). Would be great to have a website aimed at female athletes and amateur athletes across many sports and age groups. (I’ve tried to find one because I’m a journalist and I have ideas to pitch but there’s nothing for serious female athletes across multiple disciplines),
When can I start? Also are you integrating with anything like Strava to pull data?
I’m still not 100% sure what you’re all about.  I see that you want us to share with everybody, etc... but I haven’t seen any previews or any information on what exactly your app does/is.  Would love to know more. Will your app sync to larger platforms like Training Peaks or MyFitnessPal and the like for coaches and serious athletes to better integrate the female cycle into training?
Food and nutrition
What type of food could help or should be avoided?
I so far have been fortunate to not have many or severe issues like others. However, I am wondering if there are days I should train less or not at all or if that is no longer an issue? Also is there a better different way to eat?
How can I balance my food intake to help with hormones and decrease weight gain?  My weight is stagnant despite calorie deficit and training increase.
Nutrition advice for keeping weight down but everything you need to fuel you
What do you anticipate will be different in nutrition for post menopausal females?
How can I use nutrition to manage my hot flushes?
What can I do nutritionally/physically/mentally to get my period back after stopping the pill 8 months ago?
Even with a testosterone boost I have a lower sex drive than what I would like. The will (mentally) is there, but the energy isn’t. Again, maybe a diet focused on more testosterone friendly foods may help??? I have followed a keto diet for over two years now, but open to anything that helps manage my weight but boosts energy
Currently I’m tracking my cycle as if I have a period. What is the best way to manage training and nutrition in the transitional perimenopausal phase? The small amount of literature out there speaks to either menstruating women or post menopausal women.,
I’m curious about the plus sides. There’s quite little general awareness of this stage in life.,
How can I change what I do to better deal with changing symptoms.?
Would love to hear more from long term Depo users regarding their digestion.
Things can be manageable too?
How long does this last?  I’m 38 and miserable
I’m waiting on scheduling for full hysterectomy (ovaries will stay) and am interested to learn more about how my symptoms will (not) be affected.,
Create support/info for women with partial hysterectomies. We are obliviously in the dark about a lot of what is going on with our bodies because the traditional signs are gone or masked as part of other issues we navigate (IBS, thyroid, etc.),
When are you going to admit me?? I am waiting for ages (place 18...)

"""

text=text.replace('training','train')
text=text.replace('will','')
text=text.replace('really','')
text=text.replace('know','')
text=text.replace('make','')
text=text.replace('want','')
text=text.replace('still','')
text=text.replace('going','')
text=text.replace('cycling','')
text=text.replace('way','')
text=text.replace('don','')
print(text)


for char in "-,.'\n?":
    text=text.replace(char,' ') 
text= text.lower()
print(text)
word_list= text.split()
print(word_list) #total 3532




#Initializing dictionary for word count
d={}

#counting number of words each time comes up in list 
for word in word_list:
    d[word]= d.get(word,0)+1    
d
#get highest to lowest sorted
word_freq = []
for key, value in d.items():
    word_freq.append((value,key))
word_freq

word_freq.sort(reverse=True)
print(word_freq)


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 15, stopwords = stopwords)
wc.generate(text)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()
